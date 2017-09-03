init python:
    from modloader import modast, modinfo

    for mod_name, mod in modinfo.get_mods().iteritems():
        mod_info = mod.mod_info()
        if len(mod_info) == 4 and mod_info[3]:

            if persistent.nsfwtoggle == None:
                persistent.nsfwtoggle = False
                renpy.save_persistent()

            nsfwtoggle = persistent.nsfwtoggle

            rpyCode =  'screen mainmenunsfw:\n'\
                        '    imagebutton: \n'\
                        '        xpos 1521 \n'\
                        '        ypos 223 \n'\
                        '        auto "ui/nsfwButton_%s.png" \n'\
                        '        action [Show("nsfw_toggle_screen"), Play("audio", "se/sounds/open.wav")] \n'\
                        '        hovered Play("audio", "se/sounds/select.ogg") \n'

            rv = renpy.parser.parse("RPDummy", rpyCode)

            targetDisp = None
            for e in rv:
                if isinstance(e, renpy.ast.Init):
                    targetDisp = e.block[0].screen.children[0]

            modast.get_slscreen("main_menu").children.append(targetDisp)

screen nsfw_toggle_screen:
    modal True

    window id "nsfw_toggle_screen" at alpha_dissolve:
        style "nvl_window"

        left_padding 120
        left_margin 0
        right_padding 120
        right_margin 0
        top_padding 0
        top_margin 0
        bottom_padding 0
        bottom_margin 0

        imagebutton:
            idle "image/ui/close_idle.png"
            hover "image/ui/close_hover.png"
            action [Hide("nsfw_toggle_screen", transition=dissolve), Play("audio", "se/sounds/close.ogg")]
            hovered Play("audio", "se/sounds/select.ogg", Show("modmenu"))
            xalign 0.95
            yalign 0.1
            at nav_button

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            text "You have installed mods that may contain {b}NSFW{/b} scenes in them.":
                xalign 0.5
                yalign 0.5
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
                xalign 0.5
                yalign 0.5
                size 38

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 250

                textbutton "Yes":
                    action [SetPersistentNSFW("nsfwtoggle", True), SetVariable("nsfwtoggle", True), Play("audio", "se/sounds/yes.wav"), Hide("nsfw_toggle_screen", transition=dissolve)]
                    style "nsfw_toggle_screen_btn"

                textbutton "No":
                    action [SetPersistentNSFW("nsfwtoggle", False), SetVariable("nsfwtoggle", False), Play("audio", "se/sounds/yes.wav"), Hide("nsfw_toggle_screen", transition=dissolve)]

                    style "nsfw_toggle_screen_btn"

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
    style.nsfw_toggle_screen_btn_text.selected_color = "#404040"
    style.nsfw_toggle_screen_btn_text.selected_idle_color = "#ffffff"
    style.nsfw_toggle_screen_btn_text.selected_idle_underline = True
    style.nsfw_toggle_screen_btn_text.selected_hover_underline = True

init -100 python:
    @renpy.pure
    class SetPersistentNSFW(Action, FieldEquality):
        identity_fields = ['value']
        equality_fields = ['name']

        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __call__(self):
            setattr(persistent, self.name, self.value)
            renpy.save_persistent()
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(persistent, self.name) == self.value
