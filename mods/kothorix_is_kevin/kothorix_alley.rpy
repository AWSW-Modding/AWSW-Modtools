label kothorix_alley:
    #variables
    $ koth_arcade = False

    #Sets the name for the Save File Name
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Kothorix Alley"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Kothorix Alley"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Kothorix Alley"

    else:
        $ save_name = "Chapter 1 - Kothorix Alley"

    #Scene start--------------------------------------------------------------------------------------------
    nvl clear
    scene black with fade
    $ renpy.pause (1.0)
    
    window show
    if emeramet == True:
        n "We walked out of the cafe. I hoped Adine knew to give the bill to Emera."
    elif persistent.playedemera == True:
        n "We walked out of the cafe. I hoped Adine knew to give the bill to Emera."
    else:
        n "We walked out of the cafe. I hoped Adine knew who to give the bill to."

    n "We aimlessly wandered down a populated street. As usual, Kothorix was seeking attention from passersby. I spotted Maverick in the distance, though he didn't appear to see me."
    n "Not wanting another confrontation, I dragged Kothorix down to a nearby alleyway."

    scene black with dissolve
    window hide
    nvl clear

    scene town8 with fade
    $ renpy.pause (1.0)

    show kothorix normal crossed with dissolve

    Kx "Is everything alright, [player_name]?"
    c "Yeah, everything is alright. It's just..."
    menu:
        "Explain.":
            c "I think Maverick has it out for me." 
            Kx somber face "It's about Reza, isn't it?"
            c "Yeah."
            Kx "Are the rumours true?"
            c "I haven't heard them myself, so I can't answer that."
            Kx ramble face "Well, people are saying that Reza's vanishing act and the murder spree are connected."
            Kx somber face "You may also be involved."
            c "I guess I shouldn't be surprised, then."
            Kx "..."
            Kx "Are you?"
            m "The question immediately filled me with a rage that I wasn't expecting. It quickly turned to sorrow for those who had died."
            c "I do not know of Reza's intentions."
            c "The only thing I can do is to help the dragons stop him."
            c "Just look at me: how exactly am I supposed to kill a dragon?"
            Kx normal crossed "I have no idea how a human can kill a dragon, but you don't look all that strong to me."
            m "Despite the borderline insult, a smile crept its way across my face."
            Kx "For what it's worth, [player_name], I believe you."
            c "Thank you, Kothorix."

        "Avoid Topic.":
            c "Nevermind... It's complicated." 
            Kx somber face "Alright. I'll trust you."
            c "Thank you, Kothorix."

    if nodrinks == True:
        c "Despite the fact that I haven't ordered any drinks, I want some alcohol."

    else:
        c "This situation gives me a thirst that only alcohol can quench."

    Kx wtf "That's not healthy!"
    c "I know, I'm just stressed. Sorry to drag this upon you."
    Kx normal crossed "No need to apologize. You're in a situation I couldn't even imagine being in. I won't judge."
    c "Let's go to the bar, then."
    Kx "Lead the way."
    
    scene black with fade
    $ renpy.pause (0.8)
    scene buildingoutside with fade
    $ renpy.pause (1.0)

    c "Hang on."
    show kothorix normal crossed with dissolve
    Kx "What is it?"
    c "Is that an arcade?"
    Kx "Yes, it is. why do you ask?"

    menu:
        "Go to arcade.":
            c "I haven't been to an arcade in ages. Can we go in?"
            Kx "Sure! Let's have some fun."
            $ koth_arcade = True
            jump kothorix_arcade

        "Don't go to arcade.":
            c "No reason. I'm just curious."
            
            scene black with fade
            $ renpy.pause (0.5)
            jump kothorix_bar