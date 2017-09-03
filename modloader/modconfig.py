"""This file is free software under the GPLv3 license"""
import sys
import os
import shutil

from renpy.display.core import Displayable
from renpy.display.render import Render, render
import renpy
from renpy.audio.music import stop as _stop_music
import renpy.game
from renpy.text.text import Text
from renpy.display.imagelike import Solid

from modloader.modinfo import get_mods


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
