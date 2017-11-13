label kimberland_intro():
    #--------------------Save File Name--------------------
    if chapter4unplayed == False:
        $ save_name = "Ch. 4 - Lorem 1 - Hub"

    elif chapter3unplayed == False:
        $ save_name = "Ch. 3 - Lorem 1 - Hub"

    elif chapter2unplayed == False:
        $ save_name = "Ch. 2 - Lorem 1 - Hub"

    else:
        $ save_name = "Ch. 1 - Lorem 1 - Hub"

    $ lbd_route_arcade_unplayed = lbd_route_medevial_unplayed = lbd_route_park_unplayed = True
    $ lbd_routes_played = 0

    stop music fadeout 1.0
    scene black with fade

    $ renpy.pause(0.3)

    play music kimberland_town_music fadein 1.0

    $ renpy.pause(0.3)
    scene lbd_kimberland_town with fade:
        yoffset -198

    $ renpy.pause(1.0)

    scene lbd_kimberland_town at Pan((0, 198), (0,0), 8)

    $ renpy.pause(3.0)

    nvl clear
    window show

    n "So this is where Lorem wanted to take me."
    n "Wow, it's been a long time since I've seen country side this lush. The air smells so clean."
    n "This seems like a quaint little town. I have to admit, it's nice getting to see a bit more of this world."
    n "I wonder why he wanted to come here."
    n "Let's have some fun with whatever it is he wants to do."

    window hide
    nvl clear

    scene black with fade
    stop music fadeout 1.0
    $ renpy.pause(1.2)

#    if not lbd_demo_mode:
    play music case3 fadein 1.0
    $ renpy.pause(0.5)

    scene lbd_panorama2 with fade
    show lorem normal with dissolve

    $ renpy.pause(0.5)

#    if lbd_demo_mode:
#        play sound "fx/system.wav"
#        $ renpy.pause(0.5)
#        Dm "Your actions from this point forward are not going to be judged."
#        Dm "Not everything is finished and some of what's here will have to be reworked a little to give you more freedom."
#        Dm "However you "


    Lo "So here we are."
    c "Where is \"here\" anyway?"
    Lo "We're in a small town called Kimberland. Every year they host an event that myself and Ipsum simply must visit."
    Lo "It's a bit of a journey to get out here but it's always worth it."
    c "Oh what is this event?"
    Lo happy "All will be revealed in good time."
    Lo normal "This train station is really handy, we're right in the middle of everything. So then, where do you want to go?"

    #--------------------Dev debug--------------------
    if lbd_dev_debug:
        menu:
            Db "Skip to post route scenes?"

            "Yes":
                $ lbd_route_arcade_unplayed = lbd_route_medevial_unplayed = lbd_route_park_unplayed = False
                jump lbd_route_picking

            "No":
                pass

    #--------------------Demo Mode--------------------
    if lbd_demo_mode:
        $ lbd_route_park_unplayed = False
        $ lbd_routes_played = 1

    hide lorem with dissolve
    jump lbd_route_picker



#this is used to stop the music resetting after lorem on the nav screen disappears
label lbd_route_picking():
    #--------------------Save File Name--------------------
    if chapter4unplayed == False:
        $ save_name = "Ch. 4 - Lorem 1 - Hub"

    elif chapter3unplayed == False:
        $ save_name = "Ch. 3 - Lorem 1 - Hub"

    elif chapter2unplayed == False:
        $ save_name = "Ch. 2 - Lorem 1 - Hub"

    else:
        $ save_name = "Ch. 1 - Lorem 1 - Hub"

    #--------------------Dev debug--------------------
    if lbd_dev_debug:
        menu:
            Db "Skip to post route scenes?"

            "Yes":
                $ lbd_route_arcade_unplayed = lbd_route_medevial_unplayed = lbd_route_park_unplayed = False

            "No":
                pass


    if (lbd_route_arcade_unplayed) or (lbd_route_medevial_unplayed) or (lbd_route_park_unplayed):

        scene black with fade
        stop music fadeout 1.0
        $ renpy.pause(0.8)

        play music case3 fadein 1.0

        jump lbd_route_picker

    else:
        scene black with fade
        stop music fadeout 1.0
        $ renpy.pause(0.8)

        play music case3 fadein 1.0

        jump kimberland_full_ending


