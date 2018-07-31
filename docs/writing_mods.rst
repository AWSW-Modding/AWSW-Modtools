Writing Mods
============

Each mod has two components: the patcher and the additive game code.
The patcher will do all the heavily lifting for modification of the game, and the additive game code will be anything that is new to the game.

To construct a mod, see the tree below.

::

    MyMod
    |-- __init__.py
    |-- myResource.rpy
    |-- resource
        |-- custbg
            |-- myBackground.png

Any \*.rpy file is optional, and will be loaded automatically.
The main mod file is mandatory for your mod to be loaded, and **must** be named ``__init__.py``.
Every mod should start with ``from modloader.modclass import loadable_mod, Mod``.
This will include all the utilities needed to get started.

Files in the optional ``resource`` folder will be loaded into that game as if they were local to the game/ folder or the root of the archive.

Inheriting from ``Mod `` will give you access to hooks at various stages during mod loading, and properly inform the user of your mod's status.
Define a class with a decorator as shown below:

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

Please notice the tuple has a new fourth element that is True.
If the fourth element is ``True``, that indicates to the modloader to display a simple warning to people who want to enable or disable NSFW scenes.
This notice is **REQUIRED** to have your mod accepted into the Github repository. NSFW mods without the notice will **NOT** be given support.
Note that NSFW mods are not allowed on Steam.

Python and the Dangers of Rollback
----------------------------------

Rollback is an integral feature of Ren'py, allowing the user to step back in time and make different choices.
Usually rollback will play well with mods, but there are some cases that can introduce non-deterministic behavior.
The main issue that rollback has is only Python objects encoded in Ren'Py's AST(and then, only a select few statements) are rolled back.
For this reason, Python functions should not be used in hooks if you can avoid them.

Steam Updates
-------------

The AWSW modtools do not modify any of the core game files.
They will survive and (probably) continue working through most changes to the game's code.
Hooking via the stable and recommended methods will ensure that a modification to the game's code does not break your mod.

How to compile like a pro.
--------------------------

Instead of manually creating AST Nodes to insert code into the game, or even clunkily creating entries in the rpy language and then jumping to the snippets with the patcher, you can assemble small(or big!) bits of code *in-line* by abusing the Ren'py AST Parser.
This means you can get a list of objects and insert them wherever with very little effort.
We use this method internally to create the mod information menu on the main screen. See the core mod for further details.

Debugging
---------

There are several obstacles to developing mods for Ren'py.
The first(and biggest) is the fact that the developer has no console to watch for output while running the game!
We can fix that by starting AWSW via command line with some switches set. The commands are below.

While in the root directory of the game, run the command for your appropriate operating system:

Windows
~~~~~~~
``"lib/windows-i686/python.exe" -O "Angels with Scaly Wings.py"``

Linux x86 (32 bit)
~~~~~~~~~~~~~~~~~~
``./lib/linux-i686/python -O "Angels with Scaly Wings.py"``

Linux x86_64 (64 bit)
~~~~~~~~~~~~~~~~~~~~~

``./lib/linux-x86_64/python -O "Angels with Scaly Wings.py"``

If while printing, you get an error message such as ``LookupError: unknown encoding: cp437``, please make sure you are using AwSW v1.7+.

If you are using this version, please report an error on Github or the Steam Forums

Sample Code
-----------

This sample code will remove Kevin's encounter and main menu icon. The full mod structure can be found in mods/. 

.. code:: python

    """This file is free software under the GPLv3 license"""
    import renpy
    import renpy.ast as ast

    from modloader import modinfo, modast
    from modloader.modgame import sprnt
    from modloader.modgame import base as ml
    from modloader.modclass import Mod, loadable_mod

    @loadable_mod
    class AWSWMod(Mod):
        """Removes Kevin from the game"""
        def mod_info(self):
            return ("byekevin", "v0.1", "")

        def mod_load(self):
            # Find and remove where we find Kevin
            found = modast.search_for_node_type(modast.find_label("c4hatchery"), ast.Scene, 20)
            hook = modast.hook_opcode(found, None)
            hook.chain(modast.search_for_node_type(found, ast.Scene))

            # Remove Kevin from the main screen
            mainscr = modast.get_slscreen('main_menu')

            # Remove Kevin from the persistent file
            modast.remove_slif(mainscr, 'persistent.playedkevin')

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
