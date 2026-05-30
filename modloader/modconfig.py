"""This file is free software under the GPLv3 license"""
import sys
import os

import subprocess
import threading
import shutil
from urllib2 import urlopen
import json
from cStringIO import StringIO
import zipfile

import renpy
from renpy.audio.music import stop as _stop_music
import renpy.game
from renpy.ui import Action
from renpy.exports import show_screen

from modloader.modinfo import get_mods
from modloader.preload import Preload
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



def load_steam_modlist():
    """Loads and verifies the steam modlist data."""
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

steam_modlist_preloader = Preload(load_steam_modlist) # As loading the steam modlist is a single-threaded thing, there's no reason to reserve many threads to it...

def steam_downloadable_mods():
    return steam_modlist_preloader.get()


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
    

class ModmapInstallStatus:
    """Holds the install status of a modmap install request in a thread-safe way."""
    
    def __init__(self):
        self._curr_mod_id = None
        
        self._lock = threading.RLock()
        
    def set_curr(self, mod_id):
        with self._lock:
            self._curr_mod_id = mod_id
        return
    
    def get_curr(self):
        with self._lock:
            return self._curr_mod_id
        

def download_steam_mod(id, name, reload_script=True, show_install_screen=True):
    """:returns: done_flag if reload_script is False, else None. done_flag is a threading.Event which becomes set once the mod is installed. note that this return value can end interactions. """
    steammgr = steamhandler.get_instance()
    # (id, mod_name, author, desc, image_url)
    if show_install_screen:
        install_status = ModmapInstallStatus()
        install_status.set_curr(id)
        for i in renpy.config.layers:
            renpy.game.context().scene_lists.clear(i)
        show_screen("_modloader_download_screen", install_status, _layer="screens")

    done_flag = threading.Event()
    
    def cb(item, success):
        # Copy the folder
        src = item[0].filepath
        dest = os.path.join(os.getcwd(), "game", "mods", str(item[0].itemID))
        shutil.copytree(src, dest)

        steammgr.unregister_callback(steamhandler.PyCallback.Download, cb)
        done_flag.set()
        if reload_script:
            restart_python()
    
    steammgr.register_callback(steamhandler.PyCallback.Download, cb)
    steammgr.Subscribe(id)
    
    if reload_script:
        return None
    else:
        return done_flag


def download_steam_mods(modmap, reload_script=True, show_install_screen=True):
    """Download all steam mods in the mod map modmap{modid: modname}
    :returns: done_flag if reload_script is False, else None. done_flag is a threading.Event which becomes set once the mod is installed. note that this return value can end interactions.
    """
    # steammgr = steamhandler.get_instance()
    # # (id, mod_name, author, desc, image_url)
    if show_install_screen:
        install_status = ModmapInstallStatus()
        
        for i in renpy.config.layers:
            renpy.game.context().scene_lists.clear(i)
        show_screen("_modloader_download_screen", install_status, _layer="screens")
    else:
        install_status = None
    
    done_flag = threading.Event()
    
    def _install_loop(modmap, reload_script, install_status, thread_done_flag):
        for modid, modname in modmap.iteritems():
            if install_status is not None:
                install_status.set_curr(modid)
            mod_done_flag = download_steam_mod(modid, modname, reload_script=False, show_install_screen=False)
            mod_done_flag.wait()
        
        thread_done_flag.set()
        
        if reload_script:
            restart_python()
        
        return
    
    threading.Thread(name="download_steam_mods__install_loop", target=_install_loop, args=(modmap, reload_script, install_status, done_flag)).start()
    
    if reload_script:
        return None
    else:
        return done_flag




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