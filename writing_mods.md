
## Stubs
This is code you'll probably need to jump to at some point in your additive game code. They are standard Ren'py labels, and can be accessed with ```call stub_label``` or ```jump stub_label```.
#### ```_mod_fixjmp```
Use ```jump _mod_fixjmp``` to access this stub. It will return to the proper chapter menu in the game when you jump to it. You don't need to use this is you're using ```return``` and ```AWSWHomeHook.addRoute```. ```addRoute``` pushes this stub to the callstack automatically. 
#### ```_mod_incc```
This will increment the character scene counter in the game for the appropriate chapter. This needs to be called at the start of every additional route. Use ```call _mod_incc``` to access this stub. 

#### ```_mod_getchapter```
This will get the current chapter as an integer. Access this stub with ```call _mod_getchapter``` and it will put the integer value of the current chapter in ```_return``` for you to check.

#### ```_mod_fixui```
This will need to be called if you're hooking after an ending. The game disables interaction with UI at that point, so as soon as your get control of execution, you must ```call _mod_fixui```. If this is called after a say instruction, or any instruction that waits for user input, the game *will hang*.

## Magic

Anywhere in Ren'py code, you can access the global variable ```mod_currentChapter``` to get an integer value of the current chapter. For example, during chapter one, ```mod_currentChapter``` will equal ```1```. During chapter two, it will be equal to ```2```, and so on. This variable is useful for rate limiting routes or events to one per chapter. If you want to access this variable in python, use ```modlib.base.getRGlobal('mod_currentChapter')```.

## Writing Mods

Each mod has two components: the patcher and the additive game code. The patcher will do all the heavily lifting for modification of the game, and the additive game code will be anything that is new to the game. 

To construct a mod, see the tree below.
```
MyMod
|-- __init__.py
|-- myResource.rpy
|-- resource
    |-- custbg
        |-- myBackground.png
```

Any \*.rpy file is optional, and will be loaded automatically. The main mod file is mandatory for your mod to be loaded, and **must** be named ```__init__.py```. Every mod should start with ```from modloader.modlib import base as ml```. This will include all the utilities needed to get started. Using ```modlib``` is as simple as calling functions on ```ml```. The ```resource``` folder is optional as well. Files in this folder will be loaded into that game as if they were local to the game/ folder or the root of the archive. Should a file have the same name and location as one in the original game, the mod file will override the original.

To get full functionality from the modloader, it is recommended that you inherit from the modclass.Mod class. This will give you access to hooks at various stages during mod loading, and properly inform the user of your mod's status. To do this, include ```from modloader.modclass import Mod, loadable_mod``` at the top of your mod file. Define a class with a decorator as shown below:
```python
@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("MyModName", "v0.1", "AuthorName")
        
    def mod_load(self): # called immediately after loading. Most code should go here. 
        pass
        
    def mod_complete(self): # called after all mods are loaded. 
        pass
```

## Python and the Dangers of Rollback
Rollback is an integral feature of Ren'py, allowing the user to step back in time and make different choices. Usually rollback will play well with mods, but there are some cases that can introduce non-deterministic behavior. The main issue that rollback has is only Python objects encoded in Ren'Py's AST(and then, only a select few statements) are rolled back. For this reason, Python functions should not be used in hooks if you can avoid them. 

## Steam Updates
The AWSW mod tools do not modify any of the core game files. They will survive and (probably) continue working through most changes to the game's code. Hooking via the stable and recommended methods will ensure that a modification to the game's code does not break your mod. 

## Sample Code

This sample code will remove Kevin's encounter and main menu icon. The full mod structure can be found in mods/. 

```python
import renpy
import renpy.ast as ast
from modloader import modinfo
from modloader.modlib import sprnt
from modloader.modlib import base as ml # ml shortcut 
from modloader.modclass import Mod, loadable_mod # Import the base class and the decorator

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("byekevin", "v0.1", "")
        
    def mod_load(self):
        found = ml.searchPostNode(ml.findlabel("c4hatchery"), ast.Scene, 20) # search max of 20 nodes after c4hatchery label, look for the first scene initialization (which happens to be one opcode away, for now) 
        hook = ml.hook_opcode(found, None) # insert a hooking node after scene, but before the narrator's say statement
        hook.chain(ml.searchPostNode(found, ast.Scene)) # normally the hooking node would point back to the dialogue. Skip all the way to the next scene instead. 

        mainscr = ml.getsls('main_menu') # get the main screen (cache is disabled)
        ml.nullPyexpr(mainscr, 'persistent.playedkevin') # remove the if block

        eHooks = ml.getEndingHooks()
        true_search = eHooks.getPostTrueEndingIzumiScene()

        def kevinCB(node):
            if node.next is not None and isinstance(node.next, renpy.ast.Show) and node.next.imspec[0][0] == 'meetingkevin': # imspec is part of the image ID in show opcodes.
                return True

        kevin_credits = ml.searchPostNodeCB(true_search, kevinCB, 800) # search for a node using the kevinCB callback. 
        kevin_credits.chain(ml.searchPostNode(kevin_credits, ast.Scene)) # Show and with are separate instructions.
        
```
See the mods/ and devmods/ folders for further sample code. devmods/ contains a few different examples with fully annotated code. 

