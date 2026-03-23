"""This file is free software under the GPLv3 license"""
import sys
import os

import subprocess
import shutil
from urllib2 import urlopen
import json
from cStringIO import StringIO
import zipfile
from collections import namedtuple
import threading

import renpy
from renpy.audio.music import stop as _stop_music
import renpy.game
from renpy.ui import Action
from renpy.exports import show_screen

from modloader.modinfo import get_mods
from modloader import get_mod_path, workshop_enabled
if workshop_enabled:
    from steam_workshop.steam_config import has_valid_signature, MODTOOLS_ID
    import steam_workshop.steamhandler as steamhandler
    import steamhandler_extensions


BRANCHES_API = "https://api.github.com/repos/AWSW-Modding/AWSW-Modtools/branches"
ZIP_LOCATION = "https://github.com/AWSW-Modding/AWSW-Modtools/archive/{mod_name}.zip"

#steammgr = steamhandler.get_instance()


def cache(function):
    def inner():
        if not hasattr(function, "results"):
            function.results = function()
        return function.results
    return inner


def show_message(message, bg="#3485e7", fg="#fff", stop_music=True):
    if stop_music:
        _stop_music()
    for i in renpy.config.layers:
        renpy.game.context().scene_lists.clear(i)
    show_screen("message", message, bg, fg, _layer="screens")


def report_exception(overview, error_str):
    if workshop_enabled:
        print "Reporting exception"
        steammgr = steamhandler.get_instance()
        if steammgr.InitSuccess:
            exception_str = "{}\n{}".format(overview, error_str)
            #steammgr.HandleException(exception_str)


def remove_mod(mod_name, filename):
    """Remove a mod from the game and reload.

    Args:
        mod_name (str): The internal name of the mod to be removed
    """
    show_message("Removing mod {}...".format(mod_name))
    if filename is False:
        mod_class = get_mods()[mod_name]
        mod_folder = mod_class.__module__
    elif filename is True:
        mod_folder = mod_name
    else:
        mod_folder = filename
    if mod_folder.isdigit():
        steammgr = steamhandler.get_instance()
        steammgr.Unsubscribe(int(mod_folder))
    shutil.rmtree(os.path.join(os.path.normpath(renpy.config.gamedir), "mods", mod_folder))
    print "Sucessfully removed {}, reloading".format(mod_name)
    sys.stdout.flush()
    show_message("Reloading game...")
    _stop_music("modmenu_music")
    renpy.exports.reload_script()


@cache
def github_downloadable_mods():
    url_f = urlopen(BRANCHES_API)
    branches = json.load(url_f)
    url_f.close()
    data = []
    for branch in branches:
        name = branch["name"]
        if name.startswith("mod-"):
            data.append([
                ZIP_LOCATION.format(mod_name=name),
                name.replace("mod-", "", 1).encode("utf-8"),
                "DummyAuthor",
                "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?",
                "http://s-media-cache-ak0.pinimg.com/originals/42/41/90/424190c7f88c514a1c26a79572d61191.png"
            ])
    return sorted(data, key=lambda mod: mod[1].lower())


class TimeoutError(Exception):
    """Represents a timeout for waiting for a load. mostly allows the timeout parameter in the get() method, to differentiate between a timeout and a failure."""
    pass

class SteamModlist:
    """Manages the steam modlist, as is gotten by the steam_downloadable_mods method.
    It supports loading the modlist in a separate thread via the load method,
    And caching such results.
    This is needed as loading the modlist takes quite a while,
      And is an operation we would much rather do at startup, without delaying anything else.
    Any exceptions raised in the loading process will be available through the get() method.
    Once the load finishes, get() will either return a value (if no exception was raised during loading), or raise the exception raised during loading.
    """
    
    def __init__(self):
        self._loading_thread = None
        self._loading_thread_lock = threading.Lock()
        self._loaded_data = None
        self._exception = None
        self._is_loaded = threading.Event()
        return
    
    def _loading_function(self):
        """Loads and verifies the steam modlist data.
        It must take no arguments, and return a single value: the loaded data.
        It may raise an exception, in which case it'll be stored in self._exception.
        """
        
        # A different format,
        # (id, mod_name, author, desc, image_url)
        
        # This uses GetAllItems(), Which is affected by the QueryApi crash.
        #   therefore, steamhandler_extensions are preferred
        mods = []
        for mod in sorted(steamhandler_extensions.get_instance().GetAllItems(), key=lambda mod: mod[1]):
            if mod[0] == MODTOOLS_ID:
                continue  # The modtools themselves need not be here (as they're already present and can't be removed using themselves), nor should the signing system complain about them...
            file_id = mod[0]
            create_time, modify_time, signature = mod[5:8]
            is_valid, verified = has_valid_signature(file_id, create_time, modify_time, signature)
            if is_valid:
                mods.append(list(mod[:5]))
                mods[-1][3] += "\n\nVerified by {}".format(verified.username.replace("<postmaster@example.com>", ""))
            else:
                print "NOT VALID SIG", mod[1]  # Note: printing only the mod name, instead of the whole thing SIGNIFICANTLY speeds up this call
        return mods
    
    def _load_and_set(self):
        """Calls the _loading_function and sets the internal values based on its results."""
        try:
            mods = self._loading_function()
            self._loaded_data = mods
            print "Finished steam modlist load without errors"
        except Exception as e:
            print "Finished steam modlist load with errors"
            self._exception = e
            self._exception.traceback = sys.exc_info()[2]
        
        self._is_loaded.set()
        print "Done loading steam modlist"
        return
    
    def load(self):
        """Starts loading the steam modlist data if it is not already being loaded.
        This method starts a thread which loads the modlist data.
        It guarantees that for any number of repeated calls to it from any number of threads, only one loading thread will be started.
        Once the data is loaded, it is available through the get method.
        """
        with self._loading_thread_lock:
            if self._loading_thread is None:
                print "Steam modlist thread not present, Starting..."
                self._loading_thread = threading.Thread(target=self._load_and_set, name=u"Thread-load-SteamModlist")
                self._loading_thread.start()
            else:
                print "Steam modlist thread already present"
        return self._loading_thread
    
    def get(self, timeout=None):
        """Get the steam modlist data.
        If the data has already loaded, this method returns with it immediately,
        Otherwise, load() is called, and this method blocks using self.wait(timeout).
        :returns steam modlist data, If timeout has not been reached and the loading thread has not raised an error.
        :raises Exception, If timeout has not been reached and the loading thread has raised an error. this raises that very exception.
        :raises TimeoutError, If timeout has been reached.
        """
        if self.is_loaded():
            # Note: while the value of is_done can change between checking it here and referring to _loaded_data,
            #  It can only change from False to True.
            #  In that case the load() method has been called before and is currently finishing,
            #  And it'll be called again here, ignored, and _is_loaded will be waited upon, which will finish only once _loaded_data is available.
            
            print "Steam modlist data already available"
        else:
            print "Steam modlist data not available, calling load"
            self.load()
            self.wait(timeout)
            print "Loading done, fetching data"
        
        if self._exception is not None:
            raise self._exception
        
        return self._loaded_data
    
    def is_loaded(self):
        return self._is_loaded.is_set()
    
    def wait(self, timeout=None):
        """Waits for timeout seconds until loading is finished. if timeout is None (default), waits indefinitely until loading is finished.
        :returns None if loading is finished before timeout elapsed.
        :raises TimeoutError if timeout has expired before loading is finished."""
        if not self._is_loaded.wait(timeout):
            raise TimeoutError(type(self).__name__)
        return


