import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast
import sys

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod


@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("owo what's this?", "v0.1-dev", "scrlys")

    def mod_load(self):
        a4romanceL = modast.find_label("a4romanceL")

        mp_romance = modast.find_python_statement("mp.annaromance = True")
        modast.call_hook(mp_romance, a4romanceL)

    def mod_complete(self): # called after all mods are loaded.
        pass
