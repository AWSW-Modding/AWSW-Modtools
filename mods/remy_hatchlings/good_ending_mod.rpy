label hatchery_remy_good_ending_mod:
    if renpy.python.store_dicts["store"].get("hatchling", "Amely") != "Vara":
        label hatchery_remy_good_ending_mod_no_requirements:
            pass

    $ renpy.pause (1.5)

    m "Suddenly, Remy was on him, fighting for all he was worth, determined not to lose his new daughter."

    show remy angry at Position(xpos=1.3, ypos=1.0)
    show remy angry at Position(xpos=0.5, ypos=1.2) with move5
    play sound "fx/bitescr.ogg"
    $ renpy.pause(2)

    Ry "Why did it have to be this way?"
    Ry "I'm not a killer but I had to do something."
    c "I know, it's ok Remy. You did what you had to."
    Ry "I had to save Vara."
    Vr "..."
    show vara normal flip at Position(xpos=-0.1, ypos=0.8) with move5
    $ renpy.pause(1)

    label hatchery_remy_good_ending_mod_end:
        pass

label hatchery_remy_good_ending_mod2:
    if renpy.python.store_dicts["store"].get("hatchling", False) == False:
        label hatchery_remy_good_ending_mod2_no_requirements:
            pass

    Ry "Yes. After all, I'm not alone anymore. I have [hatchling] to care for and I'm sure Adine will be up for helping if it came down to that"
    if hatchling == "Amely":
        Ry look "Though if I'd adopted Vara, things might have been different - I might have been quicker. She might have lived."
        c "Don't worry about it. There's nothing you can do now. Just look to the future, will you?"
        Ry normal "I'll try."

    label hatchery_remy_good_ending_mod_end2:
        pass
