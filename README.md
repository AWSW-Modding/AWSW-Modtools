# AWSW Mod Tools
This project attempts to address issues regarding the extensibility of AWSW code. It allows prospective mod developers to to make dialogue tree changes, to add additional routes, and to modify game behaviour. This project also functions as a *mod loader*, allowing mods to be easily consumed and distributed. 
## Installation
Simply extract bootstrap.rpy, modloader, and mods to the game folder in your AWSW installation. If you're using steam, you can reach the game's root directory by right clicking the entry in your steam library, hitting 'Properties', clicking the 'Local Files' tab, and then clicking 'Browse Local Files'. If you own the DRM-Free version of AWSW, navigate to the folder that the AWSW executable exists in. This will bring you to the root directory of the game. The modloader files should be extracted in game/ and additional mods should be placed in game/mods/.

## Api

To access all the helper functions for modifying game behaviour, put ```import modlib``` at the top of your mod file.  ```modlib``` comes preloaded with a class called ```AWSWModBase``` initialized in the ```base``` member of ```modlib```. It is recommended to redeclare ```base``` as something easy to access in your mod file, such as with ```ml = modlib.base```. Useful functions in the class are listed below. 

#### ```Screen getscreen(string screen_name)```
This gets a Ren'py Screen object(long name: renpy.display.screen.Screen). This is used to get a handle to a screen you might want to edit, such as the status overlay or the main_menu.
#### ```SLScreen getsls(String screen_name)```
getsls is a helper function for getting the executable part of the Screen. This is a tree of SL* objects that Ren'py steps through and executes. You will be hooking and editing these if you're interacting with a screen.
#### ```Node findlabel(string label_name)```
Looks for a label (defined as 'label example:') in the Ren'py language. It will return a renpy.ast.Label object associated with it. 
#### ```Node hooklabel(string label_name, Function func=None)```
Takes a label name and returns an ASTHook object with utilities for hooking the label. ```func``` is called whenever the hook node is executed. Returning True in ```func``` will result in the hook not advancing to the next node. 
#### ```ASTHook hook_opcode(Node node, Function func=None)```
Hooks a node. An instance of ASTHook will be created, chained to ```node```, and returned by this function. After ```node``` executes, the hook will run, and then control flow will will be passed to the hooked node's original next instruction. Set the ```.next``` member to control what statement is called after the hook executes. If ```func``` is passed to ```hook_opcode```, it will be executed when with the hook and can control execution by returning ```True``` and setting ```hook.next```. The hook class will be passed to ```func```.
#### ```ASTHook call_hook(Node node, Node dest_node, Function func=None)```
Hooks a node, then upon execution, jumps to dest_node and pushes the instruction after node to the callstack. Using 'return' in Ren'py code thereafter will return to the node+1 operation. 
#### ```ASTHook jump_ret(Node node, Node dest_node, Node ret_node, func=None```
This will hook ```node```, redirecting execution to dest_node after node is executed. ret_node will be pushed on to the callstack, so calling return after dest_node will pass program execution to ret_node. ```func``` will be executed with the hook as a parameter when the hooking node executes. The hooking node will be returned from this function.
#### ```Node searchPostNode(Node node, NodeClass toFind, int searchLength=200)```
Takes a node (which can be found via findlabel or other functions) and searches for a node proceding it of type toFind. Searches a maximum of searchLength operations, and returns None if the instruction isn't found. 
#### ```Bool nullPyexpr(SLScreen scr, String comparison)```
Takes an SLScreen object and searches for any if statements (SLIf objects) that are direct children of it. Any if statements(and their child blocks) that match the comparison string are removed.
#### ```list findMenu(String comparison)```
#### ```list findMenu(list comparisonList)```
Will search for a Menu with an option that is equal to comparison, or contains all options in comparisonList. Returns a list of menus(ast.Menu) matching the specifications.
#### ```Node findSay(String comparison)```
Searches for a say node(ast.Say) matching the string provided. These can be anything a character says. 
#### ```Node stepOp(Node node, int n)```
Will return the operation that exists n nodes after node. This will skip hooking nodes. 
#### ```Any getRGlobal(key)```
When using '$ myVar = "yyy"' statements in the Ren'py language, the variables are stored in localized dictionary within Ren'py, normally inaccessable to mods. Use this to access the value of a variable with 'key' name. For example, calling modlib.getRGlobal('myVar') would return a string value of "yyy" if the above statement was run.
#### ```setRGlobal(key, value)```
Equivalent to '$ key = value' from within the Ren'py language. Use this to marshal data from your mod to a Ren'py script. 
#### ```AWSWMenuHook getMenuHook(Node menu)```
Returns the AWSWMenuHook class instance for that particular menu. This will allow you to add, remove, or modify choices. 
#### ```AWSWHomeHook getHomeHook()```
Returns the AWSWHomeHook class instance responsible for managing the ambassador apartment.
#### ```AWSWEndingHooks getEndingHooks()```
Returns the AWSWEndingHooks class instance responsible for managing ending hooks. 
#### ```Node findPyStatement(String code)```
Searches the entire game for a single line python statement in Ren'py code. The spaces on the end of the instruction are trimmed by Ren'py, so to find ```$ testVar = True```, pass "testVar = True" to the function. 
## ```class AWSWMenuHook```
The AWSWMenuHook class is responsible for editing a menu, the point in game where the player has options to modify the dialogue tree. After obtaining a reference to a menu node, pass the node into ```getMenuHook``` to access this class's functions. The useful functions are listed below:
#### ```deleteItem(String label)```
Deletes an option from the menu with label title. 
#### ```list getOptionCode(String option)```
This function will return a list of instructions that would be executed if a user were to pick the option matching ```option```. You really only need to acess the first node in the list. Each node is chained to the next, similar to ASTHook.
#### ```getItems()```
Returns a list of all the options in the menu. Each member of the list is a tuple of (String optionTitle, String conditionalStatement, list opcodes).
#### ```setConditional(String label, String newConditional)```
Sets the condition for displaying the option to the player of the option with the title of label. 
#### ```addItem(String label, Node hook, condition="True") ```
#### ```ASTHook addItem(String label, Function hook, condition="True")```
Adds an option to the menu with ```label``` title and ```condition``` condition. If ```hook``` is a node, then when the user selects this option, the game will jump to that node. If hook is a function, an ASTHook instance will be created and returned. The function will be executed when the user selects that option and you will be responsible for redirecting control flow. ```condition``` will be evaluated as a Python expression when the menu is shown. Evaluating as false will mean the menu option doesn't appear to the player. 

