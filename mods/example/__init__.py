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
        menu = modast.get_slscreen("main_menu")
        addition = modast.get_slscreen("this_is_a_dummy_screen")

        menu.children.append(addition.children[0])

    def mod_complete(self): # called after all mods are loaded.
        pass
