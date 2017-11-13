label lbd_lorem1:
    #--------------------Turn on Dev-mode--------------------
    if "lbdfrombootstrap" in renpy.python.store_dicts["store"]:
        if lbdfrombootstrap == "demo":
            $ lbd_demo_mode = True
            $ lbd_dev_debug = False

        else:
            $ lbd_dev_debug = True

    #if mod is not launched from the main menu
    else:
        $ lbd_dev_debug = False
        $ lbd_demo_mode = False

    #--------------------Turn on Demo-mode--------------------
    if lbd_dev_debug:
        menu:
            Db "Would you like to turn on Demo mode?."
            "Yes.":
                $ lbd_demo_mode = True

            "No.":
                $ lbd_demo_mode = False


    #--------------------Demo mode introduction--------------------
    if (lbd_dev_debug == False) and (lbd_demo_mode):
        if persistent.LBD_Played_Demo_Intro == None:
            $ persistent.LBD_Played_Demo_Intro = False
            $ renpy.save_persistent()

        call lbd_demo_intro

    elif (lbd_dev_debug) and (lbd_demo_mode):
        menu:
            Db "Would you like to see the demo intro?"
            "Yes.":
                call lbd_demo_intro

            "No.":
                pass


    #--------------------Save File Name--------------------
    if chapter4unplayed == False:
        $ save_name = "Ch. 4 - Lorem 1"

    elif chapter3unplayed == False:
        $ save_name = "Ch. 3 - Lorem 1"

    elif chapter2unplayed == False:
        $ save_name = "Ch. 2 - Lorem 1"

    else:
        $ save_name = "Ch. 1 - Lorem 1"

    $ chapter1csplayed += 1
    $ lorem1unplayed = False
    $ lorem1played = True
    #$ persistent.lorem1played = True
    $ datestatus = 0

    $ renpy.pause (0.5)

    play music case3 fadein 1.0
    $ renpy.pause (1.0)

    scene town7 with fade
    show lorem normal with dissolve

    if player_name == "Simon":
        Lo happy "Oh hello [player_name], Good to see you're as floofy as usual."
        Lo normal "I'm happy you're here, I was getting worried that you weren't going to show up."

    elif player_name == "Adam":
        Lo happy "Hey Modmaster. I was worried you weren't going to show up."
        show lorem normal with dissolve

    elif player_name == "Brian":
        Lo "Hello there."
        c "....."
        Lo think "Um, are you alright [player_name]? You seem preoccupied with that thing you're holding."
        Lo happy "I know!"
        m "Lorem gives me a mild kick in the shin, the little nails on his foot actually hurt less than you'd think, I guess he was being gentle."
        m "I look up from my PSP and look Lorem directly in the eyes."
        show lorem normal with dissolve
        c "Hmm?"
        menu:
            "What!":
                $ renpy.pause(0.5)
                c "Yes Blue Dragon, what is it?"
                Lo normal "Just getting your attention."
                m "I put my PSP in my pocket."
                c "Well you have it, what do you want?"
                Lo sad "Well you know."
                Lo normal "Just thanks for meeting me. I was quite worried you were not going to appear at all."

            "Oops, sorry.":
                $ renpy.pause(0.5)
                c "Oh I apologise, uhhhh..."
                Lo normal "The name is Lorem."
                c "Oh yes, sorry Lorem. I get a little distracted when I play games."
                Lo think "What is that thing anyway?"
                c "It's my PSP, I modded it to play emulators. I really like this little system."
                Lo think "Hmmm, right. I'll have to ask more about it another time."
                m "I put the PSP in my pocket."
                Lo normal "Anyway, thanks so much for meeting me. When we spoke I thought you only said yes to get rid of me and you wouldn't actually appear at all."

    elif player_name == "Thoroar":
        Lo normal "Hello there, How are you doing today?"
        c "I'm a bit cold."
        Lo think "Well it is a nippy day and I don't have a blanket to give you."
        c "Don't worry about it, I'll endure."
        Lo normal "Alright then, I'm happy you actually came. I was worried you weren't going to show up."

    else:
        Lo "Oh hi [player_name], thanks you so much for meeting me. I was worried you weren't going to show."
    #$ raise AssertionError("It knows too much...")

    #lorem kidnapped
    #day 47
    menu:
        "Well I'm here now.":
            $ renpy.pause(0.5)
            Lo happy "Well yes you are, let's try to do something fun."

        "Sorry for being late.":
            $ renpy.pause(0.5)
            $ datestatus += 1

            Lo happy "No worries, I usually tell people to be somewhere about 10 minutes before I actually want them to be there."
            c "That's good thinking."
            Lo normal "Yeah, Ipsum gave me the idea."
            c "Oh right, uhhhh, whose Ipsum?"
            Lo happy "Oh he's my roommate, we share an apartment together."
            Lo normal "Housing can be very expensive here."
            c "Ok then, well, let's continue with our {i}\"date\"{/i} then."
            Lo shy "..."

        "I wasn't planning to show.":
            $ renpy.pause(0.5)
            $ datestatus -= 1

            c "Yeah, I just couldn't find anything else to do."

            Lo sad "Glad to be so high on your priority list."
            Lo normal "Well let's try to make the most of it then."
            c "Whatever."

    show lorem normal with dissolve
    c "What do suggest we do?"
    Lo think "This town may be serene however there isn't exactly much here to see."
    Lo normal "Let's go to somewhere else. A mini-holiday, if you will."
    c "Sounds like it could be fun, how do we get anywhere and where are we going?"
    Lo think "...{w}...{w}..."
    Lo happy "I know where we'll go, but that's going to be a surprise."
    Lo normal "As to how we are going to get there, well considering you can't fly, I guess we'll take the train."
    c "You have trains?"
    Lo normal "Yes of course we do, just not many. The station isn't far, follow me."

    play sound "fx/steps/clean2.wav"
    scene black with fade
    $ renpy.pause(1.0)
    nvl clear
    window show

    n "We walk along the quiet streets. I notice Lorem is taking the quiet ones. I guess he doesn't like crowds all that much."
    if datestatus == 1:
        n "Lorem seems like he's a nice enough dragon? Man I'm still getting used to this; it's so bizarre being the only human in a world of mythical creatures."
        n "Well I guess to them I'm the mythical creature. It's all a matter of perspective."
        n "This is certainly a unique experience."

    elif datestatus == -1:
        n "Dragged along by a little blue bastard to some random unknown place."
        n "I should have just stayed home and read a book."

    else:
        n "So here I am following a dragon to a train station to go to some random unknown place."
        n "I don't know what decisions I made in life to lead me here."
        n "At least he seems nice but even if he isn't, a good kick would knock him out."


    n "I see what looks like train station in the distance, we're almost there now."

    window hide
    nvl clear

    scene trainstation with fade

    $ renpy.pause(0.5)

    m "We arrive and almost immediately we are stopped by Sebastian."

    show lorem normal flip at Position(xpos = 0.25)
    show sebastian normal b at Position(xpos = 0.75)
    with dissolve

    Sb "I'm sorry you two but I have to stop you."
    Lo relieved flip "All we are going to do with ride the train somewhere"
    Sb "Lorem, you know the town put limitations on citizens travelling in and out of the town."
    Lo think flip "But I rode the train a while back without a problem."
    Sb drop b "Well Lorem, it's not you I have to convince from travelling."
    Lo think flip "So you're stopping [player_name]? Can you even do that?"

    menu:
        "It's alright, we'll just go somewhere else.":
            $ renpy.pause(0.5)
            Sb normal b "Thanks for your cooperation [player_name]. I appreciate it."
            show lorem relieved flip with dissolve
            $ renpy.pause(1.0)
            Lo think flip "...{w}...{w}hmmmmm"
            Sb disapproval b "You better not be thinking of something."
            Lo normal flip "Of course not."
            Sb disapproval b "I'll be keeping an eye on you. Now please be on your way."
            c "Cya Sebastian."

            scene black with fade

            #--------------------If Demo Mode--------------------
            if (lbd_demo_mode) and not lbd_dev_debug:
                jump sneakinwithlorem

            #--------------------Dev debug--------------------
            elif lbd_dev_debug:
                menu:
                    Db "Koth mod installed?"

                    "Yes":
                        play sound "fx/steps/clean2.wav"
                        jump talking_to_koth

                    "No":
                        play sound "fx/steps/clean2.wav"
                        jump sneakinwithlorem

            #--------------------If full game Mode--------------------
            else:
                if is_koth_mod():
                    play sound "fx/steps/clean2.wav"
                    jump talking_to_koth

                else:
                    play sound "fx/steps/clean2.wav"
                    jump sneakinwithlorem

        "We'll be quick.":
            $ renpy.pause(0.5)
            $ datestatus += 1

            Sb disapproval b "Hmmmm."
            c "Come on Sebastian, I'll survive."
            Sb disapproval b "I can't stop you from going but I honestly think it's a bad idea."
            Lo normal flip "So we can go?"
            Sb normal b "Yes you can."
            Lo happy flip "Eeeeeeeeeeeeeeeeeeeee~"
            Sb normal b "Have a safe journey."

            menu:
                "[[Kiss his hand.]":
                    $ renpy.pause(0.5)

                    play sound "fx/kiss.wav"
                    $ renpy.pause (1.0)
                    show sebastian shy b with dissolve
                    c "You're such a sweetheart."

                "[[Wave goodbye.]":
                    $ renpy.pause(0.5)

                    c "Thanks Sebastian, you have a good day."
                    Sb disapproval b "Come back OK and I will."
                    c "You got a deal."
                    Lo normal flip "Don't worry, I'll keep [player_name] safe."

            hide sebastian with dissolve
            show lorem normal at center with ease
            $ renpy.pause(0.5)

            Lo "Let's go wait for the train."

        "No he can't.":
            $ renpy.pause(0.5)
            $ datestatus += 1

            c "Not to be mean about it but I am an ambassador, shouldn't that mean I can travel where ever I want without restriction?"
            Sb drop b "It's not that I can stop you from going but I do have to at least try for your own safety."
            c "Whose going to a hurt a human? It seems everywhere I go dragons are more fascinated by me than anything else."
            Sb disapproval b "I guess that's true but still, we have to keep you safe and we are too understaffed to accompany you everywhere."
            Lo normal flip "I'll do what I can to keep [player_name] safe. I know where to go to avoid..."
            Lo sad flip "...too much attention."
            Sb normal b "I guess you would. Safe journey to the both of you."
            show lorem normal with dissolve
            Sb normal b "I'll leave you two get your train. Goodbye and come back in one piece."

            hide sebastian with dissolve
            show lorem normal at center with ease
            $ renpy.pause(0.5)

            c "See you around Sebastian."
            Lo "Let's go wait for the train."

        "He'd be fired if he tried":
            $ renpy.pause(0.5)
            $ datestatus -= 1
            show lorem relieved flip with dissolve

            c "Stopping me will result in a nightmarish diplomatic situation and you'll quickly lose your job."
            c "I wouldn't count on Bryce helping you out either, he'll lose his job too!"

            Sb drop b "You don't have to be so blunt about it but you're right."
            Sb disapproval b "Fine go! See what I care."
            hide sebastian with dissolve
            show lorem sad at center with ease
            $ renpy.pause(0.5)

            Lo sad "That wasn't very nice of you."
            c "Yeah but we got what we wanted. That's all that matters."
            c "Let's go."
            Lo "..."
            c "The same applies to you too, now come on!"
            Lo relieved "I'm on my way..."

    c "You know, you still haven't told me where we are going."
    Lo normal "And I'm not going to, you'll find out when we are there."
    c "Why not tell me?"
    Lo "I like to surprise people and I'm looking forward to showing someplace new."
    Lo happy "Even if I told you the name of where we are going, what difference would it make to you?"
    c "Not much really I suppose. Fine, it can wait until we're there."
    Lo normal "Look here comes the train now."

    scene insidetrain with fade
    play nature lbd_train_ambiance fadein 1.0

    show lorem normal with dissolve

    #So lorem and mc talk about something
    call lbd_ontrain_2kimberland
    ##jump
    stop nature fadeout 0.5

    $renpy.pause(1.0)

    Lo normal "Looks like we're here."
    Lo "Come on, this is going to be fun."

    jump kimberland_intro

    return

