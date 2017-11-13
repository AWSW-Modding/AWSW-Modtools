label lbd_start_arcade:
    if chapter4unplayed == False:
        $ save_name = "Ch. 4 - Lorem 1 - Arcade"

    elif chapter3unplayed == False:
        $ save_name = "Ch. 3 - Lorem 1 - Arcade"

    elif chapter2unplayed == False:
        $ save_name = "Ch. 2 - Lorem 1 - Arcade"

    else:
        $ save_name = "Ch. 1 - Lorem 1 - Arcade"

    if is_koth_mod():
        $ lbd_arcade_music = renpy.random.choice(("sound/msc/bolt.ogg", "music/One Six.opus"))

        play music lbd_arcade_music fadein 1.0

    else:
        play music onesix fadein 1.0

    scene arcade_bg with fade
    show lorem normal with dissolve
    $ renpy.pause(0.2)

    Lo "Well here we are."

    # if kothmod is installed and player dated koth
    if (is_koth_mod_db()) and (renpy.python.store_dicts["store"].get("KothorixDated", 0) == 1):
        c "This isn't all that dissimilar from the arcade back in town."
        Lo "No surprise there, they are part of the same chain."
        c "You have chain's of arcades?"
        Lo "Yeah, there is only one chain of arcades, that I know of. Apparently it's cheaper business-wise."
        c "Fair enough."
        Lo "So, is there any game here that catches your eye?"

    # if player has the kothmod installed
    elif is_koth_mod_db():
        c "Isn't there an arcade like this back in town?"
        Lo "Yes there is, this is my favourite of the two."
        c "Not sure why, from what I saw this one looks similar to the one back in town."
        Lo "They are actually very similar but that's because they are part of the same chain of arcade's."
        Lo "However despite their differences, I prefer this one because it's a little bigger."
        c "Strange how the larger of the two arcades is in the smaller town."
        Lo think "I never thought about that before."
        Lo normal "It's not actually that strange. The town maybe small but there isn't much else to do here."
        Lo "The entertainment industry might do well here."
        c "Perhaps."
        Lo "Right then, is there any game here that catches your eye?"

    #if player doesn't have the koth mod installed
    else:
        c "Yeah we are. It's been ages since I've been inside an arcade. There's none at home anymore."
        c "Do you go to an arcade often?"
        Lo happy "I go to an arcade when I can."
        Lo normal "I can often pop in to the one in town on my postal route."
        c "So postmen go to the arcade on their route. No wonder the post is always late."
        Lo "Hey now, I'm never that late. I keep an eye on the time."
        Lo "Most of the time."
        c "What games do you play when you're on your route?"
        Lo think "Sometimes I like to play DDR or as it's otherwise known; Dancing Dragon Revolution."
        c "You play what?"
        Lo normal "DDR; a song plays and you tap buttons with your feet in time with the song."
        c "Sounds familiar. I would like to see you play it sometime."
        Lo shy "Ahh, I only ever play it when no-one is around."
        Lo "I get a little... into it."
        c "Oh I see, you get your groove on."
        Lo "Y... Y... Yeah. It's a little embarrassing."
        c "Don't worry about it."
        Lo normal "Down to business. Which game would you like to play?"


    c "No idea, honestly."
    c "I'm not sure what kind of games I like anymore."

    show lorem normal at Position(xpos=0.7) with ease
    show kevin ramble flip at Position(xpos=0.2) with easeinleft

    Kv "Do I hear the gamers call to action?"

    if persistent.playedkevin:
        c "Hello Kevin."
        Kv normal flip "Hey there [player_name]."
        Lo think "You two know each other?"
        Kv "We met before."
        Lo normal "Well that saves on the introductions."

    else:
        c "Who are you?"
        Lo normal "His name is Kevin. He's been in town for a few days now."
        Kv normal flip "Yip, I'm handing out flyers for my college. It's a rather boring job but it's easy."
        Lo normal "This is [player_name]. They're one of the human ambassadors."
        Kv ramble flip "I noticed. It was a little hard to spot but my keen detective eye never let's me down."
        Lo think "Well I guess that was kinda obvious."
        c "You think?"
        Kv normal flip "Anyway, it's good to met you [player_name]."

    Lo normal "So what has you up here?"
    Kv "I assume you're here for the same reason."

    if lbd_route_medevial_unplayed:
        Kv "The med...{w=1.0}{nw}"
        Lo "LA LA LA LA!"
        Lo "Don't say it. I'm keeping it as a surprise for [player_name]."
        Kv "Seems legit."

    else:
        Kv "The medieval festival."
        Lo "Yeah that's why we're here too. We've already been there already."
        Kv "On a date I see."
        Lo shy "Uhhh, I wouldn't quite call it that."
        show lorem normal with dissolve

    Kv "So you're having trouble picking out a game?"
    Kv "Well then, perhaps I can make a suggestion."
    Kv "Do you two know of the game series \"Ronan's Adventures\"?"
    Lo "Yeah, there's a cabinet with one of those games in the arcade back at home."
    Kv "Well one of the older games of the series is back here not in the arcade back at home."
    Kv "I'm my opinion it's the best of the bunch."

    if (renpy.python.store_dicts["store"].get("remy1unplayed", True) == False):
        c "Oh I think I've heard of that game series. If I remember right Remy plays it at work."
        Lo think "Huh, I didn't think he would be into that game series."
        Kv brow flip "Come to think of it, I don't think I've ever seen him in the arcade."

    else:
        c "Would someone mind filling me in on what this game is?"
        Lo "Oh sorry."
        Lo "Ronan's Adventures is a game series where you play as a human named Ronan and you fight bad guys."
        c "That is the most general description of a game I've ever heard."
        Lo "Well it's very basic."

    Kv normal flip "Well anyway, the cabinet here hasn't been out in about 3 years."
    Lo think "Wait, do you mean the one that came in the bright orange cabinet with random green dragon on the side of it?"
    Kv ramble flip "That's the one!"
    Lo happy "Oh wow. I used to play that one with Ipsum whenever we could."
    #I know the common gag is for arcade machines to have 3 character names but the ones I used to play would have 5.
    Kv normal flip "Ease up, Lorem and Ipsum... Are you two Lo-Ip?"
    Lo "Oh yeah, that's the name we used to use on our scores."
    Lo normal "Wow man, that feels like forever ago at this stage."
    Kv brow flip "I remember it very well. I used to see that nickname having the high score on all of the games."
    Kv "I was forever trying to get a higher score."
    Lo happy "Ha Ha Ha, I remember an old monitor's screen having \"Lo-Ip\" burnt into it. Good times."
    Kv "Well as much of an \"honour\" it is to met one of the duo. I really must be off."
    Lo normal "Alright then. It was good to met you two."
    c "Good to see you Kevin. See you around."

    show kevin normal with dissolve
    hide kevin with easeoutleft

    show lorem normal at Position(xpos=0.5) with ease

    Lo "Well if you don't mind, I think you know which game I want to play."
    c "Sure then. Let's go for it."

    play sound lbd_coin
    $ renpy.pause(0.8)

    jump lbd_init_battle



