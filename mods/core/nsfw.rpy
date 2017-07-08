init python:
    from modloader import modinfo
    for mod_name, mod in modinfo.get_mods().iteritems():
        mod_info = mod.mod_info()
        if len(mod_info) == 4 and mod_info[3]:
            persistent.nsfwToggleSet = False

    if persistent.nsfwToggleSet is None:
        persistent.nsfwToggleSet = True
        
label before_main_menu:
    if not persistent.nsfwToggleSet:
        play sound "fx/system.wav"
        s "You have installed mods that may contain NSFW scenes in them."
        s "Would you like to have these scenes enabled?"
        
        menu:
            "Yes.":
                s "You have chosen to enable NSFW scenes."
                $ nsfwtoggle = True
            "No.":
                s "You have chosen to not see the NSFW scenes."
                $ nsfwtoggle = False
        
        $ persistent.nsfwToggleSet = True