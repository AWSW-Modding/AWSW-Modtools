screen post_true_sceneselect tag smallscreen:
    modal True

    window id "modmenu" at popup:
        style "smallwindow"
        
        vbox xalign 0.5 yalign 0.5:
            spacing 10
            textbutton "Adine Groceries" action [Hide("post_true_sceneselect"), Start("adine_shopping")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("post_true_sceneselect"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