label lbd_route_picker():

    #Defaults the shown screen to ScreenNum 2
    if not "screenNum" in renpy.python.store_dicts["store"]:
        $ screenNum = 2

    if screenNum == 1:
        show lbd_panorama1

    elif screenNum == 2:
        show lbd_panorama2

    else:
        show lbd_panorama3

    $renpy.pause(0.5)

    $ picking = True
    while picking:
        #--------------------arcade option--------------------
        if screenNum == 1:
            $ sel_action = renpy.call_screen("jumpyscreen1")

            if sel_action == 2:
                $ screenNum = 2
                hide lbd_pano21
                show lbd_pano12 zorder 2
                $ renpy.pause(1.2)

            elif sel_action == 3:
                $ renpy.pause(0.2)
                scene black with fade
                $ picking = False
                jump lbd_start_arcade

            elif sel_action == 4:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                c "I hear an arcade, is there one near by?"
                Lo normal "Yes there is, there's one just up those stairs."
                c "Oh cool, good to know."
                Lo normal "If you want to go to the arcade I'm \"game\". In fact it should be fun."

                hide lorem with dissolve
                jump lbd_route_picker

            elif sel_action == 5:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                Lo normal "I know the acrade is fun but we've been there already, how about we go somewhere else?"
                c "Yeah, you're right."

                hide lorem with dissolve
                jump lbd_route_picker


        #--------------------medieval festival--------------------
        elif screenNum == 2:
            $ sel_action = renpy.call_screen("jumpyscreen2")

            if sel_action == 1:
                $ screenNum = 1
                hide lbd_pano12
                hide lbd_pano32
                show lbd_pano21 zorder 2
                $ renpy.pause(1.2)

            elif sel_action == 2:
                $ screenNum = 3
                hide lbd_pano12
                hide lbd_pano32
                show lbd_pano23 zorder 2
                $ renpy.pause(1.2)

            elif sel_action == 3:
                $ renpy.pause(0.2)
                scene black with fade
                $ picking = False
                jump lbd_medieval_start

            elif sel_action == 4:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                c "So Lorem, what's this way?"
                Lo happy "That direction goes to main attraction here at Kimberland."
                c "What is this main attraction?"
                Lo normal "Well you'll just have to head that way to find out. Trust me, it'll be fun. It always is."
                Lo normal "In fact it's the reason why I wanted to come to this town."
                c "I suppose we'll have no choice but to go then."

                hide lorem with dissolve

                jump lbd_route_picker

            elif sel_action == 5:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                Lo normal "We've already seen everything thing the festival has to offer. Let's go somewhere else."

                hide lorem with dissolve

                jump lbd_route_picker


        #--------------------mystery option--------------------
        elif screenNum == 3:
            $ sel_action = renpy.call_screen("jumpyscreen3")

            if sel_action == 1:
                $ screenNum = 2
                hide lbd_pano23
                show lbd_pano32 zorder 2
                $ renpy.pause(1.2)

            #to the park
            elif sel_action == 3:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                Lo "This route is still a secret."

                hide lorem with dissolve
                jump lbd_route_picker

            elif sel_action == 4:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                Lo "This route is still a secret."

                hide lorem with dissolve
                jump lbd_route_picker


            elif sel_action == 5:
                $ picking = False
                $ renpy.pause(0.6)
                show lorem normal zorder 3 with dissolve
                $ renpy.pause(0.5)

                Lo normal "Mystery"

                hide lorem with dissolve

                jump lbd_route_picker

            elif sel_action == 6:
                $ picking = False
                $ renpy.pause(0.6)
                jump kimberland_early_ending


#--------------------Arcade Screen--------------------
screen jumpyscreen1():
    imagebutton:
        focus_mask True
        auto "ui/lorem_nav_%s.png"
        hovered Play("audio", "se/sounds/select.ogg")
        if lbd_route_arcade_unplayed:
            action [Play("audio", "se/sounds/select3.ogg"), Return(4)]

        else:
            action [Play("audio", "se/sounds/select3.ogg"), Return(5)]

        at lorem_nav_trans

    imagebutton:
        focus_mask True
        xpos 0.5
        ypos 0.5
        if lbd_route_arcade_unplayed:
            idle "arcadeicon-idle"
            hover "arcadeicon-Selected"
            selected_idle "arcadeicon-idle"
            selected_hover "arcadeicon-Selected"
            action [Play("audio", "se/sounds/select3.ogg"), Return(3)]

        else:
            idle "arcadeicon-insensitive_idle"
            hover "arcadeicon-insensitive_Selected"
            selected_idle "arcadeicon-insensitive_idle"
            selected_hover "arcadeicon-insensitive_Selected"
            action [Play("audio", "se/sounds/select3.ogg"), Return(5)]

        hovered Play("audio", "se/sounds/select.ogg")
        at panoButtons
        style "arcicon"

    imagebutton:
        focus_mask True
        auto "ui/lbd_right_arrow_btn_%s.png"
        action [Play("audio", "se/sounds/select3.ogg"), Return(2)]
        hovered Play("audio", "se/sounds/select.ogg")
        at lbd_right_arrow_trans

