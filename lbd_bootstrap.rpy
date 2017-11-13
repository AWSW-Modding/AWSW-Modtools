label lbd_lorem1_bootstrap:
    ### Sets up the player charactor, unlike the rest of the in-game charactors the player charactor is only declared after you click start on main menu
    ### because of that we have to declare the player charactor ourselves
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ player_name = persistent.player_name
    $ chapter1csplayed = 0

    #Dev and demo mode
    #accepted Values:
    #   True = Turns on Dev_mode
    #   False = Turns off Dev_mode
    #   "demo" = Turns on demo mode and turns off Dev-mode
    #   Delete variable to turn off Dev mode

    $ lbdfrombootstrap = "demo"

    #saveFilenames
    $ chapter4unplayed = False
    $ chapter3unplayed = False
    $ chapter2unplayed = False
    #$ chapter4unplayed = False

    ### Stops main menu music
    stop music fadeout 0.5

    ### Jumps to your mod code
    jump lbd_lorem1
