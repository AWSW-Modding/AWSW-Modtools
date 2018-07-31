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

screen _modloader_download_screen(mod_id):
    add "#3485e7"
    add DynamicDisplayable(_modloader_download_progress, mod_id):
            xalign 0.5
            yalign 0.5

init python:
    from modloader import workshop_enabled
    if workshop_enabled:
        from steam_workshop.steamhandler import convert_units, get_instance

        def _modloader_download_progress(st, at, mod_id):
            steammgr = get_instance()
            bytes_downloaded, bytes_total = steammgr.GetItemDownloadInfo(mod_id)
            mod_name = steammgr.GetItemFromID(mod_id)[1]
            if bytes_downloaded == bytes_total == 0:
                return  Text("Installing {}...".format(mod_name,
                                                       convert_units(bytes_downloaded),
                                                       convert_units(bytes_total)),
                             xalign=0.5,
                             yalign=0.5,
                             substitute=False), .1
            return Text("Downloading {}: {}/{}".format(mod_name,
                                                       convert_units(bytes_downloaded),
                                                       convert_units(bytes_total)),
                        xalign=0.5,
                        yalign=0.5,
                        substitute=False), .1