#--------------------medieval Screen--------------------
screen jumpyscreen2():

    imagebutton:
        focus_mask True
        auto "ui/lorem_nav_%s.png"
        hovered Play("audio", "se/sounds/select.ogg")
        if lbd_route_medevial_unplayed:
            action [Play("audio", "se/sounds/select3.ogg"), Return(4)]

        else:
            action [Play("audio", "se/sounds/select3.ogg"), Return(5)]

        at lorem_nav_trans

    imagebutton:
        focus_mask True
        xpos 0.5
        ypos 0.5
        if lbd_route_medevial_unplayed:
            idle "medievalicon-idle"
            hover "medievalicon-selected"
            selected_idle "medievalicon-idle"
            selected_hover "medievalicon-selected"
            action [Play("audio", "se/sounds/select3.ogg"), Return(3)]

        else:
            idle "medievalicon-insensitve_idle"
            hover "medievalicon-insensitve_selected"
            selected_idle "medievalicon-insensitve_idle"
            selected_hover "medievalicon-insensitve_selected"
            action [Play("audio", "se/sounds/select3.ogg"), Return(5)]

        hovered Play("audio", "se/sounds/select.ogg")
        at panoButtons
        style "arcicon"

    imagebutton:
        focus_mask True
        auto "ui/lbd_left_arrow_btn_%s.png"
        action [Play("audio", "se/sounds/select3.ogg"), Return(1)]
        hovered Play("audio", "se/sounds/select.ogg")
        at lbd_left_arrow_trans

    imagebutton:
        focus_mask True
        auto "ui/lbd_right_arrow_btn_%s.png"
        action [Play("audio", "se/sounds/select3.ogg"), Return(2)]
        hovered Play("audio", "se/sounds/select.ogg")
        at lbd_right_arrow_trans

#--------------------Park Screen--------------------
screen jumpyscreen3():

    imagebutton:
        focus_mask True
        auto "ui/lorem_nav_%s.png"
        hovered Play("audio", "se/sounds/select.ogg")
        action [Play("audio", "se/sounds/select3.ogg"), Return(4)]
        at lorem_nav_trans

    #-----Return Home early-----
    imagebutton:
        focus_mask True
        auto "ui/home_nav_%s.png"
        hovered Play("audio", "se/sounds/select.ogg")
        action [Play("audio", "se/sounds/select3.ogg"), Return(6)]
        at home_nav_trans

    #-----Main Route option-----
    imagebutton:
        focus_mask True
        xpos 0.5
        ypos 0.5
        if lbd_route_park_unplayed:
            idle "parkicon-idle"
            hover "parkicon-selected"
            selected_idle "parkicon-idle"
            selected_hover "parkicon-selected"
            action [Play("audio", "se/sounds/select3.ogg"), Return(3)]

        else:
            idle "parkicon-insensitve_idle"
            hover "parkicon-insensitve_selected"
            selected_idle "parkicon-insensitve_idle"
            selected_hover "parkicon-insensitve_selected"
            #--------------------Demo Mode--------------------
            if lbd_demo_mode:
                action [Play("audio", "se/sounds/select3.ogg"), Return(3)]

            else:
                action [Play("audio", "se/sounds/select3.ogg"), Return(5)]

        hovered Play("audio", "se/sounds/select.ogg")
        at panoButtons
        style "arcicon"

    imagebutton:
        focus_mask True
        auto "ui/lbd_left_arrow_btn_%s.png"
        action [Play("audio", "se/sounds/select3.ogg"), Return(1)]
        hovered Play("audio", "se/sounds/select.ogg")
        at lbd_left_arrow_trans


