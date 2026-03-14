import threading
import sys
from abc import ABCMeta, abstractmethod


class TimeoutError(Exception):
    """Represents a timeout for waiting for a load. mostly allows the timeout parameter in the get() method, to differentiate between a timeout and a failure."""
    pass

class PreloadBase:
    """Manages the steam modlist, as is gotten by the steam_downloadable_mods method.
    It supports loading the modlist in a separate thread via the load method,
    And caching such results.
    This is needed as loading the modlist takes quite a while,
      And is an operation we would much rather do at startup, without delaying anything else.
    Any exceptions raised in the loading process will be available through the get_exception() method.
    Once the load finishes, Only one of the get() and get_exception() methods will return a value, while the other will return None.
      If the load is successful, then get() will return a value. if the load raised an exception, then get_exception() will return a value.
    """
    
    __metaclass__ = ABCMeta
    
    def __init__(self):
        
        # I haven't found any conclusive source on whether parallel reads and writes to different keys in dictionaries are thread-safe,
        #  So they're treated as unsafe.
        self._loading_threads = {}
        self._load_start_lock = threading.Lock()
        
        self._loaded_data = {}
        self._exception = {}
        self._return_data_lock = threading.Lock() # Lock protecting dict access to the loaded data dictionaries: self._loaded_data and self._exception
        
        self._is_loaded = {}
        self._is_loaded_lock = threading.Lock()
        
        return
    
    @abstractmethod
    def loading_function(self, *args):
        """Actually loads the required data.
        It may only take positional arguments, and return a single value: the loaded data, which will be accessible via the get() method.
        It may raise an exception, in which case it'll be stored, and accessible via the get_exception() method.
        """
        pass
    
    def _load_and_set(self, *args):
        """Calls the _loading_function and sets the internal values based on its results."""
        try:
            data = self.loading_function(*args)
            with self._return_data_lock:
                self._loaded_data[args] = data
                self._exception[args] = None
            print "Finished preload without errors"
        except Exception as e:
            print "Finished preload with errors of type={}".format(type(e))
            with self._return_data_lock:
                e.traceback = sys.exc_info()[2] # Adding traceback information to e
                self._loaded_data[args] = None
                self._exception[args] = e
        
        with self._is_loaded_lock:
            self._is_loaded[args].set()
        print "Done preloading"
        return
    
    def load(self, *args):
        """Starts preloading the data for args if it is not already being loaded.
        This method starts a thread which loads the data.
        It guarantees that for any number of repeated calls to it from any number of threads, only one loading thread will be started.
        Once the data is loaded, it is available through the get() method.
        """
        with self._load_start_lock:
            # print "args={}, l_threads={}".format(args, self._loading_threads)
            if args not in self._loading_threads:
                print "Preload thread not present, Starting..."
                with self._is_loaded_lock:
                    self._is_loaded[args] = threading.Event()
                self._loading_threads[args] = threading.Thread(target=self._load_and_set,
                                                               name=u"Thread-load-{}-{}".format(self.__class__.__name__, hash(args)),
                                                               args=args)
                self._loading_threads[args].start()
            else:
                print "Preload thread already present"
            return self._loading_threads[args]
    
    def get(self, *args, **kwargs):
        """Get the preloaded data.
        If the data has already loaded, this method returns with it immediately,
        Otherwise, load() is called, and this method blocks using self.wait(timeout).
        :returns steam modlist data, If timeout has not been reached and the loading thread has not raised an error.
        :raises Exception, If timeout has not been reached and the loading thread has raised an error. this raises that very exception.
        :raises TimeoutError, If timeout has been reached.
        """
        if "timeout" in kwargs:
            timeout = kwargs["timeout"]
        else:
            timeout = None
        
        if self.is_loaded(*args):
            # Note: while the value of is_loaded can change between checking it here and referring to _loaded_data,
            #  It can only change from False to True.
            #  In that case the load() method has been called before and is currently finishing,
            #  And it'll be called again here, ignored, and _is_loaded will be waited upon, which will finish only once _loaded_data is available.
            
            print "Preload data already available"
        else:
            print "Preload data not available, calling load"
            self.load(*args)
            self.wait(*args, timeout=timeout)
            print "Loading done, fetching data"
        
        with self._return_data_lock:
            if self._exception[args] is not None:
                raise self._exception[args]
            
            return self._loaded_data[args]
    
    def is_loaded(self, *args):
        with self._is_loaded_lock:
            return args in self._is_loaded and self._is_loaded[args].is_set()
    
    def wait(self, *args, **kwargs):
        """Waits for timeout seconds until loading is finished. if timeout is None (default), waits indefinitely until loading is finished.
        :returns None if loading is finished before timeout elapsed.
        :raises TimeoutError if timeout has expired before loading is finished."""
        if "timeout" in kwargs:
            timeout = kwargs["timeout"]
        else:
            timeout = None
        
        with self._is_loaded_lock:
            correct_is_done = self._is_loaded[args] # lock should only protect dict access and should never contain blocking actions.
            
        if not correct_is_done.wait(timeout):
            raise TimeoutError(type(self).__name__)
        return
    
