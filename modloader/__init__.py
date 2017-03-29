import renpy
import os
import sys
import modinfo
import importlib
import modinfo
import modclass

print('AWSW Mod Loader Init')
print(__name__)

def get_mod_path():
    """Get the mod path

    Returns:
        The full path to the mods folder
    """
    #TODO: Use a path combining function
    return renpy.config.gamedir + "/mods/"

def main():
    # By setting the import path to the mod folder, we can do something like `import mod`
    # NOTE: To import files in the modloader/ folder, do `from modloader import ...`
    # If we add the modloader to the path, the modlist would get reloaded again
    sys.path.append(get_mod_path())

    for mod in os.listdir(get_mod_path()):
        # Some mods require resources to be recognized by renpy. If a folder exists, force renpy to load it
        resource_dir = get_mod_path() + mod + "/resource"
        if os.path.isdir(resource_dir):
            renpy.config.searchpath.append(resource_dir)

        # Try importing the mod. If all goes well, the mod is imported through the Mod class
        print("Begin mod load: {}".format(mod))

        mod_object = importlib.import_module(mod)

        # Run through registry to see if the mod implements loadable_mod in some way. 
        if not any(modinfo.get_mods()[key][4] == mod_object for key in modinfo.get_mods()):
            modinfo.add_mod(mod_object.__name__, (None, "", "", "", mod_object))

    # After all ods are loaded, call their respective mod_complete functions
    for mod_name, mod_data in modinfo.get_mods().iteritems():
        if mod_data[0]:
            print("Completing mod {}".format(mod_name))
            mod_data[0].mod_complete()

    # force renpy to reindex all game files
    renpy.loader.old_config_archives = None

# Ensure that we have a stable renpy environment.
# The documentation won't have a stable renpy.config.gamedir, but the game will

try:
    renpy.config.gamedir
    main()
except:
    pass
