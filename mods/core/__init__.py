from modclass import Mod, addMod
from modlib import base as ml
import modinfo

import renpy
import renpy.parser as parser
import renpy.ast as ast

@addMod
class Core(Mod):
    def mod_info(self):
        return ("Core", "v0.1-dev", "Various")

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

        tocompile = """screen dummy:
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
        print("!!!!!!!!!!!!")
        result = ""
        for mod_name, version, author in modinfo.modlist:
            result += "{} by {} ({})\n".format(mod_name, author, version)

        # Renpy python globals are stored in renpy.python.store_dicts["store"]
        # We store the string here so we can access it from the screen later
        ml.setRGlobal('modsDesc', result)

