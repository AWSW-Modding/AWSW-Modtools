"""Adds a music button that plays a random music file given to it

This file is free software under the GPLv3 license
"""
import os
import random

import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

def song_choice():
    """Returns a random path for music

    Returns:
    A path to a music file
    """
    path = renpy.config.gamedir + "/mods/music_mod/resource/mx"
    music_files = [x for x in os.listdir(path) if x.endswith(('.mp3', '.wav', '.ogg'))]

    if not music_files:
        raise Exception("At least one music file is required.")

    return "mx/" + random.choice(music_files)


@loadable_mod
class AWSWMod(Mod):
    """The music mod class"""
    def mod_info(self):
        return ("meowers' music mod", "v0.1", "meowers!")


    def mod_load(self):
        music_screen = modast.get_slscreen("meowers_music_selection")
        modast.get_slscreen("main_menu").children.append(music_screen)


    def mod_complete(self):
        pass
