init python:
    def songChoice():
        import os, random
        #fixPath = os.getcwd().replace("\\", "/")
        fixPath = renpy.config.gamedir + "/mods/"
        fixPath += "music_mod/resource/mx/" # must follow this path, or else with crash
        
        list = []
        dirList = os.listdir(fixPath)
        for filename in dirList:            
            if (filename.endswith(".mp3")) or (filename.endswith(".wav")) or (filename.endswith(".ogg")):
                list.append(filename)
                
        listSize = len(list)
        if not list:
            raise Exception("/music_mod/resource/mx/ must have at least one song in it!")
        
        selectPos = int(random.random() * listSize)
        return "mx/" + list[selectPos]

screen meowers_music_selection:       
    imagebutton:
        auto "ui/music_%s.png"
        action [Play("audio", "se/sounds/open.wav"), 
                Play("music", songChoice())]
        hovered Play("audio", "se/sounds/select.ogg") 
        xalign 0.87
        yalign 0.85