import collections
import threading
import sys
import time
import os
import re
import subprocess


class TimeoutError(Exception):
    """A timeout for waiting for a load. mostly allows the timeout parameter in the get() method, to differentiate between a timeout and a failure."""
    pass

class ClearingError(Exception):
    """An action that was made invalid via a clear() call"""
    pass

class Empty(TimeoutError):
    """A pop operation on an empty queue"""
    pass

class Queue:
    """As Queue.Queue isn't available, we make our own. maxsize isn't supported."""
    
    def __init__(self):
        self._queue = collections.deque()
        self._pop_condition = threading.Condition()
        return
    
    
    def put(self, item):
        with self._pop_condition:
            self._queue.append(item)
            self._pop_condition.notify()
        return
    
    def get(self, block=True, timeout=None):
        if not block or timeout == 0: # For these non-blocking cases, We avoid the retrying located below.
            try:
                return self._queue.popleft()
            except IndexError:
                raise Empty()
            
        with self._pop_condition:
            while True:
                try:
                    return self._queue.popleft()
                except IndexError:
                    s_time = time.time()
                    self._pop_condition.wait(timeout)
                    if timeout is not None:
                        timeout -= time.time() - s_time
                        if timeout < 0:
                            raise Empty()
    
    def clear(self):
        self._queue.clear()
        return
    
    def get_nowait(self):
        self.get(False)


# As we effectively use a threadpool for the preload class, we wish to access the cpu count of the machine to allow a logical default number of threads.
#   multiprocessing (the standard way to check) is not available, so we use this one.
# Source - https://stackoverflow.com/a/1006301
# Posted by phihag, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-07, License - CC BY-SA 4.0
def available_cpu_count():
    """ Number of available virtual or physical CPUs on this system, i.e.
    user/real as output by time(1) when called with an optimally scaling
    userspace-only program"""

    # cpuset
    # cpuset may restrict the number of *available* processors
    try:
        m = re.search(r'(?m)^Cpus_allowed:\s*(.*)$',
                      open('/proc/self/status').read())
        if m:
            res = bin(int(m.group(1).replace(',', ''), 16)).count('1')
            if res > 0:
                return res
    except IOError:
        pass

    # Python 2.6+
    try:
        import multiprocessing
        return multiprocessing.cpu_count()
    except (ImportError, NotImplementedError):
        pass

    # https://github.com/giampaolo/psutil
    try:
        import psutil
        return psutil.cpu_count()   # psutil.NUM_CPUS on old versions
    except (ImportError, AttributeError):
        pass

    # POSIX
    try:
        res = int(os.sysconf('SC_NPROCESSORS_ONLN'))

        if res > 0:
            return res
    except (AttributeError, ValueError):
        pass

    # Windows
    try:
        res = int(os.environ['NUMBER_OF_PROCESSORS'])

        if res > 0:
            return res
    except (KeyError, ValueError):
        pass

    # jython
    try:
        from java.lang import Runtime
        runtime = Runtime.getRuntime()
        res = runtime.availableProcessors()
        if res > 0:
            return res
    except ImportError:
        pass

    # BSD
    try:
        sysctl = subprocess.Popen(['sysctl', '-n', 'hw.ncpu'],
                                  stdout=subprocess.PIPE)
        scStdout = sysctl.communicate()[0]
        res = int(scStdout)

        if res > 0:
            return res
    except (OSError, ValueError):
        pass

    # Linux
    try:
        res = open('/proc/cpuinfo').read().count('processor\t:')

        if res > 0:
            return res
    except IOError:
        pass

    # Solaris
    try:
        pseudoDevices = os.listdir('/devices/pseudo/')
        res = 0
        for pd in pseudoDevices:
            if re.match(r'^cpuid@[0-9]+$', pd):
                res += 1

        if res > 0:
            return res
    except OSError:
        pass

    # Other UNIXes (heuristic)
    try:
        try:
            dmesg = open('/var/run/dmesg.boot').read()
        except IOError:
            dmesgProcess = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
            dmesg = dmesgProcess.communicate()[0]

        res = 0
        while '\ncpu' + str(res) + ':' in dmesg:
            res += 1

        if res > 0:
            return res
    except OSError:
        pass

    raise Exception('Can not determine number of CPUs on this system')



