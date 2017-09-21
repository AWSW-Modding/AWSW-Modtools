
label TLAMaverickStart:

    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - TLAMaverick - Start"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - TLAMaverick - Start"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - TLAMaverick - Start"

    else:
        $ save_name = "Chapter 1 - TLAMaverick - Start"
    
$ TLAMaverickpoints = 0

Mv "..."

play music "mx/shoal.ogg" fadein 2.0

c "Maverick...maybe we can go somewhere together? "

Mv blush "Huh?"

c "Let's go to the cafe. We can talk there, eat something maybe."

c "You have no point in trusting me, but maybe by spending some time together we can better understand each other."

Mv normal "If you are trying to fool me, i swear..."

c "No Maverick. I just want to spend some time with you."

Mv normal "Fine, but don't you have to report on Police Station?"

c "Well... I can do it later, there is still whole day to do it."

Mv nice "Let it be then. Lead on."

window hide

show blackbg with dissolvemed

$ renpy.pause (1.0)

jump TLAMaverickCafe
