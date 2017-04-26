"""This file is free software under the GPLv3 license"""
import renpy
import renpy.parser as parser
import renpy.ast as ast

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    """The core mod

    This mod is responsible for being a proxy between renpy code and modlib
    """
    def mod_info(self):
        return ("Core", "v0.1", "")

    def mod_load(self):
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
        target_display = None

        tocompile = """
        screen dummy:
            imagebutton auto "ui/mods_%s.png" action [Show("preferencesbg"), Show('modmenu'), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.03 yalign 0.955
        """
        compiled = parser.parse("FNDummy", tocompile)
        target_display = None
        for node in compiled:
            #sprnt(type(e).__name__)
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    target_display = child

        modast.get_slscreen('main_menu').children.append(target_display)

    def mod_complete(self):
        # This is called after all mods are loaded, preventing us from getting a partial list of
        # mods (say, if core was loaded before myMod1).
        modast.set_renpy_global('modsDesc', ', '.join([mod_name for mod_name in modinfo.modlist]))
