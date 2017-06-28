"""This file is free software under the GPLv3 license"""
import sys

import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    """
        Post-True Scene
    """
    def mod_info(self):
        return ("post_true", "v1.0", "")

    def mod_load(self):
        # get the label, attach it to the post_true ending node
        endLabel = modast.find_label("post_true_main")
        ml.ending_hooks.hook_post_true_ending(endLabel)

    def mod_complete(self):
        pass
