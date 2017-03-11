from modloader import modlib
import renpy
import renpy.parser as parser
import renpy.ast as ast
from modloader import modinfo
from modlib import sprnt
from modlib import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Core", "v0.1", "")
        
    def mod_load(self):
        # This is called due to renpy's screen cache. Any modifications to screens with an enabled cache will fail!
        ml.DisableSCache()
        
        # Hook every point where the chapter is changed and set mod_currentChapter to the integer value of the current chapter. This will allow route mods to make comparisons. 
        h = ml.getHomeHook()
        h.hookChapter1(ml.findlabel("_core_updateChapter"))

        stmt = ml.findPyStatement('chapter2unplayed = False')
        ml.call_hook(stmt, ml.findlabel("_core_updateChapter"))
        stmt = ml.findPyStatement('chapter3unplayed = False')
        ml.call_hook(stmt, ml.findlabel("_core_updateChapter"))
        stmt = ml.findPyStatement('chapter4unplayed = False')
        ml.call_hook(stmt, ml.findlabel("_core_updateChapter"))

        # How to abuse the ren'py parser for your own personal gain!
        targetDisp = None

        tocompile = """
        screen dummy:
            imagebutton auto "ui/mods_%s.png" action [Show("preferencesbg"), Show('modmenu'), Play("audio", "se/sounds/open.wav")] hovered Play("audio", "se/sounds/select.ogg") xalign 0.03 yalign 0.955
        """
        rv = parser.parse("FNDummy", tocompile)
        targetDisp = None
        for e in rv:
            #sprnt(type(e).__name__)
            if isinstance(e, ast.Init):
                for b in e.block[0].screen.children:
                    targetDisp = b
                    
        ml.getsls('main_menu').children.append(targetDisp)

    def mod_complete(self):
        # This is called after all mods are loaded, preventing us from getting a partial list of mods (say, if core was loaded before myMod1). 
        # Rpy python globals are stored in renpy.python.store_dicts["store"], so to access our data from the screen later, we need to put it in this dictionary.
        ml.setRGlobal('modsDesc', ', '.join([mod_name for mod_name in modinfo.modlist]))