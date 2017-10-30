label start_mod_rnmc:
    $ renpy.suspend_rollback(True)

    python:
        def rnmc_yes_no_promt(string):
            ui.frame(xalign=0.5, yalign=0.5)
            ui.add("image/ui/menubg_options.png", at=popup_custom)
            ui.vbox(at=popup_custom)
            ui.null(height=30)

            ui.text(string,
                    style="yesno_prompt_text",
                    xcenter=0.5, ycenter=0.5)

            ui.null(height=50)
            ui.hbox(xcenter=0.5, ycenter=0.5)

            ui.textbutton("Yes",
                            clicked=[ui.returns(True), Play("audio", "se/sounds/yes.wav")],
                            hovered=[Play("audio", "se/sounds/select.ogg")],
                            style="yesnobutton")

            ui.null(width=250)

            ui.textbutton("No",
                            clicked=[ui.returns(False), Play("audio", "se/sounds/close.ogg")],
                            hovered=[Play("audio", "se/sounds/select.ogg")],
                            style="yesnobutton")
            ui.close()
            ui.close()

            return ui.interact()

    if not renpy.variant('touch'):
        scene heartbg with fade:
            xcenter 0.5 ycenter 0.5

        if rnmc_yes_no_promt("This is used to rename your character, continue?"):
            pass
        else:
            return

    if renpy.variant('touch'):
        image systembg = "image/ui/ingame_menu_bg3.png"
        image nvlbg = "image/ui/nvlscreen.png"

        show systembg zorder 2 at zoom_fade_in:
            xcenter 0.5 ycenter 0.5
        show nvlbg zorder 3 at zoom_fade_in:
            xcenter 0.5 ycenter 0.5 size (1921, 1080) xoffset -1
        with dissolve

        python:
            def rnmc_yes_no_promt_mobile(string):
                ui.frame(xalign=0.5, yalign=0.5)
                ui.add("image/ui/menubg_options.png", size=(1920, 350), at=popup_custom, alpha=0.2)
                ui.vbox(at=popup_custom)
                ui.null(height=30)
                ui.text(string,
                        size = 65,
                        font="Ardnas.otf",
                        xcenter = 0.5)

                ui.null(height=100)
                ui.hbox(xcenter=0.5, ycenter=05)
                ui.textbutton("Yes",
                            clicked=[ui.returns(True), Play("audio", "se/sounds/yes.wav")],
                            text_size=80,
                            text_font="Ardnas.otf",
                            drop_shadow = None,
                            text_drop_shadow = None,
                            idle_background = "#0000007d",
                            hover_background = "#5151517d",
                            minimum = (150, 120),
                            text_hover_color = "#404040",
                            text_selected_idle_color = "#fff",
                            text_idle_color = "#fff"
                            )

                ui.null(width=450)

                ui.textbutton("No",
                            clicked=[ui.returns(False), Play("audio", "se/sounds/close.ogg")],
                            text_size=80,
                            text_font="Ardnas.otf",
                            drop_shadow = None,
                            text_drop_shadow = None,
                            idle_background = "#0000007d",
                            hover_background = "#5151517d",
                            minimum = (150, 120),
                            text_hover_color = "#404040",
                            text_selected_idle_color = "#fff",
                            text_idle_color = "#fff"
                            )
                ui.close()
                ui.close()

                return ui.interact()

        if not rnmc_yes_no_promt_mobile("This is used to rename your character, continue?"):
            return

    jump enter_text

