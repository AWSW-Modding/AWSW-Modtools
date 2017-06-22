import renpy
import renpy.sl2.slast as slast
import renpy.parser as parser
import renpy.ast as ast
import sys, os, random

from modloader import modinfo, modast
from modloader.modgame import sprnt
from modloader.modgame import base as ml
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class AWSWMod(Mod):
    def insertIntoMainMenu(self, rpyString):
        rv = parser.parse("FNDummy", rpyString)

        targetDisp = None
        for e in rv:
            if isinstance(e, ast.Init):
                targetDisp = e.block[0].screen.children[0]

        modast.get_slscreen("main_menu").children.append(targetDisp)

    def readFile(self, path):
        with open(path) as f:
            return f.read()

    def readFilePart(self, path):
        with open(path) as f:
            for i in xrange(19): # 19 is placed here specifically for music_screen_meowers.rpy, change in the case file changes
                f.next()
            strReturn = ""
            for line in f:
                #raise Exception(line) #<--- use this to figure out what the first line is...
                strReturn += line
            return strReturn

    def readFilesFromInitDir(self):
        fixPath = renpy.config.gamedir + "/mods/music_mod/resource/initRead/"
        dirList = os.listdir(fixPath)
        for filename in dirList:
            if filename.endswith(".rpy"):
                readStr = self.readFilePart(fixPath + filename) # since only screen.rpy, this works. if more .rpy files added, it'll crash... Also, absolute path is needed!
                self.insertIntoMainMenu(readStr)

    ### ------------------------------------------------------

    def mod_info(self):
        return ("meowers' music mod", "v0.1", "meowers!")

    def mod_load(self):
        self.readFilesFromInitDir()

    def mod_complete(self):
        pass