steam_mod_list = SteamModlist()


def steam_downloadable_mods():
    return steam_mod_list.get()


def download_github_mod(download_link, name, show_download=True, reload_script=True):
    if show_download:
        show_message("Downloading {}".format(name))
    mod_folder = os.path.join(get_mod_path(), name)
    if os.path.exists(mod_folder):
        shutil.rmtree(mod_folder, ignore_errors=True)
    request = urlopen(download_link)
    zip_f = zipfile.ZipFile(StringIO(request.read()))
    zip_f.extractall(get_mod_path())
    root = zip_f.namelist()[0]
    os.rename(os.path.join(get_mod_path(), root),
              mod_folder)
    if reload_script:
        show_message("Reloading Game...")
        restart_python()
    

def download_steam_mod(id, name, reload_script=True):
    steammgr = steamhandler.get_instance()
    # (id, mod_name, author, desc, image_url)
    for i in renpy.config.layers:
        renpy.game.context().scene_lists.clear(i)
    show_screen("_modloader_download_screen", id, _layer="screens")
    
    def cb(item, success):
        # Copy the folder
        src = item[0].filepath
        dest = os.path.join(os.getcwd(), "game", "mods", str(item[0].itemID))
        shutil.copytree(src, dest)

        steammgr.unregister_callback(steamhandler.PyCallback.Download, cb)
        if reload_script:
            restart_python()
    
    steammgr.register_callback(steamhandler.PyCallback.Download, cb)
    steammgr.Subscribe(id)


class UpdateModtools(Action):
    def __init__(self):
        pass

    def __call__(self):
        update_modtools("https://github.com/AWSW-Modding/AWSW-Modtools/archive/develop.zip")


def update_modtools(download_link):
    print "Updating modtools..."
    print "Saving new version..."
    request = urlopen(download_link)
    with open(os.path.join(renpy.config.gamedir, "modtools-update.zip"), "wb") as zip_f:
        zip_f.write(request.read())
    request.close()

    with open(os.path.join(renpy.config.gamedir, "modloader", "modtools_files.json")) as json_f:
        modtools_files = json.load(json_f)
    for rel_path in modtools_files[0]:
        fullpath = os.path.join(renpy.config.gamedir, rel_path)
        if os.path.exists(fullpath):
            if os.path.isdir(fullpath):
                shutil.rmtree(fullpath)
            else:
                os.remove(fullpath)
    print "Writing bootloader..."
    zip_f = zipfile.ZipFile(os.path.join(renpy.config.gamedir, "modtools-updater.rpe"), 'w', zipfile.ZIP_DEFLATED)
    zip_f.write(os.path.join(renpy.config.gamedir, "modloader", "modtools_update_script.py"), "autorun.py")
    zip_f.close()
    restart_python()


def restart_python():
    print "Restarting..."
    if sys.platform.startswith('win'):
        subprocess.Popen([sys.executable, "-O", sys.argv[0]],
                         creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        with open("stdout.txt", "wb") as out, open("stderr.txt", "wb") as err:
            subprocess.Popen([sys.executable, "-O", sys.argv[0]],
                             preexec_fn=os.setpgrp,
                             stdout=out,
                             stderr=err)
    print "Exiting"
    os._exit(0)


def report_duplicate_labels():
    renpy.parser.parse_errors = renpy.game.script.duplicate_labels
    if renpy.parser.report_parse_errors():
        raise SystemExit(-1)

try:
    import ssl
except ImportError:
    start_callbacks = renpy.python.store_dicts["store"]["config"].start_callbacks
    installing_mods = next((func for func in start_callbacks if func.__name__ == "steam_callback"), None)
    if not installing_mods:
        # If there are download callbacks, we're in the middle of updating
        from modloader.fix_ssl import fix_ssl
        fix_ssl()
        restart_python()