label touch_inputter:
    if text_group==1:
        $text_list=text_list1

    elif text_group==2:
        $text_list=text_list2

    $ ui.frame(xpos=0.5, ypos=0.18,  xanchor=0.5)

    $ ui.vbox()
    $ ui.text(header_text,
            size = 55,
            font = "TitilliumWeb-Regular.ttf",
            xcenter = 0.5)

    $ ui.null(height=20)

    $ ui.hbox(xcenter = 0.5)

    $ ui.frame(background = "#0000007d", xminimum = 1000, yminimum = 80)

    $ ui.text("    " + input_header + " " + input_text,
                size = 55,
                font = "TitilliumWeb-Regular.ttf")

    $ ui.close()

    $ ui.null(height=40)

    $ ui.hbox(xcenter = 0.5)

    $ ui.textbutton("Done",
                    clicked=[ui.returns("Done"), Play("audio", "se/sounds/yes.wav")],
                    hovered=[Play("audio", "se/sounds/select.ogg")],
                    idle_background = "#0000007d",
                    hover_background = "#5151517d",
                    minimum = (240, 60),
                    margin = (15, 10, 15, 20),
                    text_size = 55,
                    text_font = "TitilliumWeb-Regular.ttf",
                    text_hover_color = "#404040",
                    text_selected_idle_color = "#ffffff",
                    text_idle_color = "#ffffff"
                    )

    $ ui.textbutton("Backspace",
                    clicked=[ui.returns("Backspace"), Play("audio", "se/sounds/select3.ogg")],
                    hovered=[Play("audio", "se/sounds/select.ogg")],
                    idle_background = "#0000007d",
                    hover_background = "#5151517d",
                    minimum = (380, 60),
                    margin = (15, 10, 15, 20),
                    text_size = 55,
                    text_font = "TitilliumWeb-Regular.ttf",
                    text_hover_color = "#404040",
                    text_selected_idle_color = "#ffffff",
                    text_idle_color = "#ffffff"
                    )

    $ ui.textbutton("Delete",
                    clicked=[ui.returns("Deleteall"), Play("audio", "se/sounds/select3.ogg")],
                    hovered=[Play("audio", "se/sounds/select.ogg")],
                    idle_background = "#0000007d",
                    hover_background = "#5151517d",
                    minimum = (280, 60),
                    margin = (15, 10, 15, 20),
                    text_size = 55,
                    text_font = "TitilliumWeb-Regular.ttf",
                    text_hover_color = "#404040",
                    text_selected_idle_color = "#ffffff",
                    text_idle_color = "#ffffff"
                    )

    if text_group==1:
        $ ui.textbutton("Caps (On)",
                        clicked=[ui.returns("lowercase"), Play("audio", "se/sounds/select3.ogg")],
                        hovered=[Play("audio", "se/sounds/select.ogg")],
                        idle_background = "#0000007d",
                        hover_background = "#5151517d",
                        minimum = (320, 60),
                        margin = (15, 10, 15, 20),
                        text_size = 55,
                        text_font = "TitilliumWeb-Regular.ttf",
                        text_hover_color = "#404040",
                        text_selected_idle_color = "#ffffff",
                        text_idle_color = "#ffffff"
                        )

    elif text_group==2:
        $ ui.textbutton("Caps (Off)",
                        clicked=[ui.returns("uppercase"), Play("audio", "se/sounds/select3.ogg")],
                        hovered=[Play("audio", "se/sounds/select.ogg")],
                        idle_background = "#0000007d",
                        hover_background = "#5151517d",
                        minimum = (320, 60),
                        margin = (15, 10, 15, 20),
                        text_size = 55,
                        text_font = "TitilliumWeb-Regular.ttf",
                        text_hover_color = "#404040",
                        text_selected_idle_color = "#ffffff",
                        text_idle_color = "#ffffff"
                        )

    $ ui.close()

    $ ui.null(height=10)

    $ ui.hbox(xalign= 0.5)

    python:
        for text_code in text_list:
            if text_code=="0":
                ui.close()
                ui.hbox(xalign= 0.5)

            elif  len(input_text)<=text_limit-1:
                ui.textbutton(text_code,
                            clicked=[ui.returns(text_code)],
                            idle_background = "#0000007d",
                            hover_background = "#5151517d",
                            minimum = (110, 110),
                            margin = (10, 10, 10, 10),              #left_margin, top_margin, right_margin, and bottom_margin
                            text_size = 50,
                            text_font = "TitilliumWeb-Regular.ttf",
                            text_hover_color = "#404040",
                            text_selected_idle_color = "#ffffff",
                            text_idle_color = "#ffffff"
                            )

            else:
                ui.textbutton(text_code,
                            idle_background = "#0000007d",
                            hover_background = "#5151517d",
                            insensitive_background = "#5151517d",
                            minimum = (110, 110),
                            margin = (10, 10, 10, 10),              #left_margin, top_margin, right_margin, and bottom_margin
                            text_size = 50,
                            text_font = "TitilliumWeb-Regular.ttf",
                            text_color = "#404040"
                            )

    $ ui.close()
    $ ui.close()
    $ button_selection=ui.interact()

    if button_selection=="Backspace":
        $ input_text=input_text[:-1]
        jump touch_inputter
    elif button_selection=="Deleteall":
        $ input_text=''
        jump touch_inputter
    elif button_selection=="uppercase":
        $text_group=1
        jump touch_inputter
    elif button_selection=="lowercase":
        $text_group=2
        jump touch_inputter
    elif button_selection=="Done":
        $ renpy.pause(0.5)
        return

    $ select_text=button_selection

    python:
        for text_code in text_list:
            if select_text==text_code:
                input_text += text_code

    jump touch_inputter

