import sys
import os
import shutil
import time
import errno
import json
import threading
import copy

import renpy.config

from steam_workshop.steamhandler import SteamMgr, PyCallback, WorkshopData, cache
from steam_workshop import steamhandler


class AttributeDict(dict, object):
    """This class allows dict members to be accessed via __getattr__, which mimics the usage of array entries in Query callbacks"""
    def __getattr__(self, item):
        try:
            return super(AttributeDict, self).__getattr__(item)
        except AttributeError:
            pass # Checking super's __getattr__ is mostly a just-in-case thing, as it generally wouldn't return anything. of course, if it fails, we want to actually add the __get_item__ call, so errors are ignored.
        try:
            return self[item]
        except KeyError:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__, item))


class ManagedThread(threading.Thread, object):
    """A threading.Thread which has a holding list.
    When this thread starts, it adds itself to the list,
    And when it finishes it removes itself from that list.
    Coherence is ensured by lock, which is a threading.Lock. it is used on all accesses to holder."""
    
    def __init__(self, holder, lock, group=None, target=None, name=None, args=(), kwargs={}):
        super(ManagedThread, self).__init__(group=group, target=target, name=name, args=args, kwargs=kwargs)
        self.holder = holder
        self.lock = lock
        return
    
    def run(self):
        with self.lock:
            self.holder.append(self)
        
        try:
            return super(ManagedThread, self).run()
        finally:
            with self.lock:
                self.holder.remove(self)


class CacheWriteError(RuntimeError, object):
    """Represents an exception that was raised in the cache write callback."""
    
    def __init__(self, cause, cause_traceback = None, *args):
        super(CacheWriteError, self).__init__(*args)
        self.cause = cause
        self.cause_traceback = cause_traceback
    
    @classmethod
    def from_exc(cls, *args):
        """Construct this exception using sys.exc_info() for the cause and traceback."""
        _, cause, cause_traceback = sys.exc_info()
        return cls(cause, cause_traceback, *args)
    
    def __str__(self):
        if not self.message.strip():
            return "{}Caused by: {}: {}".format(self.message, type(self.cause).__name__, str(self.cause))
        return "{}\n    Caused by: {}: {}".format(self.message, type(self.cause).__name__, str(self.cause))
    

