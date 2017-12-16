screen modmenu tag smallscreen:
    modal True

    python:
        from modloader.modconfig import UpdateModtools

    window id "modmenu" at popup:
        style "smallwindow"

        vbox xalign 0.5 yalign 0.5:
            spacing 10
            text "Mods loaded: [modsDesc]" style "menubutton2" # No strings attached. Ren'py uses KP linebreaking by default.

            textbutton "Add mod from workshop":
                action [Show("check_internet_downloader"),
                        Play("audio", "se/sounds/open.ogg"),
                        Stop("music", fadeout=1.0),
                        Play("modmenu_music", "mx/modmenu_music.opus", fadein=1.0),
                        Hide("modmenu")]
                hovered Play("audio", "se/sounds/select.ogg")
                style "menubutton2"

            textbutton "Remove mods" action [Show("modmenu_remove"), Play("audio", "se/sounds/open.ogg"), Hide("modmenu")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "Fetch most recent modtools" action [UpdateModtools()] style "menubutton2"

        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("modmenu"), Hide("preferencesbg", transition=dissolve), ToggleVariable('navmenuopen', False), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button

label _mod_fixansw:
    if _return:
        $ playmessage = True
    return

label _core_updateChapter:
    call _mod_getchapter
    $ mod_currentChapter = _return
    return
