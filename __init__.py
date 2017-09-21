import renpy
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod


@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Anna's better ending", "v0.1", "AdamJ1664")

    def mod_load(self):
        source = ml.search_peak_if(modast.find_say("In the weeks that followed, the dragons prepared for the comet."), ast.Scene, 100)
        anna_hook = modast.find_label("wyv_common_anna")
        hook = modast.hook_opcode(source, None)
        modast.call_hook(source, anna_hook, None)
        hook.chain(modast.search_for_node_type(source, ast.Scene))

    def mod_complete(self):
        pass
