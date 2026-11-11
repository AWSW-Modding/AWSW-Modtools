label _mod_fixjmp: # Jump tables are ugly, but such is life when you're dealing with a very limited language. 
    if not chapter4unplayed:
        jump chapter4chars
    elif not chapter3unplayed:
        jump chapter3chars
    elif not chapter2unplayed:
        jump chapter2chars
    else:
        jump chapter1chars
    

label _mod_incc:
    if not chapter4unplayed:
        $ chapter4csplayed += 1
    elif not chapter3unplayed:
        $ chapter3csplayed += 1
    elif not chapter2unplayed:
        $ chapter2csplayed += 1
    else:
        $ chapter1csplayed += 1
    return
        
label _mod_getchapter:
    if not chapter4unplayed:
        return 4
    elif not chapter3unplayed:
        return 3
    elif not chapter2unplayed:
        return 2
    else:
        return 1

label _mod_fixui:
    $ can_cont = True
    $ restore_ui()
    return

screen message(text, bg, fg):
    modal True
    add bg
    text text xalign 0.5 yalign 0.5 color fg

screen _modloader_download_screen(install_status):
    add "#3485e7"
    add DynamicDisplayable(_modloader_download_progress, install_status):
            xalign 0.5
            yalign 0.5

init python:
    from modloader import workshop_enabled
    if workshop_enabled:
        from steam_workshop.steamhandler import convert_units, get_instance

    def _modloader_download_progress(st, at, install_status):
        curr = install_status.get_curr()
        is_removing = install_status.get_phase()
        use_steam = install_status.use_steam()
        if curr is None:
            return Text("No mod is being installed...",
                         xalign=0.5,
                         yalign=0.5,
                         substitute=False), .1

        if not is_removing:
            if use_steam:
                mod_id = curr
                steammgr = get_instance()
                mod_name = steammgr.GetItemFromID(mod_id)[1]
                bytes_downloaded, bytes_total = steammgr.GetItemDownloadInfo(mod_id)
                no_install_step = False
            else:
                mod_name = curr
                no_install_step = True
            if not no_install_step and bytes_downloaded == bytes_total == 0:
                return  Text("Installing {}...".format(mod_name),
                             xalign=0.5,
                             yalign=0.5,
                             substitute=False), .1
            if use_steam:
                postfix = ": {}/{}".format(convert_units(bytes_downloaded),
                                           convert_units(bytes_total))
            else:
                postfix = ""
            return Text("Downloading {}{}".format(mod_name, postfix),
                        xalign=0.5,
                        yalign=0.5,
                        substitute=False), .1
        else:
            mod_name = curr
            return Text("Removing {}".format(mod_name),
                        xalign=0.5,
                        yalign=0.5,
                        substitute=False), .1