class CachedSteamMgr:
    """Holds a SteamMgr instance, and caches results of problematic actions (QueryApi, which gets workshop data as a whole, not parts),
    So that calls to them will not fail when done repeatedly.
    In QueryApi's case, This is done to bypass an existing cache which causes failures.
    It is highly recommended to use this whenever one needs lists of steam mods (for example, the mod browser).
    """
    
    __PAGE_CACHE_DIR = os.path.join(renpy.config.gamedir, "page_cache")
    
    def __init__(self, steam_manager):
        if not isinstance(steam_manager, SteamMgr):
            raise TypeError("steam_manager must be a steam_workshop.steamhandler.SteamMgr instance!")
        self._steam_manager = steam_manager
        
        # When the cache is used, We need to create a thread in order to behave like QueryApi.
        # As these threads are internal, we should at least keep track of which ones are active at any time.
        # This is done using ManagedThread instances, which use self._active_threads as their holder.
        self._active_threads = []
        self._active_threads_lock = threading.Lock()
        return
    
    
    def register_callback(self, type, func):
        return self._steam_manager.register_callback(type, func)
    
    def unregister_callback(self, type, func):
        return self._steam_manager.unregister_callback(type, func)
    
    
    def is_file_stale(self, file_path):
        """True if cache file given by file_path is stale."""
        # Testing if file has been updated in the last 15 minutes. If not, stale.
        #   Empirically, the problematic cache always becomes stale by this point.
        curr_time = time.time()
        cache_time = os.path.getmtime(file_path)
        return (curr_time - cache_time) >= 15 * 60
    
    def get_cache_filename(self, page):
        """Returns the cache filename matching this page number."""
        if not isinstance(page, int):
            raise TypeError("Page number must an integer!")
        if page <= 0:
            raise ValueError("Page number must be positive!")
        return os.path.join(self.__PAGE_CACHE_DIR, "page_{:02}.json".format(page))
    
    
    def _CallQueryApi(self, page):
        """Gets super's QueryApi(page), strictly by calling QueryApi.
        Fills the cache as well, and keeps python thread trapped until cache has been filled.
        :raises CacheWriteError If the cache callback raises an exception, containing the exception raised and it's traceback.
        """
        print "Cache callback: Current query callbacks:", "\n".join(str(func) for func in self._steam_manager.Callbacks[PyCallback.Query])
        print "Cache callback: Current persona callbacks:", "\n".join(str(func) for func in self._steam_manager.Callbacks[PyCallback.Persona])
        
        
        def fill_cache_query_cb(array, arr_len):
            try:
                print "Cache callback called with: (len={0}), array={1}".format(arr_len, array)
                
                # Prepare data to write: convert it to json compatible dicts
                field_names = [name for name, _ in WorkshopData._fields_]
                array_data = [{name: getattr(array[i], name) for name in field_names} for i in range(arr_len)]
                to_write = {"len": arr_len, "data": array_data}
                
                # Get cache file name
                cache_file_name = self.get_cache_filename(page)
                print "Cache file target: \"{}\"\n".format(cache_file_name)
                
                # Ensure file can be created (ensure directories)
                to_ensure = os.path.dirname(cache_file_name)
                if not os.path.exists(to_ensure):  # If not exists: create
                    os.makedirs(os.path.dirname(cache_file_name))
                elif not os.path.isdir(to_ensure):  # If exists and not dir: problem
                    raise OSError(errno.ENOTDIR, "The attempted directory \"{}\" exists and is not a directory.".format(to_ensure))
                # else: exists and is dir: no need to do anything
                
                # Write cache file
                with open(cache_file_name, "w") as cache_file:
                    json.dump(to_write, cache_file, encoding="utf-8") # While not strictly necessary, I'd rather be explicit with the encoding.
                
            except Exception as e:
                fill_cache_query_cb.error = CacheWriteError.from_exc("Error in cache file write.")
                raise e
            finally:
                print "Cache file write callback done."
                fill_cache_query_cb.done = True
            
            return
        
        fill_cache_query_cb.error = None
        self.register_callback(PyCallback.Query, fill_cache_query_cb)
        try:
            fill_cache_query_cb.done = False
            
            print "Calling QueryApi({})".format(page)
            self._steam_manager.QueryApi(page)
            
            reps = 0
            while not fill_cache_query_cb.done:
                print "Waiting for cache callback, rep {}".format(int(reps))
                reps += 1
                time.sleep(1)
            print "Done cache callback"
            
            if fill_cache_query_cb.error is not None:
                raise fill_cache_query_cb.error
            
            return
        
        finally:
            self.unregister_callback(PyCallback.Query, fill_cache_query_cb)
    
    def QueryApi(self, page):
        """Gets steam_manager's QueryApi(page), using the cache if available and not stale.
                Cache becomes stale after 15 minutes from being written (see self.is_file_stale()),
                After which the problematic one should also be stale and not fail the program.
           :raises CacheWriteError If the cache write callback raises an exception, containing the exception raised and it's traceback.
                        Note that this is the only difference in interface between this and steam_manager's version,
                        As errors in the cache callback prevent the much-needed caching, and are therefore severe.
        """
        
        print "Called cached queryAPI with page={}".format(page)
        
        # Get most recent cache file if exists
        cache_file_name = self.get_cache_filename(page)
        
        print "cache file is: \"{}\"".format(cache_file_name)
        
        # Check if cache file is available for use, and try to reclaim it if it is detected as a non-file entity.
        is_cache_availbable = False
        if os.path.exists(cache_file_name):
            print "cache file Exists"
            if os.path.isfile(cache_file_name):
                print "cache file is a file"
                is_cache_availbable = not self.is_file_stale(cache_file_name)
            elif os.path.islink(cache_file_name):
                print "cache file is a link to dir"
                os.unlink(cache_file_name) # Clear symlink to directory in the position of the cache file...
            else:
                print "cache file is a dir"
                shutil.rmtree(cache_file_name) # Clear directory in the position of the cache file...
        
        
        if is_cache_availbable:
            print "Using cache file"
            
            # There are 2 things that need to be ensured so that the json load will work like it should:
            #   1. Fields of the steamhandler.WorkshopData should be accessible via attribute name.
            #   2. Strings need to be utf-8 encoded string objects, and not unicode objects like json wishes.
            # Both of these things are ensured by workshop_data_hook:
            #   1. Values are put into an AttributeDict, which makes __getattr__ call __getitem__.
            #       This is preferred over, say, the WorkshopData, as it allows us to easily store and retrieve data using key: value pairs,
            #       Which avoids any and all issues with data getting mixed up in order.
            #   2. Both keys and values are encoded into utf-8 str's, which makes them behave appropriately.
            #       This is needed as json (as is logical) creates unicode objects, while Ren'py expects str's.
            
            def workshop_data_hook(obj):
                return AttributeDict({k.encode('utf-8') if isinstance(k, unicode) else k:
                                      v.encode('utf-8') if isinstance(v, unicode) else v
                                        for k, v in obj})
            
            # Read cache file
            print "Reading cache file \"{}\"".format(cache_file_name)
            with open(cache_file_name, "r") as cache_file:
                file_data = json.load(cache_file, encoding="utf-8", object_pairs_hook=workshop_data_hook)
            arr_len = file_data["len"]
            array = file_data["data"]
            print arr_len
            
            # Thread is used to match the behaviour of QueryApi, where the function returns quickly and before the callbacks are called
            qapi_thread = ManagedThread(holder=self._active_threads, lock=self._active_threads_lock, target=self._steam_manager.query_callback, kwargs={"array": array, "arr_len": arr_len})
            qapi_thread.start()
        else:
            print "Not using cache file"
            self._CallQueryApi(page)
        return
    
    
    
    def GetSubscribedItems(self):
        return self._steam_manager.GetSubscribedItems()
    
    def GetAllItems(self, get_all=False):
        
        # Implemented here with a performance boost (see commented out print of item),
        #  And with fix to overzealous repeat calls
        #  Implementation is also needed as this uses QueryApi, so we need to ensure that the fixed one is used.
        
        # It seems the only way the callback can access these variables is through global variables
        # Be careful!
        results = []
        
        def cb(array, arr_len):
            print "Recieve items..."
            cb.complete = False
            # Querying a page is 50 results maximum
            if arr_len == 51:
                cb.should_run_next = False
                cb.complete = True
                return
            
            for x in range(arr_len):
                item = array[x]
                if get_all:
                    all_data = copy.deepcopy((item.m_nPublishedFileId, item.m_eResult, item.m_eFileType,
                                              item.m_nCreatorAppID, item.m_nConsumerAppID, item.m_rgchTitle,
                                              item.m_rgchDescription, item.m_ulSteamIDOwner, item.m_rtimeCreated,
                                              item.m_rtimeUpdated, item.m_rtimeAddedToUserList, item.m_eVisibility,
                                              item.m_bBanned, item.m_bAcceptedForUse, item.m_bTagsTruncated,
                                              item.m_rgchTags, item.m_hFile, item.m_hPreviewFile, item.m_pchFileName,
                                              item.m_nFileSize, item.m_nPreviewFileSize, item.m_rgchURL, item.m_unVotesUp,
                                              item.m_unVotesDown, item.m_flScore, item.m_unNumChildren,
                                              item.m_pchPreviewLink, item.m_metadata))
                    results.append(all_data)
                else:
                    not_all_data = copy.deepcopy((item.m_nPublishedFileId, item.m_rgchTitle, item.m_ulSteamIDOwner,
                                                  item.m_rgchDescription, item.m_pchPreviewLink, item.m_rtimeCreated,
                                                  item.m_rtimeUpdated, item.m_metadata))
                    results.append(not_all_data)
            
            cb.should_run_next = (arr_len == 50)
            cb.i += 1
            cb.complete = True
            return
        
        cb.should_run_next = True
        cb.i = 1
        cb.complete = False
        
        self.register_callback(PyCallback.Query, cb)
        try:
            while cb.should_run_next:
                cb.complete = False # Important! make sure that consecutive runs don't claim that the function is already finished!
                self.QueryApi(cb.i)
                
                # Block
                while not cb.complete:
                    pass
        finally: # Ensure that the callback will be unregistered
            self.unregister_callback(PyCallback.Query, cb)
        
        if not get_all:
            adj_results = []
            for i, item in enumerate(results):
                print "Getting persona", i, item[1] #, item # Printing full items made this ~100x slower...
                item = list(item)
                item[2] = self.GetPersona(item[2])
                adj_results.append(tuple(item))
            results = adj_results
        
        return results
    
    
    def GetItemFromID(self, id):
        return self._steam_manager.GetItemFromID(id)
    
    @cache
    def GetPersona(self, id):
        return self._steam_manager.GetPersona(id)
    
    @cache
    def GetItemDownloadInfo(self, id):
        return self._steam_manager.GetItemDownloadInfo(id)





def get_instance():
    global _cached_instance
    
    if "_cached_instance" not in globals():
        _cached_instance = CachedSteamMgr(steamhandler.get_instance())
    
    return _cached_instance