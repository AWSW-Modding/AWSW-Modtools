"""This file is free software under the GPLv3 license"""
# pylint: disable=invalid-name
modlist = {}


def add_mod(mod_name, mod):
    """Add a mod in the registry"""
    print "Adding mod {}".format(mod_name)
    modlist[mod_name] = mod


def get_mods():
    """Get the mods in the registry"""
    return modlist


def reset_mods():
    modlist.clear()
