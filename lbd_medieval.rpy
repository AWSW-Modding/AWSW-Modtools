label lbd_medieval_start:
    #--------------------Save File Name--------------------
    if chapter4unplayed == False:
        $ save_name = "Ch. 4 - Lorem 1 - Medieval"

    elif chapter3unplayed == False:
        $ save_name = "Ch. 3 - Lorem 1 - Medieval"

    elif chapter2unplayed == False:
        $ save_name = "Ch. 2 - Lorem 1 - Medieval"

    else:
        $ save_name = "Ch. 1 - Lorem 1 - Medieval"

    scene black
    play music medieval_day_music fadein 1.0
    $ renpy.pause (0.1)

    scene medieval_day with fade
    show lorem normal with dissolve
    $ renpy.pause (0.5)

    c "So Lorem, where are we?"
    Lo happy "This is the main attraction here at Kimberland. Oh this is so exciting!"
    c "Make sure you don't forget to tell me what's going on here in all the excitement."
    show lorem think with dissolve
    $ renpy.pause(0.8)
    Lo happy "Oh of course, I almost forgot to tell you. This is a medieval festival, it happens once a year and it's always a blast."
    c "Oh, so you've been here before?"
    Lo normal "Why yes! I normally come here every year with Ipsum. Unfortunately he's been really busy with his work, though thankfully you were willing to join me this year."
    c "Does it not get boring coming here every year?"
    Lo happy "Of course not. It's always good for a laugh and you never know who you'll met here."

    $ lbd_asked_about_town = lbd_asked_about_past = lbd_asked_about_human_festivals = False
    $ lbd_talking_loop = True

    while lbd_talking_loop:
        show lorem normal with dissolve
        $ renpy.pause(0.3)

        menu:
            "[[Ask about the town.]" if not lbd_asked_about_town:
                $ renpy.pause(0.5)
                $ lbd_asked_about_town = True

                c "So are medieval festivals exclusive to this town?"
                Lo normal "Oh of course not but not all that many places decide to actually hold a medieval festival."
                c "Any particular reason for that?"
                Lo sad "Sadly most officials think a festival celebrating the past is either backwards thinking or a way of saying \"We have nothing else to offer.\""
                Lo normal "Which just isn't true. These festivals are far from how times actually were and there's so much made up stuff that we think is fact that it's hard to tell just how acurate this actually is without a book."
                Lo normal "Beside that barely even matters. It's just fun, a reason to get outside."
                c "And how about the \"nothing else to offer\" argument?"
                Lo happy "Oh yes. I find the places that actually host these to be rather scenic. May not be the most exciting place's to live but they sure are nice to visit."
                show lorem normal with dissolve
                c "I suppose it would bring in the tourists."
                Lo normal "Exactly."


            "[[Ask about past festivals.]" if not lbd_asked_about_past:
                $ renpy.pause(0.5)
                $ lbd_asked_about_past = True

                c "You said you've been here before, anything happen that you'll never forget?"
                show lorem think with dissolve
                $ renpy.pause(0.5)

                Lo "Hmmmmm"
                Lo happy "Ah yes, they held a jousting tournament one year."
                c "Dragon jousting? How does that work?"
                Lo normal "Well back when it was preformed earth dragons would hold the jousting rod in their mouths but it was rarely used to settle arguments. Usually to settle arguments they would just push head to head against each other, the first one out of the circle was the loser."
                c "All I can imagine now is Bryce and Emera doing that."
                Lo think "You mean the jousting or the battling?"
                c "Both really, depends on their alcohol content."
                Lo normal "I don't think that's far off the truth."
                Lo normal "Anyway, it's a little different these days when it's preformed for show."
                Lo "Usually a smaller runner or flyer type would sit on top of the earth dragon wielding the jousting rod."
                Lo "That change was done for two reasons. First off to include us smaller dragons in the fun. Second, it makes more of an entertaining show."

                menu:
                    "Sounds cute.":
                        $ renpy.pause(0.5)

                        Lo think "Cute? It's not supposed to be cute. Honestly it sounds more scary than anything."
                        c "I think the image of you sitting on top of a big dragon is cute, but that's just my thoughts."
                        show lorem shy with dissolve
                        $ renpy.pause(0.3)
                        Lo "I.. uhh.. {w} mhmmm..."
                        c "You know, you're really adorable when you blush."
                        Lo "You're making it worse."
                        Lo "Let's just continue with the story."
                        $ renpy.pause(0.5)
                        show lorem normal with dissolve
                        $ renpy.pause(0.4)
                        Lo "I'm ready to continue now."
                        Lo "Unfortunately jousting isn't performed here anymore."

                    "Sounds scary.":
                        $ renpy.pause(0.5)

                        Lo normal "I'll be the first to admit that big dragons fighting with each other does sound very scary."
                        Lo "I know I wouldn't last all that long."
                        c "Well why not?"
                        Lo "Well look at me, I'm small. They would be able to just swipe me out of the way."
                        c "You're clearly not built for a one on one fight but you could do well as an infiltrator."
                        Lo think "What do you mean an infiltrator?"
                        c "Your size allows you to hide in small areas. Plus you should be able to fly up high and with your colour you would be hard to spot against the sky."
                        c "To be frank, at least I can see the big guys coming but you'll be behind me ready to strike without my knowledge."
                        Lo normal "Huh, I never thought of that before. It will come in handy at the next siege where we must vanquish our enemies stronghold."
                        c "What are you talking about?"
                        Lo relieved "I don't know, I'm just trying and failing at telling a joke."
                        c "Anyway, will the jousting be on this year?"
                        Lo normal "Sadly not."

                Lo "It only happened the one year. It was a blast all the same."
                c "Did something happen?"
                Lo "Yes and no. When the earth dragons began running the entire audience ran after them."
                c "That makes no sense to do. Why would they do that?"
                Lo think "It really did seem like a good idea at the time."
                c "Don't tell me you ran after them too."
                Lo normal "I would tell you that I didn't but I'd be lying."
                Lo "So we ran after them and when one of the riders fell off, they fell right onto the audience."
                Lo "No-one was hurt but it scared the officials enough that they never held the tournament again."
                c "I don't quite understand how that was fun."
                Lo happy "I guess you just had to be there. It was an unique experience."


            "[[Mention human medieval festivals.]" if not lbd_asked_about_human_festivals:
                $ renpy.pause(0.5)
                $ lbd_asked_about_human_festivals = True

                c "You know, long ago we used to have our own medieval festivals."
                Lo think "Really? That's a strange coincidence."
                if persistent.trueending:
                    c "I'm thinking it might be more than a coincidence."
                    Lo think "What do you mean?"
                    c "It doesn't matter."

                else:
                    c "It sure is."

                Lo normal "What are human ones like?"
                c "It's been a very long time since one was held. Not long ago someone did try to hold one as a moral boost but it was turned down because it was dubbed too depressing."
                Lo think "How exactly is something this fun; depressing?"
                c "Well the living conditions during medieval times are not exactly far off how we live now."
                Lo "I don't understand, what do you mean?"
                c "That's really a conversation for another time."
                Lo normal "Your call, I don't judge. Anyway, were you ever at a human medieval festival?"
                c "I can just about remember going to one when I was a kid. The only thing I remember is this awful smell and being afraid of a knight."
                Lo think "Do you remember why there was a smell?"
                c "There were a few animals there, cows and donkeys if I remember right."
                Lo normal "I'm not sure what a cow or donkey are but ok."
                c "Off the top of my head, a cow is a bovine but I'm not quite sure what to call a donkey."


            "[[Done.]":
                $ lbd_talking_loop = False

        # auto stop the menu appearing if player asked all the questions.
        if (lbd_asked_about_town) and (lbd_asked_about_past) and (lbd_asked_about_human_festivals):
            $ lbd_talking_loop = False

    $ renpy.pause(0.5)

    Lo normal "You know there's something kinda stupid that me and Ipsum do when we come here."
    c "What is it?"
    Lo normal "We walk around real quick and buy some random stuff to use as a costumes. Then we role-play as a character that would wear what we got."
    c "Let me guess, you want to do that with me?"
    Lo happy "Oh yes, I'd love to."
    Lo normal "But only if you're up for it of course, no pressure."

    #--------------------Demo Mode--------------------
    if lbd_demo_mode:
        $ lbd_demo_no_choice = True

        while lbd_demo_no_choice:
            menu:
                Lo "Would you like to role-play?"
                "{s}Yes.{/s}":
                    lime45 "Not yet."

                "No.":
                    $ lbd_demo_no_choice = False
                    jump lbd_medieval_no

                "{s}Hell No!{/s}":
                    lime45 "Not yet."

    else:
        menu:
            Lo "Wanna RP?"
            "Yes:":
                jump lbd_medieval_yes
            "No":
                jump lbd_medieval_no
            "Hell No.":
                jump lbd_medieval_evil


