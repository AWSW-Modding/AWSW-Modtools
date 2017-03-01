#init stuff here

# Our entry point from the patcher. In mod.py we tell ren'py to jump to this label as a result of a button press in the screen we compiled. 
label jump_mainmenu_test:                
    # If the 'dev test' button is pressed, the game jumps to this directly from the main menu, which means some initialization instructions aren't run.
    # The one that matters most is setting up the MC's player object. We need to do that here. 
    # This wouldn't be required if you were jumping to the scene from somewhere after the game started.
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly) 

    jump scene_code # Jump to your scene code now. 
            
          
