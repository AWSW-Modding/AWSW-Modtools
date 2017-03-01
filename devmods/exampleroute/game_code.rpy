label exampleroute_init: # We call this at the beginning of chapter 1 to set up all the variables
    $ exampleroute_scene = 0 # This will be our scene counter. It will determine what scene we should view depending on what point we're at.

    # This will record our standing for the route. The developers use strings, but we can do better with an integer and arithmetic. 
    # 0 will be bad, 1 will be neutral, 2 will be good, and 3 will be impressed. This will allow you to make blanket decisions based on the player's status with less code later. 
    $ exampleroute_status = 1 

    $ exampleroute_lastplayed = 0 # This will be used to prevent the player from viewing more than one scene per chapter
    return


label exampleroute_entrypoint:
    call _mod_incc # This will increment the game's visit counter. Failing to call this can result in weird behavior. 
    $ exampleroute_scene += 1 # Increment our scene counter. First run will increase it from 0->1, causing scene 1 to load. The next run will increase it from 1->2, causing scene 2 to load, etc.  
    call _mod_getchapter # Get the current chapter using the stub mentioned in the docs. It will save the chapter's integer value to _return (ex. Chapter 1 -> 1)
    $ exampleroute_lastplayed = _return # Set the lastplayed variable for our route so we can hide the menu option for current chapter visit 2. 
    if exampleroute_scene == 1: # This is a jump table for the scene content. 
        jump exampleroute_scene1start
    elif exampleroute_scene == 2:
        jump exampleroute_scene2start
    elif exampleroute_scene == 3:
        jump exampleroute_scene3start
    elif exampleroute_scene == 4:
        jump exampleroute_scene4start
    else:
        return
        
label exampleroute_scene1start:
    # Scene 1 code here
    return # A return will send the user back to the main game. 
    
label exampleroute_scene2start:
    # Scene 2 code here
    return
    
label exampleroute_scene3start:
    # Scene 3 code here
    return
    
label exampleroute_scene4start:
    # Scene 4 code here
    return  