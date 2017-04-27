init python:
    from music_mod import song_choice

screen meowers_music_selection:       
    imagebutton:
        auto "ui/music_%s.png"
        action [Play("audio", "se/sounds/open.wav"), 
                Play("music", song_choice())]
        hovered Play("audio", "se/sounds/select.ogg") 
        xalign 0.87
        yalign 0.85
