from modclass import Mod, loadable_mod

@loadable_mod
class Test(Mod):
	def mod_info(self):
	    return ("Test", "v1.0", "scrlys")

