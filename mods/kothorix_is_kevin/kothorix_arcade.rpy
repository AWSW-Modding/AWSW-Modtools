label kothorix_arcade:

    #Sets the name for the Save File Name
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Kothorix Arcade"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Kothorix Arcade"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Kothorix Arcade"

    else:
        $ save_name = "Chapter 1 - Kothorix Arcade"


    stop music fadeout 1.5
    scene black with fade
    $ renpy.pause (0.8)
    play music bolt fadein 1.0
    scene arcade with fade
    $ renpy.pause (1.0)

    show kothorix normal crossed dk with dissolve

    c "Oh man, it's been ages since I've been inside an arcade. There's none at home anymore."
    c "Come on Kothorix, let's have a game of something. What's good?"
    Kx thinking dk "I don't know. These are brand new, and I haven't been able to try them yet."
    Kx normal dk "Hey, that guy over there. He looks like he might know a good game."
    m "Kothorix grabs the attention of a furry dragon who was about to leave."
    
    show kothorix normal dk at left with ease
    show kevin normal at right with easeinright

    Kv ramble dk "Are you guys interested in our Midwest Institution?"
    Kx ramble dk "Afraid not, we're just looking for a good game to play. Any recommendations?"
    Kv brow dk "Oh, I see."
    Kv normal dk "Over there. It's a neat one."
    m "The furry dragon pointed towards an empty cabinet in the corner."
    Kv "With that, I'll be off then! Good luck with the game."

    hide kevin
    show kevin normal flip at right
    hide kevin with easeoutright
    show kothorix normal crossed dk at center with ease

    c "Do you know him?"
    Kx ramble face dk "I've seen him before. He stands around handing out those fliers. He was always trying to give me one, so I avoid the guy."
    Kx normal crossed dk "Although he stopped bothering me after I threatened to shave him." 
    c "Ha. Anyway, come on, let's try that game."
    m "Looking at the cabinet, we saw that the game was called Ronan's adventures. It featured a human named Ronan and a dragon named Querisrak."
    
    if remy1unplayed == False:
        c "Hey, I think I've heard of this game before. I think it's the one Remy has on his office computer. I hope this one works."
        Kx thinking dk "What do you mean? Didn't Remy's game work?"
        c "I, um..."
        Kx "Well, I hope that doesn't happen to us, or else we'd lose our progress."
        if remy2unplayed == False:
            c "He told me a few days later that he managed to rescue his save for the game."
            Kx normal crossed dk "Well, that's good. If you lost my save, I'd make you play the game up till that point you broke it."
            c "He said the same thing." 

    Kx normal crossed dk "Hey, how about you play the human and I play as the dragon. For obvious reasons."
    c "Sure."
    Kx normal crossed dk "Here, I'll pay for it."

    play sound coin 
    $ renpy.pause (1.2)

    stop music fadeout 1.5
    scene rpg with fade

    play music kothorixtheme fadein 1.0 

    show genDrag 1 #Querisrak green dragon
    show koth 2 #Eldgar aka Kothorix
    show ronan 1
    with dissolveslow

    show genDrag 2 at Pan ((0, 0), (-50, 0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: There you are, you fiend. Finally! Are you ready to face us like a man? Return to us our females!{/font}{/color}"
    show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause (0.2)

    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Oh Querisrak, always the jealous type.{/font}{/color}"
    show koth 2 at Pan ((50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show genDrag 2 at Pan ((0, 0), (-50, 0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: You have been taking and ravaging our women for far too long.{/font}{/color}" 

    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: It began small, but now, you've taken my wife and daughters. We were friends! What did I ever do to you to deserve this?{/font}{/color}"
    show genDrag 1 at Pan ((-50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Don't blame me, they chose me. Not my fault. I am merely fulfilling a \"need.\"{/font}{/color}"
    show koth 2 at Pan ((50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: HOW DARE YOU!. They are my family! It is my job to protect them from the likes of you. Return them to me this instant or prepare for trouble!{/font}{/color}"
    show genDrag 1 at Pan ((-50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Make it double!{/font}{/color}"
    show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause (0.2)

    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Your wife and daughters are choosing to be with me. I am not holding them captive. {/font}{/color}"
    show koth 2 at Pan ((50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: I do not believe you. I CAN NOT believe you.{/font}{/color}"
    show genDrag 1 at Pan ((-50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Avoiding the truth and believing only lies will lead to nothing but pain!{/font}{/color}" 
    show koth 2 at Pan ((50, 0), (0, 0), 0.1)

    $ renpy.pause (0.2)

    show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Grrr!{/font}{/color}"
    show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause (0.2)


    #----------------------------------------------battle start----------------------------------------------

    $ usedreason = 0
    $ usedattack = 0
    $ menuchoice = 0
    $ genDragstatus = "normal"
    $ usedcosmichorror = False

    Al "{color=#FFFFF0}{font=Munro.ttf}Battle start!{/font}{/color}"

    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Al "{color=#FFFFF0}{font=Munro.ttf}Eldgar uses Musk!{/font}{/color}"

    play sound "fx/rpg/wind.ogg"
    $ renpy.pause (2.0)

    play sound "fx/rpg/hit.ogg"

    show genDrag 1 with vpunch
    Al "{color=#FFFFF0}{font=Munro.ttf}Querisrak is overwhelmed by musk and loses a turn.{/font}{/color}"
    $ renpy.pause (0.2)
    Kx "Damn it."

    $ genDragstatus = "stunned"

    play sound hitfail
    $ renpy.pause (0.1)

    show ronan 2 at Pan ((0, 0), (-10, 0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((-10, 0), (0,0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((0, 0), (-10, 0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((-10, 0), (0,0), 0.1)
    $ renpy.pause (0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan is immune to dragon musk.{/font}{/color}"

    show koth 2 at Pan ((50, 0), (0, 0), 0.1)

    $ renpy.pause (0.3)
    
    $ menuchoice = renpy.call_screen("action_menu")

    if menuchoice == 1:
        $ usedreason += 1
        show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Think about this Eldgar, you're outnumbered and outmatched. Just surrender and we'll take the females home.{/font}{/color}"
        show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause (0.2)

        show koth 1 at Pan ((0, 0), (50,0), 0.1)
        Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: How many times do I have to say this. I am NOT holding anyone captive. They choose to join me!{/font}{/color}"
        Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: How is it so difficult to understand?{/font}{/color}"
        show koth 2 at Pan ((50, 0), (0, 0), 0.1)

        $ renpy.pause (0.2)

    elif menuchoice == 2:
        $ usedattack += 1
        show ronan 2 at Pan ((0, 0), (-440, 0), 0.8)
        $ renpy.pause (0.2)
        play sound slap
        $ renpy.pause (0.2)
        show ronan 1 at Pan ((-440, 0), (0,0), 0.8)
        $ renpy.pause (0.8)

        show koth 1 at Pan ((0, 0), (50,0), 0.1)
        Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: What kind of attack was that? A slap? Is that seriously the best you got?{/font}{/color}"
        show koth 2 at Pan ((50, 0), (0, 0), 0.1)

        $ renpy.pause (0.2)

    elif menuchoice == 3:
        $ usedcosmichorror = True
        jump cosmic_horror

    else:
        Db "You somehow broke the game, good for you."
        Db "You know what, I'm not even going to let you finish the rpg I worked so hard on, I'm skipping you ahead!"
        jump kothorix_arcade_end

    #He'll always be stunned here.
    if genDragstatus == "stunned":
        $ genDragstatus = "normal"
        Al "{color=#FFFFF0}{font=Munro.ttf}Musk has worn off, Querisrak returns to normal.{/font}{/color}"


    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Al "{color=#FFFFF0}{font=Munro.ttf}Eldgar uses Earthquake!{/font}{/color}"

    play sound "fx/rpg/quake.ogg"
    show genDrag 1 with Shake((0, 0, 0, 0), 3.0, dist=30)
    show koth 2 at Pan ((50, 0), (0, 0), 0.1)
    play sound "fx/rpg/hit.ogg"
    show genDrag 1 with vpunch
    Al "{color=#FFFFF0}{font=Munro.ttf}Querisrak trips, hitting is head on a rock. Querisrak loses a turn.{/font}{/color}"

    $ genDragstatus = "stunned"
    Kx "Seriously AGAIN!"
    $ renpy.pause (0.1)

    play sound hitfail
    $ renpy.pause (0.1)

    show ronan 2 at Pan ((0, 0), (-10, 0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((-10, 0), (0,0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((0, 0), (-10, 0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((-10, 0), (0,0), 0.1)
    $ renpy.pause (0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan is a bit shook but otherwise OK.{/font}{/color}"
    c "Yay for the humans."
    $ renpy.pause (0.3)


    #-------------option menu 2-------------------------------------------------------------------
    $ menuchoice = renpy.call_screen("action_menu")

    if menuchoice == 1:
        $ usedreason += 1

        if usedreason == 1:
            show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Think about this Eldgar, you're outnumbered and outmatched. Just surrender and we'll take the females home.{/font}{/color}"
            show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

            $ renpy.pause (0.2)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: How many times do I have to say this. I am NOT holding anyone captive. They choose to join me!{/font}{/color}"
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: How is it so difficult to understand?{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

        elif usedreason == 2:
            show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I'll tell you again Eldgar, stand down.{/font}{/color}"
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: You can not win this battle. Just surrender and we all can just go home.{/font}{/color}"
            show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

            $ renpy.pause (0.2)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: {i} pant pant pant {/i} I will not stand down.{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

    elif menuchoice == 2:
        $ usedattack += 1

        if usedattack == 1:
            show ronan 2 at Pan ((0, 0), (-440, 0), 0.8)
            $ renpy.pause (0.2)
            play sound slap
            $ renpy.pause (0.2)
            show ronan 1 at Pan ((-440, 0), (0,0), 0.8)
            $ renpy.pause (0.8)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: What kind of attack was that? A slap? Is that seriously the best you got?{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

        elif usedattack == 2:
            show ronan 2 at Pan ((0, 0), (-440, 0), 0.8)
            $ renpy.pause (0.2)
            play sound slap
            $ renpy.pause (0.2)
            show ronan 1 at Pan ((-440, 0), (0,0), 0.8)
            $ renpy.pause (0.8)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Again with the slapping? That hurt!{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

    elif menuchoice == 3:
        $ usedcosmichorror = True
        jump cosmic_horror
    else:
        Db "You somehow broke the game, good for you."
        Db "You know what, I'm not even going to let you finish the rpg I worked so hard on, I'm skipping you ahead!"
        jump kothorix_arcade_end

    if genDragstatus == "stunned":
        $ genDragstatus = "normal"
        Al "{color=#FFFFF0}{font=Munro.ttf}Querisrak has come around and seems ready for battle.{/font}{/color}"

    show koth 1 at Pan ((0, 0), (50,0), 0.1)
    Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: ENOUGH OF THIS!{/font}{/color}"
    Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: It's time for my strongest attack: Lightning Storm!{/font}{/color}"

    $ renpy.pause (0.8)
    play sound lightning
    $ renpy.pause (0.4)
    show genDrag 1 with Shake((0, 0, 0, 0), 6.0, dist=30)

    show koth 2 at Pan ((50, 0), (0, 0), 0.1)
    $renpy.pause (0.2)

    play sound "fx/rpg/hit.ogg"
    show genDrag 1 with vpunch
    Al "{color=#FFFFF0}{font=Munro.ttf}Querisrak gets hit by lightning. Querisrak falls over unconscious, and it looks like he won't be getting up anytime soon.{/font}{/color}"

    $ genDragstatus = "stunned"
    Kx "Wha... why? I just want to make one attack."

    $ renpy.pause (0.2)
    play sound hitfail
    $ renpy.pause (0.1)

    show ronan 2 at Pan ((0, 0), (-10, 0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((-10, 0), (0,0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((0, 0), (-10, 0), 0.1)
    $ renpy.pause (0.1)
    show ronan 2 at Pan ((-10, 0), (0,0), 0.1)
    $ renpy.pause (0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan dodged the lightning bolt just in time.{/font}{/color}"
    c "This is just too easy."
    $ renpy.pause (0.3)


    #-------------option menu 3-------------------------------------------------------------------
    $ menuchoice = renpy.call_screen("action_menu")

    if menuchoice == 1:
        $ usedreason += 1

        if usedreason == 1:
            show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Think about this Eldgar, you're outnumbered and outmatched. Just surrender and we'll take the females home.{/font}{/color}"
            show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

            $ renpy.pause (0.2)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: How many times do I have to say this. I am NOT holding anyone captive. They choose to join me!{/font}{/color}"
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: How is it so difficult to understand?{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

        elif usedreason == 2:
            show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I'll tell you again Eldgar, stand down.{/font}{/color}"
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: You can not win this battle. Just surrender and we all can just go home.{/font}{/color}"
            show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

            $ renpy.pause (0.2)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: {i} pant pant pant {/i} I will not stand down.{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

        elif usedreason == 3:
            show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Your strongest attack barely ruffled the dandruff on my shoulders.{/font}{/color}"
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: This is your last warning Eldgar! I've told you before that you cannot win this battle. It is futile to try.{/font}{/color}"
            Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I will NOT try to talk you down again!{/font}{/color}"
            show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

            $ renpy.pause (0.2)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: {i} pant pant pant {/i} WHAT ARE YOU?!? How do keep avoiding my attacks? {/font}{/color}"
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: {i}sigh{/i} Fine you win.{/font}{/color}"
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: You can explain to the females why they are being forced to go home!{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

    elif menuchoice == 2:
        $ usedattack += 1

        if usedattack == 1:
            show ronan 2 at Pan ((0, 0), (-440, 0), 0.8)
            $ renpy.pause (0.2)
            play sound slap
            $ renpy.pause (0.2)
            show ronan 1 at Pan ((-440, 0), (0,0), 0.8)
            $ renpy.pause (0.8)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: What kind of attack was that? A slap? Is that seriously the best you got?{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

        elif usedattack == 2:
            $ usedattack += 1
            show ronan 2 at Pan ((0, 0), (-440, 0), 0.8)
            $ renpy.pause (0.2)
            play sound slap
            $ renpy.pause (0.2)
            show ronan 1 at Pan ((-440, 0), (0,0), 0.8)
            $ renpy.pause (0.8)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Again with the slapping? That hurt!{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)

        elif usedattack == 3:
            show ronan 2 at Pan ((0, 0), (-440, 0), 0.8)
            $ renpy.pause (0.2)
            play sound slap
            $ renpy.pause (0.2)
            show ronan 1 at Pan ((-440, 0), (0,0), 0.8)
            $ renpy.pause (0.8)

            show koth 1 at Pan ((0, 0), (50,0), 0.1)
            Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: Stop slapping me! It hurts!{/font}{/color}"
            show koth 2 at Pan ((50, 0), (0, 0), 0.1)

            $ renpy.pause (0.2)


    elif menuchoice == 3:
        $ usedcosmichorror = True
        jump cosmic_horror
    else:
        Db "You somehow broke the game, good for you."
        Db "You know what, I'm not even going to let you finish the rpg I worked so hard on, I'm skipping you ahead!"
        jump kothorix_arcade_end


    #----------wife appears----------happy ending yay--------------------
    if usedreason == 3:
        show wifeDrag at Pan ((0, 0), (1200,0), 1.5)
        $ renpy.pause(1.5)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Eldgar! Querisrak! Ronan! Stop fighting.{/font}{/color}"

        if genDragstatus == "stunned":
            $ genDragstatus = "Normal"
            Al "{color=#FFFFF0}{font=Munro.ttf}By the sound of his beloved's voice, Querisrak regains consciousness.{/font}{/color}"

        show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Ashima, we have come to take you home.{/font}{/color}"
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Querisrak, I didn't think you cared. You work all day and you're out all night, I thought...{/font}{/color}"
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: I thought you didn't want to be together any more. It hurt too much to spend all my time in an empty home and in a cold bed, waiting for a man I thought was done with me.{/font}{/color}"
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: I love you, Ashima. I know I don't say that enough, but you're the best thing that has ever happened to me. I never want to lose you.{/font}{/color}"
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Are our kids OK?{/font}{/color}"
        show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Yes, we are all OK. Eldgar wasn't lying; we chose to come here with him. He's a great friend who offered me a shoulder to cry on when I needed it.{/font}{/color}"
        
        show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I guess that means we owe you an apology, Eldgar. Sorry.{/font}{/color}"
        show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause (0.1)

        show koth 1 at Pan ((0, 0), (50,0), 0.1)
        Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: It's OK. {/font}{/color}"
        show koth 2 at Pan ((50, 0), (0, 0), 0.1)

        $ renpy.pause (0.1)

        show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: I'm so sorry, Ashima. I love you Ashima, and I always have and always will.{/font}{/color}"
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Will you take me home?{/font}{/color}"
        show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause (0.1)

        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Yes, yes I will.{/font}{/color}"

        stop music fadeout 2.0


    #----------wife appears----------bad ending boo--------------------
    elif usedattack == 3:
        show wifeDrag at Pan ((0, 0), (1200,0), 1.5)
        $ renpy.pause(1.5)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Eldgar! Querisrak! Ronan! Stop fighting.{/font}{/color}"
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Why are you even here!{/font}{/color}"

        if genDragstatus == "stunned":
            $ genDragstatus = "Normal"
            Al "{color=#FFFFF0}{font=Munro.ttf}By the sound of his beloved's voice, Querisrak regains consciousness.{/font}{/color}"

        show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Ashima, we have come to rescue you!{/font}{/color}"
        show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)
        $ renpy.pause(0.1)

        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Oh my god, you hurt Eldgar! You idiots! I chose to come here!{/font}{/color}" 

        show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I guess that means we owe you an apology, Eldgar. I'm sorry I hurt you.{/font}{/color}" 
        show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause (0.1)

        show koth 1 at Pan ((0, 0), (50,0), 0.1)
        Ks "{color=#FFFFF0}{font=Munro.ttf}Eldgar: I'll be fine in a while. {/font}{/color}"
        show koth 2 at Pan ((50, 0), (0, 0), 0.1)

        $ renpy.pause (0.1)

        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Querisrak, you work all day and you're out all night. It's clear that you don't actually love me and I am just a trophy wife for you to show off!{/font}{/color}"
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Eldgar offered what I need, love.{/font}{/color}"

        show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: I love you Ashima. I know I don't say that enough, you are the best thing that has ever happened to me. I never want to lose you.{/font}{/color}"
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Are our kids OK?{/font}{/color}"
        show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause(0.1)

        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Yes, the kids are fine."

        show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: I'm so sorry, Ashima. I love you, Ashima! I always have and always will.{/font}{/color}"
        Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Will you take me home?{/font}{/color}"
        show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause (0.1)

        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: No.{/font}{/color}"
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: I've spent too much time in an empty house and a cold bed waiting for a man I thought was done with me.{/font}{/color}"
        Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Goodbye, Querisrak.{/font}{/color}"

        stop music fadeout 2.0


    #--------------------Forced Bad ending--------------------
    else:
        show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
        Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I'm sorry Eldgar, but it's time to end this!{/font}{/color}"
        show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

        $ renpy.pause (0.1)

        jump cosmic_horror

    #--------------------return to end of scene--------------------
    jump kothorix_arcade_end

#--------------------Cosmic horror attack--------------------
label cosmic_horror:
    show ronan 2
    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: Grrrrrrrr!{/font}{/color}"
    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan invokes Cosmic Horror! {/font}{/color}"

    play sound "fx/rpg/whoosh.ogg"
    scene space
    show koth 2
    with dissolve

    play sound "fx/rpg/horror.ogg"

    $ renpy.pause (1.0)

    show skull with dissolveslow3

    hide skull
    scene rpg
    show genDrag 1
    show koth 2
    show ronan 1
    with dissolve

    play sound "fx/rpg/hit.ogg"
    show koth 2 with vpunch
    Al "{color=#FFFFF0}{font=Munro.ttf}Eldgar is overcome by cosmic forces and is badly injured.{/font}{/color}"


    #----------wife appears----------very bad ending boo--------------------
    show wifeDrag at Pan ((0, 0), (1200,0), 1.5)
    $ renpy.pause(1.5)
    Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Eldgar! Querisrak! Ronan! Stop fighting.{/font}{/color}"
    Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Why are you even here!{/font}{/color}"

    if genDragstatus == "stunned":
        $ genDragstatus = "Normal"
        Al "{color=#FFFFF0}{font=Munro.ttf}By the sound of his beloved's voice, Querisrak regains consciousness.{/font}{/color}"

    show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: Ashima, we have come to rescue you!{/font}{/color}" 
    show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause(0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Oh my god, Eldgar! What have you idiots done! Why would you hurt him!{/font}{/color}"

    show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: We... we.. thought.{/font}{/color}"
    show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause(0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: Oh, so that was the problem.{/font}{/color}"

    show genDrag 2 at Pan ((0, 0), (-50,0), 0.1)
    Gd "{color=#FFFFF0}{font=Munro.ttf}Querisrak: So you actually chose to be with him?{/font}{/color}" 
    show genDrag 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause(0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: YES. I will not be your trophy wife! We're though Querisrak, and I don't want to see you again.{/font}{/color}"

    show ronan 2 at Pan ((0, 0), (-50, 0), 0.1)
    Al "{color=#FFFFF0}{font=Munro.ttf}Ronan: I'm sorry.{/font}{/color}"
    show ronan 1 at Pan ((-50, 0), (0,0), 0.1)

    $ renpy.pause (0.1)

    Al "{color=#FFFFF0}{font=Munro.ttf}Ashima: {b}Oh shut it and leave!{/b}{/font}{/color}"

    stop music fadeout 2.0

    #--------------------return to end of scene--------------------
    jump kothorix_arcade_end


label kothorix_arcade_end:
    $renpy.pause (1.0)
    scene black with fade
    play music bolt fadein 1.0
    $ renpy.pause (0.5)
    scene arcade with fade
    $ renpy.pause (1.0)

    show kothorix normal crossed dk with dissolve

    c "Well, that was... different."
    c "At home, these kinds of games are much longer, and the guy we fight is clearly an unforgivable character."
    c "Plus, the whole domestic dispute thing at the end was a bit off..." 
    Kx ramble face dk "Yeah, it is a different kind of game. I guess that's why Kevin recommended it."
    c "Come to think of it, these arcade machines are similar to the ones we had at home."
    Kx normal crossed dk "Yeah, what of it?"
    c "Also, how do dragons without hands play these games?"
    Kx ramble face dk "Yeah, they are at a disadvantage in that regard. In most places you can use a mat with buttons on it."
    c "Wait, what? A mat is placed on the floor and the dragon press the buttons with their paws?"
    Kx normal dk "It works just like DDR, a game more formally known as Dancing Dragon Revolution."
    c "Well, I suppose that's logical, but how well does it work in practice?" 
    Kx somber face dk "Not great. Anyone who wants a mat must request it from behind the counter. Worse still, the mat takes up a lot of space."
    Kx "As a result, those without hands don't bother with the arcade."
    Kx normal crossed dk "But that's not too bad. It means more free cabinets for us to use."
    Kx "Speaking of which, would you like to have another game?"
    c "No, I don't, let's just move on to the bar."
    Kx "Okie Dokie."

    stop music fadeout 2.0

    scene black with fade
    $ renpy.pause (0.5)
    play music terrace fadein 1.0
    jump kothorix_bar