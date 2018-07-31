screen modmenu tag smallscreen:
    modal True

    python:
        from modloader import workshop_enabled, is_github
        if workshop_enabled:
            from steam_workshop.steam_config import has_steam
        else:
            def has_steam():
                return False
        if is_github:
            from modloader.modconfig import UpdateModtools

        from modloader import modinfo

        list_of_mods = ""

        for mod_name in modinfo.modlist:
            mod_name = mod_name.replace("-", " ")
            mod_name = mod_name.replace("_", " ")

            if len(mod_name) > 1:
                mod_name =  "".join(name[0].upper() + name[1:] + " " for name in mod_name.split(" "))[:-1]

            list_of_mods += mod_name + ", "

        list_of_mods = list_of_mods[:-2]


    frame id "modmenu" at popup:
        style "smallwindow"

        add "ui/managemods_title.png" xalign 0.01 yalign 0.1 at title_slide

        vbox xalign 0.5 ypos 0.15:
            spacing 30

            #List of mods
            vbox xalign 0.5 yalign 0.5:
                spacing 10
                text "Mods loaded:" style "menubutton2"

                text "[list_of_mods]" style "menubutton2":
                    xmaximum 1500

            #mod management buttons
            vbox xalign 0.5 yalign 0.5:
                if has_steam():
                    textbutton "Add mod from workshop":
                        action [Show("check_internet_downloader", use_steam=True),
                                Play("audio", "se/sounds/open.ogg"),
                                Stop("music", fadeout=1.0),
                                Play("modmenu_music", "mx/modmenu_music.opus", fadein=1.0),
                                Hide("modmenu")]
                        hovered Play("audio", "se/sounds/select.ogg")
                        style "menubutton2"

                if is_github():
                    textbutton "Add mod from Github":
                        action [Show("check_internet_downloader", use_steam=False),
                                Play("audio", "se/sounds/open.ogg"),
                                Stop("music", fadeout=1.0),
                                Play("modmenu_music", "mx/modmenu_music.opus", fadein=1.0),
                                Hide("modmenu")]
                        style "menubutton2"

                textbutton "Remove mods":
                    action [Show("modmenu_remove", transition=Dissolve(1.0)),
                            Play("audio", "se/sounds/open.ogg"),
                            Hide("modmenu")]
                    hovered Play("audio", "se/sounds/select.ogg")
                    style "menubutton2"

                if is_github():
                    textbutton "Fetch most recent modtools":
                        action [UpdateModtools()]
                        style "menubutton2"

        #Close Button
        imagebutton:
            idle "image/ui/close_idle.png"
            hover "image/ui/close_hover.png"
            action [Hide("modmenu"),
                    Hide("preferencesbg", transition=dissolve),
                    ToggleVariable('navmenuopen', False),
                    Play("audio", "se/sounds/close.ogg")]
            hovered Play("audio", "se/sounds/select.ogg")
            style "smallwindowclose"
            at nav_button


        #credits button
        textbutton "Credits":
            xpos 0.90
            ypos 0.75
            style "menubutton"
            action [Show("modtools_credits_scroll"),
                    Stop("music", fadeout=1.0),
                    Play("modmenu_music", "<from 2.5>mx/One-World.opus", fadein=1.0)]
            at modmenu_button_slide

label _mod_fixansw:
    if _return:
        $ playmessage = True
    return

label _core_updateChapter:
    call _mod_getchapter
    $ mod_currentChapter = _return
    return

transform modmenu_button_slide:
    alpha 0.0 xoffset 350
    easein 0.7 alpha 1.0 xoffset 0
    on hide:
        easeout 0.7 alpha 0.0 xoffset 200

transform modtools_credits_trans:
    xoffset 0

    on start:
        1.5
        linear 40 xoffset -5890