label lbd_medieval_yes:
    c "Ok. Let's have some fun."


    jump lbd_medieval_end


label lbd_medieval_no:
    if persistent.playedzhong == True:
        define Fv = Character("Zhong", color="#7e9147", image="zhong")

    c "I'm not really comfortable doing that. "
    show lorem sad with dissolve
    $ renpy.pause(0.8)

    c "Lorem, I'm sorry. It's just I don't want to draw too much attention."
    Lo "It's ok, I understand."
    Lo normal "How about we just have a walk around and just see the sights?"
    c "Sounds good, sorry again."
    Lo normal "[player_name], please don't worry about it. I'm happy just being here."

    Lo normal "Are you hungry?"
    c "Yeah, I could do with some food."
    Lo "The stall over there is selling mystery treats on a stick, how about we get something from there, my treat."
    c "Why did you call them \"mystery treats\"?"
    Lo happy "It's more ominous that way. Now come on!"

    show lorem normal with dissolve
    show lorem normal at right with ease:
        xoffset 50

    show zhong normal c flip at left with easeinleft

    if persistent.playedzhong == True:
        Fv "Hello [player_name] and Lorem. How can I help you two today?"
        c "Zhong! What are you doing here?"
        Fv "I am where the festivals take me."
        c "That's a strange answer."
        Fv smile c flip "Yeah I know, I'm just messing with you."
        Fv normal c flip "I travel to some popular events to sell some homemade snacks. This festival usually works out rather well for me."
        c "Oh yeah, I remember you're saving up money to bring your son somewhere."
        Fv shy c flip "Yeah, the things that I do for him."

    else:
        Fv "How can I help you two today?"
        c "Oh hey."

    Fv normal c flip "So what can I get you?"
    c "What's available?"
    Fv "We have mystery meat skewers, mystery cheese skewers and mystery vegetable skewers."
    c "Let me guess, the mystery makes it more ominous."
    Lo "{i}snickers{/i}"
    Fv smile c flip "I'm guessing Lorem told you the joke already."
    Lo "Yeah I did, but [player_name] set me up for the joke. I couldn't help myself."
    Fv normal c flip "What are you buying?" #Res-e 4 reference

    $ lbd_player_food_option = "None"

    menu:
        "Mystery Meat.":
            $ lbd_player_food_option = "meat"

            $ mp.vegetarian = False
            $ mp.save()

            c "I'll give the mystery meat a go."

        "Mystery Veggies.":
            $ lbd_player_food_option = "veg"

            c "I'll take the veggies please."

        "Mystery Cheese.":
            $ lbd_player_food_option = "cheese"

            c "Against my better judgement, I'll take the cheese."

    Fv "Here you are. Now what would you like Lorem?"

    #if result = 1 ; lorem orders veg
    #if result = 2 ; Lorem orders cheese

    if renpy.random.randint(1, 2) == 1:
        if lbd_player_food_option == "veg":
            Lo normal "I'll take the same as well please."

        else:
            Lo normal "I'll take a mystery veg skewer."

        Fv "Here's your mystery veggies Lorem."

    else:
        if lbd_player_food_option == "cheese":
            Lo normal "I'll also have the unnervingly named cheese please."

        else:
            Lo normal "The scary cheese for me."

        Fv "Here you go Lorem."

    Fv "Well now you two are sorted, will I put the bill on [player_name]'s tab?"
    Lo normal "No, I'll cover it."

    menu:
        "[[Stop Lorem.]":
            $ renpy.pause(0.5)

            c "Lorem wait. We'll put it on my tab, Emera can take care of it then."
            Lo "I'm sure that's a pain for our friend here. I'll just pay him so he can get on with his day."
            c "Well alright, your choice."

        "[[Let Lorem pay.]":
            pass

    Lo "Here's your money. Thanks for the food."
    Fv "Pleasure doing business, you two have a good day."

    hide zhong with easeoutleft
    show lorem normal at center with ease

    $ renpy.pause(0.1)

    c "Thanks Lorem."
    Lo normal "Don't mention it."

    hide lorem normal with dissolve

    nvl clear
    window show

    n "We continue to walk around the festival. We take in the sights and even some more food."
    n "There are large earth dragons in full suits of armor. I have no idea how they get them on but they are scary looking."
    n "I can't help but think Lorem is a lot more disappointed than he's letting on, it seems he was really looking forward to the roleplay."
    n "At least this is all very refreshing. It's nice to get away from the police work."
    n "Lorem seems of have spotted something."
    n "Oh Lorem please no..."

    nvl clear

    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Oh yes, I think so."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} {i}sigh{/i}"
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Please? It'll be fun."
    n "I guess I do owe him something."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} Fine, fine. Let's do it."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Weeeeeeeeeeeeeeee, off to the stocks you go foul human!"

    nvl clear

    n "I approach the stocks, it's one where onlookers can throw wet sponges at you. I can honestly say, I'm not looking forward to this."
    n "The stallsman tried to tie me into a very awkward fitting stock. Clearly not made for humans but I'm stuck none the less."
    n "Looking at Lorem I see a very devilish grin spread across his face and a crowd build up behind him."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} This was a bad idea. Lorem, be kind."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Silence human, accept your punishment."

    nvl clear

    n "Here it comes..."
    play sound lbd_stock_slap
    $ renpy.pause(0.5)

    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} {i}pfffft{/i} You may be small but you have a good arm."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Thanks, how about another? {nw=1.5}"

    play sound lbd_stock_slap
    $ renpy.pause(0.5)

    n "There's so much water in my eyes I can't see clearly but I do see that crowd behind Lorem."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Ha Ha Ha. This is fun, good thing I got three sponges {nw=1.5}"

    play sound lbd_stock_slap
    $ renpy.pause(0.5)

    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} {i}pffft{/i} Alright Lorem, you had you fun. Time to let me out of this thing."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Yeah [player_name], We had our fun."
    n "The audience sounds disappointed, I guess they wanted a turn too."

    nvl clear

    n "I'm let out of the stock, my face dripping wet. Rubbing the water out of my eye's I see Lorem with this big proud grin."
    n "If it wasn't so cute I'd kick him."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} Come Lorem, let's be off."

    window hide
    nvl clear

    jump lbd_medieval_end

label lbd_medieval_end:
    scene black with Fade(1.2, 0.5, 0.5)
    stop music fadeout 1.5

    $ lbd_route_medevial_unplayed = False

    jump lbd_route_picking
