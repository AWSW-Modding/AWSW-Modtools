init python:
    from modloader import modinfo
    persistent.nsfwToggleSet = True
    for mod_name, mod in modinfo.get_mods().iteritems():
        mod_info = mod.mod_info()
        if len(mod_info) == 4 and mod_info[3]:
            persistent.nsfwToggleSet = False
        
label before_main_menu:
    if not persistent.nsfwToggleSet:
        play sound "fx/system.wav"
        s "You have installed mods that may contain NSFW scenes in them."
        s "Please note that these mods are meant for players who are at or above the legal age for viewing adult content. \"Legal age\" is defined by the country that the player is currently living in."
        s "If the player is not of age, it is assumed that they will not select \"yes\" at the selection page."
        s "Of course, this approach relies on the player's honesty, and as such, there is the possibility that the player may end up lying."
        s "If this occurs, the sole responsiblity of such an act lies with the player, not the mod team or the community."
        s "Would you like to have these scenes enabled?"
        
        menu:
            "Yes.":
                s "You have chosen to enable NSFW scenes."
                $ nsfwtoggle = True
            "No.":
                s "You have chosen to not see the NSFW scenes."
                $ nsfwtoggle = False
        
        $ persistent.nsfwToggleSet = True