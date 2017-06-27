label wyv_betterannaending:

    stop music fadeout 2.0
    scene black with dissolveslow

    $ renpy.pause (1.0)

    nvl clear
    window show
    play music "mx/clocks.ogg"

    n "Seeing her in the hospital broke my heart everyday. Just looking at her, she looked like a ghost of herself."
    n "I couldn’t live with myself if she died and leaving to go back would just add attempts."
    n "All I wanted her to do was live a peaceful life, nothing more, but then again, I wanted to save humanity."
    n "The choice I have to make, which will it be? Do I try and cure her cancer, or do I just step through the portal and forget she ever existed? After all, I have no idea if there’s a way to save her..."
    n "Or... maybe there is a way, but it would cost literally everything."
    n "I think she’s worth more than everything..."

    window hide

    s "What happened to Anna after [player_name]’s decision?"
    s "Let’s have Anna explain."

    $ renpy.pause (0.8)
    show testingroom at Pan ((0, 233), (0, 233), 0.0) with dissolve
    $ renpy.pause (1.0)

    nvl clear
    window show

    n "I woke up in my bed, but this time without tubes attached to my nose."
    n "I forget how I even fell asleep. How long was I out?"
    n "My eyes finally adjusted to find yellow figure sitting on a chair looking at a magazine."

    window hide

    show adine normal b flip flip at left with dissolve

    An "Is that?"
    Ad normal b flip "Oh good, you’re awake!"

    show anna sad at right with dissolve

    An sad "Thanks for noticing."
    Ad "I don’t think we’ve properly met, my name is Adine."
    An "I recognize you. You were the girl at the restaurant that me and [player_name] went to..."
    An "Wait a minute..."
    An "Where is [player_name]?"
    Ad disappoint b flip "I don’t think I should tell you now..."
    An rage "TELL ME!!!" with vpunch

    m "She looked to the side and sighed nodding."

    stop music fadeout (1.0)
    $ renpy.pause (0.8)
    play music "mx/fragments.ogg" fadein (1.0)
    $ renpy.pause (0.8)

    show anna sad with dissolve
    Ad disappoint b flip "[player_name] came to the hospital about a week ago."
    Ad "[player_name] mentioned how our species and humans are alike, like 99 percent alike."
    An cry "Oh no..."
    Ad "There was begging and begging until they finally agreed."
    Ad sad b flip "[player_name]’s body was sacrificed for you. All of it."
    Ad disappoint b flip "I wish there was something left of it, but there’s only a tombstone ready for honor."
    An despair "No, no, NO!"
    An "THIS CAN’T BE HAPPENING!!!" with vpunch
    Ad sad b flip "I’m sorry Anna..."

    show anna cry with dissolve 

    m "At that moment, my world felt like it was falling all around me."
    m "She came over and wrapped her wings around me as I soaked my blanket in tears."
    m "I was about to push her off, but eventually I just wrapped my arms around her neck crying on her shoulders."

    Ad disappoint b flip "[player_name] was my friend too."
    An despair "Yeah, but I was in love!"
    An "I don’t know if [player_name] told you, but we were more than just friends."
    An "I didn’t have a single friend to begin with, but [player_name] was willing to be there for me."
    An "We even shared the same bed together, and not just by sleeping might I mind you."
    Ad sad b flip "Then this must be harder for you than it is for me!"
    An cry "Just one more time I would’ve wanted [player_name] to have my body, one more time..."
    An "But now, I guess there’s no one at all who would be willing to be there for me..."
    An "No one willing to be my friend..."
    An despair "WHY DID [player_name] EVEN LET ME SURVIVE IF I’M JUST GONNA BE LONELY AGAIN???" with vpunch 
    Ad sad b flip "Anna?"
    An cry "What is it?"
    An sad "You’re gonna say “we could be friends”, aren’t you?"
    Ad "..."
    Ad "It’s the least I can do..."
    Ad "Leaving this hospital while having you distraught is the worse thing I could ever do..."
    An "It’s something I would do..."
    Ad annoyed b flip "But I’m not an asshole, now am I?"
    An "I hate people, and people hate me."
    Ad disappoint b flip "I don’t hate you..."
    An "..."
    Ad "Besides, if we become friends, we could fill in the void [player_name] left in us."
    An "..."
    An "You know what..."
    An "That would be the best option..."
    Ad think b flip "We’ll have to have some time of making things up, so I’ll invite you to my house in a few days."
    Ad "Right now though, I think you should take time to get on your feet."
    An "Alright."
    Ad disappoint b flip "Bye now..."
    An "Bye..."
    
    show adine disappoint b at left with dissolve
    $ renpy.pause (0.4)
    show adine disappoint b flip at left with dissolve

    Ad "And one last thing..."
    Ad "Don’t think too much about it."
    An "I don’t think that’s possible."
    $ renpy.pause(3.0)
    Ad "Just forget I said anything..."
    An "Okay..."

    scene black with fade
    $renpy.pause (0.5)
    nvl clear
    window show

    n "After a few weeks, I was finally back on my feet. It was good to be cancer free, but there was still that piece missing from me."
    n "As much as I wanted to, I couldn’t bring myself to forget. I’d have dreams of me being in a bed alone in the cosmos until [player_name] would come up and cuddle me."
    n "My dream would end too soon before we kissed or started to make love."
    n "Soon I would be visiting Adine. I have no idea what to expect."

    window hide

    stop music fadeout (1.0)
    $renpy.pause (0.5)
    play music "mx/warming.ogg" fadein (1.0)
    scene town4 at Pan((0, 0), (0, 0), 0.0) with fade
    $renpy.pause (0.5)

    show anna sad with dissolve
    An sad "Here we are..."
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.5)
    Ad "Coming!"

    show anna sad at right with ease
    show adine normal b flip at left with dissolve

    Ad normal b flip "Oh, it’s you!"
    An "Hey..."
    Ad think b flip "Still thinking about...?"
    An "Yeah..."
    An "Who’s that?"
    hide anna
    hide adine
    show anna sad at Position (xpos = 0.80)
    show adine normal b flip at Position (xpos = 0.20)
    show amely normal flip at Position (xpos = 0.40) 
    with dissolve

    Ad normal b flip "Who, this? This is Amely!"

    m "My heart froze."
    m "I knew who Amely was too vividly."

    An "H-hi..."
    Ad think b flip "Is something the matter?"
    An "N-nothing..."
    Ad "Okay..."
    Ad normal b flip "I hope you don’t mind, but I’m taking care of her today."
    An "I don’t mind."
    Ad "Okay, come inside!"
    hide anna 
    hide adine
    hide amely
    with dissolve

    scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow
    $ renpy.pause (1.5)

    m "Her house looked like the size of an apartment. It was small, but roomy."

    show anna sad at Position (xpos = 0.80)
    show adine normal b flip at Position (xpos = 0.20)
    show amely normal flip at Position (xpos = 0.40)
    with dissolve

    Ad "So what would you like to do?"
    An face "I was the one invited, how should I know?"
    Ad annoyed b flip "Alright, let me rephrase."
    Ad "Do you want me to make us do something?"
    An sad "Yeah, sure, whatever..."
    Ad normal b flip "Well usually when I’m bored and I’m with Amely, we look at magazines."
    An "Magazines? Isn’t that stuff usually just fake stories and stupid games."
    Ad annoyed b flip "Hey, you wanted my take on what to do, so this is what I’ve decided."
    An "Whatever..."

    show adine think b flip with dissolve

    m "She picked up a copy with the picture of a female on the front."
    m "She started flipping through with Amely looking over her shoulder."

    Ad normal b flip "Ooh, let’s try the matching friends game."
    An "Alright..."
    Ad "Because you’re my guest, I’ll begin with you."
    An "Go ahead."
    Ad think b flip "Let’s see..."
    Ad normal b flip "#1 If going on vacation, where would you prefer to go most?"
    An normal "Probably the beach. There’s free reign there."
    Ad "Interesting..."
    Ad "#2 Which type of desserts do you prefer most?"
    An "Mostly ice cream. It comes in all types of flavors and styles."
    Ad "I agree totally!"
    Ad "Here’s the final question..."
    Ad think b flip "Umm..."
    Ad "Maybe I should skip over this one..."
    An smirk "Why? Too NSFW for the kid?"
    Ad "Mostly because it might remind you of..."
    Ad sad b flip "You know who..."
    An sad "Oh..."
    An "Do it anyways..."
    Ad "If you chose to date a dragon or a mythical species, which would it be?"
    An "..."
    An "Right now, I’d choose a dragon because of memories..."
    Ad think b flip "Hmm..."
    Ad normal b flip "Welp, I guess I can say we have a lot in common."
    An normal "Cool."
    An "What’s next?"
    Ad "Let’s see."

    m "We flipped through a few more pages, sharing laughs and things of that sort. I never knew how fun it was until Adine showed me."

    Ad think b flip "I think I should go drop off Amely, it’s getting pretty late."
    An "Alright, see you when you get back."
    Ad "Bye!"
    Am "It was nice meeting you!"
    An "Sure."

    hide adine 
    hide amely
    with easeoutright

    show anna at center with ease

    m "With that, I was left pondering."

    An "I’m having a good relationship with Adine now."
    An "I may have to tell her soon though... about Amely..."

    m "Soon Adine came back in almost an instant."

    show anna at right with ease
    show adine normal b flip at left with easeinleft

    Ad normal b flip "I’m back!"
    An "That was quick."
    Ad giggle b flip "Many things can be done with wings!"
    An face "Did you seriously fly her back?"
    Ad normal b flip "Don’t worry, I’m trained."
    Ad "Now if I did any of my stunts, then that would be a problem."
    An sad "Whatever..."
    show anna normal with dissolve
    Ad "So, what do you wanna do now?"
    An "It’s getting late, so I should be heading back to my apartment."
    An sad "Or... what’s left of it..."
    Ad think b flip "What do you mean?"
    An "It was raided, and I mean everything."
    An "Books, bed, TV, even money."
    Ad "What did you do that was so bad?"
    An face "Apparently trying to solve cancer not only for me, but for everyone else..."
    show anna sad with dissolve
    Ad "If it’s that bad, then stay here for the night."
    An normal "Really?"
    Ad normal b flip "Sure!"
    Ad giggle b flip "But if you wanna sleep in a bed, we need to share it."
    An "I don’t mind really, just as long as we don’t start running bases if you know what I mean."
    Ad "Don’t be silly!"

    play sound "sfx/switch1.ogg"
    scene black
    $ renpy.pause (1.0)
    stop music fadeout 1.0
    $ renpy.pause (2.0)
    play music "mx/martyr.ogg" fadein 1.0
    $ renpy.pause (2.0)
    
    m "We both got into the bed facing away from each other to make ourselves more comfortable."
    m "Soon, memories flooded back in of [player_name]."

    Ad "Are you comfortable?"
    An "Yeah..."
    Ad "..."
    Ad "What’s wrong?"
    An "Just..."
    An "Well..."
    An "You know..."
    Ad "Oh..."

    $ renpy.pause (3.0)

    m "Soon I couldn’t hold it in and I started crying."
    An "God dammit [player_name]!"
    m "Soon, I felt her wings go around me as she put her head on my shoulder."
    Ad "You need this..."
    An "I do..."

    $ renpy.pause (3.0)

    m "Soon I did the same, wrapping my arms around her putting my head under her’s."
    An "Adine?"
    Ad "Yes?"
    An "I need a place to stay... do you think you could..."
    Ad "Yes..."
    An "..."
    An "Thank you..."

    stop music fadeout 1.0
    $ renpy.pause(1.5)
    play music "mx/anna4.ogg" fadein 1.0

    nvl clear
    window show

    n "Our friendship grew ever since."
    n "We not only started having a friend relationship, but we’ve been having a loving one."
    n "Reading magazines with her was always fun, watching Humans (even though it reminded me of [player_name]) with her were memories to replay, and cuddling was the best."
    n "Soon, we ran bases, but it happened after an experience we both wish we could forget."

    window hide
    scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow

    $ renpy.pause (1.5)

    show adine normal b flip at left
    show anna normal at right
    with dissolve

    Ad "Anna, there’s something I’ve been meaning to ask you."
    An smirk "What, do you wanna marry me?"
    Ad giggle b flip"Don’t be silly!"
    Ad normal b flip "It’s about Amely."
    An sad "Oh..."
    Ad "I’ve always wanted to be a 24/7 parent for her, but never had the partner to do help."
    Ad "But with you along, maybe we can..."
    An "I’m sorry, but no..."

    show adine disappoint b flip with dissolve

    m "Her mood changes in an instant, looking in utmost distraught."
    Ad "No?"
    Ad sad b flip "Why?"
    An sad "It would be too hard to explain."
    An "Besides, if I did tell you, you’d probably kick me out and stop being my friend."
    Ad annoyed b flip "Like it’s already hard enough for you to explain."
    An "I mean it’s gonna be hard for you to ever understand."
    Ad "Like it’s already hard enough for me to..."
    An rage "FINE!!! I’ll tell you..." with vpunch
    show adine disappoint b flip
    show anna sad
    with dissolve

    stop music fadeout 1.0
    $ renpy.pause (1.0)
    play music "mx/library.ogg" fadein 1.0
    $ renpy.pause (1.0)

    m "I told her. Everything."
    m "From beginning to end, I told her the sick truth about Amely."
    m "Everything hurtful in my essay hit her harder and harder, breaking me down as she broke down."

    show adine frustrated b flip with dissolve

    m "Once I finished, her face went to shear anger, looking like she wanted to bite my face off in one fair chomp."

    Ad "Get out..."
    An "W-what?"
    Ad "GET THE HELL OUT!!!" with vpunch
    Ad "WHO’S IDEA IN FUCKSVILLE WAS IT TO ALLOW YOU TO BE EXCUSED FROM ALL CHARGES???"
    An "The ones who thought it was appropriate because I saved [player_name]..."
    Ad "GET THE FUCK OUT OF HERE YOU BITCH!!!" with vpunch 
    An cry "Fine, I’ll leave..."
    An despair "I’LL LEAVE AND REMOVE MYSELF FROM SOCIETY IF THAT’S WHAT YOU WANT!!!" with vpunch

    hide anna
    show anna despair flip 
    with dissolve
    hide anna with easeoutright

    m "I ran as fast as I could, charging out of there with tears draining from my eyes."

    #(pathway from portal)
    scene np2x at Pan ((0, 100), (0, 100), 0.0) with fade

    m "I kept thinking of what I would do to end my life."
    m "I soon saw the beach the idea came of drowning myself."

    scene beach at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
    $ renpy.pause (2.5)

    m "I kept running until I tripped, lying down as I cried on the sand."
    m "I scooped up a hand full of sand in both hands while on my hands and knees, raising them up while offering my head to show God."

    show anna despair at center with dissolve
    An despair "IS THIS WHAT YOU WANT???"
    An "ME BEING A LONELY BASTARD HAVING NO PURPOSE TO SERVE?? ?"
    An "IS THAT WHAT YOU WANT???"

    play sound "fx/impact3.ogg"
    show anna despair at Position(xpos=0.5, xanchor='center', ypos=1.0, yanchor="top") with move9

    m "I soon collapsed once again, this time passing out from all the stress"
    scene black with fade

    $ renpy.pause(0.8)

    nvl clear
    window show

    n "I had a dream."
    n "I was again in a bed in the cosmos, but remembering what happened before I passed out."
    n "I began crying, soaking the pillow and bed sheets."
    n "I soon felt arms wrap around me again and I knew who it was."

    nvl clear

    n "{color=#d5705f}Anna:{/colour} [player_name], don’t end this dream! I have so much to ask."
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} I’m here now... ask what you need."
    n "{color=#d5705f}Anna:{/colour} Is there still a reason to live?"
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} Of course."
    n "{color=#d5705f}Anna:{/colour} Then what reason is there?"

    nvl clear

    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} Because you would be leaving her."
    n "{color=#d5705f}Anna:{/colour} Adine? She hates me now."
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} No she doesn’t."
    n "{color=#d5705f}Anna:{/colour} Yes she fucking does!"
    n "{color=#d5705f}Anna:{/colour} Out of all people, you’re watching me, so you should know..."
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} Anna?"

    nvl clear

    n "{color=#d5705f}Anna:{/colour} What?"
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} I have to go, but I’ll always be in your heart."
    n "{color=#d5705f}Anna:{/colour} Don’t say that, you’ve donated your whole body to me!"
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} I didn’t donate my soul."
    n "{color=[persistent.playercolor]}[player_name]:{/color=[persistent.playercolor]} Without my soul, we wouldn’t be here."
    n "{color=#d5705f}Anna:{/colour} [player_name], don’t go..."

    nvl clear

    n "He kissed me on my lips and then faded away with my dream."

    window hide

    stop music fadeout 1.0
    $ renpy.pause (0.8)
    play music "mx/sweetmemories.ogg" fadein 1.0
    $ renpy.pause(1.0)

    scene beachx at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
    $ renpy.pause (2.5)

    m "I soon woke up, finding a pair of wings wrapped around me and a crying wyvern’s head on my shoulders."

    show adine disappoint b flip at left with dissolve
    $ renpy.pause (0.5)
    show anna cry at right with dissolve
    Ad "I’m sorry Anna!"
    An "It’s okay Adine..."
    Ad "NO! IT’S NOT OKAY!!!"
    Ad "Do you know why I was in that hospital when you were recovering?"
    An "Why?"
    Ad "Because of all people, [player_name] wanted me to be your replacement friend!"
    Ad "But now, I’ve betrayed all trust with both of you!"
    An despair "It’s my fault I’ve put Amely in the position she’s in!"
    show anna cry at right with dissolve
    Ad "You were desperate, I understand now..."

    m "We cried for what seemed like hours when it was really minutes."

    An sad "Adine?"
    Ad disappoint b flip "What?"
    An "Let’s adopt Amely..."
    Ad sad b flip "You’ll do it for me?"
    An "On one condition..."
    Ad think b flip "What?"
    An rage "Never, tell, Remy."
    An "Otherwise, I’ll definitely be thrown in jail."
    Ad disappoint b flip "Okay, I’ll try."

    An sad "Good..."
    Ad "Let’s head back."
    An "Okay..."

    hide adine 
    hide anna
    with dissolve
    scene black with dissolve
    $ renpy.pause (0.4)

    scene np2y at Pan ((0, 100), (0, 100), 0.0) with fade

    m "We walked back not saying a word on what happened."
    m "We looked side to side, making the moment more awkward for us."

    scene town4x at Pan((0, 0), (0, 0), 0.0) with fade

    m "We soon arrived at her front doorstep."
    play sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/silence.ogg"
    queue sound "fx/cling.ogg"

    m "She started taking the keys under her doormat and unlocking the door until she dropped them."
    m "I went to go grab them for her as she went to grab them."
    m "We stared at eachother, blushing uncomfortably as I let go of the keys for her to grab. Soon she opened the door and we went in."

    scene black with fade

    stop music fadeout 1.0
    $ renpy.pause(0.8)
    play music "mx/feelings.ogg" fadein 1.0
    $ renpy.pause(0.8)

    scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow
    $ renpy.pause (1.5)

    show adine disappoint b flip at left
    show anna sad at right
    with dissolve

    m "We sat down on the bed, looking down on the floor."

    Ad "Where did we go wrong?"
    An "Probably at the part where I..."
    Ad annoyed b flip "Now’s not the time Anna..."
    An "I know..."
    show adine disappoint b flip at left with dissolve

    m "We looked around for a bit before I gave in to my tension and hugged Adine. She then to returned the favor."

    An "I’m sorry about literally everything."
    Ad "I’m sorry too..."

    m "Our hug grew stronger until i put my hand on the back of her neck as she did to me."
    m "Soon our heads came together as our lips pressed, while we shed tears in enjoyment."

    show anna at Position(xpos=0.65, xanchor='center', ypos=1.0, yanchor="top")
    show adine at Position(xpos=0.35, xanchor='center', ypos=1.0, yanchor="top")
    with move9

    m "I soon pushed her down on the bed as our lips pressed harder and harder with our tongues swirling around in our mouths."
    m "I then put my thumb under her goggles slipping them off her head."

    Ad "Anna... what are you doing?"
    An "We have to take them off don’t we?"
    Ad "..."
    Ad "Do it... please..."

    scene black with fade
    $ renpy.pause(0.2)
    nvl clear
    window show
    $ renpy.pause(0.8)

    n "After that day, we called the orphanage to give Amely a permanent home."
    n "I was now willing to be a parent, and was it the best thing to ever happen to me."
    n "I loved Amely so much, making me hate myself for what I did to her before."
    n "Most importantly though, I loved Adine, and she loved me back."
    n "That was all I needed in life, love."

    window hide 
    nvl clear

    s "Let’s go back 10 years."
    s "Let’s go back to when Anna was just 13."
    s "Anna was in recess. Having no one to play with, she decided she would sit next to a tree and do school work."
    s "Soon she was approached by someone."

    stop music fadeout 1.0
    $ renpy.pause(1.0)
    #play music "mx/general.ogg" fadein 1.0
    #play music "mx/morningrise.ogg" fadein 1.0
    #play music "mx/movingon.ogg" fadein 1.0
    play music "mx/partingsong.ogg" fadein 1.0
    $ renpy.pause(1.0)

    window show

    n "{color=#BE4685}???:{/colour} Hello there."
    n "{color=#d5705f}Anna:{/colour} Hi?"
    n "{color=#BE4685}???:{/colour} What are you doing?"
    n "{color=#d5705f}Anna:{/colour} What does it look like?"
    n "{color=#BE4685}???:{/colour} My name is Lisa and I’m the new student here."
    n "{color=#d5705f}Anna:{/colour} Well here’s a survival tip, don’t be friends with anyone here."
    n "{color=#BE4685}Lisa:{/colour} Then why are kids alive here and with others?"
    n "{color=#d5705f}Anna:{/colour} ..."
    n "{color=#d5705f}Anna:{/colour} What do you want? Lunch money?"
    n "{color=#BE4685}Lisa:{/colour} Well, I was wondering if you would be my friend."

    nvl clear

    n "{color=#BE4685}Lisa:{/colour} Like I said, I’m the new kid here and I really have no one to hang with now."
    n "{color=#d5705f}Anna:{/colour} I don’t know if I would want to."
    n "{color=#d5705f}Anna:{/colour} I’ve never had a friend before, and I don’t know if I would want one."
    n "{color=#BE4685}Lisa:{/colour} Trust me, being lonely is the worst possible thing."
    n "{color=#BE4685}Lisa:{/colour} If you wanted a gateway to suicide, then stay lonely..."
    n "{color=#d5705f}Anna:{/colour} ..."
    n "{color=#d5705f}Anna:{/colour} Fine... I guess I’ll be your friend."
    n "{color=#BE4685}Lisa:{/colour} Great, is what you’re doing there important?"
    n "{color=#d5705f}Anna:{/colour} No, this is just to get a head start on my homework for tonight."
    n "{color=#BE4685}Lisa:{/colour} Well then come with me, I know something fun we could do."

    nvl clear

    n "{color=#d5705f}Anna:{/colour} Alright."
    n "{color=#BE4685}Lisa:{/colour} ..."
    n "{color=#BE4685}Lisa:{/colour} I never caught your name, what is it?"
    n "{color=#d5705f}Anna:{/colour} It’s Anna."
    n "{color=#BE4685}Lisa:{/colour} Well, Anna, it’s nice to meet you and I hope you’ll make friends in the future."

    nvl clear

    n "Lisa, you touched my heart that day."
    n "I finally have love, Lisa"
    n "A child too."
    n "I did it Lisa."
    n "I did it..."

    window hide

    jump wyv_anna_customcredits
