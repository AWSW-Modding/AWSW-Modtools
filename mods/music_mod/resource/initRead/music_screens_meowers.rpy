init python:
    def songChoice():
        import os, random
        fixPath = renpy.config.gamedir + "/mods/music_mod/resource/mx/" # must follow this path, or else with crash
        
        addedList = []
        dirList = os.listdir(fixPath)
        for filename in dirList:            
            if (filename.endswith(".mp3")) or (filename.endswith(".wav")) or (filename.endswith(".ogg")):
                addedList.append(filename)
                
        listSize = len(addedList)
        if not addedList:
            raise Exception("/music_mod/resource/mx/ must have at least one song in it!")
        
        return "mx/" + addedList[int(random.random() * listSize)]

screen meowers_music_selection:       
    imagebutton:
        auto "ui/music_%s.png"
        action [Play("audio", "se/sounds/open.wav"), 
                Play("music", songChoice())]
        hovered Play("audio", "se/sounds/select.ogg") 
        xalign 0.95
        yalign 0.95