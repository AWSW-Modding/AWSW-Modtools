modlist = {}

def add_mod(mod_name, mod):
	print("Adding mod {}".format(mod_name))
	modlist[mod_name] = mod

def get_mods():
    return modlist
