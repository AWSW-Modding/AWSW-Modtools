label lbd_demo_bad_mood_ending():
    stop music
    play sound "fx/system.wav"
    $ renpy.pause(0.1)

    Dm "Admittedly the ending you are going to get is a bit harsh."
    Dm "More work is needed to get it to flow a little better but it was left as is just to give you some idea just how horrible you can be to Lorem in this mod."
    Dm "And is this the worst possible ending?"
    Dm "Don't count on it."
    Dm "Enjoy."

    jump lbd_bad_mood_ending

label lbd_bad_mood_ending():
    $ lbd_gotmilk = lbd_gotbread = False

    scene black with fade
    stop music fadeout 1.5
    $ renpy.pause(0.5)

    play sound "fx/steps/clean2.wav"

    $ renpy.pause(0.5)

    play music fort_severn fadein 1.5

    scene kimberland_trainstation with fade

    m "We enter the train station at Kimberland and decide to wait until the next train."
    m "Lorem stands in a queue to ask at an info kiosk when the next train back to town is due."
    m "I just sit nearby and wait for him."
    m "After a few minutes Lorem comes back."

    show lorem sad with dissolve

    Lo "The train back to town will be along in about 10 minutes. If you don't mind, I'm off to the bathroom."
    c "I don't care Lorem."
    Lo "Of course not."

    hide lorem sad with easeoutleft

    m "He wonders off in a random direction. {i}sigh{/i} What to do?"

    nvl clear
    window show

    n "At the entrance I see a mother walk in with 3 kids. The smallest and presumably youngest one is wearing a worn out old red hat, the kinda that look like a baseball hat."
    n "I can only guess it's used as a way to easily spot him in a crowd or something."
    n "The other two older siblings begin screaming (well screeching more like) while running around their mother. If I had to guess the smallest one is 6, the oldest is 12 and the middle child is about 9."
    n "Soon their attention turns to the smallest child."

    nvl clear

    n "The oldest child takes the hat from the youngest. He holds it out of reach of the small child, the small child begins to jump up and down to try and grab the hat."
    n "I notice the small child begin to tear up and his siblings laugh at him."
    n "The mother is clearly distressed and distracted with trying to sort out tickets for everyone."
    n "The small child stops jumping and just sits on the floor sobbing. He shortly shouts out \"It's the only thing Dad left me, you two got all the cool stuff!\""
    n "Only then did the mother take notice and she actually slapped the oldest child on the back of his head while snatching the hat off of him."
    n "She places the hat gingerly on the head of the small child before going back to trying to sort out tickets."
    n "Clearly shaking, the small child stands up and intentively inspects the hat for damage."

    nvl clear

    n "Devastation suddenly washes over the child's face as he exclaims \"It's ripped!\""
    n "The middle and youngest child are grabbed and pulled in a direction by the mother who had just finished getting their tickets prepared."
    n "While passing a bin, the hat gets tossed in."

    nvl clear

    n "A little blue figure runs up to the bin and pulls out the hat, following the family the figure stops the mother by handing her the hat."
    n "After a short conversation the blue figure sits down about as far away from me as possible."

    window hide
    nvl clear

    menu:
        "[[Go to Lorem.]":
            $ renpy.pause(0.5)

            play sound "fx/steps/clean2.wav"
            $ renpy.pause(1.0)
            stop sound fadeout 0.2
            $ renpy.pause(0.4)

            show lorem sad with dissolve
            $ renpy.pause(0.5)

            Lo "What do you want now?"
            c "I just thought I'd come over."
            Lo "Why? So you can torment me further?"
            menu:
                "Yes.":
                    $ renpy.pause(0.5)

                    Lo "Well don't bother because I'm done talking to you."
                    c "Suit yourself."
                    m "Lorem sits still and quiet for a while before the train pulls into the platform."
                    m "He gets up and walks over the train without a word."
                    c "OK, be that way."

                "No.":
                    $ renpy.pause(0.5)

                    Lo "Oh I don't believe you one bit!"
                    c "I think what you done for that kid was very kind."
                    Lo "You saw that?"
                    c "Yes I did. He looked very upset."
                    Lo "What do you think coming over here and telling me that I done something nice is going to accomplish?"
                    Lo "Do you think everything you done is just going to be magically forgiven?"
                    Lo "Well you're wrong."
                    Lo "{i}sigh{/i} How stupid am I to think you'd be any different from the rest? {w=0.5}Don't answer that!"
                    Lo "The train is here. Let's just go."

        "[[Stay where you are.]":
            $ renpy.pause(0.5)

            m "I guess I should leave him alone. He wouldn't have sat over there if he wanted to talk to me."
            m "Not much to do but sit and wait."
            m "I kind of regret not going over and bothering him, at least it would give me something to do."
            m "Here comes the train. Time to go home and back to bed."

    scene black with fade
    $ renpy.pause(1.0)

    scene trainstation-dusk with fade
    $ renpy.pause(0.2)
    show lorem sad
    show bryce stern b flip at Position(xpos = 0.15)
    show sebastian disapproval b at Position(xpos = 0.85)
    with dissolve

    $ renpy.pause(0.8)

    Br "So you've come back from your little trip."
    c "Yes we're back from.. What did you say it was called?"
    Lo "..."
    c "Lorem?"
    show bryce brow b flip with dissolve
    Lo "..."
    Br stern b flip "Lorem, where were you two?"
    Lo "We were in Kimberland."
    Br brow b flip "Is that so."
    Sb "Oh, isn't the medieval festival on this time of year?"
    Br "Yes it is."
    Lo "Um.. Can I please go home now?"
    Br "Yes Lorem, you can leave. I'll be around later to check on you."
    Lo "Thanks Bryce."

    show lorem sad flip with dissolve
    hide lorem with easeoutright

    show bryce stern b flip at Position(xpos = 0.20)
    show sebastian disapproval b at Position(xpos = 0.8)
    with ease

    c "Well I better be going too I suppose."
    Br brow b flip "And what makes you think you get off so easy?"

    menu:
        "I'm the Ambassador.":
            $ renpy.pause(0.5)

            Br stern b flip "That you are but that doesn't mean we can't give out to you."

        "Avoid making a scene.":
            $ renpy.pause(0.5)

            c "Well I highly doubt you'd be willing to make a scene in public."
            Br "You believe that?"
            c "Why yes I do."

        "You're nice.":
            $ renpy.pause(0.5)

            Br "I'm nice? That is not something I expected you to say."
            Br stern b flip "Well yes, I'm nice to those who are respectful. Judging by Lorem's demeanour, you are far from that."

    Br stern b flip "Let's get you home. We still have to protect you even if you make it your mission not to be protected."

    menu:
        "[[Be flirty.]":
            $ renpy.pause(0.5)

            c "Is my escort going to walk me home?"
            play sound "fx/throat_clear.ogg"
            Sb "Will you please be serious!"
            Br stern b flip "So here's what's going to happen. Sebastian will walk you home, I'll check on Lorem."
            Br "Once I'm done with Lorem, I visit you and we'll have a chat."

        "[[Be snarky.]":
            $ renpy.pause(0.5)

            c "I was thinking of going to the shop actually?"
            Br brow b flip "Oh really, what were you going to get?"

            #if player drank the milk in the fridge
            if (persistent.c1liquid) or (renpy.python.store_dicts["store"].get("undrunk", True) == False):
                $ lbd_gotmilk = True

                c "Well I was thinking of getting some milk, I  drank it all the first night I was here."
                Br stern b flip "I don't think you got milk."
                c "Then what was the container in my fridge full of?"
                Br "Was it white liquid?"
                c "Yeah and it tasted salty."
                m "Both Bryce and Sebastian struggle to hold back laughter."
                Br "I wouldn't worry about it if I were you, but I guess you could call it a kind of milk."
                Br "So here's what's going to happen. Sebastian will walk you home, I'll check on Lorem."
                Br "Once I'm done with Lorem, I visit you and we'll have a chat."

            else:
                $ lbd_gotbread = True

                c "To be entirely honest, I want to try your bread."
                Br brow b flip "Our bread?"
                c "Yeah, it's been a while since I had a sandwich or something. So I'd like to get some bread."
                Br stern b flip "Well fine. Here's how this is going to work."
                Br "Sebastian is going to walk you home, I'm going to go check on Lorem."
                Br "Once I'm done with Lorem I'll visit you and we'll have a chat."

    c "Fine."

    #    play soundloop "fx/steps/steps.ogg" fadein 0.5
    #    scene town_road_b at Pan((0, 0), (0, 360), 5.0) with fade

    #    $ renpy.pause(1.0)

    #    nvl clear
    #    window show

    #    n "Walking along the road beside a very quiet Sebastian, it "

    #    stop soundloop fadeout 1.0

    #    window hide
    #    nvl clear

    #    Db "Test pause."
    play sound "fx/steps/rough_gravel.wav" fadein 0.5
    scene black with Fade(0.8, 1.0, 0.8)
    #$ renpy.pause (2.0)

    play sound "fx/door/handle.wav"
    $ renpy.pause(0.5)
    play sound "fx/door/creaky.wav"
    $ renpy.pause(2.5)
    scene black with dissolve
    $ renpy.pause(1.0)
    #stop music fadeout 1.0
    play sound "fx/switch.wav"
    $ renpy.pause(0.6)

    scene o2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow

    m "The door's hinges creak open and with the flick of a switch, the apartment was flooded with light."

    show sebastian disapproval b at Position(xpos = 0.5) with dissolve

    $ renpy.pause(0.8)

    menu:
        "You didn't have to rat out on me.":
            $ renpy.pause(0.5)

            Sb "Actually yes I did. Part of my job is keeping tabs on you and reporting your activity."

        "Thanks Sebastian.":
            $ renpy.pause(0.5)

            Sb "You're welcome."

    Sb "I'll give you a quick warning. When I told Bryce that you left he wasn't very happy."
    Sb "So I suspect his talk with you will be a very serious one."
    Sb normal b "Good luck with that but it's time for me to go."
    Sb "Goodnight [player_name]."

    show sebastian normal b flip with dissolve
    hide sebastian with easeoutright

    m "I'd like to go to bed right about now."

    $ renpy.pause(0.8)
    play sound "fx/knocking1.ogg"

    $ renpy.pause(1.0)
    m "I assume that's Bryce."

    menu:
        "[[Answer the door]":
            pass

        "[Ignore Bryce and go to bed]":
            play sound "fx/switch.wav"
            scene o3 at Pan ((0, 250), (128, 250), 0.0)

            play sound "fx/knocking2.ogg"
            queue sound "fx/knocking1.ogg"
            queue sound "fx/knocking2.ogg"
            queue sound "fx/knocking1.ogg"

            c "Goodnight Bryce."

            stop sound fadeout 1.5
            scene black with Fade (1.2, 2.0, 0.0)

            if lbd_demo_mode:
                jump lbd_demo_ending

            return


    play sound "fx/door/handle.wav"
    $ renpy.pause(0.5)

    show bryce stern b with easeinright
    Br "I bumped into Lorem on my way over to him."
    Br "He told me about what happened and about your big day out."
    c "What about it?"
    #m "I notice that Bryce is noticibly irrited."

    Br angry b "Why DARE you leave the town?"
    Br "You know we have to protect you. We can't have you waltzing around."
    Br "Do you have no regard for your own damn safety?"

    c "Right, of course I care about my safety."
    Br stern b "Then can we come to an understanding that you won't wander around in danger again?"
    c "Fine."
    Br "Glad to hear it."


    if not lbd_demo_mode:
        #--------------------Dev debug--------------------
        if lbd_dev_debug:
            menu:
                Db "What's brycestatus?"
                "neutral":
                    $ brycestatus = "neutral"

                "bad":
                    $ brycestatus = "bad"

                "good":
                    $ brycestatus = "good"


        # Bryce knows how badly you treated Lorem and thinks less of you for it.
        if brycestatus == "bad":

            Br angry b flip "How DARE you leave!"
            Br "You know we have to protect you, there's a REASON for that!"

        elif brycestatus == "neutral":
            $ brycestatus = "bad"

        elif brycestatus == "good":
            $ brycestatus = "neutral"

    Br "And about Lorem."
    c "Yes?"
    Br "I suggest you leave him alone from now on."
    c "Oh really?"
    Br "Yes, you done enough to him and leave him be."

    if lbd_gotmilk:
        Br stern b "Before I forget, I got your milk."
        c "Oh right, thanks."
        Br "Here you go. Nice and salty, just the way you like it."

    elif lbd_gotbread:
        Br stern b "Before I forget, I got your bread."
        c "Oh right, thanks."
        Br "Hmmm, here you go."

    Br "Now good night."

    hide bryce with easeoutright
    play sound "fx/door/handle.wav"

    c "Well, I guess it's time for bed."
    stop music fadeout 1.2
    scene black with fade

    if lbd_demo_mode:
        jump lbd_demo_ending

    return

