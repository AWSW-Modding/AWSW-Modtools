label hatchery_extension:

    if renpy.python.store_dicts["store"].get("hatchery_done", False) == False:
        label hatchery_none:
        pass

    Ry "Remember when we went to the orphanage yesterday?"
    Ry "Well I've decided that I might do some good in the world for once and adopt one of the hatchlings"

    menu:
        "That's a good idea":
            pass
        "Maybe not":
            Ry sad "You're right. I'm not strong enough to look after a child. I'm not going to let them suffer because of my poor skills and inability to do simple tasks."
            c "See you then"
            $ remystatus = "neutral"
            label hatchery_denied:
            pass

    c "It's the right thing to do, adopting helps them have a better start."
    Ry smile "I've decided that it'll be between Amely and Vara, when we saw them they really struck something in me. The need to protect others from the darkness."
    c "Well why don't we go back to the hatchery? Being proactive about things is the best way of getting them done."

    stop music fadeout 1.0
    scene black with fade
    $ renpy.pause (1.0)
    show hatchery at Position(xpos=0.0, xanchor='left', ypos=1.0, yanchor='bottom') with ease

    play music "mx/choices.ogg" fadein 2.0
    show remy normal at right with dissolve

    Ry "Well we're here now."

    Am "Remy!"

    show amely normal flip at Position(xpos = -0.2)
    show amely normal flip at Position(xpos = 0.67) with move6

    Ry smile "Hey there Amely, how are you doing?"
    Am "Good! Adine let us play with her Ixomen Sphere and we had to make it really flat to stop it rolling away and then we had to find the on button. It was fun!"
    Ry normal "That sounds great."
    Am "We also did some colouring in and I drew you Remy. Here it is:"

    play sound "fx/scribblex.ogg"
    show black with dissolvemed
    $ renpy.pause (0.5)
    show drawing at left with dissolvemed
    $ renpy.pause (4.5)
    hide drawing with dissolvemed
    $ renpy.pause (0.5)
    hide black

    Ry smile "That's really good!"
    Am "Let's go and talk with Adine, come on!"
    Ry normal "I guess we should knock then."

    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    show adine normal b flip at left with dissolve

    if adinestatus in ["good", "impressed"]:
        Ad "Hey there [player_name], Remy"
    else:
        Ad "Hello again."

    Am "Remy's here!"
    Ry look "[player_name] and I are here about adopting one of the hatchlings under your care. Specifically either Vara or Amely."
    Ad think b flip "Well why don't you come in and we can sign some forms?"

    scene black with fade
    $ renpy.pause (1.0)
    scene hatchery administration at Pan((260, 0), (0, 120), 0.7) with dissolvemed

    show adine normal b at right with easeinright
    show remy normal flip at left with easeinleft
    show amely normal flip at Position(xpos = 0.05) with easeinleft

    Ad "I'll just fetch Vara for you then; even though she hasn't learned to talk yet, she's still really enthusiastic about you both."

    $ renpy.pause (0.5)
    hide adine
    show adine normal b flip at right
    $ renpy.pause (0.5)
    hide adine with easeoutright
    $ renpy.pause (1.0)

    show adine normal at Position(xpos = 1.4)
    show vara normal at Position(xpos = 0.95) with easeinright
    Vr "..."

    Ad "Vara! Come on, Remy and [player_name] are here!"
    Ry smile flip "I think she's already found us"

    show adine giggle b at right with easeinright

    Ad "Clever girl."

    show adine normal b at right with dissolve

    Ry normal flip "It's about time I do some good in my life."
    Ry "Maybe I'll adopt both of them; that would be most fair and best for them."
    Ad think b "Well officially we're only allowed to let you adopt one hatchling at a time to let them form a true bond with you but in your case, maybe I'll allow you to bend the rules slightly."
    Ry "No, it's fine, I understand why there are rules. I wouldn't want you in any trouble with your superiors either. That would just be cruel."
    Ad normal b "Well, if you're sure, who would you like to adopt?"

    menu:
        "Amely":
            $hatchling = "Amely"
            hide vara with dissolveslow

        "Vara":
            $hatchling = "Vara"
            hide amely with dissolveslow
            show vara normal at Position(xpos = 0.37) with move5
            $ renpy.pause (1.0)
            show vara normal flip at Position(xpos = 0.05) with dissolve


    Ry "I'll start again from the beginning, no distractions. It'll be you and I, by ourselves and we'll raise them to the best of our ability with love and care."

    if hatchling == "Vara":
        Vr "..."
    else:
        Am "Thanks"

    Ad think b "We're going to have to do some papers and then you'll be free to go with them."

    $ renpy.pause (1.0)
    play sound "fx/scribblex.ogg"
    $ renpy.pause (1.0)

    Ad normal b "Congratulations Remy, she's yours now! I'm sure you'll be a great parent."
    Ry look flip "Maybe this will fill my empty heart. And possibly do good to the child as well. I'm doing it for them, they need someone to help raise them, to help them through their childhood, to care for them as an individual."
    Ry "...As well as a reason to live once you're gone."
    c "Don't say that. You have lots of reasons. Your job, Adine, [hatchling]. People who love and care about you. And I might not be going back if all goes to plan."
    Ry angry flip "You shouldn't do that for me, your people need you more than I do. Your race is in need and you're their ambassador. It would be irresponsible of you not to return to them."
    c "We'll see. They shouldn't need me once I return the generator after this whole business with Reza is dealt with."

    if hatchling == "Vara":
        Vr "..."
        Ry normal flip "Come on Vara, we'll be going now."
    else:
        Am "When will we be going home?"
        Ry normal flip "We could go now. Come on [player_name], let's take Amely to her new home."

    scene black with fade
    $ renpy.pause (1.0)
    scene remyapt at Pan ((300, 80), (0,80), 5.0) with dissolveslow
    $ renpy.pause (3.3)
    show remy normal flip at left with easeinleft

    if hatchling == "Vara":
        show vara normal flip at Position(xpos = 0.05) with easeinleft
        Ry "How do you like your new home Vara?"
        Vr "..."
        hide vara with easeoutright
        Ry smile flip "Be careful"
    else:
        show amely normal flip at Position(xpos = 0.05) with easeinleft
        Ry "How do you like your new home Amely?"
        Am "I love it!"
        Am "I'm going to be an explorer and work out where everything is!"
        hide amely with easeoutright
        show remy smile flip at left with dissolve
        $ renpy.pause (1.0)
        Ry "Be careful!"
        Am "Don't worry about me"

    label hatchery_extension_end:
    pass

label hatchery_nokiss:
    if renpy.python.store_dicts["store"].get("hatchery_done", False) == False:
        return

    c "They'll be plenty of time for that later with [hatchling]."
    return


label hatchery_tie:
    if renpy.python.store_dicts["store"].get("hatchery_done", False) == False:
        return

    c "It'll make a good impression with [hatchling], you'll be the perfect role model for her."
    return