class Preload:
    """A class for preloading of resources via threads.
    Calls to loading_function are grouped by parameter list and preloaded by load(). their results are cached, and are accessible via get().
    this is useful for resources, where their loading is IO-bound and may hang the main thread, and which are not expected to change during the course of the program.
    
    To load a resource, call load() with the parameters to send to loading_function.
        multiple separate resources may be loaded at once, identified by their parameter lists.
        only positional parameters are supported.
    To retrieve a resource, call get() with the same parameters.
    To wait upon a resource load without retrieving it, call wait().
    Callbacks are also supported, as per register_callback().
    
    Preloading is done by a threadpool, and as such, many calls to load can be done in short succession without significant performance costs.
    """
    
    def __init__(self, loading_function, max_workers=None):
        """
        :parameter loading_function: The function used to load the resource.
        :parameter max_workers: (default None) The maximum number of preloading threads. default is min(32, available_cpu_count() + 4), taken from concurrent.futures.ThreadPoolExecutor
        """
        
        self._loading_function = loading_function
        self._name = self._loading_function.__name__ # Used for debugging
        
        if max_workers is None: # ensure worker count is valid
            try:
                max_workers = min(32, available_cpu_count() + 4) # taken from concurrent.futures.ThreadPoolExecutor
            except Exception: # On the offchance that cpu count fails, we don't actually care enough to raise an error about it. it may be treated as 1.
                max_workers = 5 # 1 (failed cpu count) + 4
        elif not isinstance(max_workers, int):
            raise TypeError("max_workers is not an integral type!")
        elif max_workers < 1:
            raise ValueError("max_workers must be an a positive integer. number given: {}".format(int(max_workers)))
        
        # I haven't found any conclusive source on whether parallel reads and writes to different keys in dictionaries are thread-safe,
        #  So they're treated as unsafe.
        self._job_queue = Queue()
        self._loading_threads = []
        for i in range(max_workers):
            self._loading_threads.append(threading.Thread(target=self._manage_job_queue,
                                                          name=u"Preload-o{}-{:02}".format(id(self), i)))
            self._loading_threads[-1].daemon = True
            self._loading_threads[-1].start()
        
        self._loaded_data = {}
        self._exception = {}
        self._callbacks = []
        # A lock used both to keep the load data dicts sane, and to ensure all callbacks are called on the appropriate results.
        self._load_data_lock = threading.Lock()
        
        
        self._is_loaded = {} # Presence of a key here is used to detect if that said key is being loaded
        self._is_loaded_lock = threading.Lock()
        
        self._clear_session_num = 0 # clear() uses session numbers to ensure that once clear is called, all ongoing actions are invalidated
        self._clear_session_lock = threading.RLock()
        
        return
    
    def _manage_job_queue(self):
        while True:
            next_job = self._job_queue.get()
            print "[{}]{} next job: {} ({})".format(self._clear_session_num, self._name, next_job[1], next_job[2:])
            job_clear_session = next_job[0]
            if not self._is_clear_session_valid(job_clear_session):
                continue
            job_type = next_job[1]
            if job_type is "load":
                self._load_and_set(job_clear_session, *next_job[2])
            elif job_type is "callback":
                new_callback, finished_loads = next_job[2], next_job[3]
                self._call_callbacks(finished_loads, (new_callback,), clear_session=job_clear_session)
            else:
                raise ValueError("Unrecogised job of type: \"{}\"".format(job_type))
    
    
    def _load_and_set(self, clear_session, *args):
        """Calls the _loading_function and stores it results for get()."""
        try:
            data = self._loading_function(*args)
            exception = None
            print "Finished preload without errors"
        except Exception as e:
            print "Finished preload with errors of type={}".format(type(e))
            data = None
            exception = e
            exception.traceback = sys.exc_info()[2]  # Adding traceback information to e
        
        with self._clear_session_lock:
            if not self._is_clear_session_valid(clear_session):
                return # Invalidated
            with self._load_data_lock:
                self._loaded_data[args] = data
                self._exception[args] = exception
                curr_callbacks = tuple(self._callbacks)
            
            with self._is_loaded_lock:
                self._is_loaded[args].set()
            # print "Done preloading"
            self._call_callbacks((args,), curr_callbacks, clear_session=self._clear_session_num)
        return
    
    def load(self, *args):
        """Starts preloading the result of loading_function(*args) if it is not already being loaded.
        It guarantees that for any number of repeated calls to it from any number of threads, loading_function() will only be called once for each distinct args.
        Once the data is loaded, it is available through the get() method.
        """
        with self._clear_session_lock:
            with self._is_loaded_lock:
                if args in self._is_loaded:
                    print "({}) Preload already present: {}".format(self._name, args)
                    return
                
                self._is_loaded[args] = threading.Event()
            
            print "({}) Preload not present, Starting... {}".format(self._name, args)
            self._job_queue.put((self._clear_session_num, "load", args))
        return
    
    def get(self, *args, **kwargs):
        """Get the preloaded data corresponding to args.
        If the data has already loaded, this method returns with it immediately,
        Otherwise, load(*args) is called, and this method blocks using self.wait(*args, timeout=timeout).
        :parameter timeout - name only (default None) - identical to self.wait() timeout parameter.
        :returns preloaded result of loading_function(*args), If timeout has not been reached and the loading thread has not raised an error.
        :raises Exception, If timeout has not been reached and the loading thread has raised an error. this raises that very exception.
        :raises TimeoutError, If timeout has been reached.
        """
        if "timeout" in kwargs:
            timeout = kwargs["timeout"]
        else:
            timeout = None
        
        with self._clear_session_lock:
            if self.is_loaded(*args):
                # Note: while the value of is_loaded can change between checking it here and referring to _loaded_data,
                #  It can only change from False to True.
                #  In that case the load() method has been called before and is currently finishing,
                #  And it'll be called again here, ignored, and _is_loaded will be waited upon, which will finish only once _loaded_data is available.
                
                print "({}) Preload data already available: {}".format(self._name, args)
            else:
                print "({}) Preload data not available, calling load: {}".format(self._name, args)
                self.load(*args)
                self.wait(*args, timeout=timeout)
            
            with self._load_data_lock:
                if self._exception[args] is not None: # by this point, args must be present in both data dicts
                    raise self._exception[args]
                
                return self._loaded_data[args]
    
    def clear(self):
        """Clears the loaded data, along with any ongoing loading and callback actions.
        Note that it can't stop them outright, but it invalidates their results."""
        with self._clear_session_lock:
            print "Clearing {}".format(self._name)
            self._clear_session_num += 1
            self._loaded_data.clear()
            self._exception.clear()
            self._is_loaded.clear()
            self._job_queue.clear()
            return
    
    def _is_clear_session_valid(self, clear_session):
        with self._clear_session_lock:
            return clear_session == self._clear_session_num
    
    
    def register_callback(self, callback):
        """Register a callback to be run on the result of each load when finished.
        The callback will also be run on each already finished load.
        A callback must receive two positional arguments: the result of the finished load, and the exception raised during it.
        It is guaranteed that each callback will eventually run exactly once on each load.
        """
        
        with self._clear_session_lock:
            with self._load_data_lock:
                self._callbacks.append(callback)
                finised_loads = tuple(self._loaded_data.keys())
        
            self._job_queue.put((self._clear_session_num, "callback", callback, finised_loads))
        return
    
    def _call_callbacks(self, loads, callbacks, clear_session):
        """calls each callback in callbacks on each result of loads"""
        for load_key in loads:
            data = None
            exception = None
            try:
                with self._clear_session_lock:
                    if not self._is_clear_session_valid(clear_session):
                        return # Once a clear session passes, this whole thing is invalidated
                    data = self.get(*load_key)
            except Exception as e:
                exception = e
            for callback in callbacks:
                try:
                    if not self._is_clear_session_valid(clear_session):
                        return # Once a clear session passes, this whole thing is invalidated
                    callback(data, exception)
                except Exception: # callback exceptions are ignored and do not affect other callbacks.
                    pass
        return
    
    
    def is_loaded(self, *args):
        with self._clear_session_lock:
            with self._is_loaded_lock:
                return args in self._is_loaded and self._is_loaded[args].is_set()
    
    def wait(self, *args, **kwargs):
        """Waits for timeout seconds until loading is finished. if timeout is None (default), waits indefinitely until loading is finished.
        :parameter timeout - name only (default None) - the number of seconds to wait. by default - indefinitely.
        :returns None if loading is finished before timeout elapsed.
        :raises TimeoutError if timeout has expired before loading is finished."""
        if "timeout" in kwargs:
            timeout = kwargs["timeout"]
        else:
            timeout = None
        
        with self._clear_session_lock:
            with self._is_loaded_lock:
                try:
                    correct_is_done = self._is_loaded[args] # lock should only protect dict access and should never contain blocking actions.
                except AttributeError:
                    raise ClearingError("wait{}".format(args))
            
        if not correct_is_done.wait(timeout):
            raise TimeoutError(type(self).__name__)
        return
    
