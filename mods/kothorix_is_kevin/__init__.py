"""This file is free software under the GPLv3 license"""
import renpy
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    """Replaces Kevin scenes with Kothorix"""
    def mod_info(self):
        return ("Kothorix_mod", "v0.1", "AdamJ1664")

    def mod_load(self):
        home_hook = ml.get_home_hook()

        kothorix_date_scene = modast.find_label("Kothorix_mod_date")
        kothorix_date_initalize = modast.find_label("KothorixDate_init")

        home_hook.hook_chapter_1(kothorix_date_initalize)
        home_hook.add_route("Meet with Kothorix.", kothorix_date_scene, "MeetKothorix == 1 and KothorixDated < 1")


        found = modast.search_for_node_type(modast.find_label("c4hatchery"), ast.Scene, 20)
        golab = modast.find_label("Kothorix_mod")
        hook = modast.hook_opcode(found, None)
        modast.call_hook(found, golab, None)
        hook.chain(modast.search_for_node_type(found, ast.Scene))


        ending_hooks = ml.get_ending_hooks()
        true_search = ending_hooks.get_post_izumi_node()

        def kevin_cb(node):
            """Check if ``node`` is the node that we see Kevin

            Args:
                node (Node): The current node

            See also:
                :meth:`modloader.modlib.AWSWModBase.search_post_node_callback`
            """
            # Python does short-circuit evaluation; we don't evaluate the next boolean
            # statement if the current one isn't true. So in our case, if node.next is None,
            # we don't calculate if node.next is an instance of Show. Similarly, if node.next is
            # not None but it isn't an instance of Show, we don't check the imspec of the object
            if node.next is not None and isinstance(node.next, renpy.ast.Show) \
                and node.next.imspec[0][0] == 'meetingkevin':
                return True

            kevin_credits = modast.search_for_node_with_criteria(true_search, kevin_cb, 800)
            kevin_credits.chain(modast.search_for_node_type(kevin_credits, ast.Scene))

    def mod_complete(self):
        pass