# The game starts here.
label lbd_init_battle:
    #### Some variables that describes the game state.
    #[cookie_health, cookie_health_max, cookies_left, attack_mushrooms, has_items]
    $ items = [5, 10, 10, 3, True]
    #[max_hp, curr_hp, Alive, Att_boost, max_att, min_att, turn, just_revived]
    $ ronan = [50, 50, True, False, 7, 2, False, False]
    $ lorem = [30, 30, True, False, 5, 2, False, False]
    $ wolf = [100, 100, True, False, 10, 2, False]

    $ end_batte_status = "unknown"
    $ lbd_arcade_cheated = False

    $ persistent.showautoforwardbutton = False

    $ musicVol = renpy.game.preferences.get_volume("music")
    $ soundVol = renpy.game.preferences.get_volume("sfx")

    if musicVol != 0:
        $ renpy.game.preferences.set_volume("music", 0.8)

    if soundVol != 0:
        $ renpy.game.preferences.set_volume("sfx", 1.0)

    if is_koth_mod():
        $ lbd_battle_music = renpy.random.choice(("music/day 15.opus", "music/day 20.opus", "music/day 24.opus", "music/day 27.opus", "sound/msc/kothorix_theme.ogg"))
    else:
        $ lbd_battle_music = renpy.random.choice(("music/day 15.opus", "music/day 20.opus", "music/day 24.opus", "music/day 27.opus"))

    if not "lbd_num_time_failed" in renpy.python.store_dicts["store"]:
        $ lbd_num_time_failed = 0
        $ lbd_told_code = False

    ##cheating
    $ init_arc_listener()

    ## Rolling back over the cheat init will break the cheat system.
    $ renpy.block_rollback()

    play music lbd_battle_music fadein 1.0

    scene black
    with irisout

    #victory theme #39
    slwnarr "Ronan was one day summoned by the call of aid of a small village in need."

    ##Blocking it again because renpy is a buggy mess
    $ renpy.block_rollback()

    show koth_intro:
        xoffset -560

    slwnarr "An evil character named Draco has built a dam on the villages only river."
    slwnarr "Thankfully the village built a water reserve to survive short droughts, however reserves are quickly running out."
    slwnarr "Without water the villagers cannot grow crop or survive for long."

    hide koth_intro
    show buddy_intro:
        xoffset 530 yoffset -50

    slwnarr "A brave local villager volunteered to accompany Ronan in hunting down and defeating Draco."
    slwnarr "His bravery is fuelled by their loved one and newly born child."

    hide buddy_intro
    show ronan_intro:
        xoffset 320

    slwnarr "Will the brave and mighty Ronan be able to save the village?"
    slwnarr "Will his companion survive the grueling fight that is yet to come?"
    slwnarr "We will see."

    jump battle_1_loop