label lbd_ontrain_2kimberland:
    $ lbd_talking_loop = lbd_ask_about_trains = True
    $ lbd_talk_about_old_methods = lbd_talk_about_boteny = False

    while lbd_talking_loop:
        show lorem normal with dissolve
        $ renpy.pause(0.2)

        menu:
            "[[Ask about trains.]" if lbd_ask_about_trains:
                $ renpy.pause(0.5)
                $ lbd_ask_about_trains = False

                c "You said there aren't many trains around. What do you mean by that?"
                Lo "Trains are slowly becoming more important for our everyday lives."
                c "Are trains new here?"
                Lo "Oh of course not, they are just spreading very slowly because the old methods still work for most places."
                $ lbd_talk_about_old_methods = True
                c "What old methods? What are the methods for?"
                Lo think "I guess this is a badly structured conversation. Perhaps I should start over."
                Lo normal "OK. Trains are not new to here but are slow to expand. They usually make their way to a town to bring cargo to it."
                Lo happy "Thankfully us being able to use them for travel is a bonus."
                c "What kind of cargo are you talking about?"
                Lo normal "Well two kinds of cargo usually; post and food."
                Lo "Once upon a time everywhere was close to everywhere else, so just walking to another town was almost an everyday thing."
                Lo "However the demand for space increased which lead to towns popping up further away from other towns."
                Lo "Obviously this made transporting food difficult. It was common for towns to tend their own food supply."
                Lo "For this town what would be mostly wheat and livestock. Wheat can grow basically anywhere."

                Lo "Important stuff like medicine would have to be brought to the town, usually by someone who can fly."
                c "I see, that doesn't sound like fun. Dumb question for you, what changed when the train connected to the town?"
                Lo think "It's hard for me to say, the station opened up when I was a kid."
                Lo happy "However when it opened, it was the first time I got to try coffee. I really liked it."
                menu:
                    "What's so special about coffee?":
                        Lo normal "We are above what's called \"The Coffee Bean-Growing Belt\". Basically it's the climate where coffee can grow naturally."
                        Lo "Now I know how to grow my own coffee beans but even getting the seeds would have been very difficult."
                        c "Do you grow your own coffee beans?"
                        Lo think "Well I did think about it but Ipsum wouldn't let me."
                        Lo normal "He doesn't really like me drinking coffee at home. He says I can get a little out of hand if I drink too much."
                        c "I suppose with your smaller size to most, coffee would effect you a bit more."
                        Lo "Another reason I haven't grown any coffee myself is that I can only grow Robusta coffee."
                        c "How is that a problem?"
                        Lo "Robusta coffee isn't as nice as Arabica. The Robusta kind is much easier to grow and can grow at sea level."
                        Lo "Compared to Arabica which needs to be at least six hundred meters above sea level."
                        Lo "Not to mention that Robusta coffee has much more caffeine in it, which adds to why Ipsum won't let me grow any."
                        $ lbd_talk_about_boteny = True

                    "You drink coffee?":
                        Lo happy "Yes I do. I love the stuff."
                        Lo normal "Unfortunately I can't drink much of of it because of my size. It basically just effects me more than it would someone larger."
                        c "Well you seem energetic enough without coffee."
                        Lo "That's why Ipsum won't let me drink too much of it at home. He says I can get a little out of hand."
                        menu:
                            "At least you have someone to look after you.":
                                $ datestatus += 1

                                Lo shy "Yeah. I guess I am lucky that way."

                            "Letting someone boss you around, pathetic.":
                                $ datestatus -= 1

                                Lo sad "Hmmmm"
                                Lo "I like to think he's just looking after me."

                        show lorem normal with dissolve

                Lo happy "You know, I remember my mother queueing up for about half an hour just to buy some. I only remember because I was there and incredibly bored."
                Lo normal "Coffee was the latest thing and until then was only something the really rich could drink."

            "[[Ask about \"old methods\".]" if lbd_talk_about_old_methods:
                $ renpy.pause(0.5)
                $ lbd_talk_about_old_methods = False

                c "You mentioned \"old methods\", that's someone travelling to a different town for something they need. Yeah?"
                Lo happy "Yes of course."
                Lo "According to what I read, it worked rather well years ago."
                Lo normal "Sometimes that old method is still used today, even in places that have a train link."
                c "What would these old methods be used for?"
                Lo "Well I can't speak for everywhere but in town the only things that get sent manually are high priority post and medicine."
                c "Do you mean to tell me your town doesn't have medicine?"
                Lo "Oh not at all. Of course our town has medicine but sometimes an uncommon medicine is needed and the town might not have it."

                menu:
                    "What happens when medicine is needed?":
                        Lo think "Well it depends."
                        Lo normal "If the person who needs the medicine either knows a flyer type or is a flyer type and is able to fly. Then they'll usually get the medicine very fast."
                        Lo "Often, Adine would fly somewhere to get something for one of the kids at the orphanage."
                        Lo "She's a fast flyer and would usually be back in under an hour."
                        menu:
                            "That's sweet of her.":
                                Lo happy "Yeah it really is."
                                Lo normal "She is known to help take care of the sick when she can."

                            "I see.":
                                Lo normal "She tries to help them best she can."

                        c "How about in cases where you can't ask someone to go get medicine for you?"
                        Lo normal "Simple really, they'll have to pay someone to go get it for them."
                        Lo normal "Usually the chemist will sort out those details."
                        Lo "There is a short list of couriers that chemists use, I'm on that list."
                        c "Do you often get a job out of it?"
                        Lo think "Hmm, it's seasonal really."
                        Lo "Not many get sick in the middle of a season, it's really only when a season changes that they get sick."
                        c "Any idea why that is?"
                        Lo happy "It's obvious really."
                        Lo normal "You get used to habits that you pick up during a season. A common example would be leaving your window open at night during the summer only to keep doing it when going into winter."
                        Lo "So as long as I take care of myself, I'll usually get a few jobs from the chemist. The pay is fairly good but sometimes I do it for free for someone with limited funds."

                    "That doesn't sound like a very good system.":
                        Lo think "I assume you're referring to a town not having all the medicine it needs?"
                        c "Yeah, like isn't it dangerous and more expensive not to have all the medicine you need?"
                        Lo normal "It's not really dangerous, even if someone to collect the medicine isn't available, it would take 2 days maximum to get it by the train."
                        Lo "The cost on the other hand. It seems more expensive but if we kept every kind of medicine in a town that small then the medicine would expire before anyone needs it."
                        Lo "So it really is cheaper just to get what you need as you need it instead of trying to cover the cost of expired medication."
                        c "That makes sense."

            "[[Ask about botany.]" if lbd_talk_about_boteny:
                $ renpy.pause(0.5)
                $ lbd_talk_about_boteny = False

                c "I can't help but notice that you seem to know your stuff about plants. Do you study botany?"
                Lo happy "Yeah I do."
                Lo think "Well no, not exactly."
                Lo normal "I've just been taking care of plants for about as long as I can remember."
                Lo "It began with some small potted plants in my room and honestly that hasn't really changed. That plants have just gotten bigger."
                c "Does that not get a little out of hand?"
                Lo "Yes and no. I live in an apartment without a garden and Ipsum won't let me keep too many plants in the living room. So I'm limited to just my room."
                Lo "As a compromise I got the bigger of the two rooms."
                c "Don't plants need light aswell in order to grow correctly?"
                Lo "They do, some plants more than others."
                Lo "As long as I grow plants that don't need too much light, then they'll grow just fine."
                ## All stuff you can grow indoors BTW
                Lo "Right now I have an aloe vera plant, carrots, green garlic, scallions and various herbs."
                Lo happy "Rather than decorative, I try to grow more useful plants. However sometimes I try to grow a more complicated plant, like roses."
                Lo normal "There's something just relaxing about tending a plant's needs."

                menu:
                    "You can always tend to my needs.":
                        $ datestatus -= 1
                        $ renpy.pause(0.5)

                        Lo relieved "{i}sigh{/i}"
                        Lo "Let's just move on."

                    "How so?":
                        $ renpy.pause(0.5)

                        Lo normal "Honestly I just like planting a seed and watching it grow."
                        Lo "I like to work with my hands and the smell of soil is very relaxing."
                        Lo sad "Although sometimes it makes me feel old."
                        c "How can plant's make you feel old?"
                        Lo normal "Because you plant a seed and it feels like no-time before it's taller than me when in fact it had been growing for a few years."
                        c "I suppose that can make you feel old. What do you do with a plant once it's fully grown?"
                        Lo think "It depends on the plant."
                        Lo normal "It's one I grow for food then obviously I just harvest it."
                        Lo "If it's one I grew for decoration then I would either put it on display or just sell the plant at a market."
                        ### Note to self, possible rant on markets.
                        c "Makes sense"

            "[[Done.]":
                $ lbd_talking_loop = False

        if (lbd_ask_about_trains == False) and (lbd_talk_about_old_methods == False) and (lbd_talk_about_boteny == False):
            $ lbd_talking_loop = False
            show lorem normal with dissolve

    return

