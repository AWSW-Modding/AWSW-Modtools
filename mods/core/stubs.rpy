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
