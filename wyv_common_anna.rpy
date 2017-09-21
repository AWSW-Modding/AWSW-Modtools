label wyv_common_anna:

    image creditswyv = "crt/creditswyv.png"
    image town4x = "nbg/town4x.jpg"
    define Mg = Character("Mod Manager", color="#919191", image="")
   # (Lisa Purple-red name tag)
    #I don't need to test if the player already got an ending, those variables and achieves are taken care of after the credits

    #If's as set by Wyvernosis
    #(Adine needs to survive, needs to be on a good status with you, and you need to have the romance with Anna.)

    #annaromance
        #You can only be on good status with anna if you sleep with her and play all 4 scenes
            # $ annastatus = "good"
            # $ annascenesfinished = 4

    #Adine alive
            # $ adinedead = False

    #Adine stats
            # if adinestatus == "abandoned":

            #or
            #adinestatus = "neutral" and adinescenesfinished = 3
            #If the player uses skip they cannot get adinestatus = good in chanp3 adine scene


    #time for the fun if's
    if annastatus == "good":
        if annascenesfinished == 4:
            if adinedead == False:
                if adinescenesfinished == 3:
                    define Am = Character("Amely", color="#D6968C", image="amely")
                    jump wyv_betterannaending

                else:
                    jump wyv_anna_stockcredits             
            else:
                jump wyv_anna_stockcredits
        else:
            jump wyv_anna_stockcredits
    else:
        jump wyv_anna_stockcredits


#large italic font: Times new roman size 50
#sub font: Lato light (not quite right but close enough)
#The beginning of the games Credits
label wyv_anna_customcredits:
    stop music fadeout (2.0)

    $ renpy.pause (1.2)

    $ _game_menu_screen = None

    stop sound fadeout 2.0

    play sound "mx/fragilemind.ogg" fadein 0.5

    show cganna at Pan ((0, 150), (900,0), 20.0)
    show creditswyv at right
    with dissolvemed

    $ renpy.pause (8.0)

    scene black with dissolvemed

    show rezathroatslit at Pan ((500, 326), (1280,0), 20.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (8.0)

    show black2 at left with dissolvemed

    show credits2 at left with dissolvemed

    $ renpy.pause (8.0)

    return


label wyv_anna_stockcredits:
    scene black with dissolveslow
    $ renpy.pause (2.0)

    nvl clear
    window show

    n "A few days later, she passed away quietly in her sleep."
    $ annadead = True
    n "The council held a funeral in her honor, which I didn't attend."
    n "Now that I had been with Anna until the end, I had a decision to make."
    n "I could either stay here, accept this outcome and all its consequences, or, by using the portal and Izumi's coordinates, travel back in time and return to the day of my arrival in this world."
    n "This way, I could get the chance to try again."
    n "No doubt, it would be a risk to relive this rollercoaster of emotions. After all, I would have to go through all the events and their dangers again, but maybe it would be worth it..."
    stop music fadeout 2.0
    window hide

    $ renpy.pause (3.0)
    $ _game_menu_screen = None
    stop sound fadeout 2.0

    #Stock credits
    play sound "mx/fragilemind.ogg" fadein 0.5

    show rezathroatslit at Pan ((500, 326), (1280,0), 20.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (8.0)

    show black2 at left with dissolvemed
    show credits2 at left with dissolvemed

    $ renpy.pause (8.0)

    return