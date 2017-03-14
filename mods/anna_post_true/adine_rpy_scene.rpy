label adine_post_true_bootstrap:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ adinescenesfinished = 4 # Set this to bypass the check for testing.
    jump adine_post_true_entry

label adine_post_true_entry:
    $ adine_post_mood = 0

    if adinescenesfinished != 4:
        return
        
    