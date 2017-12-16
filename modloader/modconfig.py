"""This file is free software under the GPLv3 license"""
import sys
import os
import ssl

import subprocess
import shutil
from urllib2 import urlopen
import json
from cStringIO import StringIO
import zipfile
from collections import namedtuple

from renpy.display.core import Displayable
from renpy.display.render import Render, render
import renpy
from renpy.audio.music import stop as _stop_music
import renpy.game
from renpy.text.text import Text
from renpy.display.imagelike import Solid
from renpy.ui import Action

from modloader.modinfo import get_mods
from modloader import get_mod_path


BRANCHES_API = "https://api.github.com/repos/AWSW-Modding/AWSW-Modtools/branches"
ZIP_LOCATION = "https://github.com/AWSW-Modding/AWSW-Modtools/archive/{mod_name}.zip"



def cache(function):
    def inner():
        if not hasattr(function, "results"):
            function.results = function()
        return function.results
    return inner


class MessageDisplayable(Displayable):
    def __init__(self, message, bg, fg, *args, **kwargs):
        super(MessageDisplayable, self).__init__(*args, **kwargs)
        self.message = message
        self.bg = bg
        self.fg = fg

    def render(self, width, height, st, at):
        rv = Render(width, height)

        sr = render(Solid(self.bg), width, height, st, at)
        rv.blit(sr, (0, 0))

        td = Text(self.message, size=32, xalign=0.5, yalign=0.5, color=self.fg, style="_text")
        tr = render(td, width, height, st, at)

        rv.blit(tr, (width/2 - tr.width/2, height/2 - tr.height/2))
        return rv


def show_message(message, bg="#3485e7", fg="#fff", stop_music=True):
    if stop_music:
        _stop_music()
    renpy.game.interface.draw_screen(MessageDisplayable(message, bg, fg), False, True)


def remove_mod(mod_name, filename):
    """Remove a mod from the game and reload.

    Args:
        mod_name (str): The internal name of the mod to be removed
    """
    show_message("Removing mod {}...".format(mod_name))
    if not filename:
        mod_class = get_mods()[mod_name]
        mod_folder = mod_class.__module__
    else:
        mod_folder = mod_name
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
    mod_info = namedtuple("DownloadableModInfo", ["download_link",
                                                  "mod_name",
                                                  "author",
                                                  "description",
                                                  "image"])
    data = []
    for branch in branches:
        name = branch["name"]
        if name.startswith("mod-"):
            data.append(mod_info(ZIP_LOCATION.format(mod_name=name),
                                 name.replace("mod-", "", 1),
                                 "DummyAuthor",
                                 "DummyDescription",
                                 "http://s-media-cache-ak0.pinimg.com/originals/42/41/90/424190c7f88c514a1c26a79572d61191.png"
                                 ))
    return sorted(data, key=lambda s: s.mod_name)


def download_github_mod(name, download_link, show_download=True, reload_script=True):
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
