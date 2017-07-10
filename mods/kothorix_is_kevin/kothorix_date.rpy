#The post meet with Kothorix date scene
label Kothorix_mod_date:
    #setting some variables
    $ exampleroute_scene += 1   #I still don't know what this does. I think it's threatening me, help I'm scared
    $ KothorixDated += 1        #Stops the "Meet with Kothorix." option from appearing again
    $ mchasbeenwarned = False
    $ knowAnnaDate = False

    #Sets the name for the Save File Name
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Kothorix Cafe"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Kothorix Cafe"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Kothorix Cafe"

    else:
        $ save_name = "Chapter 1 - Kothorix Cafe"

    #Add music to the scene that I never realized was mute
    play music "mx/elegant.ogg" fadein 1.0   

    c "Hey, what's this on the back of Kothorix's photo?" ### comma
    show callmecard at truecenter with moveinright
    c "It's his phone number."
    hide callmecard with moveoutleft

    play sound dialout
    m "{i}ring.... ring....{/i} {w=30.0}{nw}" #banana uwu
    stop sound
    Kx "Yes?"
    c "Hello, Kothorix, it's me [player_name] from the other day."

    #He still doesn't like you using his name, I think you should stop.
    if player_name == "Kothorix":
        Kx "Why are you still using my name? I don't like it, but I guess I can't stop you!"
        Kx "What do require from the {b}real{/b} Kothorix?"
    elif player_name == "Adam":
        Kx hey you "Hey modmaster, what can I do for you?"
    else:
        Kx "Oh, it's the human! What do you want?" 

    c "Do you want to hang out again today? It was fun the last time."
    Kx "Oh no! A fan girl." 
    c "Hey, I ain't no fan girl. I'm just giving you the opportunity to hang out with a real celebrity." 
    Kx "Trying to call my bluff, huh?"
    c "What? You think I didn't notice how quickly you were willing to walk with me to the portal?"
    Kx "..."
    m "I think I struck a nerve."
    Kx "Fine."
    Kx "I was planning to get a coffee, anyway. Meet me at the cafe."
    c "By the way, I'd like to thank you for including me in your plans today. You were planning to invite me, yes?" 
    Kx "Uh... I guess."

    stop music fadeout 1.0      #Stops any playing music
    stop sound fadeout 1.0      #Stops any active sound FX's

    #Scene Begin
    scene black with fade
    $ renpy.pause (0.5)
    play music terrace fadein 1.0
    #Custom background to reference the 50 shades of reza mod
    scene cafer with fade
    $ renpy.pause (1.2)

    #Adine is alive so she can serve you.
    $ satwindow = False
    $ twocoffee = False

    m "No sign of Kothorix. I suppose I'll pick a table for us then."
    menu:
        "Sit by window.":
            $ satwindow = True
            #the sound effect makes it sound like he's unsticking his face from the window.
            m "It's a nice day outside. Might as well enjoy the view."
            play sound runawayfxkx
            $ renpy.pause (0.3)
            scene cafe with dissolve
            $ renpy.pause (1.5)
            m "What was that?"


        "Sit away from window.":
            m "It's a bit hot beside the window. I'll sit closer to the counter."

    show adine normal b flip at left with easeinleft
    
    if adinestatus == "bad":
        Ad annoyed b flip "As much as I don't want to serve you, I have to."
        Ad normal b flip "What can I get you?"
        menu:
            "Two coffees.":
                $ twocoffee = True
                Ad frustrated b flip "So you're going to be here twice as long. Great"

                hide adine 
                show adine frustrated b at left

            "One coffee.":
                Ad "On its way."

                hide adine
                show adine normal b at left
    else:  
        Ad "Oh, hello [player_name]. What can I get you today?"
        menu:
            "Two coffees":
                $ twocoffee = True
                Ad think b flip "Two cups of coffee? Is someone joining you?"
                menu:
                    "Kothorix.":
                        $ mchasbeenwarned = True
                        c "I'm meeting with a guy named Kothorix. We met the other day."
                        Ad annoyed b flip "Be careful with him."
                        c "Why?"
                        Ad normal b flip "He tends to latch onto people who give him attention."
                        if adinestatus == "good":
                            c "Does he like someone?"
                            Ad giggle b flip "Yeah he does. It's hilarious because he has no chance with her."
                            Ad normal b flip "Before you ask, I'm not saying who he likes. However, she may come in a while if you're lucky."
                        c "Noted. Thank you, Adine."

                    "Yeah, but not saying who.": #comma
                        Ad normal b flip "I'll see them in a bit anyway."

                Ad "Two cups of coffee coming up."

                hide adine
                show adine normal b at left

            "One coffee":
                $ twocoffee = False
                c "Just the one cup of coffee please, Adine."
                if food == "coffee":
                    c "I enjoyed the coffee last time."
                    Ad think b flip "That time with Reza?"
                    c "Yeah, that time. I can't say much for the company I was with, but the coffee was great." # commas
                    Ad giggle b flip "Thanks, I made that coffee myself."
                Ad normal b flip "One cup of coffee coming up."

                hide adine
                show adine normal b at left

    hide adine with easeoutleft

    if satwindow == True:
        m "Looking out, I saw Kothorix on his way down the street."
        m "He was still waving at people, flicking his mane for attention." 
    else:
        m "Suddenly, Kothorix arrived."

    show kothorix normal with dissolve
    Kx "So, you want to have a date then. I can't blame you, I am attractive."
    Kx thinking "How did you get my number anyway?"
    c "It was on the back of the photo you gave me yesterday."
    Kx normal "Oh right, you weren't supposed to get one of those pictures."

    show kothorix normal crossed distance flip at right with ease
    show adine normal b flip at left with easeinleft

    if twocoffee == True:
        if adinestatus == "bad":
            play sound cuptable
            queue sound silence
            queue sound cuptable
            $ renpy.pause (1.0)

            Ad "Here's the coffee." 
            Kx "Oh! Hello, my dear."
            Ad annoyed b flip "STOP trying to get my number!"

            hide adine
            show adine annoyed b at left
        else:
            play sound cuptable
            queue sound silence
            queue sound cuptable
            $ renpy.pause (1.0)

            Ad "Here's your coffee, gentlemen. Enjoy." # comma
            Kx "Wait, you forgot something."
            Ad think b flip "What did I forget?"
            Kx "You forgot to leave your number."
            Ad annoyed b flip  "Stop trying to get my number."

            hide adine
            show adine annoyed b at left

    else:
        if adinestatus == "bad":
            play sound cuptable
            $ renpy.pause (0.5)

            Ad "Here's your coffee, [player_name]." # comma
            Ad "What can I get the gentleman?"
            Kx "Rawr, I'll take your number."
            Ad annoyed b flip "You say that every time you come in here. The answer hasn't changed." 
            Kx "In that case, I'll have a cup of tea." # comma
            Ad normal b flip "Coming right up."

            hide adine
            show adine normal b at left
        else:
            play sound cuptable
            $ renpy.pause (0.5)

            Ad "Enjoy your coffee, [player_name]." # comma
            Ad "What can I get you Kothorix?"
            Kx "Rawr, I wouldn't mind getting your number."
            Ad annoyed b flip "You say that every time you come in here. The answer hasn't changed."
            Kx "In that case, I'll have a cup of tea." # comma
            Ad normal b flip "Coming right up."

            hide adine
            show adine normal b at left

    hide adine with easeoutleft
    show kothorix normal crossed distance flip at center with ease
    show kothorix normal crossed with dissolvequick

    if twocoffee == True:
        Kx "Thanks for ordering me coffee."
        c "No problem, Kothorix." ### coffee

    c "You horn-dog."
    Kx thinking "Why are you calling me a dog? What's a dog?"
    c "A dog is a small furry animal that humans keep as pets."
    c "Long ago, dogs and humans formed a mutual bond. The dogs helped out their human counterparts with their superior sense of smell, while the humans protected the dogs from external harm." 
    c "The dog quickly overtook the wolf in terms of population."
    c "Eventually, dogs evolved to have the ability to communicate with humans at birth, which is why dogs are one of few creatures that look into a human's eyes."
    Kx displeased "A bit extreme of an explanation." 
    Kx thinking "Do these dogs have horns?"
    c "No. Dogs don't have horns."
    Kx "Then why did you call me a horn-dog?"
    c "Nevermind, it's just a saying."

    if satwindow == True:
        Kx normal crossed distance "Ahh, I see my bae walking down the street."
        Kx "And in she comes now."

    elif satwindow == False:
        Kx normal crossed distance "I see my bae coming in for her usual coffee."

    if annastatus == "good":
        m "I waved at Anna as she came into the cafe. She smiled at me. Upon seeing Kothorix, her smile quickly turned to a scowl."

        show kothorix normal at left with ease
        show anna normal at right with easeinright #new

        An "Hello, [player_name], what brings you?"
        Kx ramble "I have a name, you know! I know that you know it."
        An face "Yes, Kothorix, I do remember your name. {i}Thank you sooooo much for reminding me of it.{\i}"
        An normal "[player_name], you should be careful with this guy..."
        show kothorix displeased at left with dissolvequick 

        if mchasbeenwarned == True:
            Ad "I've already warned [player_name], Anna."
            An face "..."
            Ad "Sorry."
        else:
            if adinestatus == "bad":
                An normal "This guy is a fame-whore. He'll stick like glue to anyone who can get him noticed."
                Kx wtf "What!? No way. Not true."
                Ad frustrated "Of course not... Kothorix would {i}never{/i} stoop that low, would he?"
                c "I see. Thanks for the heads up, Anna."

            else:
                An normal "This guy is a fame-whore. He'll stick like glue to anyone who can get him noticed."
                Kx wtf "What!? No way. Not true."
                Ad "Yes, it is."
                c "I see. Thanks for the heads up, Anna."

        Kx displeased "Looks like it's as good time as any for you to depart, Anna."

        menu:
            "Calm them down.":
                c "I'm sorry, but I don't think this is not a good time for this conversation."
                show kothorix sad down at left
                show anna sad at right 
                with dissolve

                An "You're right."
                An normal "[player_name], if this guy gives you any trouble, let me know. I'll run some {i}tests{/i} on him for you."
                c "Thank you, Anna."
                Kx wtf "Don't I get a say in this?"
                An "No."

            "Inquire.":
                $ knowAnnaDate = True
                c "How do you two know each other?"
                An sad "..."
                Kx normal crossed "We dated for a time."
                An face "That's not quite how it happened!"
                c "Well, Anna, why don't you tell me about your dating adventures."
                An "It was, and still is, a stalker and innocent Anna kind of adventure."
                Kx wtf "Not true."
                c "I see."
                show kothorix uninterested distance flip at left with dissolve
                An sad "I confronted him about it and he insisted on taking me out for an apology dinner."
                An "I knew he wouldn't take a no for an answer, and he knows where I work, so I couldn't hide."
                An face "So, I agreed."
                Kx "It was a nice dinner. I made it myself."
                An disgust "Yes, since beans on toast is such a delicacy around here. Especially on a date to Tatsu Park!"

                if remy3unplayed == False:
                    if remystatus == "good":
                        Kx "I thought it was pretty romantic."
                    else:
                        Kx "I thought it was nice."
                else:
                    Kx "I thought it was nice."

                An face "I'm sorry, [player_name]. I shouldn't have brought this up."

        An normal "I'm going to have my coffee now. Enjoy your day, [player_name]."
        show kothorix normal crossed at left with dissolve

        An "Oh! Before I leave..."

        show anna at center with ease

        #Slapping Koth
        play sound slap
        show kothorix eyes closed
        $ renpy.pause (0.2)
        show anna at right with ease
        $ renpy.pause (0.1)
        show anna at right with ease
        show kothorix sad down

        #Hiding anna and showing an upset Kothorix
        $ renpy.pause (0.3)
        An "For old times' sake."
        show anna normal flip
        hide anna with easeoutright
        show kothorix at center with ease

        Kx somber face "Let's leave."


    elif annastatus == "bad":
        m "I waved at Anna as she came into the cafe. She doesn't respond. Upon seeing Kothorix, her expression quickly turned into a smirk." 

        show kothorix normal at left with ease
        show anna normal at right with easeinright

        An "Hello ye two, what brings you here?"
        Kx ramble "[player_name] offered to have coffee with me and I, being fair and benevolent, agreed."
        m "I'm pretty sure that's not what happened."
        Kx normal crossed distance "Are you in here for your usual coffee?"
        An disgust "Yes, but how would you know that?"
        Kx "I've seen you come in here from time to time."
        An "... How'd you see me come in here?"
        Kx ramble"... {w=0.5}{nw}"

        show kothorix sad down at left with dissolvequick

        An rage "I knew it, you're stalking me!"
        Kx ramble "No, I’m not. I just happened to see you around."
        Kx normal crossed distance "So, while you’re here, why don’t you give me your number?"
        An "You want my number? Why would I give a stalker my number?!"
        m "Anna stood still for a moment, fuming."
        show anna furious at right

        show anna at center with ease

        #Slapping Koth
        play sound slap
        show kothorix eyes closed
        $ renpy.pause (0.2)
        show anna at right with ease
        $ renpy.pause (0.1)
        show anna at right with ease
        show kothorix sad down

        #Hiding anna and showing an upset Kothorix
        show anna disgust
        $ renpy.pause (0.5)
        show anna disgust flip
        hide anna with easeoutright
        show kothorix at center with ease
     
        An "Don't let me see you again!"
        Kx somber face "Let's leave."


    else: 
        #anna status neutral
        m "I waved at Anna as she came into the cafe. She smiled at me. Upon seeing Kothorix, her expression quickly turned to concern."

        show kothorix normal at left with ease
        show anna normal at right with easeinright 

        An "Hello, [player_name]." 
        Kx "{i}..cough..{\i}"
        An face "Hello, Kothorix."
        Kx ramble "You do remember my name! I was almost worried there for moment."
        An face "Believe me, I've tried to forget!"
        Kx normal "You see, [player_name]! I always leave an impact on the ladies."
        Kx ramble "So, Anna, how about you give me your number?"
        An disgust "If you're not careful, I'll imprint my number on your face!"
        An normal "[player_name], I've decided warn you about this guy."
        show kothorix displeased at left with dissolvequick     

        if mchasbeenwarned == True:
            Ad "Anna, I've already told him."
            An face "..."
            Ad "Sorry."
        else:
            if adinestatus == "bad":
                An normal "This guy is a fame-whore. He'll stick like glue to anyone who can get him noticed."
                Kx wtf "What!? No way. Not true."
                Ad frustrated "Of course not... Kothorix would {i}never{/i} stoop that low, would he?"
                c "I see. Thanks for the heads up, Anna."

            else:
                An normal "This guy is a fame-whore. He'll stick like glue to anyone who can get him noticed."
                Kx wtf "What!? No way. Not true."
                Ad "Yes, it is."
                c "I see. Thanks for the heads up, Anna."

        show kothorix uninterested distance flip at left with dissolvequick  
        Kx "Don't believe them, [player_name]. They've always been jealous of me." 
        show anna normal at right with dissolve
        m "Anna erupted into a fit of laughter."
        An "Ha ha ha, I needed a laugh today."
        
        show kothorix sad down at left with dissolve
        An "Well, you have been warned."
        An "Before I leave..."

        show anna at center with ease

        #Slapping Koth
        play sound slap
        show kothorix eyes closed
        $ renpy.pause (0.2)
        show anna at right with ease
        $ renpy.pause (0.1)
        show anna at right with ease
        show kothorix sad down

        #Hiding anna and showing an upset Kothorix
        $ renpy.pause (0.3)
        An "That's for stalking me."
        show anna normal flip
        hide anna with easeoutright
        show kothorix at center with ease
     
        Kx somber face "Let's leave."

    if twocoffee == False:
        Ad "Tea?"

    jump kothorix_alley