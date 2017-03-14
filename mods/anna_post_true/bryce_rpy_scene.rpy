label bryce_post_true_bootstrap:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ brycescenesfinished = 4 # Set this to bypass the check for testing.
    jump bryce_post_true_entry

label bryce_post_true_entry:
    if brycescenesfinished != 4:
        return