label mod_remy_christmas_search_bedroom:

c "(I probably shouldn't be looking in here, but I'll just take a quick peek.)"

play sound "fx/door/door_open.wav"
$ renpy.pause(1.5)

c "(Now that's a huge bed, even for a dragon. I suppose they need to account for wings and such, but even considering that, it's pretty big.)"

$ renpy.pause(1.5)

c "(What's this? I think there's a book on the dresser.)"
m "On further inspection, the book reveals itself to be a diary, and a fairly old one judging by the leather bound cover. It must be at least 4 years old, though the pages themselves look almost completely untouched."

$ remy2options += 1
$ remy2bed = False
jump remy2menu

label mod_remy_christmas_take_diary:

play sound "fx/door/door_open.wav"
$ renpy.pause(1.5)

c "(I definitely shouldn't be taking thism but it might be useful for the investigation and to learn more about Remy.)"

$ remy2options += 1
$ remy2bed = None
jump remy2menu