#### ```ASTHook addItemCall(String label, Node hook, condition="True")```
Performs the same function as ```addItem``` does with a node, except ```hook``` will be called, meaning you can have a ```return``` instruction to continue normal game execution.
## ```class AWSWHomeHook```
The AWSWHomeHook class is responsible for editing the menu that appears in the Ambassador apartment, where the player can choose a character route. The exposed functions are listed below. 

#### ```addRoute(title, Node destination, condition="True")```
Adds a route to all chapter menus that displays if condition evaluates to true. When the user selects this option, the game will pass control to the destination Node. Executing a return instruction will redirect control back to the menu and continue the game normally. 
#### ```hookChapterChange(Node hook_node)```
#### ```hookChapterChange(Function func)```
If the first argument to this function is a function, it will be called whenever the chapter changes(chapter 1 to chapter 2, etc.). If the first argument is a node, the current instruction will be pushed to the callstack and the game will jump to ```hook_node```. Using the ```return``` statement in Ren'py code will jump back to the original game code. 
#### ```addAnwerMachineCheckHook(Node dest_node)```
#### ```addAnwerMachineCheckHook(Function func)```
Will add a hook to the point where it is determined whether the answering machine dialogue should pop up. If you're passing a node to an additive code label, run ```return True` if the dialogue should pop up, and ```return False``` if it should not. If using a python function, return True if it should show and False if it should not. 
#### ```addAnswerMachineScene(Node dest_node)```
#### ```addAnswerMachineScene(Function func)```
Will add a hook that will be called after the message check returns true. If the first argument is a node, the game will jump to the specified node. Make sure you have a return statement to resume normal execution in this case. If the argument is a function, ```func``` will be called with the hooking node as the only argument. Returning false in this python function will prevent the next instruction from being executed, meaning you'll need to manually jump somewhere next. 
#### ```hookChapter1(Node node)```
Will add a hook after all variables are declared in chapter 1. This is called right after the played enters the ambassador apartment, but before the route menu is displayed. Idea for initializing route variables. The node passed to this function is called when the hook is executed. Use ```return``` in Ren'py code to get back to the game.
## ```class AWSWEndingHooks```
This class is responsible for hooking any ending-related parts of the game. Currently implemented functions of this class are listed below. 