label kimberland_early_ending:
    show lorem normal zorder 3 with dissolve
    $ renpy.pause(0.5)

    if (lbd_demo_mode) and (lbd_routes_played == 1):
        Lo "We just got here. You don't really want to leave, do you?"

    elif (lbd_demo_mode == False) and (lbd_routes_played == 0):
        Lo "We just got here. You don't really want to leave, do you?"

    else:
        Lo "Hey now, you don't really want to go home yet do you?"

    menu:
        "Yes.":
            pass

        "No.":
            $ renpy.pause(0.5)

            Lo "Good! There's still stuff to do here."
            Lo happy "Now let's go have some fun."
            hide lorem with dissolve
            jump lbd_route_picker

    $ renpy.pause(0.5)
    Lo relieved "Are you serious?"

    menu:
        "I'm sorry but yes.":
            $ renpy.pause(0.5)

            Lo think "Is everything ok?"
            c "I suppose I'm just.."
            menu:
            #    "Feeling sick.":
            #        $ renpy.pause(0.5)

            #        Lo normal "Oh ok then, I'm sorry you're feeling sick. You should have said so, it could have waited for another time."
            #        c "Yeah, thanks. Do you mind if we head back?"
            #        Lo "Not at all my friend, come on."


                "Tired.":
                    $ renpy.pause(0.5)
                    Lo think "Hmmmm, I see."
                    c "I guess I just had a bad night sleep."
                    Lo normal "I guess I shouldn't judge. You are in a whole new world with big scary dragons. {i}Rawr!{/i}"

                    menu:
                        "Ha ha, I guess so.":
                            $ renpy.pause(0.5)

                            c "It is kind of unnerving. At least everyone I met so far seems very friendly."
                            Lo normal "That's good. I can honestly say there are a few unfriendly ones out there but most back in town are nice plus no-one will cross Bryce."
                            c "Oh, is Bryce scary or something?"
                            Lo normal "Yes, he very much can be. If you cross him he'll either get mad at you with is very frightening or he'll challenge you to a drinking contest which never ends well for his opponent."

                            # if player done Bryces first date and drank beer
                            if renpy.python.store_dicts["store"].get("beer", False) == True:
                                c "As I know all too well."
                                Lo think "Oh you joined him on the night out. Did any memories survive?"
                                c "Not many. The last thing I remember clearly is him passed out at the bar."
                                Lo "Where did you stay that night?"
                                c "I woke at his little apartment, so I guess I stayed there."
                                Lo normal "Well alright then."

                            else:
                                c "I'll be sure to remember that. Thanks for the heads up."
                                Lo normal "You're welcome buddy."


                        "Oh no, not the big scary dragons!":
                            $ renpy.pause(0.5)

                            c "The scary blue dragon is so frightening!"
                            Lo normal "{i}Rawr Rawr{/i} I use my tickle attack!"
                            m "Lorem then jumps towards me trying to tickle my sides to the best of his abilities."
                            c "Oh nooo! I surrender Lorem, your tickle attack is too overpowering!"
                            Lo "I think you mean \"It's super effective!\""

                    show lorem normal with dissolve
                    Lo "Anyway, I guess we should get going then."

                    jump lbd_good_mood_ending

                "Don't really want to be here.":
                    $ renpy.pause(0.5)

                    c "Look Lorem, I just don't want to be here. I'd like to go back."
                    Lo sad "I guess this wasn't a good idea huh?"

                    menu:
                        "No, it wasn't.":
                            $ renpy.pause(0.5)

                            c "Lorem, what about this seemed like a good idea?"
                            Lo "I just thought it would be nice to get out of that town, do something fun for a day."
                            c "Seriously!"
                            Lo "Yeah... I don't quite understand what's wrong but I'm sorry."
                            c "Let's just leave."

                            if (lbd_dev_debug == False) and (lbd_demo_mode):
                                jump lbd_demo_bad_mood_ending
                            else:
                                jump lbd_bad_mood_ending

                        "It's a good idea.":
                            $ renpy.pause(0.5)

                            c "No Lorem, it's a nice idea but this is just all too much for me. There is so much here to get used to."
                            c "Things are bad back home however not only is everything here fine but it's all populated by mythical creatures."
                            c "Do you have any idea just how shocking that is?"
                            Lo relieved "Oh I see. I wasn't thinking about you and how all this must be for you."
                            c "It's OK Lorem, I appreciate you trying to make this a fun day."
                            Lo sad "Sorry again."
                            Lo normal "But for the record, you're a mythical creature to me and yet here we are on a day out."

                            menu:
                                "You mean a date.":
                                    show lorem shy with dissolve
                                    $ renpy.pause(1.5)
                                    Lo "Ye... ye.. yeah."

                                "Heh, I suppose you're right.":
                                    $ renpy.pause(0.5)

                                    c "It's all a matter of perspective."
                                    Lo happy "Exactly."

                            Lo normal "So I guess we should get going then."
                            jump lbd_good_mood_ending

                #Last chance to turn back
                "Hmff, do you really want to stay?":
                    $ renpy.pause(0.5)

                    Lo sad "Yes I do. I like this place and I rarely get to come here."
                    c "Alright then, let's stay a while longer."
                    Lo sad "I mean, I don't want you to feel you have to."
                    c "It's OK, let's just have some fun."
                    Lo normal "OK. Let's just make the most of it."
                    hide lorem with dissolve
                    jump lbd_route_picker


        "I'm leaving with or without you.":
            $ renpy.pause(0.5)

            Lo relieved "Hmffff."
            Lo sad "Fine. I can't really be alone here anyway, let's just go then."
            c "What do you mean by \"I can't really be alone here\"?"
            Lo "I just get a little scared when I'm in strange places on my own."
            c "That's pathetic."
            Lo sad "...{w=1.5}{nw}"
            Lo sad "You know what?"

            #menu:
            #    Db "What's the date like?"

            #    "V-Bad.":
            if (datestatus == -4) or (datestatus == -3):
                Lo sad "You're right."
                Lo "I hope you're happy. I genuinely hope you're happy now."
                Lo "You've just been horrible this whole time."
                Lo cry "Just... why?"
                Lo "You have no idea just how much I was looking forward to this, none at all!"
                Lo "Is it so much to ask for you but to not be a prick? Just for one damn day!"
                Lo "Do you get some sick thrill from imposing your horrid \"personality\" on to others?"
                Lo sad "Or do you just want to bring everyone else down to be as miserable as you?"
                c "Well... {w=0.7}{nw}"
                Lo "No. {w}No. {w}No! {w}NO!"
                Lo "You don't get to answer that with some snarky response."
                Lo "Now if you excuse me, I'm leaving. With or without you."
                jump lbd_bad_mood_ending

            elif (datestatus == -2) or (datestatus == -1):
                Lo "I don't have to take that from you."
                Lo "I was really looking forward to coming here and doing as much as possible."
                Lo "And you just want to go home."
                Lo "Well fine then!"
                Lo "Let's go."
                jump lbd_demo_bad_mood_ending

            elif datestatus in [0, 1, 2, 3, 4]:
                Lo "I'm not sure what's wrong."
                Lo "You haven't been bad but we didn't spend enough time together for me to really get to know you."
                Lo normal "Say what you will, but I don't get the impression that you're a bad or mean person."
                Lo "Let's since you seem to really want to."
                jump lbd_good_mood_ending

            else:
                Lo "Where is this attitude coming from?"
                Lo "You've been great this whole time but what's with this shift?"
                Lo think "Is something wrong?"
                c "No, I just want to leave now."
                if (lbd_demo_mode) and ((lbd_route_medevial_unplayed == False) or (lbd_route_arcade_unplayed == False)):
                    Lo normal "I'm not going to hold it against you."
                    Lo "At least we had some fun here today."
                    jump lbd_good_mood_ending

                else:
                    Lo normal "We didn't really do anything here today."
                    Lo "I'm going to assume something got to you and you want to get away."
                    Lo "I understand."
                    jump lbd_good_mood_ending

            #    "Bad.":
            #        Lo cry "You're right."
            #        jump lbd_bad_mood_ending

            #    "Meh.":
            #        Lo cry "You're right."

            #    "Good.":
            #        Lo cry "You're right."

            #I guess Lorem cries.



label kimberland_full_ending:
    #Good enough ending
    if datestatus >= 0:

        scene kimberland_evening with fade
        show lorem normal with dissolve
        $renpy.pause(0.8)

        Lo "We should be heading back. It's getting late and if we miss the next train we'll be camping here for the night."
        c "Did you have fun today?"
        Lo happy "I had a blast, thank you so much for coming here with me."
        Lo happy "You were a lot of fun to hang out with."
        c "Thanks, you too."
        Lo normal "Let's get a move on, if I remember right the next train is soon."

        jump lbd_good_mood_ending

    #bad ending
    else:
        scene kimberland_evening with fade
        show lorem sad with dissolve
        $renpy.pause(0.8)

        Lo "It's getting late, we should be heading back."
        c "Did you have fun today?"
        lo "I would have..."
        lo "Now there's a train to catch."

        jump lbd_demo_bad_mood_ending

    #--------------------Demo Mode--------------------
    if lbd_demo_mode:
        pass
