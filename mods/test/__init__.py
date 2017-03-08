from modloader.modclass import Mod, loadable_mod

@loadable_mod
class Test(Mod):
    def __init__(self):
        print("Init!")

    def mod_load(self):
        print("Load!")

    def mod_complete(self):
        print("Complete!")

    def mod_unload(self):
        print("Unload!")

    def mod_info(self):
        return ("Test", "v1.0", "scrlys")
