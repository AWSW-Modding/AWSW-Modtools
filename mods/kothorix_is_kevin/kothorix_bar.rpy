label kothorix_bar:
    
    $ gotMeat = True

    #Sets the name for the Save File Name
    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Kothorix Bar"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Kothorix Bar"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Kothorix Bar"

    else:
        $ save_name = "Chapter 1 - Kothorix Bar"

    #if player knows Zhong, if not Wr is defined as "Waiter"
    if persistent.playedzhong == True:
        define Wr = Character("Zhong", color="#7e9147", image="zhong")

    #Scene Begin
    scene bare with fade
    $ renpy.pause (1.4)

    show kothorix normal dk with dissolve
    Kx "I like this place."

    #actual scene
    c "What would you like to order?"
    Kx "I'm not sure right now."
    c "Our day may have had a rocky start, but let's try to enjoy ourselves."
    Kx "What do you suggest we do?"

    if persistent.playedzhong == True:
        c "Hey, Zhong."
    else:
        c "Hey, waiter."

    show kothorix normal crossed distance flip dk at right with ease
    show waiter flip at left with easeinleft

    Wr "Hello, gentlemen. What can I get you two?"
    c "The menu, please."

    if nodrinks == False:
        Wr "Which menu would you like? You should remember the drinks menu... then again, you may not."
        c "Both. I guess I don't remember all of them, after all."

    else:
        Wr "Food or drinks?"
        c "Both, please."

    if persistent.playedzhong == True:
        m "With a quick flick of the wrist, Zhong handed us three menus: two food, one drink. A nervous look appeared on Kothorix's face."

    else:
        m "With a quick flick of the wrist, the waiter handed us three menus: two food, one drink. A nervous look appeared on Kothorix's face."

    Wr "If you need anything, signal me over."
    Kx "Before you go, can you put on my song?"
    Wr "Sure thing."

    show waiter 
    hide waiter with easeoutleft
    show kothorix normal crossed distance flip dk at center with ease
    show kothorix normal crossed dk with dissolvequick

    #Goodbye moonmen
    stop music fadeout 1.0
    play music moonmen fadein 1.0  
    $ renpy.pause(2.5)

    Kx unamused point_distance dk "Not that one! {w=2.9}{nw}"

    stop music fadeout 1.0
    play music alps fadein 1.0
    $ renpy.pause(1.5)

    show kothorix normal crossed with dissolve
    c "Kothorix! Are you OK? You look awfully nervous."
    Kx displeased dk "I wish you'd have told me beforehand that we were going to get food! I didn't bring that much money with me."
    c "Did you forget that I'm an ambassador?"
    Kx "No, but what does that have to do with anything?"
    c "It means that we don't have to pay a thing."
    Kx ramble face dk "So we are eating for free?"
    c "Yup."
    Kx normal crossed dk "In that case, we can order the good stuff."
    c "Oh yeah, we can. Let's see what this place has to offer."

    play sound bookopen
    $ renpy.pause(0.8)

    m "The menu contained a wide variety of meat-centric dishes, including juicy Auroch steaks and thick Mouflon ribs. A few meat-free options were also available."
    c "What do you want to order, Kothorix?"
    Kx thinking dk "Hmmm, I think I know what I want. I'm ready to order. How about you?"
    menu: 
        "Yeah, I want some meat.":
            Kx normal crossed dk "I feel like that everyday."

        "Veggies sound nice.":
            $ gotMeat = False
            Kx normal crossed dk "Your choice."

    play sound bookclose
    $ renpy.pause(0.8)

    if persistent.playedzhong == True:
        c "Hey Zhong, we're ready to order."

    else:
        c "Hey waiter, we're ready to order."

    show kothorix normal crossed distance flip dk at right with ease
    show waiter flip at left with easeinleft

    Wr "What can I get you, [player_name]?"

    if gotMeat == True:
        c "Can I get the Mouflon ribs in BBQ sauce?" #My fav food from the Chinese is spare ribs in BBQ sauce.

    else:
        c "I'd like the meat-free Chilli con carne with a side of Falafel." #And I like Falafel, I hope chick peas exist in the dragon world

    Wr "Sure thing. What can I get you, Kothorix?"
    Kx ramble flip dk "Get me an angus steak, cooked medium rare! With a glass of good champagne to go along with it."
    Wr "No problem."

    show waiter 
    hide waiter with easeoutleft
    show kothorix normal crossed distance flip dk at center with ease
    show kothorix normal crossed dk with dissolvequick

    if koth_arcade == True:
        #arcade video games
        c "The arcade was fun. I haven't had a chance to play a game in a while."
        Kx normal crossed dk "Yeah, it is nice to get a game in at the arcade."
        Kx thinking dk "You said your world doesn't have arcades anymore. Why is that?"
        c "The arcade machines used too much power. Keeping people alive was seen as more important than entertaining a handful of civilians."
        Kx "Too much power? The human world must not have that many sources of electricity."
        c "No, we don't. We depended on our non-renewable sources for upkeep. Once they began run out, we ran into problems."
        c "By the time we humans got around to renewable sources of power, we had already run out of the non-renewable resources needed to get us started."
        Kx ramble face dk "So the generators you're here for are very important to you?"
        c "Yeah, they are."
        Kx displeased dk "Can you, uh, talk about this in public?"
        c "Not really, no."
        Kx "Then why are you talking about it?"
        c "I don't really care anymore." 
        Kx thinking dk "I don't think I should be asking, but I'm too curious."
        Kx "I've heard that the portal uses a whole lot of power. Given that the humans don't have much, how do they power it?"
        
        menu:
            "Answer Him.":
                c "Actually, they never told me."
                Kx ramble face dk "So, you don't know?"
                c "That's not what I said."
                c "I only said that they didn't tell me. That doesn't mean that I can't figure it out on my own."
                Kx thinking dk "Then where does the power come from?"
                c "I've already told you the answer to that. Haven't you realised it yet?"
                Kx somber face dk "No."
                c "I told you that the hospital has power. It's also the only building with enough power for the portal."
                Kx wtf dk "They didn't... They couldn't..."
                c "Just my guess."
                Kx wtf dk "I hope you're wrong."
                c "I hope so, too."

            "Avoid Question.":
                c "You really shouldn't be asking."
                Kx somber face dk "Sorry."

        Kx normal crossed dk "So, what were you saying about your games?"

    else:
        if remy1unplayed == False:
            #Remy video games
            c "Actually, I regret not going to the arcade."
            Kx ramble face dk "Why's that?"
            c "It's been a while since I've played a game, and even longer since I was at an arcade. The last time I played a game was with Remy, in his bedroom."
            c "Had quite the explosive finish, too. The computer was wrecked."
            Kx normal dk "Leave it to the humans to break everything."
            c "Hey, we ain't that bad."
            Kx "Well, you did manage to expose my \"getaway\" town."
            c "Yeah, but if Reza and I hadn't come here, we wouldn't have been having so much fun."
            Kx normal crossed dk "I suppose you've got a point there."
            Kx normal crossed dk "So, what were you saying about your games?"
            
        else:
            #no video games
            c "Actually, I regret not going to the arcade."
            Kx ramble face dk "Why's that?"
            c "It's been a very long time since I've played one. Didn't even get the chance to try one here."
            Kx "Oh, so you have games on Earth?"
            c "Yeah, we do."
            Kx normal crossed dk "Well, it's a shame we didn't go then. Unfortunately, the place is closed now."
            Kx thinking dk "But, I have to ask. What are they like in your world?"
            c "That's hard to answer, considering that I don't know what your games are like."
            Kx normal crossed dk "Ok, how about you tell me about the last game you played?"
            c "Sure. The last game I played had a very different combat system from the norm."
            c "Rather than purely beating up the person you're fighting you can try to reason with them instead."
            c "Choosing the reasonable route usually led to the better ending."
            Kx ramble face dk "Sounds interesting. What do you have to play games on?"
            c "First off, it's \"had.\" I don't have anyway to play games with back on Earth."
            Kx thinking dk "Why's that?"
            c "I'd rather not get into that topic."
            Kx normal crossed dk "Well, alright. What were you saying about your games again?"

    c "Oh yeah! What do you have to play games on?"
    Kx ramble face dk "Well, nowadays we have computers, if you can afford one. There's also the arcade."
    c "Saying \"nowadays\" makes it sound like times have changed." 
    #The last game console they had was the Atari 2600 equivalent
    Kx "Yes, they have. Home game systems were very popular for a while. They were simple machines. You plugged them into your TV and put the game into the system." 
    c "Oh yes, we used to have those. Not anymore, though."
    Kx somber face dk "I don't think anyone here is going to make one for a while either." 
    c "Did something happen?"
    Kx ramble face dk "Yeah. There were too many machines on the market. No one knew which system would get the games, some worked out for several years. Others... not so much." 
    Kx thinking dk "I think the term for it is \"consumer burn.\" No one knew what to buy, so no one bought anything."
    Kx normal crossed dk "Now, it's just computers and arcades."
    c "Huh. This sounds familiar."
    c "Regardless, do you play games at home?"
    Kx ramble face dk "Yeah, I do. The computer is decent enough to run most games just fine."
    c "Playing anything good at the moment?"
    Kx "Funny you say that. There's a new game on the market called \"Demons with Fleshy Limbs.\""
    Kx normal crossed dk "Basically, it's a human dating sim. There's a lot more to it, though, so the only spoiler I'll give is that it features time travel."

    #Zhong returns with food, nice tasty food. 
    show kothorix normal crossed distance flip dk at right with ease
    show waiter flip at left with easeinleft

    if gotMeat == True:
        Wr "Here's your Mouflon ribs in BBQ sauce, sir."
        m "The ribs are passed down on a wide, flat bowl. A smaller bowl, containing only water and a slice of lemon, is given as well."

    else:
        Wr "Here's your meat-free Chilli con carne and Falafel, sir."
        m "The Chilli con carne, embedded in a bed of rice, is passed down. With it came a glass of water and Falafel."

    Wr "Kothorix, here's your steak."

    if persistent.playedzhong == True:
        m "The steak, twice the size of my face, was laid down in front of Kothorix. Alongside it, an empty glass."
        play sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound champagne
        m "Pulling out a bottle of champagne, Zhong filled the glass about two-thirds of the way up."

    else:
        m "The steak, twice the size of my face, was laid down in front of Kothorix. Alongside it, an empty glass."
        play sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound "fx/silence.ogg"
        queue sound champagne
        m "Pulling out a bottle of champagne, the waiter filled the glass about two-thirds of the way up."

    Wr "Enjoy your food."

    show waiter 
    hide waiter with easeoutleft
    show kothorix normal crossed distance flip dk at center with ease
    show kothorix normal crossed dk with dissolvequick

    m "Suddenly, Kothorix held up a glass."
    Kx "Cheers!"
    if gotMeat == True:
        #player have no glass
        m "It took a moment for Kothorix to notice he was the only one with a glass."
        Kx "Um, do you need a glass?"
        c "Don't worry, the bowl should do."
        play sound glass_bowl
        $ renpy.pause(0.5)
        m "I take a drink from my bowl of water."

        if persistent.playedzhong == True:
            m "As if on queue, Zhong looked over in horror."

        else:
            m "As if on queue, the waiter looked over in horror."

        Wr "Sir, that was for your hands! You aren't meant to drink from it."

        if persistent.playedzhong == True:
            m "Looking over at Zhong, I raise my bowl to him."

        else:
            m "Looking over at the waiter, I raise my bowl to him."

        c "I know."
        m "And I drank again."

    else:
        #player has a glass
        play sound glass_glass
        $ renpy.pause(0.8)
        c "Cheers, Kothorix."

    play sound "<loop 10 >fx/eating.wav"
    m "With rapturous attitude, we devour our meals."
    m "Turns out that dragons can eat large chunks of meat. Thankfully, humans weren't on the menu."
    m "As I watched Kothorox rip into his meat, I wondered just how injured Reza was after he was bitten."
    stop sound fadeout 1.0
    $ renpy.pause(0.6)

    Kx "Thank you for the meal, [player_name]. I haven't had a good meal in a while."
    c "Personally, I think it's nice to get out and enjoy ourselves."
    
    c "So... do you fancy anyone at the moment?"
    Kx thinking dk "What do you mean by \"fancy?\""
    c "It's a way of saying \"Are you carrying the torch for anyone.\""
    Kx "I don't understand."
    c "Is there anyone around you see as fit?"
    Kx disgusted dk "Oh, just speak English already!"
    c "Is there a girl in your life?"
    Kx ramble face dk "Oh! I understand now."

    if knowAnnaDate == True:
        Kx "Well, there was this date with Anna. Remember her from the cafe?."
        c "I really don't think beans on toast count as a date."
        Kx unamused point "Semantics. A date's a date."
    else:
        Kx "Well, there was this date with Anna once."
        c "I noticed you caller her \"your bae.\""
        Kx normal crossed dk "Yeah, that girl is mad for me, but it wouldn't have worked out between us. Her work prevented the two of us from meeting up."
        ###delete

    Kx normal crossed dk "I had one before Anna as well. I'll have to admit: I was enthralled by her."
    c "What happened?"
    Kx ramble face dk "Actually, it's a little embarrassing."
    Kx "We had a picnic date planned for Tatsu park."
    Kx "Everything was going great until the walk home."
    Kx "We had started walking along an unlit road when some guy jumped out of the bushes and started screaming at us."
    Kx "She took off running, and boy, was she fast."
    Kx "I tried to go after her, but she could run faster than me. She got away."
    Kx "When I met her the next day, she wanted nothing to do with me."
    Kx "Our relationship was over as soon as it started."
    Kx normal crossed dk "I don't really hold it against the guy, whoever it was. In retrospect, it's a pretty funny story. Good for conversation."
    c "It's an unique story alright."

    Kx thinking dk "Didn't you say you wanted a drink?"
    c "I ended up deciding against it."

    if brycedead == False:
        if brycestatus == "bad":
            show kothorix at left with ease
            show bryce normal at right with easeinright

            Br "Alcohol, the one thing I really need to deal with my favourite human."
            c "You're telling me. What are you doing here?"
            show kothorix displeased dk at left with dissolve
            Br laugh "Oh, you know, the usual. It's still my job to protect you, and I haven't seen you with this guy before."
            Br normal "So, when'd you two meet?"

            if toPortal == True:
                Kx ramble dk "Well, we met the other day and [player_name] offered to give me a tour of the portal."
                Kx "What a magnificent device."
                Br stern "Wait, that was you two?! [player_name], you know no one is allowed up there without permission. Why did you take him up there?"
                show kothorix somber face dk at left with dissolve
                c "What harm can he do?"
                Br stern "He could have been a spy, a reporter, or someone with a really large nose. Word gets out about the location of the portal, and this town is flooded with unwelcome cameras."
                show kothorix wtf dk at right with dissolve
                c "Bryce, seriously? A magic door opens up and two alien bodies appear, and you expect there to be no attention?"
                c "Once here, all they'd have to do is look up at a hill and see it. I think letting a few dragons in to see it might be doing you a favor."
                Br angry "[player_name], don't you dare..."
                Kx disgusted dk "Hey, it was a harmless action. Don't work yourself up."
                Br stern "We'll settle this elsewhere."

                show bryce stern flip at right
                hide bryce with easeoutright
                show kothorix displeased dk at center with ease
                $ renpy.pause(0.8)

                c "Thanks for that."
                Kx "Don't mention it."
                Kx normal crossed dk "But, this is our night, so let's enjoy ourselves. Bryce-free."
                c "It's getting late. If you don't mind, I'd like to go home."
                Kx "Yeah, I suppose it is late. Here, let me walk you home."

            else:
                c "I found him wandering around when I was taking the eggs to the hatchery."
                Kx displeased dk "I wasn't \"wandering about.\" I was merely enjoying a casual stroll when I saw you."
                Br stern "I see."
                Kx ramble dk "Yeah, [player_name] was on his way somewhere and we bumped into each other. We talked, and I ended up giving him my card."
                Br laugh "I hear that you like to do that."
                show kothorix displeased dk at right with dissolve
                $ renpy.pause(1.2)
                Br normal "Please continue."
                Kx ramble dk "After that, [player_name] offered to meet up. So now we're here."
                Br normal "Sounds like you two are hitting it off then. I have to run now; the bar's not going to empty itself out."
                m "He laughs, then leaves."
                
                show bryce normal flip at right
                hide bryce with easeoutright
                
                Kx normal crossed dk "Enjoy your evening."

                show kothorix normal crossed dk at center with ease

                $ renpy.pause(0.8)

                c "Speaking of the evening, it's getting late."
                Kx "I know it is. Let me walk you home."
                c "Thank you."

        else:
            show kothorix at left with ease
            show bryce laugh at right with easeinright

            Br "Is my favourite human talking about alcohol?"
            c "Ha. I'm just not up for it right now."
            Br laugh "More for me then."

            if brycescenesfinished >= 3:
                if brycestatus == "good":
                    Br smirk "Oh, am I interrupting a date?"
                    Br flirty "And here I was thinking that I had a chance to woo the human."
                    c "I'm not going to say that you don't." 
                    Br "Great to hear it."
                else:
                    pass
            else:
                pass

            Br normal "So, what are you two doing here?"

            if toPortal == True:
                Kx ramble dk "Well, we met the other day and [player_name] offered to give me a tour of the portal."
                Kx "What a magnificent device."
                Br stern "[player_name], why'd you take him up there? You know you need permission to get up there."
                m "I was going to say something, but Kothorix cut me off."
                Kx somber face dk "I'm sorry Bryce, don't give [player_name] too much trouble. I... I nagged him until he brought me up there."
                Br "Well, I'll let it slide for now. Just make sure it doesn't happen again, alright?"
                c "Understood."
                Br "I'll leave y'all now. Have a good rest of the night."

                show bryce normal flip at right
                hide bryce with easeoutright
                show kothorix normal crossed dk at center with ease
                $ renpy.pause(0.8)

                Kx ramble face dk "So, do you want to head home?"
                c "Yeah, I do. It's getting late."
                Kx normal crossed dk "Let me walk you home."

            else:
               #player is good standing with Bryce and didn't take Koth to the portal
                c "We met the day I took the egg's to the hatchery."
                Kx ramble dk "Yeah you know that square where Kevin hands out his flyers for his college? That's where we met."
                c "Kothorix gave me his \"card,\" which had his number on the back. I gave him a call today and we decided to met up."

                if brycescenesfinished >= 3:
                    if brycestatus == "good":
                        Br laugh "I would say that ye are cute couple but..."
                        Br flirty "I might have my own intentions for [player_name]."
                        c "Well, you might want to hurry up then."
                        Br "Noted."
                        c "Don't make me regret telling you that."
                    else:
                        pass
                else:
                    pass

                Br normal "I know Kothorix; I know most people in this town. He's harmless, really."
                Kx normal crossed dk "Thanks for the positive review."
                Kx "Now if you don't mind, [player_name] and I have out own night to spend together."
                Br flirty "Oh, I see, I won't keep you then."
                c "It's not how it sounds."

                if brycescenesfinished >= 3:
                    if brycestatus == "good":
                        Br "Saving yourself for a hunk? You should know who to call then."
                        Br "Enjoy your evening"
                    else:
                        Br "{i}Oh of course not. {\i}"
                else:
                    Br "{i}Oh of course not. {\i}"

                show bryce normal flip at right
                hide bryce with easeoutright
                show kothorix normal crossed dk at center with ease
                $ renpy.pause(0.8)

                c "That was fun."
                Kx "It's getting a bit late, [player_name]. I think we should head back for the evening."
                c "Oh so this is a date now. In that case will you be a gent and walk me home?"
                Kx "Of course I will."
    else:
        #bryce is dead 
        c "I'd like to head on home, who knows what sort of troubles tomorrow has in store for me. I need my sleep."
        Kx "You've made this a very fun day for me. The least I can do is walk you home."
        c "I'd like that."

    scene black with fade
    $ renpy.pause (1.0)
    nvl clear
    window show
    play music terrace fadein 1.0

    n "Considering that it was late and with Reza at large; there wasn't many dragons outside."
    n "With no-one to get attention from, Kothorix was left with just me."
    n "He seems both disappointed and happy about it."
    n "Seeing a character out of his element is always an interesting sight. It's only then do you see their real character."

    window hide
    $ renpy.pause (1.0)
    scene np5e with fade
    $ renpy.pause (1.4)

    show kothorix normal crossed dk with dissolve

    Kx "Hey [player_name] thank you so much for this time together. I really needed the company. You should try seeing a few others as well; I know they'll like it."
    
    menu:
        "Inquire.":
            c "Is something wrong? Do you need help?"
            Kx "You've helped me enough. I really needed some feel good time." 
            c "I'm glad I could provide that, but you seem to have something else on your mind."
            Kx somber face dk "I don't want to ruin the night for you."
            c "Honestly I'll feel worse if you left it at that."
            Kx "Well..."
            Kx sad down dk "Recently, I betrayed a friend's trust."
            Kx "I apologized to them, I just still feel terrible for it. They said it was alright, but that doesn't make it right."
            Kx "Outside of a few provoked responses, they are not talking to me."
            Kx "Even after I tried to get him to open up again, he'd always shrug off the conversation in a very business-like manner."
            Kx ramble face dk "I know you may think that me saying sorry and them saying its OK should do me and to just get over yourself."
            Kx "A persons trust is very special thing and it hurts a lot to have it betrayed. I know how it feels all to well."
            Kx "To me, betrayal of one's trust is one of the worst things I could do."
            Kx somber face dk"I have many wounds, and some of them are physical ones. However, those aren't the ones that hold me down. It's the weights in my heart that I have to carry with me every day."
            Kx eyes closed dk "Several years ago, a friend lied to me, and it ended in a physical injury that still hurts to this day."
            Kx sad down dk "After that, I made a promise to myself: I'd never hurt others like that."
            Kx "I'm such a hypocrite."
            Kx "I want to earn back that trust by making up for what I did. I don't deserve to have it handed back to me on a silver platter."
            Kx sad down dk "We had only recently become friends and we are trying to help others."
            Kx somber face dk "I... I want to help, but how can I help anyone if I can't even help my own friends?"
            c "That's an awfully unpleasant situation."
            Kx "Yeah, it is. Do you have any advice for dealing with this sort of thing?"
            c "My only recommendation would be to not pressure them with your apology."
            c "It may be tempting, but for now, just accept their OK and make up for how you hurt them by remaining their friend."
            c "Someday, they'll need you to be there for them, and you can be there for them."
            Kx sad down dk "..."
            m "A single tear flowed down Kothorix's face."
            c "It's good that you're still upset."
            Kx somber face dk "What do you mean?"
            c "The guilt shows that you're a good person at heart, and it'll prevent you from making that mistake again."
            Kx normal crossed dk "Thank you, [player_name]. I needed to hear that."

        "Ignore topic.":
            c "And thank you too, Kothorix. I was in need of a good day as well."

    Kx "Well I suppose it's that time again..."
    Kx hey you dk "I'm Kothorix, and you have a rawrnderful day."

    hide kothorix with dissolve

    #Fade out
    scene black with fade
    $ renpy.pause(1.0)

    nvl clear
    window show
    n "I suppose now I can say that I had a date with the \"Scaly with Angel Wings.\""
    n "He was an interesting sort. Can't help but feel there's more to him than he's let on, though."
    n "I don't think I'll get the chance to hang out with him again."

    if persistent.trueending:
        n "Well, not this time anyway."
        n "Next time, things will be different."

    window hide

    $ renpy.pause(0.5)
    stop music fadeout 2.0
    $ renpy.pause(1.0)

    #Restore previous scene
    play music "mx/elegant.ogg" fadein 1.0                      #Gives the new scene music
    scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed    #Gives the scene a background

    return