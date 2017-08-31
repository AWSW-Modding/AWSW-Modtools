screen modmenu_remove:
    modal True

    window id "modmenu_remove" at alpha_dissolve:
        style "nvl_window"
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("modmenu_remove", transition=dissolve), Play("audio", "se/sounds/close.ogg"), Show("modmenu")] hovered Play("audio", "se/sounds/select.ogg") xalign 1.1 yalign -0.1 at nav_button

        frame:
            yalign -0.2
            xalign 0.5

            text "Remove mods" style "menubutton2"

        python:
            from modloader.modinfo import get_mods


            y_pos = 0.0

            for modname in get_mods():
                renpy.ui.textbutton(modname, (Show("modmenu_remove_confirm", modname=modname), Play("audio", "se/sounds/open.ogg")), hovered=Play("audio", "se/sounds/select.ogg"), yalign=y_pos, style="menubutton2")
                y_pos += 0.12


screen modmenu_remove_confirm(modname) tag smallscreen2:
    modal True

    window id "modmenu_remove_confirm" at popup2:
        style "alertwindow"

        python:
            from modloader.modconfig import remove_mod

        if modname == "Core":
            textbutton "Continue" action [Hide("modmenu_remove_confirm"), Show("modmenu_remove"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton" xalign 0.5 yalign 0.8

            label "You cannot remove the Core mod.":
                style "yesno_prompt"
                text_style "yesno_prompt_text"
        else:
            hbox xalign 0.5 yalign 0.8:
                spacing 250
                textbutton "Yes" action [Hide("modmenu_remove_confirm"), Play("audio", "se/sounds/close.ogg"), lambda remove_mod=remove_mod, modname=modname: remove_mod(modname), Show("modmenu_remove")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
                textbutton "No" action [Hide("modmenu_remove_confirm"),  Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"

            label "Are you sure you want to remove [modname]?":
                style "yesno_prompt"
                text_style "yesno_prompt_text"
