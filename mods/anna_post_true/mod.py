import modlib
from modlib import sprnt
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy
import renpy.ast as ast
import modinfo
import sys

ml = modlib.base

renpy.config.developer = True
golab = ml.findlabel("anna_post_true_entry") # Getting the label from our additive code. 
posttruehook = ml.endingHooks.hookPostTrueEnding(golab) # If we wanted, we could have a scene play post true ending, after credits, but before the return to main_menu. 

NoFunAllowed = False # Set this to true if you don't feel like playing through the true ending to watch the scene.
if NoFunAllowed:       
    tocompile = """
    screen dummy:
        imagebutton auto "ui/dev_%s.png" action [Start('anna_post_true_bootstrap'), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.03 yalign 0.88
    """ # This is ren'py code we want to compile. The parser can accomplish this for us. 
    rv = parser.parse("FNDummy", tocompile) # Assembles an AST for the above code. 
    targetDisp = None
    for e in rv:
        if isinstance(e, ast.Init): # Find the init node. All screens are inserted into this node to be called on game initialization. 
            # Get the first object in the block member of the init node (This is an object of type Screen). The block member is a list of nodes to be executed. 
            # This will just contain the screen node, hence why we can use [0]. We know the screen will always occupy that slot. The screen contains a member called "screen" which is the actual code, the SLScreen. 
            # Access the SLScreen's children, which will just contain one SLDisplayable, our target.
            targetDisp = e.block[0].screen.children[0]
                
    ml.getsls('main_menu').children.append(targetDisp) # Append our compiled SLDisplayable to the main_menu screen. This inserts the 'dev test' button you see. 

