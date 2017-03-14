label remy_post_true_bootstrap:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ remyscenesfinished = 4 # Set this to bypass the check for testing.
    jump remy_post_true_entry

label remy_post_true_entry:
    if remyscenesfinished != 4:
        return
        
    