init python:
    from modloader import modast, modinfo

    for mod_name, mod in modinfo.get_mods().iteritems():
        mod_info = mod.mod_info()
        if len(mod_info) == 4 and mod_info[3]:

            #main nsfw toggle settings
            if persistent.nsfwtoggle == None:
                persistent.nsfwtoggle = False
                renpy.save_persistent()

            nsfwtoggle = persistent.nsfwtoggle

            #main menu button
            rpyCode =  'screen mainmenunsfw:\n'\
                        '    imagebutton: \n'\
                        '        xpos 1521 \n'\
                        '        if persistent.anygoodending:\n'\
                        '            ypos 332\n'\
                        '        else:\n'\
                        '            ypos 223 \n'\
                        '        auto "ui/nsfwButton_%s.png" \n'\
                        '        action [Show("nsfw_toggle_screen", None, False), Play("audio", "se/sounds/open.wav")] \n'\
                        '        hovered Play("audio", "se/sounds/select.ogg") \n'

            rv = renpy.parser.parse("RPDummy", rpyCode)

            targetDisp = None
            for e in rv:
                if isinstance(e, renpy.ast.Init):
                    targetDisp = e.block[0].screen.children[0]

            modast.get_slscreen("main_menu").children.append(targetDisp)

            #start up variables
            if persistent.showNSFWWarning == None:
                persistent.showNSFWWarning = True
                renpy.save_persistent()

            if persistent.showNSFWWarning == True:

                def skip_scenes_nsfw(node, skip, max_search=10000):
                    skipped = 0

                    for _ in range(1, max_search):
                        node = node.next

                        if node and isinstance(node, renpy.ast.Scene):
                            if skipped == (skip - 1):
                                return node

                            skipped += 1

                    return None

                def skip_nodes_nsfw(node, skip):
                    for _ in range(1, skip):
                        node = node.next

                    return node

                from_label_node = modast.find_label("splashscreen")
                from_scene_node = skip_scenes_nsfw(from_label_node, 1)
                from_scene_node = skip_nodes_nsfw(from_scene_node, 1)

                mod_label_node = modast.find_label("NSFW_warning")

                modast.call_hook(from_scene_node, mod_label_node, None)


screen nsfw_ok_prompt(string):
    modal True
    add "heartbg.png" align (0.5, 0.5)

    frame xalign 0.5 yalign 0.5 at popup_custom_nsfw:
        add "image/ui/menubg_options.png" align (0.5, 0.5)

        vbox at popup_custom_nsfw:
            null height 30

            text string:
                xcenter 0.5
                ycenter 0.5
                style "yesno_prompt_text"

            null height 50

            textbutton "OK":
                action [Play("audio", "se/sounds/yes.wav"), Hide("nsfw_ok_prompt", Dissolve(1.0))],
                hovered [Play("audio", "se/sounds/select.ogg")]
                style "yesnobutton"

#label before_main_menu:
label NSFW_warning:
    scene heartbg with fade:
        xcenter 0.5 ycenter 0.5
    $ renpy.suspend_rollback(True)

    $ renpy.pause(0.5)
    play sound "fx/system.wav"
    s "NSFW mods detected{cps=2}...{/cps}{w=1.0}{nw}"

    python:
        player_input = renpy.call_screen("nsfw_toggle_screen", True)

        if player_input == True:
            renpy.pause(0.8)
            renpy.play("fx/system.wav", "sound")
            dummy = mts_ok_prompt("You have enabled NSFW scenes.")

        elif player_input == False:
            renpy.pause(0.8)
            renpy.play("fx/system.wav", "sound")
            dummy = mts_ok_prompt("You have disabled NSFW scenes.")

        renpy.suspend_rollback(False)