label enter_text:
    $ renpy.pause(0.5)
    #if not renpy.variant('touch'):
    if not renpy.variant('touch'):
        $ player_entering_name = True

        while player_entering_name:
            python:
                ui.frame(xalign=0.5, yalign=0.5)
                ui.add("image/ui/choicebg.png", xalign=0.5, yalign=0.5, size=(1921, 1080), xoffset=-1, at=zoom_fade_in)
                ui.vbox(xalign=0.5, yalign=0.5, at=zoom_fade_in)
                ui.text('What is your name:', xcenter=0.5, ycenter=0.5, size=45, underline=True)
                ui.null(height=10)
                ui.input('Brian', length=15, xcenter=0.5, ycenter=0.5, exclude='{%.!\"£$€^&*()@:;<>,~#+=-_}', size=45, color="#ffffff")
                ui.close()

                new_player_name = ui.interact()
                new_player_name = new_player_name.strip()

                renpy.pause(0.2)
                renpy.say(s, "The name you have entered is: [new_player_name].{cps=2}..{/cps}{w=2.0}{nw}")


            if rnmc_yes_no_promt("Accept the name: [new_player_name]?"):
                $ renpy.pause(0.5)
                $ player_entering_name = False
                s "It's good to meet you [new_player_name]."

    if renpy.variant('touch'):
        python:
            text_list1=["Q","W","E","R","T","Y","U","I","O","P","0",
                              "A","S","D","F","G","H","J","K","L","0",
                              "Z","X","C","V","B","N","M","0"]
            text_list2=["q","w","e","r","t","y","u","i","o","p","0",
                              "a","s","d","f","g","h","j","k","l","0",
                              "z","x","c","v","b","n","m","0"]
            input_text = ''
            input_header = 'Name:'
            text_limit = 15
            text_list=text_list1
            text_group=1

        $ header_text = "What is your name? (leave blank for 'Brian')"
        call touch_inputter

        $ new_player_name = input_text.strip() or "Brian"


    if "takeTwo" in renpy.python.store_dicts["store"]:
        jump colorend_cust

    else:
        jump colormenu1_cust

label colormenu1_cust:
    $ renpy.pause(0.2)
    menu:
        s "Choose a color."

        "{color=#0000ff}B{/color}lue":
            $ new_playercolor = "#0000FF"
            $ new_playercolorname = "blue"
            jump colorend_cust

        "{color=#ff0000}R{/color}ed":
            $ new_playercolor = "#ff0000"
            $ new_playercolorname = "red"
            jump colorend_cust

        "{color=#ffff00}Y{/color}ellow":
            $ new_playercolor = "#ffff00"
            $ new_playercolorname = "yellow"
            jump colorend_cust

        "{color=#008000}G{/color}reen":
            $ new_playercolor = "#008000"
            $ new_playercolorname = "green"
            jump colorend_cust

        "{color=#d3d3d3}G{/color}ray":

            $ new_playercolor = "#d3d3d3"
            $ new_playercolorname = "gray"
            jump colorend_cust

        "[[Show more colors.]":
            jump colormenu2_cust