label sneakinwithlorem:
    $ renpy.pause(0.5)
    scene outsidestation with fade

    show lorem normal with dissolve
    $ renpy.pause(0.2)

    c "Well that's a shame, what do we do now Lorem?"
    Lo happy "I have a plan."
    c "What are you thinking then? We could go to the bar and just have a chat if you want."
    Lo normal "Nah, that sounds rather dull. Let's do something fun instead."
    c "Ok then, please continue with your plan."
    Lo happy "Yes, how about we sneak in to the station and hop onto the train when the train shows up?"

    menu:
        "Yes.":
            pass

        "No.":
            $ renpy.pause(0.5)

            show lorem normal with dissolve
            lime45 "Well fine. Since you really don't want to experience what this mod has to offer, I'll just drop you into the stock date."
            lime45 "The boring stock date where you just sit there in a room with Lorem."
            lime45 "No mini-game, no adventure, no scenery, no new music, no romance, etc."
            lime45 "Just you and him."
            lime45 "I hope you enjoy it."
            lime45 "Oh I almost forgot to mention, I disabled the games skip feature for the date. So, be sure to read the whole thing."

            jump lbd_stock_lorem1

    $ datestatus += 2
    $ renpy.pause(0.5)

    c "Is that even legal?"
    Lo normal "{i}pfffffff{/i} Well that's a subjective question."
    c "Not really. Stealing food is illegal not matter how hungry you are."
    m "Lorem waves his arms dismissively."
    Lo "Don't get so bogged down in the little details. We're out to have fun, who is Sebastian to say we can't?"
    c "Hmm, I'm not so sure. I have to act with a certain level of decorum while I'm here."
    m "Lorem again waves his arms dismissively."
    Lo "Where's the fun in that? What's the human phrase again, \"let your hair down.\""
    c "Yeah it is, who do you know that?"
    Lo "I read it in a book once."
    c "Fine then. How do we do it?"
    Lo happy "Yay."
    Lo normal "What we'll do is wait until the train arrives to hop over the wall and run onto the train."
    c "And how pray tell, do we get over the wall?"
    Lo think "I can just fly but you I'm afraid, will have to climb the wall."
    c "I'm not sure how well that'll work. I was never particularly good at climbing a wall."
    Lo "Hmm."
    Lo happy "I have an idea."
    c "What is it?"
    Lo normal "All in good time, for now let's just wait for the train."

    scene black with fade
    nvl clear
    $ renpy.pause(0.5)
    window show

    n "We wait by the wall for the train."
    n "Once we heard the train approach we try to get ready."
    n "I attempt to grab the wall and jump up."
    n "Instead I slip and pretty much land on my face. It hurt a lot."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} [player_name], what happened? are you OK?"
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} Yeah, I'm fine. I just can't grip the wall."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} Let me help you."

    nvl clear

    n "Lorem darts behind me and jumps up on my back."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} I got a grip on you now try to climb the wall."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} OK Lorem, I hope you know what you're doing."

    nvl clear

    n "Once again I try to climb the wall but this time Lorem his flapping his wings trying to help pull me up."
    n "It's a struggle but I have just enough grip on the gaps between bricks to start climbing."
    n "I fling my arm over the wall just as my own weight begins to fall back on to me."
    n "I hear Lorems heavy panting as he struggles to help me up."
    n "I swing my leg over the wall with all the of the energy I can muster."

    nvl clear

    n "Now laying on my belly on the wall, I feel Lorem sit on my back."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} Oi you! This isn't time to rest, we have a train to catch."
    n "{b}{color=#5ab7e1}Lorem:{/colour}{/b} {i}pant.. pant{/i} Yes yes {i}pant{/i} let's go."
    n "{b}{color=[persistent.playercolor]}[player_name]:{/colour}{/b} Come on, the door is open!"
    n "We jump off of the wall and aboard the train, hearing Sebastian shout at us on the way in the closing door."

    window hide
    nvl clear

    scene insidetrain with fade
    play nature lbd_train_ambiance fadein 1.0

    show lorem normal with dissolve
    $ renpy.pause(0.2)

    c "Heh we made it."
    Lo "Just about, yeah. {i}pant{/i}"
    c "Oh before I forget, thanks for the lift."
    Lo "Hey don't mention it but can we please sit down now?"
    c "Sure, sure. There's two seats side by side free over there."
    Lo "Yeah, it's been a while since I had to something like that."
    Lo "So, what would you like to talk about?"

    #So lorem and mc talk about something
    call lbd_ontrain_2kimberland

    stop nature fadeout 0.5

    $ renpy.pause(1.0)

    Lo normal "Looks like we're here."
    Lo "Come on, this is going to be fun."

    jump kimberland_intro

