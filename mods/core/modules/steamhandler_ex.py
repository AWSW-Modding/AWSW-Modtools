import os
import shutil
import time
import errno
import cPickle
import threading
from itertools import islice
import copy

from steam_workshop.steamhandler import SteamMgr, PyCallback, cache
from steam_workshop import steamhandler


def _get_mod_resource_dir(filename=__file__):
    """For a given filename which is contained in a mod's modules directory,
        Returns that mod's resource dir path.
        Raises ValueError if filename is not contained in a modules dir."""
    dirpath = os.path.dirname(filename)
    subdir_pos = dirpath.rfind("modules")
    if subdir_pos == -1:
        raise ValueError("filename \"{}\" seems to not be a mod module!".format(filename))
    return os.path.realpath(os.path.join(dirpath[:subdir_pos], "resource"))
    


class CachedSteamMgr:
    """Holds a SteamMgr instance, and caches results of problematic actions (QueryApi, which gets workshop data as a whole, not parts),
    So that calls to them will not fail when done repeatedly.
    In QueryApi's case, This is done to bypass an existing cache which causes failures.
    """
    
    __PAGE_CACHE_DIR = os.path.join(_get_mod_resource_dir(__file__), "page_cache")
    
    def __init__(self, steam_manager):
        if not isinstance(steam_manager, SteamMgr):
            raise TypeError("steam_manager must be a steam_workshop.steamhandler.SteamMgr instance!")
        self._steam_manager = steam_manager
        self.threads = [] # This can create threads in QueryApi, which will persist after the call returns (as is required).
        # We at least keep track of them, so that the dillagent programmer can ensure they're handled properly.
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
        return os.path.join(self.__PAGE_CACHE_DIR, "page_{:02}.pkl".format(page))
    
    
    def _CallQueryApi(self, page):
        """Gets super's QueryApi(page), strictly by calling QueryApi.
        Fills the cache as well, and keeps python thread trapped until cache has been filled."""
        print "Cache callback: Current query callbacks:", "\n".join(str(func) for func in self._steam_manager.Callbacks[PyCallback.Query])
        print "Cache callback: Current persona callbacks:", "\n".join(str(func) for func in self._steam_manager.Callbacks[PyCallback.Persona])
        
        
        def fill_cache_query_cb(array, arr_len):
            try:
                print "Cache callback called with: (len={0}), array={1}".format(arr_len, array)
                
                # Get cache file name
                cache_file_name = self.get_cache_filename(page)
                print "Cache file target: \"{}\"\n".format(cache_file_name)
                
                # Ensure file can be created (ensure directories)
                to_ensure = os.path.dirname(cache_file_name)
                if not os.path.exists(to_ensure):  # If not exists: create
                    os.makedirs(os.path.dirname(cache_file_name))
                elif not os.path.isdir(to_ensure):  # If exists and not dir: problem
                    raise OSError(errno.ENOTDIR, "The attempted directory \"{}\" exists and is not a directory.".format(to_ensure))
                # else: already done
                
                # Write cache file
                with open(cache_file_name, "wb") as cache_file:
                    cPickle.dump(arr_len, cache_file)
                    cPickle.dump(tuple(islice(array, arr_len)), cache_file)
            
            except Exception as e:
                print "Cache callback raised Exception:", str(e)
            finally:
                print "Cache callback done."
                fill_cache_query_cb.done = True
                return
        
        
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
            return
        
        finally:
            self.unregister_callback(PyCallback.Query, fill_cache_query_cb)
            return
    
    def QueryApi(self, page):
        """Gets super's QueryApi(page), using the cache if available and not stale.
                Cache is not stale for about 15 minutes, after which the problematic one should also be stale and not fail the program."""
        
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
            # Read cache file
            print "Reading cahce file \"{}\"".format(cache_file_name)
            with open(cache_file_name, "rb") as cache_file:
                arr_len = cPickle.load(cache_file)
                array = cPickle.load(cache_file)
                print arr_len
            
            # Thread is used to match the behaviour of QueryApi, where the function returns quickly and before the callbacks are called
            qapi_thread = threading.Thread(target=self._steam_manager.query_callback, kwargs={"array": array, "arr_len": arr_len})
            self.threads.append(qapi_thread)
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
        
        while cb.should_run_next:
            cb.complete = False # Important! make sure that consecutive runs don't claim that the function is already finished!
            self.QueryApi(cb.i)
            
            # Block
            while not cb.complete:
                pass
        
        # # Remove duplicates
        # results = {item[0]: item for item in results}.values()
        
        if not get_all:
            adj_results = []
            for i, item in enumerate(results):
                print "Getting persona", i, item[1] #, item # Printing full items made this ~100x slower...
                item = list(item)
                item[2] = self.GetPersona(item[2])
                adj_results.append(tuple(item))
            results = adj_results
        
        self.unregister_callback(PyCallback.Query, cb)
        
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
    
    print "steamhandler_ex id={}".format(id(_cached_instance))
    return _cached_instance