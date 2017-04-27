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
    """Anna's post-true scene

    Adds a new scene with Anna after the true ending
    """
    def mod_info(self):
        return ("anna_post_true", "v0.1", "")

    def mod_load(self):
        renpy.config.developer = True

        # Get the label from the new code and hook it to the end
        golab = modast.find_label("anna_post_true_entry")
        ml.ending_hooks.hook_post_true_ending(golab)

        # This is a debug option. If no_fun_allowed is set to true, you don't
        # have to play through the ending to see the scene
        no_fun_allowed = False
        if no_fun_allowed:
            # Fortunately, we can compile renpy code on the fly using :meth:`renpy.parser.parse`
            tocompile = """
            screen dummy:
                imagebutton auto "ui/dev_%s.png" action [Start('anna_post_true_bootstrap'), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.03 yalign 0.88
            """
            compiled_nodes = parser.parse("FNDummy", tocompile)
            target_display = None
            for node in compiled_nodes:
                # Find the init node. This node has all screens to be called when the game starts
                if isinstance(node, ast.Init):
                    # Get the first object in the block member (a list of nodes to be executed)
                    # of the init node. The first object is an object of :class:`renpy.ast.Screen`
                    # We can get the first element because the block always has the Screen node
                    # A Screen node contains a member called ``screen`` which has the actual code
                    # (The actual code is of type :class:`renpy.sl2.slast.SLScreen`)
                    # After getting the code, get the children, which will just contain one
                    # :class:`renpy.sl2.slast.SLDisplayable`, which is what we want
                    target_display = node.block[0].screen.children[0]

            # After getting the SLDisplayable, append that to the main menu screen.
            # That's how we put the button "DEV TEST" on the main menu screen
            modast.get_slscreen('main_menu').children.append(target_display)

    def mod_complete(self):
        pass
