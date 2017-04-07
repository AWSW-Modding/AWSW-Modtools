"""This file is free software under the GPLv3 license."""

import os
import sys
import importlib
import renpy
from modloader import modinfo, modclass

print 'AWSW Mod Loader Init'


def get_mod_path():
    """Get the mod path

    Returns:
        The full path to the mods folder
    """
    return os.path.join(renpy.config.gamedir, "mods")


def main():
    """Load the mods"""
    # By appending the mod folder to the import path we can do something like
    # `import test` to import the mod named test in the mod folder.
    sys.path.append(get_mod_path())
    # NOTE: To import files in the modloader/ folder, do
    # `from modloader import ...`. If we add the modloader to the path,
    # the modules would be reimported every time they are imported.
    # In most cases, that's fine, but when modinfo is reimported, we lose the
    # current list of mods.

    for mod in os.listdir(get_mod_path()):
        # Some mods require resources to be recognized by renpy.
        # If a folder exists, force renpy to load it
        resource_dir = get_mod_path() + mod + "/resource"
        if os.path.isdir(resource_dir):
            renpy.config.searchpath.append(resource_dir)

        print "Begin mod load: {}".format(mod)

        # Try importing the mod.
        # Note: This doesn't give my mod functionality. To give the mod
        # function, make a Mod class and apply the loadable_mod decorator
        mod_object = importlib.import_module(mod)

        # Put the mod into the registry if it doesn't already exist
        # This is for legacy detection of the previous mod importation system
        # Avoid using this as it might get removed in later commits
        mods = modinfo.get_mods()
        if not any(mods[key][4] == mod_object for key in mods):
            info = (None, "", "", "", mod_object)
            modinfo.add_mod(mod_object.__name__, info)

    # After all mods are loaded, call their respective mod_complete functions
    for mod_name, mod_data in modinfo.get_mods().iteritems():
        if mod_data[0]:
            print "Completing mod {}".format(mod_name)
            mod_data[0].mod_complete()

    # Force renpy to reindex all game files
    renpy.loader.old_config_archives = None

# When we build the documentation, renpy.config.gamedir will not exist
# However, when the game is ran, it will exist. We take abuse of that

try:
    _ = renpy.config.gamedir
    BUILDING_DOCUMENTATION = False
except AttributeError:
    BUILDING_DOCUMENTATION = True

if not BUILDING_DOCUMENTATION:
    main()