#### ```ASTHook hookPostTrueEnding(Node node)```
This will jump to ```node``` after the true ending final scene. Use ```return``` in the additive code to end your scene, and the game will continue back to the main menu like normal. 

#### ```Node getPostTrueEndingIzumiScene()```
This function will return the node directly after Izumi's "final tear" scene. 
 
#### ```AWSWMenuHooks getEndingPickerMenu()```
This function will return an instance of ```AWSWMenuHooks``` which will allow you to edit the entries in the chapter 5 menu where the player chooses who to go to the fireworks with.

## ```class ASTHook```
The ASTHook class is returned by any of the hooking functions. Its purpose is to all you to modify execution of the game. There are several useful properties on the AST class. First, the ```.next``` member points to the next node that should be executed. This can be set by assigning a node to ```next``` or calling ```chain``` on the class. When the ASTHook node is executed, it checks for a member function called ```hook_func```. If it exists, ```hook_func``` will be executed with the ASTHook class as the first parameter. If ```hook_func``` returns True, the ASTHook will not set the next node. Instead, you must call ```renpy.ast.next_node(Node node)``` manually. This can be used to redirect execution based on circumstances beyond the capabilities of the node alone. 

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

Defining ```def mod_init():``` in the root of your mod file will cause this function to get called after all mods are loaded. This is useful for interaction with other loaded mods, or accessing the ```modinfo``` module to get information about the mods. 

Anywhere in Ren'py code, you can access the global variable ```mod_currentChapter``` to get an integer value of the current chapter. For example, during chapter one, ```mod_currentChapter``` will equal ```1```. During chapter two, it will be equal to ```2```, and so on. This variable is useful for rate limiting routes or events to one per chapter. If you want to access this variable in python, use ```modlib.base.getRGlobal('mod_currentChapter')```.

## Writing Mods

Each mod has two components: the patcher and the additive game code. The patcher will do all the heavily lifting for modification of the game, and the additive game code will be anything that is new to the game. 

To construct a mod, see the tree below.
```
MyMod
|-- mod.py
|-- myResource.rpy
|-- resource
    |-- custbg
        |-- myBackground.png
```

Any *.rpy file is optional, and will be loaded automatically. The main mod file is mandatory for your mod to be loaded, and **must** be named ```mod.py```. Every mod should start with ```import modlib```. This will include all the utilities needed to get started. Using ```modlib``` is as simple as declaring ```ml = modlib.base``` and accessing the class's functions. The ```resource``` folder is optional as well. Files in this folder will be loaded into that game as if they were local to the game/ folder or the root of the archive. Should a file have the same name and location as one in the original game, the mod file will override the original.

## Python and the Dangers of Rollback
Rollback is an integral feature of Ren'py, allowing the user to step back in time and make different choices. Usually rollback will play well with mods, but there are some cases that can introduce non-deterministic behavior. The main issue that rollback has is only Python objects encoded in Ren'Py's AST(and then, only a select few statements) are rolled back. For this reason, Python functions should not be used in hooks if you can avoid them. 

## Steam Updates
The AWSW mod tools do not modify any of the core game files. They will survive and (probably) continue working through most changes to the game's code. Hooking via the stable and recommended methods will ensure that a modification to the game's code does not break your mod. 

## Sample Code

This sample code will remove Kevin's encounter and main menu icon. The full mod structure can be found in mods/. 

