screen post_true_sceneselect tag smallscreen:
    modal True

    window id "modmenu" at popup:
        style "smallwindow"
        
        vbox xalign 0.5 yalign 0.5:
            spacing 10
            textbutton "Adine" action [Hide("post_true_sceneselect"), Start("adine_post_true_bootstrap")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "Anna" action [Hide("post_true_sceneselect"), Start("anna_post_true_bootstrap")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "Bryce" action [Hide("post_true_sceneselect"), Start("bryce_post_true_bootstrap")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"
            textbutton "Remy" action [Hide("post_true_sceneselect"), Start("remy_post_true_bootstrap")] hovered Play("audio", "se/sounds/select.ogg") style "menubutton2"

        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("post_true_sceneselect"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button
        
label post_true_main:
    if annascenesfinished == 4:
        jump anna_post_true_entry
    elif adinescenesfinished == 4:
        jump adine_post_true_entry
    elif remyscenesfinished == 4:
        jump remy_post_true_entry
    elif brycescenesfinished == 4:
        jump bryce_post_true_entry
    else:
        return