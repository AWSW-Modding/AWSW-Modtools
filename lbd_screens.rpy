#----------Screens----------
screen silly_timers(intervals, sfx):
    default play_time = 0.001 # We play the very first sound asap.
    for i in intervals:
        timer play_time action Play("cpswright", sfx)
        $ play_time += i

screen action_menu2():
    tag menu

    frame:
        style_group "action_menu2"

        hbox:
            textbutton _("Reason With") action Return (1)
            null width 350
            textbutton _("Attack") action Return (2)
            null width 350
            textbutton _(" Inventory ") action Return (3)

screen item_screen:
    modal True

    frame:
        style_group "item_menu"
        vbox:
            if items[2] > 0:
                textbutton _("Eat Cookie (Gain HP) {size=-5}{u}{i}[items[2]] remaining{/i}{/u}{/size}") action Return (4)
                null height 20
            if (items[3] > 0) and not (ronan[3]):
                textbutton _("Eat mushroom (Boost attack) {size=-5}{u}{i}[items[3]] remaining{/i}{/u}{/size}") action Return (5)
                null height 20

            textbutton _("Return") action Return (6)

screen lbd_battle_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 300
        vbox:
            text "Little Buddy" size 32 xalign 0.5 antialias False font "Munro.ttf" underline True
            null width 40
            null height 5
            hbox:
                bar:
                    yoffset -7
                    xmaximum 200
                    value lorem[1]
                    range lorem[0]
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[lorem[1]] / [lorem[0]]" size 26 antialias False font "Munro.ttf"

    frame:
        xalign 0.20 yalign 0.05
        xminimum 220 xmaximum 300
        vbox:
            text "Ronan" size 32 xalign 0.5 antialias False font "Munro.ttf" underline True
            null width 40
            null height 5
            hbox:
                bar:
                    yoffset -7
                    xmaximum 200
                    value ronan[1]
                    range ronan[0]
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[ronan[1]] / [ronan[0]]" size 26 antialias False font "Munro.ttf"

    frame:
        xalign 0.97 yalign 0.05
        xminimum 220 xmaximum 600
        vbox:
            text "Draco" size 32 xalign 0.5 antialias False font "Munro.ttf" underline True
            null height 5
            hbox:
                text "[wolf[1]] / [wolf[0]]" size 26 antialias False font "Munro.ttf"

                null width 5

                bar:
                    yoffset -7
                    xmaximum 500
                    value wolf[1]
                    range wolf[0]
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

    text "Ronan vs. Draco" xalign 0.5 yalign 0.05 size 38 antialias False font "Munro.ttf"

init -2:
    ###------Arcade inventory menu--------
    style item_menu:
        bar_vertical False

    style item_menu_vbox:
        xcenter 0.5
        ycenter 0.5

    style item_menu_frame:
        xminimum 1175
        yminimum 313
        xalign 0.5
        yalign 0.55
        background "arch/textboxsmaller.png"
        hover_background "arch/textboxsmaller.png"
        selected_background "arch/textboxsmaller.png"

    style item_menu_button:
        background "#0707A7"
        hover_background "#1578A5"
        selected_background "#71CDF7"
        xalign 0.5
        yalign 0.5

    style item_menu_button_text:
        text_align 0.5
        size 60
        color "#FFFFF0"
        selected_color "#FFFFF0"
        insensitive_color "#404040"
        antialias False
        font "Munro.ttf"

    style item_menu_text:
        text_align 0.5
        size 60
        color "#FFFFF0"
        antialias False
        font "Munro.ttf"
        xalign 0.5
        yalign 0.5

    ###-------------Arcade action menu styleing
    style action_menu2_frame:
        xcenter 0.5
        ycenter 0.84
        yoffset 5
        xminimum 1836
        yminimum 319
        background "arch/textboxnew.png"
        hover_background "arch/textboxnew.png"
        selected_background "arch/textboxnew.png"

    style action_menu2_hbox:
        xcenter 0.5
        ycenter 0.5

    style action_menu2_button:
        background "#0707A7"
        hover_background "#1578A5"
        selected_background "#71CDF7"
        xalign 0.5
        yalign 0.5

    style action_menu2_button_text:
        text_align 0.5
        size 60
        color "#FFFFF0"
        selected_color "#FFFFF0"
        antialias False
        font "Munro.ttf"