```python
import modlib
import renpy
import renpy.ast as ast
ml = modlib.base

found = ml.searchPostNode(ml.findlabel("c4hatchery"), ast.Scene, 20) # search max of 20 nodes after c4hatchery label, look for the first scene initialization (which happens to be one opcode away, for now) 
hook = ml.hook_opcode(found, None) # insert a hooking node after scene, but before the narrator's say statement
hook.chain(ml.searchPostNode(found, ast.Scene)) # normally the hooking node would point back to the dialogue. Skip all the way to the next scene instead. 

mainscr = ml.getsls('main_menu') # get the main screen (cache is disabled)
ml.nullPyexpr(mainscr, 'persistent.playedkevin') # remove the if block
```

See the mods/ and devmods/ folders for further sample code. devmods/ contains a few different examples with fully annotated code. 

## Getting what you want in spite of everyone else. 
Reverse engineering is a fact of life, and while I will do my best to make modding AWSW as painless as possible, it will still need to be done. Luckily, you have all the information you need right here. 

* Extract the archive with Rpatool: [Rpatool](https://github.com/Shizmob/rpatool) 
    Move rpatool into the same folder as archive.rpa (normally located in AWSW's game/ folder) and run with  ```python rpatool.py -x archive.rpa```. It is recommended that you move rpatool and archive.rpa into a subdirectory first, as rpatool extracts the archive into the **current directory**. 
* Decompile rpyc files (the game's code) with unrpyc: [UnRpyc](https://github.com/CensoredUsername/unrpyc)
    Move the contents of the git repository into a folder in the directory where the extracted archive files are. Decompile the rpyc files with ```python unrpyc.py ../*.rpyc```. See how the developers did it. (You'll also need this to figure out the handles for the characters and stock images.)
* Look at the example code!
* Look at the ren'py engine code (just kidding)
* When in doubt, see the the Ren'py docs: [Docs](https://www.renpy.org/doc/html/index.html)
* If none of the above options help: hold tight for the debug overlay, or ask for help!

## How to compile like a pro. 
Instead of manually creating AST Nodes to insert code into the game, or even clunkily creating entries in the rpy language and then jumping to the snippets with the patcher, you can assemble small(or big!) bits of code *in-line* by abusing the Ren'py AST Parser. This means you can get a list of objects and insert them wherever with very little effort. We use this method internally to create the mod information menu on the main screen. See the core mod or the dev_test mod for further details. 

## Debugging
There are several obstacles to developing mods for Ren'py. The first(and biggest) is the fact that the developer has no console to watch for output while running the game! We can fix that by starting AWSW via command line with some switches set. The commands are below.

While in the root directory of the game, run the command for your appropriate operating system:
#### Windows:
```
"lib/windows-i686/python.exe" -EO "Angels with Scaly Wings.py"
```
### Linux x86 (32 bit)
```
./lib/linux-i686/python.exe -EO "Angels with Scaly Wings.py"
```
### Linux x86_64 (64 bit)
```
./lib/linux-x86_64/python.exe -EO "Angels with Scaly Wings.py"
```

Should you print to the console in your code, you may run into an error such as ``` LookupError: unknown encoding: cp437```. This occurs because you're executing a local version of python, which only has utf-8 string encodings loaded in. You can fix this by using ```sprnt``` from ```modlib``` or encoding your string with ```myStr.encode('utf-8')``` before printing. 

## Roadmap

[*] Complete

[!] Important!

[.] In progress

#### Level 1 (usability: barely*)
*You are here. Good luck.*

[\*] \# Modify Renpy screens

[\*] \# Hook interpretted opcodes

[\*] \# Virtual file system for resources 

#### Level 2 (usability: better)
[.] \# Hook Menus

[.] \# Better menu finding algorithm

\# Easy hooking for any instruction type

\# Docs and easy hooking for screen lang objects
#### Level 3 (usability: easy)

[.] # Complete abstraction of apartment menu

[!] # Debug overlay(menu option jump viewing, code peaking, on the fly decompilation)

[*] \# Post true ending hook

\# Post chracter ending hooks

\# Pre ending hooks

\# Ending determination point hook

\# Fine grain character patching

\# Postponing chapters and key game events without manual label lookup

\* results may vary