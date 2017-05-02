label lewdtoggler

    $ nsfwtoggle = False 
    
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
return