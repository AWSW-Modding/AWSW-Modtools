import renpy
import renpy.ast as ast
from modloader.modlib import base as ml
from modloader.modlib import sprnt
from modloader.modclass import loadable_mod, Mod

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("bryce_6thscene", "v0.1", "")
        
    def mod_load(self):
        menuNode = ml.findMenu(["Accept.", "Reject.", "Scream."])[0] # Find a menu with the options in this list, grab the first result since we know there's only going to be one. 
        bryce_menu = ml.getMenuHook(menuNode) #Initialize a menu hook for this menu.
        nodes = bryce_menu.getOptionCode("Accept.") # Get the list of nodes that are run when the user presses "Accept."


        # This is where modding gets tricky. There are many different ways to accomplish this, but this is the one I chose. 
        # What we want is the instruction before the "return to apartment menu" if-case so we can hook it and pass execution to our code.
        # We accomplish that by searching for a pattern of instructions. 
        hookNode = ml.searchPostNode(nodes[0], ast.Python) # Find the first python statement in the accept block. This corresponds to "$ mp.bryceromance = True" in the source code.


        # Search five statements ahead to get to the last python statement(the statement before the if block)
        # This is a 1:1 relation to the source code because each statement here does not consist of multiple nodes. "stop music" is one UserStatement node, so it works.
        # If we were dealing with Say instructions, each "say" in the source code corresponds to 3 opcodes in memory, because they are accompanied by StartTranslate and EndTranslate blocks. You would need to compensate for that. 
        hookNode = ml.stepOp(hookNode, 5)


        # For debugging purposes, making sure my math was correct. 
        # This will print out the class name of the found node for verification.
        #sprnt("Found Node" + type(hookNode).__name__)

        # The actual hooking is done here once we've found the point in code we want to redirect. 
        # We redirect hookNode to the bryce_sixthscene label we defined in our additive code. 
        # A "return" statement in the additive code thereafter will return to hookNode+1 and resume normal execution.
        hook = ml.call_hook(hookNode, ml.findlabel("bryce_sixthscene")) 