label battle_1_loop:
    scene lbd_battle_background
    show screen lbd_battle_stats_screen
    show kothsprite2
    show ronansprite3
    show aidithsprite2
    with Pixellate(2.0, 5)

    $ renpy.pause(1.2)
    w "Why do you approach my den?"
    r "You are taking water away from the villagers. I am here to make sure you return it."
    w "Ha Ha Ha, that village had it coming for a long time now."
    w "No-one will miss the villagers when they all die from drought."
    lb "You monster!"
    w "Oh I'm the monster am I?"
    lb "Yes! We need that water!"
    w "You know nothing of your crimes but enough talk, have at you!"
    r "You don't stand a chance, evil do'er!"
    lb "Yeah, we're uhhhhh gonna kick you in your bottom!"

    while (wolf[2]) and ((ronan[2]) or (lorem[2])):

        #If ronan was just revived
        if ronan[7]:
            show ronansprite3 at lbd_battle_respawn
            $ ronan[2] = True
            $ ronan[7] = False
            $ renpy.pause(1.2)
            r "I have returned."

        $ ronan[6] = True
        while (ronan[6]) and (ronan[2]):

            $ sel_action = renpy.call_screen("action_menu2")

            if (sel_action == 1):
                #reason with
                narr "Option not implemented"

            elif (sel_action == 2):
                #attack
                $ ronan[6] = False

                #random mega attack 5% chance of success
                if renpy.random.randint (1,100) in [1,65,43,87,2]:
                    narr "Mega awesome attack boost!!!"

                    if ronan[3]:
                        $ ronan[3] = False
                        $ player_damage = lbd_damage((ronan[5] + 1), ronan[4], 4)
                        $ wolf[1] = max((wolf[1] - player_damage), 0)
                        narr "Roman attacks Draco with mega mushroom and mega awesome attack power (damage dealt - [player_damage]HP)"

                    else:
                        $ player_damage = lbd_damage((ronan[5] + 1), ronan[4], 2)
                        $ wolf[1] = max((wolf[1] - player_damage), 0)
                        narr "Roman attacks Draco with mega awesome attack power (damage dealt - [player_damage]HP)"
                else:

                    if ronan[3]:
                        $ ronan[3] = False
                        $ player_damage = lbd_damage((ronan[5] + 1), ronan[4], 2)
                        $ wolf[1] = max((wolf[1] - player_damage), 0)
                        narr "Roman attacks Draco with mega mushroom power (damage dealt - [player_damage]HP)"

                    else:
                        $ player_damage = lbd_damage((ronan[5] + 1), ronan[4])
                        $ wolf[1] = max((wolf[1] - player_damage), 0)
                        narr "Roman attacks Draco (damage dealt - [player_damage]HP)"

            elif sel_action == 3:
                if items[4]:
                    $ item_used = renpy.call_screen("item_screen")

                    if item_used == 4:
                        #cookies
                        if ronan[1] == ronan[0]:
                            narr "You are already at MAX HP"

                        else:
                            $ real = max(renpy.random.randint(1, items[1]), items[0])
                            $ ronan[1] = min(ronan[1] + real, ronan[0])
                            $ items[2] = items[2] - 1
                            $ ronan[6] = False
                            if (items[2] == 0) and (items[3] == 0):
                                $ items[4] = False

                            narr "Ronan gains [real]HP"

                    elif item_used == 5:
                        #attack mushroom
                        $ ronan[3] = True
                        $ items[3] = items[3] - 1
                        $ ronan[6] = False
                        if (items[2] == 0) and (items[3] == 0):
                            $ items[4] = False

                        narr "Ronan's next attack will be boosted"

                #No items remaining
                else:
                    narr "You have no items remaining"

        call check_of_the_living

        #if buddy was just revied
        if lorem[7]:
            show aidithsprite2 at lbd_battle_respawn
            $ lorem[2] = True
            $ lorem[7] = False
            $ renpy.pause(1.2)
            lb "I'm back baby, let me at em!"

        $ lorem[6] = True
        while (lorem[6]) and (lorem[2]) and (wolf[2]):
            #if health remaining is less than or equal to 25% of total health, it bumps his chance of eating a cookie
            if (((lorem[1] % lorem[0]) * 100) <= 25) and (items[2] > 0):
                #4 in 11 chance he'll try to eat a cookie; 36% chance
                $ lorem_attack = renpy.random.randint(1, 11)

            else:
                #1 in 8 chnace he'll try to eat the cookie; 12.5% chance
                $ lorem_attack = renpy.random.randint(1, 8)

            if (lorem_attack in [1,3,4,5,6,7,8]):
                #attack
                $ lorem[6] = False

                #random mega attack 5% chance of success
                if renpy.random.randint (1,100) in [1,65,43,87,2]:
                    narr "Mega awesome attack boost!!!"

                    $ lorem_damage = lbd_damage((lorem[5] + 1), lorem[4], 2)
                    $ wolf[1] = max((wolf[1] - lorem_damage), 0)
                    narr "Little bud attacks Draco with mega awesome attack power (damage dealt - [lorem_damage]HP)"

                else:
                    $ lorem_damage = lbd_damage((lorem[5]), lorem[4])
                    $ wolf[1] = max((wolf[1] - lorem_damage), 0)
                    narr "Little bud attacks Draco (damage dealt - [lorem_damage]HP)"

            elif ((lorem_attack in [2,9,10,11])) and (items[2] > 0):
                #cookies
                if lorem[1] == lorem[0]:
                    pass
                    #narr "You are already at MAX HP"
                    #Lo "Uhhh, I didn't notice that."

                else:
                    $ real = max(renpy.random.randint(1, items[1]), items[0])
                    $ lorem[1] = min(lorem[1] + real, lorem[0])
                    $ items[2] = items[2] - 1
                    $ lorem[6] = False

                    if (items[2] == 0) and (items[3] == 0):
                        $ items[4] = False

                    narr "{i}*munch* *munch*{/i}"
                    narr "Little buddy eats a cookie and gains [real]HP"

        call check_of_the_living

        if wolf[2]:
            $ living_targets = []

            if ronan[2]:
                $ living_targets.append(1)
            if lorem[2]:
                $ living_targets.append(2)

            $ wolf_damage = lbd_damage(wolf[5], wolf[4])

            if (renpy.random.choice(living_targets) == 1):
                $ ronan[1] = max((ronan[1] - wolf_damage), 0)
                narr "Draco {i}*chomps*{/i} down on Ronan (damage dealt - [wolf_damage]HP)"
            else:
                $ lorem[1] = max((lorem[1] - wolf_damage), 0)
                narr "Draco {i}*chomps*{/i} down on little bud (damage dealt - [wolf_damage]HP)"

        call check_of_the_living

    #End of the battle
    hide screen lbd_battle_stats_screen
    jump lbd_battle_ending