screen nsfw_toggle_screen(fromStartUp):
    modal True
    if not fromStartUp:
        add "heartbg.png" align (0.5, 0.5)

    frame id "nsfw_toggle_screen" at popup_custom_nsfw:

        add "image/ui/nvlscreen.png" align (0.5, 0.5) size (1921, 1081) xoffset -1 yoffset -1 #zorder 2

        if not fromStartUp:
            imagebutton:
                idle "image/ui/close_idle.png"
                hover "image/ui/close_hover.png"
                action [Play("audio", "se/sounds/close.ogg"), Hide("nsfw_toggle_screen", Dissolve(1.0))]
                hovered [Play("audio", "se/sounds/select.ogg")]
                xalign 0.95
                yalign 0.1
                at nav_button

        frame xalign 0.05 yalign 0.07:
            margin(0,0,0,0)
            padding(0,0,0,0)

            hbox:
                spacing 25

                text "Show NSFW warning on startup?":
                    xcenter 0.5
                    ycenter 0.5
                    size 28

                imagebutton:
                    xcenter 0.5
                    ycenter 0.5
                    idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                    hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                    selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                    selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                    action [MTSTogglePersistentBool("showNSFWWarning"),
                            Play("audio", "se/sounds/yes.wav")]
                    hovered Play("audio", "se/sounds/select.ogg")
                    focus_mask None

        frame:
            padding (140,0,140,0)
            margin (0,0,0,0)
            yfill True

            vbox:
                align (0.5, 0.5)
                spacing 10

                text "You have installed mods that may contain {b}NSFW{/b} scenes in them.":
                    align (0.5, 0.5)
                    size 44

                null height 20

                text "Please note that these mods are meant for players who are at or above the legal age for viewing adult content. \"Legal age\" is defined by the country that the player is currently living in.":
                    size 36

                text "If the player is not of age, it is assumed that they will not select \"yes\" at the selection page.":
                    size 36

                text "Of course, this approach relies on the player's honesty, and as such, there is the possibility that the player may end up lying.":
                    size 36

                text "If this occurs, the sole responsiblity of such an act lies with the player, not the mod team or the community.":
                    size 36

                null height 20

                text "Would you like to have these scenes enabled?":
                    align (0.5, 0.5)
                    size 38

                hbox:
                    align (0.5, 0.5)
                    spacing 250

                    textbutton "Yes":
                        if not fromStartUp:
                            action [MTSSetPersistent("nsfwtoggle", True),
                                    SetVariable("nsfwtoggle", True),
                                    Play("audio", "se/sounds/yes.wav"),
                                    Hide("nsfw_toggle_screen", None),
                                    Show("nsfw_ok_prompt", dissolve, "You have enabled NSFW scenes.")]
                        else:
                            action [MTSSetPersistent("nsfwtoggle", True),
                                    SetVariable("nsfwtoggle", True),
                                    Play("audio", "se/sounds/yes.wav"),
                                    Return (True),
                                    Hide("nsfw_toggle_screen", transition=dissolve)]

                        hovered Play("audio", "se/sounds/select.ogg")
                        style "nsfw_toggle_screen_btn"

                    textbutton "No":
                        if not fromStartUp:
                            action [MTSSetPersistent("nsfwtoggle", False),
                                    SetVariable("nsfwtoggle", False),
                                    Play("audio", "se/sounds/close.ogg"),
                                    Hide("nsfw_toggle_screen", None),
                                    Show("nsfw_ok_prompt", dissolve, "You have disabled NSFW scenes.")]

                        else:
                            action [MTSSetPersistent("nsfwtoggle", False),
                                    SetVariable("nsfwtoggle", False),
                                    Play("audio", "se/sounds/close.ogg"),
                                    Return (False),
                                    Hide("nsfw_toggle_screen", transition=dissolve)]

                        hovered Play("audio", "se/sounds/select.ogg")
                        style "nsfw_toggle_screen_btn"

transform popup_custom_nsfw:
    xalign 0.5 yalign 0.5 alpha 0.0 yzoom 0.0
    easein 0.3 alpha 1.0 yzoom 1.0
    on hide:
        easeout 0.5 alpha 0.0 yzoom 0.0

init python:
    style.nsfw_toggle_screen_btn = Style(style.default)
    style.nsfw_toggle_screen_btn.background = "#00000060"
    style.nsfw_toggle_screen_btn.xalign = 0.5
    style.nsfw_toggle_screen_btn.yalign = 0.5
    style.nsfw_toggle_screen_btn.xcenter = 0.5
    style.nsfw_toggle_screen_btn.ycenter = 0.5
    style.nsfw_toggle_screen_btn.left_margin = 0
    style.nsfw_toggle_screen_btn.right_margin = 0
    style.nsfw_toggle_screen_btn.bottom_margin = 0
    style.nsfw_toggle_screen_btn.top_margin = 0
    style.nsfw_toggle_screen_btn.left_padding = 12
    style.nsfw_toggle_screen_btn.right_padding = 12
    style.nsfw_toggle_screen_btn.bottom_padding = 0
    style.nsfw_toggle_screen_btn.top_padding = 0
    style.nsfw_toggle_screen_btn_text.color = "#ffffff"
    style.nsfw_toggle_screen_btn_text.size = 42
    style.nsfw_toggle_screen_btn_text.drop_shadow = (2,2)
    style.nsfw_toggle_screen_btn_text.hover_color = "#404040"
    style.nsfw_toggle_screen_btn_text.idle_underline = False
    style.nsfw_toggle_screen_btn_text.hover_underline = False
    style.nsfw_toggle_screen_btn_text.selected_color = "#404040"
    style.nsfw_toggle_screen_btn_text.selected_idle_color = "#ffffff"
    style.nsfw_toggle_screen_btn_text.selected_idle_underline = True
    style.nsfw_toggle_screen_btn_text.selected_hover_underline = True
