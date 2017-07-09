screen modmenu_download:
    modal True

    window id "modmenu_download" at alpha_dissolve:
        style "nvl_window"
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("modmenu_download", transition=dissolve), Play("audio", "se/sounds/close.ogg"), Show("modmenu")] hovered Play("audio", "se/sounds/select.ogg", Show("modmenu")) xalign 1.1 yalign -0.1 at nav_button
