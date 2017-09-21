import renpy
import sys, os, random

from modloader import modast
from modloader.modast import get_screen
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    def insertIntoMainMenu(self, rpyString):
        rv = renpy.parser.parse("FNDummy", rpyString)
        targetDisp = None
        for e in rv:
            if isinstance(e, renpy.ast.Init):
                targetDisp = e.block[0].screen.children[0]
        modast.get_slscreen("main_menu").children.append(targetDisp)

    def readFilePart(self, path):
        with open(path) as f:
            for i in xrange(17): # 17 is placed here specifically for music_screens_meowers.rpy, change in the case file changes
                f.next()
            strReturn = ""
            for line in f:
                strReturn += line
            return strReturn       

    ### ------------------------------------------------------

    def mod_info(self):
        return ("meowers' music mod", "v1.0", "meowers!")

    def mod_load(self):
        path = renpy.config.gamedir + "\\mods\\music\\resource\\initRead\\music_screens_meowers.rpy"
        readString = self.readFilePart(path)
        self.insertIntoMainMenu(readString)

    def mod_complete(self):
        pass
