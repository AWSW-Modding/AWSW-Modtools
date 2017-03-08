import os
import sys
import importlib

import renpy

import modinfo

def get_mod_path():
    """Get the mod path

    Returns:
        The full path to the mods folder
    """
    #TODO: Use a path combining function
    return renpy.config.gamedir + "/mods/"

# By setting the import path to the mod folder, we can do something like `import mod`
# NOTE: To import files in the modloader/ folder, do `from modloader import ...`
# If we add the modloader to the path, the modlist would get reloaded again
sys.path.append(get_mod_path())

for mod in os.listdir(get_mod_path()):
    # Some mods require resources to be recognized by renpy. If a folder exist, force renpy to load it
    resource_dir = get_mod_path() + mod + "/resource"
    if os.path.isdir(resource_dir):
        renpy.config.searchpath.append(resource_dir)

    # Try importing the mod. If all goes well, the mod is imported through the Mod class
    try:
        importlib.import_module(mod)
    except Exception, e:
        print("Oh no in {}".format(mod))
        print(e)
        raise e # Raise it again even though the stacktrace provides nothing useful

# After all mods are loaded, call their respective mod_complete functions
for mod_name, mod in modinfo.get_mods().iteritems():
    print("Completing mod {}".format(mod_name))
    mod.mod_complete()
