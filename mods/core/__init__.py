"""This file is free software under the GPLv3 license"""
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod
from modloader.modinfo import get_mod_folders
from modloader.modast import set_renpy_global

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

        steam_only = all(folder.isdigit() or folder == "core" for folder in get_mod_folders())

        if not steam_only:
            tocompile += """text "Non-Steam mods detected. The safety or appropriateness of these mods cannot be guaranteed." xalign 0.16 yalign -0.005"""

        compiled = parser.parse("FNDummy", tocompile)
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    modast.get_slscreen('main_menu').children.append(child)

        set_renpy_global("show_workshop_downloader", False)


    @staticmethod
    def mod_complete():
        # This is called after all mods are loaded, preventing us from getting a partial list of
        # mods (say, if core was loaded before myMod1).
        modast.set_renpy_global('modsDesc', ', '.join([mod_name for mod_name in modinfo.modlist]))