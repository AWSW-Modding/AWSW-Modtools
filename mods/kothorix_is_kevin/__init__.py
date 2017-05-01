import renpy
import renpy.ast as ast
from modloader import modinfo
from modloader.modlib import sprnt
from modloader.modlib import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Kothorix_mod", "v0.1", "AdamJ1664")
        
    def mod_load(self):

        #Kothorix date scene
        home_hook = ml.getHomeHook() #I dont know what this does
        kothorix_date_scene = ml.findlabel("Kothorix_mod_date") #Finds the date label from Kothorix_scene
        kothorix_date_initalize = ml.findlabel("KothorixDate_init") #Finds a label to initalize variables
        home_hook.hookChapter1(kothorix_date_initalize) #This sets up some variables at the start of the game, you need to start a new game for it to work
        #Shows "Meet with Kothorix." when MeetKothorix is set to one (Set to one when you take eggs to the hatchery) and KothorixDated is less that one (set to 1 when you start the scene)
        #When user clicks on "Meet with Kothorix." the date scene from Kothorix_scene will play
        home_hook.addRoute("Meet with Kothorix.", kothorix_date_scene , "MeetKothorix == 1 and KothorixDated < 1")
       
        
        #this part hooks into the scene that spawns kevin and skips it
        found = ml.searchPostNode(ml.findlabel("c4hatchery"), ast.Scene, 20)
        golab = ml.findlabel("Kothorix_mod") # Getting the label from our additive code.
        hook = ml.hook_opcode(found, None)
        ml.call_hook(found, golab, None) 
        hook.chain(ml.searchPostNode(found, ast.Scene))


        #this is what removes kevin from ending credits
        eHooks = ml.getEndingHooks()
        true_search = eHooks.getPostTrueEndingIzumiScene()

        def kevinCB(node):
            if node.next is not None and isinstance(node.next, renpy.ast.Show) and node.next.imspec[0][0] == 'meetingkevin':
                return True

        kevin_credits = ml.searchPostNodeCB(true_search, kevinCB, 800)
        kevin_credits.chain(ml.searchPostNode(kevin_credits, ast.Scene)) # Show and with are separate instructions.
        
    