"""This file is free software under the GPLv3 license"""
# pylint: disable=invalid-name

import os.path
from os import listdir
import renpy.config
#import os.listdir # listdir

modlist = {}

moddirnames = [f for f in listdir(os.path.join(os.path.normpath(renpy.config.gamedir), "mods"))]


def add_mod(mod_name, mod):
    """Add a mod in the registry"""
    print "Adding mod {}".format(mod_name)
    modlist[mod_name] = mod


def get_mods():
    """Get the mods in the registry"""
    return modlist


def reset_mods():
    """Remove all mods from the registry"""
    modlist.clear()

def get_mod_folders():
    return moddirnames
