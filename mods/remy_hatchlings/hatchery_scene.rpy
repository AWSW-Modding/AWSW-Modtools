label hatchery_scene:

    if adine1unplayed == False:
        Ad think b "Given that you invited me in that day, why don't you come in - it's really quite gusty out there."
    else:
        Ad think b "Why don't you come in?"

    menu:
        "Why not?":
            Ad normal b "Sure thing, let's all go inside, shall we."
        "I'm quite busy at the moment...":
            Ad sad b "You don't have to. I know you're having a lot of problems with Reza - I thought you were sent away?"
            c "They changed their minds, so I suppose you'll be stuck with me for a little while longer."
            c "I should return to the police station now."
            return

    stop music fadeout 1.0
    scene black with fade
    $ renpy.pause (1.0)
    scene hatchery administration at Pan((260, 0), (0, 120), 0.7) with dissolvemed
    play music "mx/fireplace.ogg" fadein 2.0

    show adine normal b at right with easeinright
    show remy normal flip at left with easeinleft
    show vara normal flip at Position(xpos = 0.05) with easeinleft

    $ renpy.pause (0.5)

    Ad "This also happens to be the orphanage I volunteer at. All the children are outside right now apart from Vara here. She and Amely have been put under specialist care for what's happened to them. I'm looking after them both throughout the day."
    c "Would it be possible for us to see Amely again?"
    Ad giggle b "Sure thing! I'll just go and get her, she needs the attention, poor thing after all that's happened to her."

    $ renpy.pause (0.5)
    hide adine
    show adine normal b flip at right
    $ renpy.pause (0.5)
    hide adine with easeoutright
    $ renpy.pause (1.0)

    Ry sad flip "You know, this brings back memories of Amelia  and how we could have had our own child one day when we were ready for that."
    Ry "I mean we did try a couple of times but I guess we just weren't destined for that then. Ever."
    c "Well this is an orphanage if you feel like doing that at some point."
    Ry shy flip "I guess."
    Vr shocked flip "..."

    m "It wasn't long before Adine came back to the three of us, escorting a small dragon."
    show remy normal flip at left with dissolve
    show vara normal flip at Position(xpos = 0.05) with dissolve
    $ renpy.pause (1.0)
    show adine normal b at right with easeinright
    $ renpy.pause (0.5)
    show amely normal at Position(xpos = 0.95) with easeinright
    $ renpy.pause (1.0)

    Ad "Amely, this [player_name] and Remy. Say hello."
    Am "Hello"
    Ry smile flip "Hello Amely, how are you?"
    Am "Good!"

    $ renpy.pause (1.0)
    play sound "fx/varagrowl.ogg"
    Vr growl flip "..."
    $ renpy.pause (0.5)

    Ry "Hello you to, Vara."
    show vara normal flip at Position(xpos = 0.05) with dissolve

    Ry "How's Adine treating you both?"
    Am "Good. She is fun."
    Vr "..."
    Ad "I've been showing them my magazines and they say that the pair of them are both going to have a turn for the better soon."
    Ry "What?"
    Ad annoyed b "My magazines. They tell you what sort of thing you've got to look out for in the near future as well as your love interests."
    Ry look flip "I don't think they can do that. Magazines are sold to the general public, how would they be able to tell you as in an individual that?"
    Ad think b "Well I might have been given a hint as to who your potential new mate is from said magazines, I could tell you what to look out for."
    show vara shocked flip at Position(xpos = 0.05) with dissolve
    Ry look flip "I really don't think that's relevant at the moment - we're looking after the hatchlings for a little, or at least until [player_name] reports back to the police station."
    c "I should be doing that now, I'll see you all later."
    Ry "I should be going back as well, it's getting late."

    Ad "It's getting to Amely's bedtime now anyways, I'll help her in."
    hide amely with dissolve

    $ hatchery_done = True
    stop music fadeout 1.0

    return