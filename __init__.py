
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
        return ("TLAMaverick", "v0.1", "Keegen")
        
    def mod_load(self):
        
        label2 = modast.find_label("TLAMaverickStart")
        menu2 = modast.find_menu("I would never do such a thing.")[0]

        print label2
        print menu2

        modast.add_menu_option(menu2, "I have no point in killing you.", label2) #Tatsu Park choice
        
        menu = modast.get_slscreen("main_menu")
        addition = modast.get_slscreen("TLAMaverick_main_menu")

        menu.children.append(addition.children[0])
    
        
    def mod_complete(self):
        pass
    