label lbd_battle_ending:
    $ remove_arc_listener()

    #if everyone is dead
    if (wolf[2] == False) and (ronan[2] == False) and (lorem[2] == False):
        narr "You all suck."
        $ end_batte_status = 5


    if not wolf[2]:
        #if only buddy lives
        if (ronan[2] == False) and (lorem[2] == True):
            stop music fadeout 1.0
            w "Arg! I have been bested!"
            w "At least I took that bastard out with me."

            hide kothsprite2 with Dissolve(1.5)

            lb "And stay dead!"
            lb "..."
            lb "Well now what do I do?"

            scene black with Fade(1.0, 0.5, 0.5)
            play music battle_one_lives fadein 2.0
            scene battle_ending_scene with fade
            $ renpy.pause(8.0)

            slnarr "The lowly villager may have been triumphant."
            slnarr "However the mighty Ronan has been vanquished."
            slnarr "Who will rise to replace our hero?"

            $ end_batte_status = 3

        #If only ronan lives
        elif (ronan[2] == True) and (lorem[2] == False):
            stop music fadeout 1.0
            w "Arg! I have been bested!"
            r "Evil never pays Draco and this is your punishment!"
            w "Heh heh heh, be sure to bring your friend back with you."
            w "I only wish I could see his wife's face..."

            hide kothsprite2 with Dissolve(1.5)

            r "Goodbye."

            scene black with Fade(1.0, 0.5, 0.5)
            play music battle_one_lives fadein 2.0
            scene battle_ending_scene with fade
            $ renpy.pause(8.0)

            slnarr "The mighty Ronan has once again vanquished his foes"
            slnarr "The villagers rejoice as the river returns to water their crop."
            slnarr "Celebration soon ends once the sight of a single figure emerges over the horizon."

            $ end_batte_status = 2

        # if both ronan and buddy live
        elif (ronan[2] == True) and (lorem[2] == True):
            stop music fadeout 1.0
            w "Arg! I have been bested!"
            r "Evil never pays Draco and this is your punishment!"
            w "Evil? Look no further than your precious village."
            r "What do you mean?"
            w "It matters not. Not anymore."

            hide kothsprite2 with Dissolve(1.5)

            lb "Come on Ronan. My village still needs it's water back."
            r "What was Draco referring to?"
            lb "I don't know."

            scene black with Fade(1.0, 0.5, 0.5)
            play music battle_both_live fadein 2.0
            scene battle_ending_scene with fade
            $ renpy.pause(8.0)

            slnarr "The sun rises to welcome in a new day with one less evildoer in the world."
            slnarr "The mighty Ronan and his companion have fought valiantly and rose up victorious."
            slnarr "Questioning his actions Ronan wonders if slaying Draco was truly just."
            slnarr "Finding solace in his companion surviving the encounter, Ronan restores water to the village."
            slnarr "The villagers celebrate the return of Ronan and the water, however Ronan does not stay to rejoice."

            $ end_batte_status = 1

        #if saved wolf with reason
            #Ronan the nobal hero once again demonstrated his steely resolve and mercy.
            #an enemy turned friend is friend to the end

    #if wolf killed both charactors
    else:
        stop music fadeout 1.0

        hide ronansprite3
        hide aidithsprite2
        with Dissolve(1.5)

        w "Shame. However at least now I will be unimpeded."

        scene black with Fade(1.0, 0.5, 0.5)

        $ renpy.pause(0.8)
        slwnarr "A moment of silence."
        slwnarr "The greatest fighter this world hath ever known, lays in the depths of his mortal slumber."
        slwnarr "May he continue to fight where ever he may be."

        $ end_batte_status = 4


    $ persistent.showautoforwardbutton = True

    if musicVol != 0:
        $ renpy.game.preferences.set_volume("music", musicVol)

    if soundVol != 0:
        $ renpy.game.preferences.set_volume("sfx", soundVol)

    jump lbd_end_arcade