label colormenu2_cust:
    $ renpy.pause(0.2)
    menu:
        s "Choose a color."
        "{color=#00ffff}C{/color}yan":
            $ new_playercolor = "#00ffff"
            $ new_playercolorname = "cyan"
            jump colorend_cust

        "{color=#ff00ff}M{/color}agenta":
            $ new_playercolor = "#ff00ff"
            $ new_playercolorname = "magenta"
            jump colorend_cust

        "{color=#00ff00}L{/color}ime":
            $ new_playercolor = "#00ff00"
            $ new_playercolorname = "lime"
            jump colorend_cust

        "{color=#ffa500}O{/color}range":

            $ new_playercolor = "#ffa500"
            $ new_playercolorname = "orange"
            jump colorend_cust

        "{color=#ffffff}W{/color}hite":

            $ new_playercolor = "#ffffff"
            $ new_playercolorname = "white"
            jump colorend_cust

        "[[Show more colors.]":
            jump colormenu3_cust

label colormenu3_cust:
    $ renpy.pause(0.2)
    menu:
        s "Choose a color."
        "{color=#ffd700}G{/color}old":

            $ new_playercolor = "#ffd700"
            $ new_playercolorname = "gold"
            jump colorend_cust

        "{color=#c0c0c0}S{/color}ilver":

            $ new_playercolor = "#c0c0c0"
            $ new_playercolorname = "silver"
            jump colorend_cust

        "{color=#b5a642}B{/color}rass":

            $ new_playercolor = "#b5a642"
            $ new_playercolorname = "brass"
            jump colorend_cust

        "{color=#cd7f32}B{/color}ronze":

            $ new_playercolor = "#cd7f32"
            $ new_playercolorname = "bronze"
            jump colorend_cust

        "{color=#cb6d51}C{/color}opper":

            $ new_playercolor = "#cb6d51"
            $ new_playercolorname = "copper"
            jump colorend_cust

        "[[Show more colors.]":
            jump colormenu4_cust

label colormenu4_cust:
    $ renpy.pause(0.2)
    menu:
        s "Choose a color."

        "{color=#808000}O{/color}live":

            $ new_playercolor = "#808000"
            $ new_playercolorname = "olive"
            jump colorend_cust

        "{color=#8b4513}B{/color}rown":

            $ new_playercolor = "#8b4513"
            $ new_playercolorname = "brown"
            jump colorend_cust

        "{color=#008080}T{/color}eal":

            $ new_playercolor = "#008080"
            $ new_playercolorname = "teal"
            jump colorend_cust

        "{color=#800080}P{/color}urple":

            $ new_playercolor = "#800080"
            $ new_playercolorname = "purple"
            jump colorend_cust

        "{color=#800000}M{/color}aroon":

            $ new_playercolor = "#800000"
            $ new_playercolorname = "maroon"
            jump colorend_cust

        "[[Show more colors.]":
            jump colormenu1_cust

label colorend_cust:
    $ renpy.pause(0.2)
    $ testMC = Character("[new_player_name]", color=new_playercolor, callback=rolly)
    $ renpy.pause(0.5)
    testMC "So how does this look?"
    testMC "Does it look ok?"

    menu:
        "Yes":
            $ renpy.pause(0.1)
            testMC "That's great \\o/"

            if rnmc_yes_no_promt("Commit changes? (Last chance to change your mind!)"):
                s "Applying changes{cps=2}...{/cps}{w=1.0}{nw}"
                play sound "fx/system.wav"

                $ persistent.player_name = new_player_name
                $ persistent.playercolor = new_playercolor
                $ persistent.playercolorname = new_playercolorname

            else:
                s "Aborting changes{cps=2}...{/cps}{w=1.0}{nw}"
                play sound "se/sounds/close.ogg"

            $ renpy.suspend_rollback(False)
            return

        "No":
            $ renpy.pause(0.1)
            testMC "Well whats wrong?"

            menu:
                "The Name":
                    $ takeTwo = True
                    jump enter_text

                "The Color":
                    $ takeTwo = True
                    $ renpy.pause(0.2)
                    jump colormenu1_cust

transform RNMC_title_slide:
    alpha 0.0 xoffset -350
    easein 0.7 alpha 1.0 xoffset 0
    on hide:
        easeout 0.7 alpha 0.0 xoffset -200
