"""This file is free software under the GPLv3 license"""
import sys
import os
import renpy
sys.path.append(os.path.join(renpy.config.gamedir, "modloader", "dll"))
import ssl

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

from modloader.modinfo import get_mods
from modloader import get_mod_path


BRANCHES_API = "https://api.github.com/repos/AWSW-Modding/AWSW-Modtools/branches"
ZIP_LOCATION = "https://github.com/AWSW-Modding/AWSW-Modtools/archive/{mod_name}.zip"


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


def remove_mod(mod_name):
    """Remove a mod from the game and reload.

    Args:
        mod_name (str): The internal name of the mod to be removed
    """
    show_message("Removing mod...")
    mod_class = get_mods()[mod_name]
    mod_folder = mod_class.__module__
    shutil.rmtree(os.path.join(renpy.config.gamedir, "mods", mod_folder))
    print "Sucessfully removed {}, reloading".format(mod_name)
    sys.stdout.flush()

    renpy.exports.reload_script()


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
    return data


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
        renpy.exports.reload_script()
