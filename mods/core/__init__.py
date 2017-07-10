"""This file is free software under the GPLv3 license"""
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod


@loadable_mod
class AWSWMod(Mod):
    """The core mod.

    This mod is responsible for being a proxy between renpy code and modlib
    """

    @staticmethod
    def mod_info():
        """Get the mod info
        Returns: a three element tuple containing the mod name, version and description
        """
        return ("Core", "v0.1", "")

    @staticmethod
    def mod_load():
        """Run various housekeeping tasks for ease of modding.
        Disables the screen cache.
        Adds the MODS button to the main menu.
        """
        # This is called due to renpy's screen cache. Any modifications to screens with an
        # enabled cache will fail!
        modast.disable_slast_cache()

        # Hook every point where the chapter is changed and set mod_currentChapter to the
        # integer value of the current chapter. This will allow route mods to make comparisons.
        home_hook = ml.get_home_hook()
        home_hook.hook_chapter_1(modast.find_label("_core_updateChapter"))

        stmt = modast.find_python_statement('chapter2unplayed = False')
        modast.call_hook(stmt, modast.find_label("_core_updateChapter"))
        stmt = modast.find_python_statement('chapter3unplayed = False')
        modast.call_hook(stmt, modast.find_label("_core_updateChapter"))
        stmt = modast.find_python_statement('chapter4unplayed = False')
        modast.call_hook(stmt, modast.find_label("_core_updateChapter"))

        # How to abuse the ren'py parser for your own personal gain!
        tocompile = """
        screen dummy:
            imagebutton auto "ui/mods_%s.png" action [Show("preferencesbg"), Show('modmenu'), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.03 yalign 0.955
        """

        compiled = parser.parse("FNDummy", tocompile)
        target_display = None
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    target_display = child

        modast.get_slscreen('main_menu').children.append(target_display)

    @staticmethod
    def mod_complete():
        """Insert a NSFW warning if any mods register as NSFW"""

        for mod_name, mod in modinfo.get_mods().iteritems():
            mod_info = mod.mod_info()
            if len(mod_info) == 4 and mod_info[3]:
                # Append the NSFW selection each game
                # Credits to yoshisman8 for the code
                toggler = modast.find_label("lewdtoggler")
                bootup = modast.find_label("nameentry")
                modast.call_hook(bootup, toggler)
                break

        # This is called after all mods are loaded, preventing us from getting a partial list of
        # mods (say, if core was loaded before myMod1).
        modast.set_renpy_global('modsDesc', ', '.join([mod_name for mod_name in modinfo.modlist]))