label lbd_good_mood_ending():
    $ lbd_gotmilk = lbd_gotbread = False

    scene black with fade
    stop music fadeout 1.5
    $ renpy.pause(0.5)

    play sound "fx/steps/clean2.wav"

    $ renpy.pause(0.5)

    play music lbd_case1 fadein 1.5

    scene kimberland_trainstation with fade

    m "We enter the train station at Kimberland and decide to wait until the next train."
    m "Lorem stands in a queue to ask at an info kiosk when the next train back to town is due."
    m "I just sit nearby and wait for him."
    m "After a few minutes Lorem comes back."

    show lorem normal with dissolve

    Lo "The train back to town will be along in about 10 minutes. If you don't mind, I'm off to the bathroom."
    c "Work away buddy, stay safe."
    Lo "I won't be long."

    hide lorem with easeoutleft

    m "He wonders off in a random direction. {i}sigh{/i} What to do?"

    nvl clear
    window show

    n "At the entrance I see a mother walk in with 3 kids. The smallest and presumably youngest one is wearing a worn out old red hat, the kinda that look like a baseball hat."
    n "I can only guess it's used as a way to easily spot him in a crowd or something."
    n "The other two older siblings stroll in casually. If I had to guess the smallest one is 6, the oldest is 12 and the middle child is about 9."
    n "Their attention turns to the smallest child who had just fallen down."

    nvl clear

    n "The oldest child picks up the now crying babe while the middle child picks up the little red hat and runs away."
    n "The mother is clearly distressed and distracted with trying to sort out tickets for everyone."
    n "The small child begins screaming \"Gib back my hat!\""
    n "Only then did the mother take notice, she called back the middle child wand snatches the hat off of him."
    n "She places the hat gingerly on the head of the small child before going back to trying to sort out tickets."
    n "The youngest child intentively inspects the hat for damage when it is blown out of his hand by a gust of wind."

    nvl clear

    n "A little blue figure swoops in to grab the hat in mid-air. The figure approaches the mother and hands her the hat."
    n "After a short conversation the blue figure walks over to me."

    window hide
    nvl clear

    show lorem normal with dissolve

    Lo "I hope I didn't take too long."
    c "Glad to have you back."
    Lo "Well the train is here now, we better get going before it heads home without us."
    #note maybe add a short conversation here.
    #m "Lorem plonks himself down beside me."
    #c ""

    scene black with fade
    $ renpy.pause(1.0)

    scene trainstation-dusk with fade
    $ renpy.pause(0.2)
    show lorem normal
    show bryce stern b flip at Position(xpos = 0.15)
    show sebastian disapproval b at Position(xpos = 0.85)
    with dissolve

    $ renpy.pause(0.8)

    Br "So you've come back from your little trip."
    c "Yes we're back from.. What did you say it was called?"
    Lo "We were in Kimberland."
    Br "At least Kimberland is safe enough."
    Sb "Did you two go to the medieval festival there?"
    Lo happy "Yeah we did. It was a lot of fun."
    Br brow b flip "Is that so?"
    show lorem normal with dissolve
    Br stern b flip "You know that shouldn't have gone without an escort."
    Lo normal "I was with him."
    Br "A police escort Lorem."
    Lo sad "Oh."
    Lo "It was my idea Bryce, I didn't mean for [player_name] to get into any trouble."
    Br "Well, at least you're both back now."
    Br "Sebastian will walk you home [player_name] and I'll have a chat with Lorem about this."
    c "Alright Bryce."
    Sb "Please follow me [player_name]."

    play sound "fx/steps/rough_gravel.wav" fadein 0.5
    scene black with Fade(0.8, 1.0, 0.8)
    #$ renpy.pause (2.0)

    play sound "fx/door/handle.wav"
    $ renpy.pause(0.5)
    play sound "fx/door/creaky.wav"
    $ renpy.pause(2.5)
    scene black with dissolve
    $ renpy.pause(1.0)
    #stop music fadeout 1.0
    play sound "fx/switch.wav"
    $ renpy.pause(0.6)

    scene o2 at Pan ((0, 250), (128, 250), 3.0) with dissolveslow
    show sebastian normal b at Position(xpos = 0.50) with dissolve

    $ renpy.pause(0.5)

    c "So how much trouble am I in?"
    Sb drop b "It's hard to tell really."
    Sb disapproval b "Bryce was mad when I told you left the town."
    Sb "However, he seemed surprisingly calm when we talked at the station."
    c "I think I see what you mean."
    c "What do you think about me leaving?"
    Sb normal b "You obviously should have had an escort but between you and me, I don't see what the big deal is."
    Sb "I think a desire to explore this world is very expected from you."
    Sb "We always have to remember that this place is all new to you."
    Sb "It's a shame about Reza, otherwise someone would be available to take you to places."
    c "Yeah, it would be nice to travel around."
    c "Well thanks for walking me home Sebastian."
    Sb "Don't mention it."
    Sb "I should be going, Bryce should be along shortly."
    c "Goodnight."
    Sb "You too!"

    show sebastian normal b flip with dissolve
    hide sebastian with easeoutright

    c "Well today with Lorem was fun. I hope I get to hang out with him again."

    $ renpy.pause(0.8)
    play sound "fx/knocking1.ogg"

    $ renpy.pause(1.0)
    m "I assume that's Bryce."
    play sound "fx/door/handle.wav"
    $ renpy.pause(0.5)

    show bryce stern b with easeinright

    Br "Hello there [player_name], did you have a good day?"
    c "Yes I did."
    Br "I'm glad one of us did. I had to explain to a very pissed off Emera that you left town."
    c "Sorry Bryce."
    Br stern b "Can we come to an understanding that you're not to leave town without an escort?"
    c "Yes."
    Br normal b "Good."
    Br normal b "I should technically give out to you about what you've done."
    Br "However you went to a fairly safe town and gave Lorem a good time."
    Br "So this time I'll lenient just don't do it again please."
    c "Sure thing Bryce."
    Br "I'm sure you're exhausted, so I'll leave you be. Goodnight."
    c "Goodnight Bryce."

    show bryce normal b flip with dissolve
    hide bryce with easeoutright

    play sound "fx/door/handle.wav"

    c "Well, I guess it's time for bed."
    stop music fadeout 1.2
    scene black with fade

    if lbd_demo_mode:
        jump lbd_demo_ending

    return




label lbd_demo_ending:
    scene heartbg with fade:
        xcenter 0.5 ycenter 0.5

    $ renpy.pause(0.5)
    play sound "fx/system.wav"

    lime45 "That's the mod so far."
    lime45 "Please consider leaving feedback on it's progress and direction."
    lime45 "This is a very ambitious project and I hope you like it."
    lime45 "Thanks for playing."

    return