screen modtools_credits_scroll:
    modal True

    timer 45 repeat False action [Hide("modtools_credits_scroll"), Stop("modmenu_music", fadeout=2.0), Play("music", "mx/menu.ogg", fadein=2.0)]

    python:
        list_of_modtoolers_top = [["SCRLYS", "EARLY ADOPTOR", "modtools_credits/scrlys.png", "Ground work for the modtools, updated them to be more compatible and documentation."],
            ["BLUE", "STEAM INTEGRATION", "modtools_credits/blue.png", "Updated modtools and Ren'Py to work with Steam."],
            ["MEOWERS", "BETA ELEMETS", "modtools_credits/meowers.png", "Made beta/temp framework and debugging."]
        ]

        list_of_modtoolers_bottom = [["ED", "EARLY ADOPTOR", "modtools_credits/ed.png", "Ground work for the modtools and documentation."],
            ["AdamJ1664/PerfectLime45", "GUI DESIGNER", "modtools_credits/lime.png", "Made the screens used for the modtools and added NSFW content handling." ],
            ["M.B. SAUNDERS", "AwSW GAME", "modtools_credits/saunders.png", "Game producer, writer and designer."]
        ]


    frame at modtools_credits_dissolve:
        background "#000000C8"
        margin(0,0,0,0)
        padding(0,0,0,0)
        xysize(1920, 1080)

        text "MODTOOLS CREDITS":
            size 80
            font "Ardnas.otf"
            align (0.5, 0.01)
            text_align 0.5
            layout "nobreak"


        frame at modtools_credits_trans:
            margin(0,0,0,0)
            padding(0,0,0,0)
            xysize(7200, 900)
            background None
            yalign 0.5

            hbox:
                ysize(900)
                yalign 0.5
                null width 2000

                add "aSebWalk":
                    align (0.5, 0.5)

                null width 150

                vbox:
                    yalign 0.5

                    hbox:
                        yalign 0.0

                        for name, title, img, desc in list_of_modtoolers_top:
                            vbox:
                                spacing 10
                                yalign 0.2
                                xsize 800

                                text "[title]":
                                    size 65
                                    font "Ardnas.otf"
                                    align (0.15, 0.5)
                                    layout "nobreak"

                                hbox:
                                    add "[img]" size(200,200)
                                    null width 20

                                    vbox:
                                        xsize 580

                                        text "[name]":
                                            size 55
                                            font "Ardnas.otf"
                                            yalign 0.5
                                            layout "nobreak"
                                            yoffset -8

                                        text "[desc]":
                                            size 40
                                            font "TitilliumWeb-Regular.ttf"
                                            yalign 0.5
                                            layout "greedy"
                                            min_width 580
                                            yoffset -6
                                            line_spacing -10

                            null width 400

                    null height 125

                    hbox:
                        yalign 1.0

                        null width 400

                        for name, title, img, desc in list_of_modtoolers_bottom:
                            vbox:
                                spacing 10
                                yalign 0.8
                                xsize 800

                                text "[title]":
                                    size 65
                                    font "Ardnas.otf"
                                    align (0.15, 0.5)
                                    layout "nobreak"

                                hbox:
                                    add "[img]" size(200,200)

                                    null width 20

                                    vbox:
                                        xsize 580

                                        text "[name]":
                                            size 55
                                            font "Ardnas.otf"
                                            yalign 0.5
                                            yoffset -8
                                            layout "nobreak"

                                        text "[desc]":
                                            size 40
                                            font "TitilliumWeb-Regular.ttf"
                                            yalign 0.5
                                            layout "greedy"
                                            min_width 580
                                            yoffset -6
                                            line_spacing -10

                            null width 400

                null width 210

                vbox:
                    xsize 700
                    align (0.5,0.5)

                    text "MUSIC":
                        size 55
                        font "Ardnas.otf"
                        xalign 0.5

                    text "Crinkles":
                        size 40
                        font "TitilliumWeb-Regular.ttf"
                        xalign 0.5
                        layout "nobreak"

                    null height -10

                    text "Eric Matyas":
                        size 40
                        font "TitilliumWeb-Regular.ttf"
                        xalign 0.5
                        layout "nobreak"

                    null height 70

                    text "ANIMATION":
                        size 55
                        font "Ardnas.otf"
                        xalign 0.5

                    text "SushiOverAura":
                        size 40
                        font "TitilliumWeb-Regular.ttf"
                        xalign 0.5
                        layout "nobreak"

                    null height 70

                    text "From all of us to you,\nHappy Modding!":
                        size 40
                        font "TitilliumWeb-Regular.ttf"
                        xalign 0.5
                        layout "greedy"
                        text_align 0.5
                        line_spacing -10

                    null height 70

                    text "DISCLAIMER:":
                        size 20
                        font "Ardnas.otf"
                        xalign 0.5
                        bold True

                    null height -5

                    text "Angels with Scaly Wings visual novel is owned by M.B. Saunders, \n who was nice enough to include this fan development into his project.":
                        size 16
                        font "TitilliumWeb-Regular.ttf"
                        xalign 0.5
                        layout "greedy"
                        text_align 0.5
                        line_spacing -8


                #null width 610



transform modtools_credits_dissolve:
    on show:
        alpha .0
        linear 1.5 alpha 1.0
    on hide:
        alpha 1.0
        linear .5 alpha .0

image aSebWalk:
    "modtools_credits/sebwalk 0.png"
    pause 0.25
    "modtools_credits/sebwalk 1.png"
    pause 0.25
    "modtools_credits/sebwalk 2.png"
    pause 0.25
    "modtools_credits/sebwalk 3.png"
    pause 0.25
    repeat
