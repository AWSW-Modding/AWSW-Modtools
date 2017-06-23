Writing Mods
============

Each mod has two components: the patcher and the additive game code. The patcher will do all the heavily lifting for modification of the game, and the additive game code will be anything that is new to the game. 

To construct a mod, see the tree below.

::

    MyMod
    |-- __init__.py
    |-- myResource.rpy
    |-- resource
        |-- custbg
            |-- myBackground.png

Any \*.rpy file is optional, and will be loaded automatically. The main mod file is mandatory for your mod to be loaded, and **must** be named ``__init__.py``. Every mod should start with ``from modloader.modlib import base as ml``. This will include all the utilities needed to get started. Using ``modlib`` is as simple as calling functions on ``ml``. The ``resource`` folder is optional as well. Files in this folder will be loaded into that game as if they were local to the game/ folder or the root of the archive. Should a file have the same name and location as one in the original game, the mod file will override the original.

To get full functionality from the modloader, it is recommended that you inherit from the modclass.Mod class. This will give you access to hooks at various stages during mod loading, and properly inform the user of your mod's status. To do this, include ``from modloader.modclass import Mod, loadable_mod`` at the top of your mod file. Define a class with a decorator as shown below:

.. code:: python

    @loadable_mod
    class AWSWMod(Mod):
        def mod_info(self):
            return ("MyModName", "v0.1", "AuthorName")

        def mod_load(self): # called immediately after loading. Most code should go here. 
            pass

        def mod_complete(self): # called after all mods are loaded. 
            pass

However, to make a NSFW mod, it's slightly different.

.. code:: python

    @loadable_mod
    class AWSWMod(Mod):
        def mod_info(self):
            return ("MyModName", "v0.1", "AuthorName", True)

        def mod_load(self): # called immediately after loading. Most code should go here. 
            pass

        def mod_complete(self): # called after all mods are loaded. 
            pass

Please notice the tuple has a new fourth element that is True. If the fourth element is True, that indicates to the modloader to display a simple warning to people who want to enable or disable NSFW scenes.

Python and the Dangers of Rollback
----------------------------------

Rollback is an integral feature of Ren'py, allowing the user to step back in time and make different choices. Usually rollback will play well with mods, but there are some cases that can introduce non-deterministic behavior. The main issue that rollback has is only Python objects encoded in Ren'Py's AST(and then, only a select few statements) are rolled back. For this reason, Python functions should not be used in hooks if you can avoid them. 

Steam Updates
-------------

The AWSW mod tools do not modify any of the core game files. They will survive and (probably) continue working through most changes to the game's code. Hooking via the stable and recommended methods will ensure that a modification to the game's code does not break your mod. 

How to compile like a pro.
--------------------------

Instead of manually creating AST Nodes to insert code into the game, or even clunkily creating entries in the rpy language and then jumping to the snippets with the patcher, you can assemble small(or big!) bits of code *in-line* by abusing the Ren'py AST Parser. This means you can get a list of objects and insert them wherever with very little effort. We use this method internally to create the mod information menu on the main screen. See the core mod or the dev_test mod for further details. 

Debugging
---------

There are several obstacles to developing mods for Ren'py. The first(and biggest) is the fact that the developer has no console to watch for output while running the game! We can fix that by starting AWSW via command line with some switches set. The commands are below.

While in the root directory of the game, run the command for your appropriate operating system:

Windows
~~~~~~~
``"lib/windows-i686/python.exe" -EO "Angels with Scaly Wings.py"``

Linux x86 (32 bit)
~~~~~~~~~~~~~~~~~~
``./lib/linux-i686/python -EO "Angels with Scaly Wings.py"``

Linux x86_64 (64 bit)
~~~~~~~~~~~~~~~~~~~~~

``./lib/linux-x86_64/python -EO "Angels with Scaly Wings.py"``

Should you print to the console in your code, you may run into an error such as ``LookupError: unknown encoding: cp437``.
This occurs because you're executing a local version of python, which only has utf-8 string encodings loaded in. You can fix this by using ``sprnt`` from ``modlib`` or encoding your string with ``myStr.encode('utf-8')`` before printing.


Sample Code
-----------

This sample code will remove Kevin's encounter and main menu icon. The full mod structure can be found in mods/. 

.. code:: python

    import renpy
    import renpy.ast as ast

    from modloader import modinfo, modast
    from modloader.modgame import sprnt
    from modloader.modgame import base as ml # ml shortcut
    from modloader.modclass import Mod, loadable_mod # Import the base class and the decorator

    @loadable_mod
    class AWSWMod(Mod):
        """Removes Kevin from the game"""
        def mod_info(self):
            return ("byekevin", "v0.2", "")

        def mod_load(self):
            found = modast.search_for_node_type(modast.find_label("c4hatchery"), ast.Scene, 20) # search max of 20 nodes after c4hatchery label, look for the first scene initialization (which happens to be one opcode away, for now)
            hook = modast.hook_opcode(found, None) # insert a hooking node after scene, but before the narrator's say statement
            hook.chain(modast.search_for_node_type(found, ast.Scene)) # normally the hooking node would point back to the dialogue. Skip all the way to the next scene instead.

            mainscr = modast.get_slscreen('main_menu') # get the main screen (cache is disabled)
            modast.remove_slif(mainscr, 'persistent.playedkevin') # remove Kevin from the persistent file

            ending_hooks = ml.get_ending_hooks()
            true_search = ending_hooks.get_post_izumi_node()

            def kevin_cb(node):
                if node.next is not None and isinstance(node.next, renpy.ast.Show)
                    and node.next.imspec[0][0] == 'meetingkevin': # imspec is part of the image ID in show opcodes.
                    return True

            kevin_credits = modast.search_for_node_with_criteria(true_search, kevin_cb, 800) # search for a node using the kevinCB callback.
            kevin_credits.chain(modast.search_for_node_type(kevin_credits, ast.Scene)) # Show and with are separate instructions.

        def mod_complete(self):
            pass

See the mods/ and devmods/ folders for further sample code. devmods/ contains a few different examples with fully annotated code. 