label lbd_end_arcade:
    if is_koth_mod_db():
        play music lbd_arcade_music fadein 1.0

    else:
        play music onesix fadein 1.0

    scene arcade_bg with fade
    $ renpy.pause(0.05)

    #--------------------Dev debug--------------------
    if lbd_dev_debug:
        menu:
            Db "Which ending did you get?"

            "Ronan and buddy live":
                $ end_batte_status = 1

            "Only Ronan lived":
                $ end_batte_status = 2

            "Only littleBuddy lived":
                $ end_batte_status = 3

            "You both died":
                $ end_batte_status = 4

            "Everyone died":
                $ end_batte_status = 5

    #which game ending the player got

    #ronan and buddy live = 1
    if end_batte_status == 1:
        show lorem normal with dissolve
        $ renpy.pause(0.2)

        Lo happy "WE WON."

        if lbd_arcade_cheated:
            Lo "We had to cheat to get there but we still won."
            c "Yeah, but who could resist a small bit of cheating?"
            Lo normal "No-one, that's who!"

            if lbd_told_code == False:
                Lo think "Hmm, I just realised something."
                c "What?"
                Lo "I never told you the cheat code, how do you know it?"
                c "Will \"I guessed\" be a good enough answer?"
                Lo normal "Is it the only answer I'll get?"
                c "Yes."
                Lo think "Then I suppose I'll have to accept that you just guessed such a code."

        else:
            Lo "We didn't even have to cheat to win either."

            menu:
                "[[Complement.]":
                    $ renpy.pause(0.5)

                    c "We're MLG pro Lorem, we don't need to cheat!"
                    Lo think "We're what?"
                    c "Nevermind. {s}Three sixty no-scope.{/s}"

                "[[Rude.]":
                    $ renpy.pause(0.5)

                    c "What kind of gamer needs to cheat to win?"
                    Lo think "Hmm? I'm not sure."
                    c "A bad one."
                    Lo normal "Most cheaters would be insulted but I have to agree."

        show lorem normal with dissolve

        Lo "I'm happy with the outcome but just in-case you're not, would you like to have another go at the game?"

        menu:
            "Yes.":
                $ renpy.pause(0.5)

                if lbd_arcade_cheated:
                    Lo "Well we cheated last time, how about this time we try to win without cheating?"
                    c "Does it make any difference?"
                    Lo "None at all, I'm just trying to give us a challenge."
                    c "I'll think about it."

                    play sound lbd_coin
                    $ renpy.pause(0.8)
                    jump lbd_init_battle

                if lbd_told_code == False:
                    Lo "I know we don't need it but it might be a fun thing to try out this time."
                    c "What would be fun?"
                    Lo "Well I know of a trick that would \"help\" us beat the game."
                    c "Spam the attack button?"
                    Lo think "No, but that sometimes does work."
                    Lo normal "I'm talking about {i}cheating{/i}. Like I said, we don't need it but it might be fun."

                    menu:
                        "Tell me.":
                            $ renpy.pause(0.5)
                            $ lbd_told_code = True

                            Lo normal "You can enter a cheat code into the game to get a few options to \"help\" you along."
                            Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                            Lo normal "Just enter it when playing the game."
                            c "How do you know this anyway?"
                            Lo shy "Ipsum has a cheat book and uhhhh I use it a lot."
                            c "Cheeky bugger."
                            Lo normal "Oi, I recent that."
                            c "Yet you don't disagree. I see."
                            show lorem think with dissolve
                            $ renpy.pause(0.5)
                            Lo normal "I suppose not."

                        "Don't tell me.":
                            $ renpy.pause(0.5)

                            Lo "Well OK, your call."

                    play sound lbd_coin
                    $ renpy.pause(0.8)
                    jump lbd_init_battle


                c "Might as well have another go at it."
                Lo "Not that it would accomplish all that much."
                Lo "But let's have some fun anyway."

                play sound lbd_coin
                $ renpy.pause(0.8)
                jump lbd_init_battle

            "No.":
                $ renpy.pause(0.5)

                c "I'm happy with the outcome aswell and I have a feeling that trying to get another ending won't make any difference."
                Lo "Well it was nice to be here again. I'm glad we had some fun."


    #only ronan lives = 2
    elif end_batte_status == 2:
        show lorem normal with dissolve
        $ renpy.pause(0.2)

        Lo "That didn't go too badly."
        Lo "I kinda wanted to survive the fight though."
        c "Hey now, you didn't do too badly."
        Lo "Would you like to have another go at the game? This time we can try to get both our characters to survive."

        #Play again?
        menu:
            "Yes.":
                $ renpy.pause(0.5)

                if (lbd_told_code == False):
                    Lo think "You know there is something I can tell you about the game."
                    c "What do you mean Lorem?"
                    Lo normal "It's something that could \"help\" your character survive the fight."
                    c "Oh I see, you mean some {i}cheating{/i} help."
                    Lo "Yes I do, would you like to hear it?"

                    menu:
                        "Yes.":
                            $ renpy.pause(0.5)
                            $ lbd_told_code = True

                            Lo normal "You can enter a cheat code into the game to get a few options to \"help\" you along."
                            Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                            Lo normal "Just enter it when playing the game."
                            c "How do you know this anyway?"
                            Lo shy "Ipsum has a cheat book and uhhhh I use it a lot."
                            c "Cheeky bugger."
                            Lo normal "Oi, I recent that."
                            c "Yet you don't disagree. I see."
                            show lorem think with dissolve
                            $ renpy.pause(0.5)
                            Lo normal "I suppose not."

                        "No.":
                            $ renpy.pause(0.5)

                            Lo normal "Your choice. Let's have another go at this then."

                else:
                    $ renpy.pause(0.5)

                    Lo think "Hmmm."
                    Lo normal "Just to remind you of an option for some \"help\"."
                    Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                    c "Thanks Lorem."

                play sound lbd_coin
                $ renpy.pause(0.8)
                jump lbd_init_battle

            "No.":
                $ renpy.pause(0.5)

                Lo normal "Well alright then, no worries."
                c "Well at least we had some fun."
                Lo happy "That we did. Now let's head back outside."


    #only buddy lives = 3
    elif end_batte_status == 3:
        show lorem normal with dissolve
        $ renpy.pause(0.2)

        Lo "That's not too bad."
        Lo "Shame about your character dying."
        Lo happy "I'm just happy I actually lived for once."
        c "What do you mean for once?"
        Lo normal "Well whenever myself and Ipsum play this game, he always lives and I always die."
        Lo happy "But this time I actually made it to the end of the game and won!"

        show lorem normal with dissolve

        $ renpy.pause(0.5)

        c "Shame my character died on me but at least we still beat the game."
        Lo "Yeah, it's always nice to beat a game."
        Lo "Would you like to have another go at the game? This time we can try to get both our characters to survive."

        menu:
            "Yes.":
                $ renpy.pause(0.5)

                if (lbd_told_code == False):
                    Lo think "You know there is something I can tell you about the game."
                    c "What do you mean Lorem?"
                    Lo normal "It's something that could \"help\" your character survive the fight."
                    c "Oh I see, you mean some {i}cheating{/i} help."
                    Lo "Yes I do, would you like to hear it?"

                    menu:
                        "Yes.":
                            $ renpy.pause(0.5)
                            $ lbd_told_code = True

                            Lo normal "You can enter a cheat code into the game to get a few options to \"help\" you along."
                            Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                            Lo normal "Just enter it when playing the game."
                            c "How do you know this anyway?"
                            Lo shy "Ipsum has a cheat book and uhhhh I use it a lot."
                            c "Cheeky bugger."
                            Lo normal "Oi, I recent that."
                            c "Yet you don't disagree. I see."
                            show lorem think with dissolve
                            $ renpy.pause(0.5)
                            Lo normal "I suppose not."

                        "No.":
                            $ renpy.pause(0.5)

                            Lo normal "Your choice. Let's have another go at this then."

                else:
                    $ renpy.pause(0.5)

                    Lo think "Hmmm."
                    Lo normal "Just to remind you of an option for some \"help\"."
                    Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                    c "Thanks Lorem."

                play sound lbd_coin
                $ renpy.pause(0.8)
                jump lbd_init_battle

            "No.":
                $ renpy.pause(0.5)

                Lo normal "Well alright then, no worries."
                c "Well at least we had some fun."
                Lo happy "That we did. Now let's head back outside."


    #wolf wins = 4
    elif end_batte_status == 4:
        show lorem sad with dissolve
        $ renpy.pause(0.2)

        Lo sad "Awww. We lost."

        $ lbd_num_time_failed = lbd_num_time_failed + 1

        Lo "Would you like to try again?"

        menu:
            "Yes":
                $ renpy.pause(0.5)

                if (lbd_num_time_failed > 1) and (lbd_told_code == False):
                    Lo relieved "We seem to be having some trouble. Would you like some help?"
                    Lo normal "Some {i}cheating{/i} help?"
                    menu:
                        "Yes":
                            $ renpy.pause(0.5)
                            $ lbd_told_code = True

                            Lo normal "You can enter a cheat code into the game to get a few options to \"help\" you along."
                            Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                            Lo normal "Just enter it when playing the game."
                            c "How do you know this anyway?"
                            Lo shy "Ipsum has a cheat book and uhhhh I use it a lot."
                            c "Cheeky bugger."
                            Lo normal "Oi, I recent that."
                            c "Yet you don't disagree. I see."
                            show lorem think with dissolve
                            $ renpy.pause(0.5)
                            Lo normal "I suppose not."


                        "No":
                            $ renpy.pause(0.5)

                            Lo normal "Your choice."
                            Lo normal "Let's get him this time, that little thing can't beat us. We're the good guys!"
                            c "You're a little too invested in this."

                elif (lbd_num_time_failed > 1) and (lbd_told_code == True):
                    $ renpy.pause(0.5)

                    Lo think "Did you forget the cheat code I gave you?"
                    Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"


                else:
                    $ renpy.pause(0.5)

                    Lo normal "Well alright, let's hope it goes better this time."

                play sound lbd_coin
                $ renpy.pause(0.8)
                jump lbd_init_battle

            "No":
                $ renpy.pause(0.5)

                Lo sad "Awww well."
                Lo normal "At least we had some fun, let's be off."


    #everyone dies = 5
    #This option isn't even possible, yes here it is
    elif end_batte_status == 5:
        show lorem sad with dissolve
        $ renpy.pause(0.2)

        Lo sad "Awww. We lost."

        $ lbd_num_time_failed = lbd_num_time_failed + 1

        Lo "Would you like to try again?"

        menu:
            "Yes":
                $ renpy.pause(0.5)

                if (lbd_num_time_failed > 1) and (lbd_told_code == False):
                    Lo relieved "We seem to be having some trouble. Would you like some help?"
                    Lo normal "Some {i}cheating{/i} help?"
                    menu:
                        "Yes":
                            $ renpy.pause(0.5)
                            $ lbd_told_code = True

                            Lo normal "You can enter a cheat code into the game to get a few options to \"help\" you along."
                            Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"
                            Lo normal "Just enter it when playing the game."
                            c "How do you know this anyway?"
                            Lo shy "Ipsum has a cheat book and uhhhh I use it a lot."
                            c "Cheeky bugger."
                            Lo normal "Oi, I recent that."
                            c "Yet you don't disagree. I see."
                            show lorem think with dissolve
                            $ renpy.pause(0.5)
                            Lo normal "I suppose not."


                        "No":
                            $ renpy.pause(0.5)

                            Lo normal "Your choice."
                            Lo normal "Let's get him this time, that little thing can't beat us. We're the good guys!"
                            c "You're a little too invested in this."

                elif (lbd_num_time_failed > 1) and (lbd_told_code == True):

                    Lo think "Did you forget the cheat code I gave you?"
                    Lo normal "The code is: {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_up_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_down_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_left_arrow.png}  {image=arch/code/lbd_right_arrow.png}  {image=arch/code/lbd_b_letter.png}  {image=arch/code/lbd_a_letter.png}"


                else:
                    $ renpy.pause(0.5)

                    Lo normal "Well alright, let's hope it goes better this time."

                jump lbd_init_battle

            "No":
                $ renpy.pause(0.5)

                Lo sad "Awww well."
                Lo normal "At least we had some fun, let's be off."


    scene black with Fade(1.2, 0.5, 0.5)
    stop music fadeout 1.5

    $ lbd_route_arcade_unplayed = False

    jump lbd_route_picking