label lbd_demo_intro:
    scene heartbg with fade:
        xcenter 0.5 ycenter 0.5
    $ renpy.suspend_rollback(True)

    $ renpy.pause(0.5)
    play sound "fx/system.wav"
    s "Beginning Lorem's Better Date Demo{cps=2}...{/cps}{w=1.0}{nw}"

    if persistent.LBD_Played_Demo_Intro == True:
        menu:
            Dm "Would you like to replay the introduction for the Lorem mod?"

            "Yes.":
                pass

            "No.":
                $ renpy.pause(0.8)
                $ renpy.suspend_rollback(False)
                scene black with fade
                return

    #-----Continue with the intro for the mod-----
    if chapter4unplayed == False:
        $ save_name = "Lorem mod intro"

    elif chapter3unplayed == False:
        $ save_name = "Lorem mod intro"

    elif chapter2unplayed == False:
        $ save_name = "Lorem mod intro"

    else:
        $ save_name = "Lorem mod intro"

    $ noisedissolve = ImageDissolve(im.Tile("ui/noisetile.png"), 1.5, 1, reverse=True)
    $ renpy.pause(1.0)
    $ renpy.suspend_rollback(False)

    scene black with fade
    play music lbd_case1 fadein 1.5
    $ renpy.pause(1.0)
    $ renpy.suspend_rollback(False)

    scene visiting_ipsum with noisedissolve
    $ renpy.pause(0.05)
    show lorem normal with dissolve
    $ renpy.pause(0.2)

    Lo "Hello there."
    Lo "I wanted to personally welcome you to my better date mod."
    Lo "Lime is here too, say \"hi\" Lime!"
    lime45 "Hi Lime."
    Lo relieved "You're such a smart ass, you know that?"
    Lo normal "Well, with the unpleasantries out of the way. I just wanted to talk to you about something."
    c "Go ahead Lorem."
    Lo think "Well I think Lime should tell you. Take it away Lime!"
    lime45 "Thanks Lorem."

    show lorem normal with dissolve

    lime45 "So basically this is a Demo for the Lorem Mod I've been working on for a while."
    lime45 "Some of ye might know of it already and a handful have tried it during it's development."
    lime45 "It began as a tech demo showing off a few things, namely that mods can talk to each other."
    lime45 "Which is something important for compatibility between mods or even a mod series perhaps?"
    lime45 "Over time a playable mod began to clad around the tech demo and I wound up with this."
    lime45 "There isn't exactly much being showed off and the good and best endings have not been implemented."
    lime45 "So really this demo is for feedback purposes."
    lime45 "There are some surprises in this demo and there is some more stuff that I'm keeping to myself for the final version."
    lime45 "A lot of time and work has gone into this mod so far a lot more is needed to finish it."
    lime45 "If you want to help out in the development please consider volunteering to do some writing or donating to my Ko-Fi. You can find a link to it in the credits file."
    lime45 "And yes, a nice chunk of money has already been spent on this mod and with more money I could get more assets."
    lime45 "So yeah, that's that."
    lime45 "I really hope you enjoy this mod and leave some feedback letting me know how this turning out."

    lime45 "Soooo then, Lorem, why are we here?"

    Lo happy "Oh right, Ipsum and I are visiting his parents."
    lime45 "Oh right, you do know that [player_name] is expecting to go on an epic adventure with you yeah?"
    Lo relieved "Yeah... I'm sorry."
    Lo "It's just how my schedule worked out."

    show lorem normal at Position(xpos=0.7) with ease
    show ipsum normal flip at Position(xpos=0.25) with easeinleft

    Ip "Mam and Dad are expecting us inside, what's the hold up?"
    lime45 "Hello Ipsum."
    Ip happy flip "Oh hello there Lime."
    Lo sad "Hey Ipsum?"
    Ip think flip "Yes?"
    Lo sad "I had promised Lime that I would go on an adventure with [player_name]."
    Ip think flip "I see."
    Ip normal flip "Ahh that's OK."
    Lo think "What do you mean?"
    Ip happy flip "You know my mam, she'll understand and only ask you to have at least one drink."
    Lo normal "Well alright then."
    Lo "So Lime and [player_name], I'll be back shortly and we'll have our adventure."
    Lo "I just have to pop inside for a bit, just to be nice."

    hide ipsum
    hide lorem
    with easeoutleft

    # if player has their music volume turned way down low or has it muted
    if renpy.game.preferences.get_volume("music") < 0.08:
        scene visiting_ipsum_night with Dissolve(3.0)
        $ renpy.pause(0.8)

    else:
        stop music fadeout(1.0)
        $ renpy.pause(1.0)
        play music lbd_seasons_change fadein(0.1)
        scene visiting_ipsum_night with Dissolve(11.50)

        play music lbd_case1 fadein 0.8
        $ renpy.pause(0.8)

    show lorem drunk with easeinright

    Lo "That was one hell of a party!"
    lime45 "Lorem, that took longer than \"a bit\"."
    Lo "{i}hic{/i} Um yeah, what?"
    Lo "Ohh right, the thing. {i}hic{/i}"
    m "Lorem almost stumbles over, he is way too drunk right now."
    lime45 "Hey [player_name], sorry about this. I hope this doesn't put you off the epic adventure that's in-store for you."
    Lo "Wait.. wait.. wait.. why yawl spinning around like that? {w=1.2}"

    show lorem drunk at Position(xpos=0.5, xanchor='center', ypos=1.0, yanchor="top") with move9
    play sound "fx/impact3.ogg"

    lime45 "I guess we have to wait until he's sober."
    c "What do we do now?"
    lime45 "I'll leave him a note on his hat and we'll fade to black. Hopefully we'll fade in on the date."
    c "Wait what?"
    play sound lbd_pencil_writing
    lime45 "{i}Meet [player_name] at the park tomorrow.{/i}"
    stop sound
    lime45 "There we go. See you tomorrow."

    stop music fadeout 1.2
    $ renpy.pause(0.8)
    scene black with fade

    if persistent.LBD_Played_Demo_Intro == False:
        $ persistent.LBD_Played_Demo_Intro = True
        $ renpy.save_persistent()

    return
