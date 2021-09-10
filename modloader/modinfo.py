"""This file is free software under the MIT license"""
# pylint: disable=invalid-name

import os.path
from os import listdir
try:
    import renpy.config
except AttributeError:
    # Building documentation
    pass


modlist = {}
moddirnames = []


def add_mod(mod_name, mod):
    """Add a mod in the registry"""
    print "Adding mod {}".format(mod_name)
    modlist[mod_name] = mod


def get_mods():
    """Get the mods in the registry"""
    return modlist


def get_mod(mod_name):
    """Get a mod in the registry"""
    if mod_name in modlist:
        return modlist[mod_name]
    else:
        raise KeyError("Mod \"{}\" not found.".format(mod_name))


def has_mod(mod_name):
    """Check if a mod is loaded"""
    return mod_name in modlist


def reset_mods():
    """Remove all mods from the registry"""
    modlist.clear()
    moddirnames[:] = listdir(os.path.join(os.path.normpath(renpy.config.gamedir), "mods"))


def get_mod_folders():
    return moddirnames


def get_mod_folder(mod_name):
    """Get a name of the folder of a mod"""
    return get_mod(mod_name).__module__


def get_mod_path(mod_name):
    """Get a full path of a mod"""
    return os.path.join(os.path.normpath(renpy.config.gamedir), "mods", get_mod(mod_name).__module__)