label check_of_the_living:
    if (ronan[2]) and (ronan[1] == 0):
        $ ronan[2] = False
        r "Remember me how I lived"
        hide ronansprite3 with dissolvegame

    if (lorem[2]) and (lorem[1] == 0):
        $ lorem[2] = False
        lb "I'm dead I guess"
        hide aidithsprite2 with dissolvegame

    if (wolf[2]) and (wolf[1] == 0):
        $ wolf[2] = False

    return


#####CHEATS######
label konami_code:

    $ player_cheating = True
    while player_cheating:

        $ cheat_action = renpy.call_screen("cheating_screen")

        #[max_hp, curr_hp, Alive, Att_boost, max_att, min_att, turn]
        #[cookie_health, cookie_health_max, cookies_left, attack_mushrooms, has_items]

        if cheat_action == 1:
            narr "Cookies restocked."
            $ items[2] = 10
            $ lbd_arcade_cheated = True

        elif cheat_action == 2:
            narr "Mushrooms restocked."
            $ items[3] = 3
            $ lbd_arcade_cheated = True

        elif cheat_action == 3:
            #if ronan dead
            if not ronan[2]:
                $ ronan[7] = True

            #if buddy is dead
            if not lorem[2]:
                $ lorem[7] = True

            narr "Health restored."
            $ ronan[1] = ronan[0]
            $ lorem[1] = lorem[0]
            $ lbd_arcade_cheated = True

        else:
            if lbd_arcade_cheated == False:
                narr "Alright, don't cheat then."

            else:
                narr "Come back anytime."

            $ player_cheating = False



    return

screen cheating_screen:
    modal True

    frame:
        xminimum 1175
        yminimum 450
        xalign 0.5
        yalign 0.55
        background "arch/textboxcheatmenu.png"
        hover_background "arch/textboxcheatmenu.png"
        selected_background "arch/textboxcheatmenu.png"

        vbox:
            xcenter 0.5
            ycenter 0.5

            style_group "item_menu"

            text "{size=+5}{u}Cheaters Menu{/u}{/size}"

            null height 30

            textbutton _("Restock Cookies {size=-8}{u}{i}[items[2]] remaining{/i}{/u}{/size}"):
                if (items[2] < 10):
                    action Return (1)
                else:
                    action None


            null height 20

            textbutton _("Restock Mushrooms {size=-8}{u}{i}[items[3]] remaining{/i}{/u}{/size}"):
                if (items[3] < 3):
                    action Return (2)
                else:
                    action None
            null height 20

            textbutton _("Restore Health {size=-8}{u}{i}Ronan: [ronan[1]]/Little buddy: [lorem[1]]{/i}{/u}{/size}"):
                if (ronan[0] == ronan[1]) and (lorem[0] == lorem[1]):
                    action None
                else:
                    action Return (3)

            null height 20

            textbutton _("Return") action Return (6)
