"""This file is free software under the MIT license"""
# pylint: disable=invalid-name

import os.path
from os import listdir
from collections import defaultdict
try:
    import renpy.config
except AttributeError:
    # Building documentation
    pass


modlist = {}
moddirnames = []
mod_load_order = []

# Error catching: if the same name is repeated,
# save the old copies so we can report a detailed error.
overloaded_mod_names = defaultdict(list)

def add_mod(mod_name, mod):
    """Add a mod in the registry"""
    print "Adding mod {}".format(mod_name)
    if mod_name in modlist:
        print("IMPORT ISSUE: Given a mod name of {0!r} by both {1!r} and {2!r}.".format(mod_name, modlist[mod_name].__module__, mod.__module__))
        overloaded_mod_names[mod_name].append(modlist[mod_name])
    modlist[mod_name] = mod


def get_mods():
    """Get the mods in the registry"""
    if overloaded_mod_names:
        # Error: can't have multiple mods with the same name.
        # Report the error now, as we've likely finished
        # importing all mods, so have captured the full issue.
        from modloader import report_mod_errors
        complete_overloads = {
            mod_name: mod_classes + [modlist[mod_name]] for mod_name, mod_classes in overloaded_mod_names.items()
        }
        formatted_overloads = {
            mod_name: " and ".join("{0!r}".format(mod_class.__module__) for mod_class in mod_classes) for mod_name, mod_classes in complete_overloads.items()
        }
        report_mod_errors(
            "While importing mods, ones with the same name were installed in multiple folders.\n\n"
            + "\n".join("  Mods named {0!r} were installed in {1}".format(mod_name, formatted_overload_list) for mod_name, formatted_overload_list in formatted_overloads.items())
            + "\n\nPlease remove the duplicated mods or change the names in their metadata."
        )
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
