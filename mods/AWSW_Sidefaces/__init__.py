import renpy
import renpy.ast as ast

from modloader import modinfo
from modloader.modclass import Mod, loadable_mod



@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("AWSW_Sidefaces", "v1.0", "AdamJ1664")

    def mod_load(self):
        pass

    def mod_complete(self):
        pass