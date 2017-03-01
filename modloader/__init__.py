import renpy
import os
import sys
import imp
import modinfo
import importlib
# So technically anything up here's going to be imported into mods since we're making a copy of our globals. It's safe to import them anyway. 

modinfo.init()
    
def getdir():
    return renpy.config.gamedir

print("AWSW Mod Loader Init")

search_dir = getdir() + "/mods/"
if not os.path.exists(search_dir):
    os.makedirs(search_dir)

sys.path.append(getdir() + "/modloader/")
sys.path.append(getdir() + "/mods/")

loaded_mods = []

for object in os.listdir(search_dir):
    fullpath = search_dir + object
    if os.path.isdir(fullpath):
        for object2 in os.listdir(fullpath):
            modobj = fullpath + '/' + object2
            if object2 == 'mod.py':
                print(('Loaded mod ' + object).encode('utf-8'))
                name = os.path.splitext(os.path.split(modobj)[-1])
                modinfo.modlist.append(object)
                loc = dict()
                glo = dict(globals())
                execfile(modobj, glo, loc) # We want to isolate mods from each other, but give them a copy of our globals so modinfo is not reloaded.
                loaded_mods.append((glo, loc)) # Grab locals so we can initialize the mods later.
            elif object2 == 'resource' and os.path.isdir(modobj):
                renpy.config.searchpath.append(modobj)

for (glo, loc) in loaded_mods:
    if 'mod_init' in loc:
        comb = glo.copy()
        comb.update(loc)
        func = loc['mod_init']
        exec(func.__code__, comb) # This is nasty!
                
# force renpy to reindex all game files
renpy.loader.old_config_archives = None