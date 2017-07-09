"""This file is free software under the GPLv3 license."""

from types import ModuleType
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


# Credit to Matthew for this code: https://stackoverflow.com/a/17194836/3398583, modified by muddyfish
def rreload(module, modules=None):
    """Recursively reload modules."""
    print "RELOADING", module.__file__
    sys.stdout.flush()
    reload(module)
    if modules is None:
        modules = [module]
    else:
        modules.append(module)
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)
        if type(attribute) is ModuleType:
            if attribute not in modules:
                if get_mod_path() in attribute.__file__:
                    rreload(attribute, modules)


def main(reload_mods=False):
    """Load the mods"""
    # By appending the mod folder to the import path we can do something like
    # `import test` to import the mod named test in the mod folder.
    sys.path.append(get_mod_path())
    # NOTE: To import files in the modloader/ folder, do
    # `from modloader import ...`. If we add the modloader to the path,
    # the modules would be reimported every time they are imported.
    # In most cases, that's fine, but when modinfo is reimported, we lose the
    # current list of mods.

    import testing.test as test
    test.test_tests()

    modinfo.reset_mods()

    modules = []
    for mod in os.listdir(get_mod_path()):
        # Some mods require resources to be recognized by renpy.
        # If a folder exists, force renpy to load it
        resource_dir = os.path.join(get_mod_path(), mod, 'resource')
        if os.path.isdir(resource_dir):
            renpy.config.searchpath.append(resource_dir)

        print "Begin mod load: {}".format(mod)

        # Try importing the mod.
        # Note: This doesn't give my mod functionality. To give the mod
        # function, make a Mod class and apply the loadable_mod decorator
        mod_object = importlib.import_module(mod)
        if reload_mods:
            rreload(mod_object, modules)

    # After all mods are loaded, call their respective mod_complete functions
    for mod_name, mod in modinfo.get_mods().iteritems():
        print "Completing mod {}".format(mod_name)
        mod.mod_complete()

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
