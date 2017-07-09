screen modmenu tag smallscreen:
    modal True

    window id "modmenu" at popup:
        style "smallwindow"
        
        vbox xalign 0.5 yalign 0.5:
            spacing 10
            text "Mods loaded: [modsDesc]" style "menubutton2" # No strings attached. Ren'py uses KP linebreaking by default.
            textbutton "Add mod from workshop" action [Show("modmenu_download"), Hide("modmenu")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "Remove mods" action [Show("modmenu_remove"), Hide("modmenu")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"

        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("modmenu"), Hide("preferencesbg", transition=dissolve), ToggleVariable('navmenuopen', False), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button

label _mod_fixansw:
    if _return:
        $ playmessage = True
    return
    
label _core_updateChapter:
    call _mod_getchapter
    $ mod_currentChapter = _return
    return