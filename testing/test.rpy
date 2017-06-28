screen screen_test_get_screen tag smallscreen:
    if persistent.test:
        text "hi!"

label label_test_find_label:
    $ this_is_a_very_unique = "variable"
    c "This should not be displayed"
    Br "I'm the best character"

    menu:
        "Yes you are!":
            pass

        "Of course!":
            pass

label label_extra:
    c "You die now."

