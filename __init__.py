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
        return ("adine_holla_dolla", "v0.1", ":^)")

    def mod_load(self):
        hookNode = modast.search_for_node_type(modast.find_say("We probably should be getting you some real help.").next, ast.Scene, 500)
        adine_scene = modast.find_label("adine_shopping")
        hook = modast.call_hook(hookNode, adine_scene)

    def mod_complete(self):
        pass
