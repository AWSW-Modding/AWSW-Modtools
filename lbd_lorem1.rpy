label lbd_stock_lorem1:

    $ chapter1csplayed += 1
    $ lorem1unplayed = False
    $ lorem1played = True
    $ persistent.lorem1played = True

    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - Lorem 1"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - Lorem 1"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - Lorem 1"

    else:
        $ save_name = "Chapter 1 - Lorem 1"

    $ lorem1mood = 0

    stop music fadeout 1.0
    scene black with fade
    $ renpy.pause (1.0)

    scene bare with dissolveslow
    play music "mx/fountain.ogg" fadein 2.0
    $ renpy.pause (0.3)

    m "I went to the bar Lorem had suggested as our meeting place. When I looked around, I saw Bryce sitting at a table, talking to someone I couldn’t see. I lingered on him for a second, but soon spotted Lorem in the corner of my eye."

    show lorem normal with dissolve

    Lo "There you are!"
    c "Hey, Lorem."
    Lo relieved "It's good to see you! I thought you might not show up."

    menu:
        "Am I late?":
            $ renpy.pause (0.5)

            Lo normal "Not at all! I got here early."

        "Well, I'm here now.":
            $ renpy.pause (0.5)

            Lo happy "Yeah, I can certainly see that."
            show lorem normal with dissolve
            $ lorem1mood += 1

        "I almost didn't.":
            Lo "I'm glad you came anyway."
            show lorem normal with dissolve
            $ lorem1mood -= 1


    c "I'm kinda surprised you wanted to meet me here. Don't take this the wrong way, but are you even old enough to drink?"
    Lo think "What are you talking about?"
    Lo happy "Oh, I see."
    Lo normal "I can assure you I am a fully grown adult. My species doesn't get much bigger than this."
    Lo happy "Speaking of which, are you fully grown yet? How big do humans usually get and how do you stack up, comparatively speaking?"
    Lo think "Oh, and would you mind if I took some notes?"
    c "Before we get to that, you haven't even told me yet what exactly all this is for. Are you sure you're not a reporter?"
    Lo happy "If I was, Sebastian wouldn’t have let me meet you in the first place."
    c "And I thought the uniform was just a clever disguise."
    Lo normal "It's real, though. Sebastian knows I work for the local post office."
    c "Excuse me, but this still doesn't really tell me anything about why I'm here. You're a postman who wants to interview me for... what, exactly?"
    Lo relieved "Sorry, I guess I got ahead of myself here. Maybe a full introduction is in order, and after that, you can still decide whether you want to go through with this or not."

    menu:
        "Sounds good to me.":
            pass

        "Sure, go ahead.":
            $ lorem1mood += 1

        "I already regret coming here.":
            $ lorem1mood -= 1


    $ renpy.pause (0.5)

    Lo happy "I recently graduated college with a degree in computing and moved in here with a good friend of mine."
    Lo think "This town doesn't exactly offer the best opportunities to put my degree to good use, though."
    c "Then why move here in the first place?"
    Lo normal "Living in the city can be very expensive. I can always move later when I get a job there. I've got other plans right now, though."
    Lo happy "I'm working on a video game."


    menu:
        "That's what this is all about? A video game?":
            $ renpy.pause (0.5)

            Lo normal "You got it!"

        "Oh, you said this was going to be about something serious.":
            $ renpy.pause (0.5)

            Lo relieved "But this is serious!"
            show lorem normal with dissolve
            $ lorem1mood -= 1

        "A video game? Sounds interesting.":
            Lo "Exactly!"

            show lorem normal with dissolve
            $ lorem1mood += 1


    Lo "Video games and computers are just starting to catch on in places like this town. Making good content will be very important to give a good first impression."
    Lo happy "And humans have always been part of our media - books, movies, and now games. With you on our side, this could be an amazing opportunity!"
    c "Well..."
    Lo shy "Oh. Maybe this wasn't such a good idea after all."

    menu:
        "Why?":
            $ renpy.pause (0.5)

            Lo relieved "I don't know. You don't seem so thrilled about doing this anymore..."

        "You're right about that. I can't help but feel a little deceived by this.":
            $ renpy.pause (0.5)

            show lorem relieved with dissolve
            $ lorem1mood -= 1

    Lo "Besides, your job must be really stressful, and you're probably already in the spotlight all the time. And now, to top it all off, you get some postman harassing you for an interview."
    Lo "If you wanted to leave, I'd get that."

    $ lbd_triedtoleave = False

    menu:
        "Stay.":
            $ lbd_triedtoleave = False

            c "Well, I'm already here and have nothing else to do, so let's make the most of this."
            Lo happy "Yes! Thank you!"

        "Leave.":
            $ lbd_triedtoleave = True

            lime45 "Did you really think it would be that easy?"

    $ lbd_num_times_tried_skip = 0

    while lbd_triedtoleave:
        menu:
            "Stay.":
                $ lbd_triedtoleave = False

                c "Well, I'm already here and have nothing else to do, so let's make the most of this."
                Lo happy "Yes! Thank you!"

            "{s}Leave.{/s}":
                $ lbd_num_times_tried_skip = lbd_num_times_tried_skip + 1

                if lbd_num_times_tried_skip == 10:
                    lime45 "Congratulations, you clicked a button 10 times."

                elif lbd_num_times_tried_skip == 20:
                    lime45 "Congratulations, you clicked a button 20 times."

                elif lbd_num_times_tried_skip == 30:
                    lime45 "I'm beginning to bore of this."

                elif lbd_num_times_tried_skip == 40:
                    lime45 "Ok, you're clicking the button 99 times to see what will happen."
                    lime45 "You think just because Saunders done it, that I will reference to it."

                elif lbd_num_times_tried_skip == 50:
                    lime45 "Well I hate to disappoint you but that's not going to happen."

                elif lbd_num_times_tried_skip == 60:
                    lime45 "{i}sigh{/i} since we're going to be here a while, why don't I tell you a story?"

                elif lbd_num_times_tried_skip == 70:
                    lime45 "Hmm, what story to tell."
                    lime45 "Oh I have one for you."
                    lime45 "This one time I went to the cinema but I didn't have all that much money with me."
                    lime45 "So I went to a nearby farmers market and bought a loaf of rye bread."
                    lime45 "Inside the cinema, I bought a fanta and snuck in the loaf of bread."
                    lime45 "I just sat there and ate the loaf of bread. It lasted the entire movie (whatever movie that was) and it tasted like Guinness."
                    lime45 "So there's the story."

                elif lbd_num_times_tried_skip == 80:
                    lime45 "Really?? You got a story, what more do you want from me?"

                elif lbd_num_times_tried_skip == 90:
                    lime45 "You are really are going for 99 clicks ain't you? Do you really have nothing else to do?"
                    lime45 "Like eat a loaf of bread for example."

                elif lbd_num_times_tried_skip == 95:
                    lime45 "Congratulations, you clicked a button 95 times....."
                    lime45 "Huff and puff."

                elif lbd_num_times_tried_skip == 98:
                    lime45 "Congratulations, you clicked a button 98 times....."
                    lime45 "Like Windows 98, it was the one after Windows 95."
                    lime45 "But there is a chance you're a little too young to remember those old operating systems."
                    lime45 "Not that I blame you for it."
                    lime45 "Windows 98 was nice in ways but Win98SE helped fix so many issues."
                    lime45 "It does run rather well but the modern software support is naturally terrible."
                    lime45 "However, Windows XP is very stable and has good modern software support."
                    lime45 "Give it a go on an old machine or for playing old games that have issues on more modern operating systems."
                    lime45 "Which could be due to several reasons."
                    lime45 "But a huge part of it would be related to subsystems like audio for example. It got a fairly major overhaul from WinXP to Win Vista."
                    lime45 "Speaking of Vista, it may be terrible but it really paved the way into modern day Windows."
                    lime45 "But that's a rant for another time."
                    lime45 "Wow, when I started writing this I had no idea what to say for this but look, I came up will all this BS. Well, I'll be hitting the old dusty trail."

                elif lbd_num_times_tried_skip == 99:
                    lime45 "Nice try but no dice!"
                    $ renpy.pause(3.0)
                    lime45 "See?"
                    lime45 "Nothing."
                    lime45 "Just like I said...{w=1.0}{nw}"

                    play sound "fx/system.wav"
                    show lime_achievement
                    call syscheck
                    if system == "normal":
                        s "You bothered the Lime a grand total of 99 times!"

                    elif system == "advanced":
                        s "You bothered the Lime a grand total of 99 times. Absolutely amazing!"

                    else:
                        s "You bothered the Lime a grand total of 99 times. He needs more hobbies anyway."

                    lime45 "..."
                    lime45 "Screw you too!"
                    hide lime_achievement

                elif lbd_num_times_tried_skip == 100:
                    lime45 "This isn't funny anymore. You sat there clicking a button 100 times."
                    lime45 "I'm just going to move you on in the story, one of us has to."

                    menu:
                        "Lime, plz no!":
                            lime45 "No?"
                            c "Please, I really don't want to play the stock date. It's boring."
                            lime45 "Go on."
                            c "Uhhh, it was very badly written and your version is much better."
                            lime45 "And the twists?"
                            lime45 "How about the milkmaid and robots?"
                            c "Why do you treat me like this? I am tired of your cunning!"
                            lime45 "I can imagine. This is exactly how the milkmaid feels when she meets the robots in path 7."
                            lime45 "I have the mod with me but I want to hear this blurb. Speak now and I'll send you on your way."
                            c "This mod is incredible."
                            c "I really appreciate every bit of the wordings."
                            c "The main character the milkmaid is {b}Passionate{/b} and {b}Sensitive{/b} and the plot twist with the robots, is good too."
                            c "This mod adds to people's lives; anyone who plays this mod with be surprised by the twist."
                            c "I also loved the way it started."
                            lime45 "Hmmm, I see."
                            lime45 "Well you're clearly insane but your blurb made me laugh so I'll give you something fun."
                            lime45 "Right, because this is so short notice it's going to be very very rushed but we're too far gone to put you back at the start of the mod."
                            lime45 "Give me a sec to google some stuff {w=0.8}....{w=0.8}....{w=0.8}....{w=0.8} Right, hold on! This is going to be shit."

                            stop music fadeout 0.8
                            scene black with fade
                            $ renpy.pause(0.8)
                            play music desert_wind fadein 1.5

                            $ renpy.pause(0.5)
                            scene bridge_keeper with fade
                            $ renpy.pause(0.8)

                            Bridgekeeper "Stop. Who would cross the Bridge of Death must answer me these questions three, ere the other side he see."

                            c "Ask me the questions, bridgekeeper. I am not afraid."

                            Bridgekeeper "What... {w=0.2}is your name?"


                            menu:
                                "Scrotie McBoogerballs":
                                    lime45 "You lie, get out of my face."
                                    if lbd_demo_mode:
                                        jump lbd_demo_ending

                                    return

                                "[player_name]":
                                    pass

                                "Ivana Mandic":
                                    lime45 "You lie, get out of my face."
                                    if lbd_demo_mode:
                                        jump lbd_demo_ending

                                    return

                            $ lbd_questing = True
                            while lbd_questing:
                                Bridgekeeper "What... {w=0.2}is your quest?"

                                $ lbd_joke_ans = renpy.input("Quest")

                                if lbd_joke_ans == "":
                                    pass
                                else:
                                    $ lbd_questing = False

                            $ lbd_questing = True
                            while lbd_questing:
                                Bridgekeeper "What... {w=0.2}is your favourite colour?"

                                $ lbd_joke_ans = renpy.input("Colour")

                                if lbd_joke_ans == "":
                                    pass
                                else:
                                    $ lbd_questing = False

                            Bridgekeeper "Go on. Off you go."
                            c "Oh, thank you. Thank you very much."

                            scene black with fade
                            stop music fadeout 1.2
                            $ renpy.pause(0.8)

                            lime45 "Well, that's the end of that. Back to the stock date you go."

                            play music "mx/fountain.ogg" fadein 2.0
                            scene bare with dissolveslow
                            $ renpy.pause (0.3)
                            show lorem normal with dissolve

                        "OK":
                            pass

                    $ lbd_triedtoleave = False

                    c "Well, I'm already here and have nothing else to do, so let's make the most of this."
                    Lo happy "Yes! Thank you!"

                else:
                    lime45 "Nice try but no dice!"

    c "At least I won't have to be so careful now. With a reporter, I'd have to worry about things being misinterpreted or being taken out of context."
    Lo normal "You should still be careful. What you tell me now will influence how your entire species will be represented in my game."
    Lo happy "Don't worry, though. I'll treat this delicate matter with the required finesse."

    menu:
        "Don't get ahead of yourself. We haven't even started yet.":
            $ lorem1mood -= 1

        "I'm sure of it.":
            $ lorem1mood += 1

        "Okay.":
            pass

    $ renpy.pause (0.5)

    Lo think "How should we do this? Let me think..."
    c "Why do you want to make this game in the first place?"
    Lo happy "I've always wanted to make a video game. I've had this idea for a while, and it seems now is the right time to do it. It's almost as if you arrived at the perfect moment."
    c "I don't know. Don't you think my visit will overshadow your efforts? People may not be so interested in playing a game about humans anymore if they had a real one show up."
    Lo normal "Good point, but the vast majority won't get to meet you personally, anyway. If I say I did and modeled the humans in the game after you, people will flock to it to get a similar experience."

    menu:
        "Does that mean I'm going to be your game's mascot?":
            $ renpy.pause (0.5)

            Lo think "I guess you could say so."

        "So now I'm part of your viral marketing campaign, great.":
            $ renpy.pause (0.5)

            Lo relieved "That's just a necessary evil, I think. They have to know somehow."
            $ lorem1mood -= 1

        "As long as it's based on the truth, you have my support.":
            $ renpy.pause (0.5)

            Lo happy "Awesome!"
            $ lorem1mood += 1

    show lorem normal with dissolve

    c "Okay, but why focus on humans? What makes us so important?"
    Lo think "If there’s one thing that people here love, it’s humans. It doesn’t matter if they just see them in the media or believe in them as mythical creatures."
    Lo normal "For me, humans were always real. I just didn't know whether I'd ever get a chance to meet one myself. I guess I can cross that one off the bucket list."
    Lo happy "Now that we're here, I can tell you that no expense will be spared to make our portrayal of humans as accurate as possible."

    menu:
        "You certainly seem passionate enough about this.":
            pass

        "Those are some messed up priorities.":
            $ lorem1mood -= 1

        "I'm with you on this.":
            $ lorem1mood += 1

    $ renpy.pause (0.5)

    Lo normal "For good reason! I just love humans."
    c "If you say it like that, it actually ends up sounding pretty weird."
    c "Besides, what if I turn out to be a horrible person? What would you think about humans then?"
    Lo think "It wouldn't change anything, because I wouldn't base my opinion of an entire species on interactions with a single individual."
    c "Then what is your current opinion of us based on?"
    Lo normal "Just the myths we have and the previous portrayals of humans in our media, but I suppose that's why I'm here talking with you right now. I want the truth, and all of it!"
    c "Telling you all of it might not be such a good idea..."
    Lo think "Oh yeah, I guess that would take a lot more time than we have today."
    c "Anyway, what's the actual game about? What do you do?"
    Lo happy "It's a community simulation game. It all starts with the player character moving into a procedurally generated community, which is inhabitated by all kinds of mythical creatures. Humans included."
    c "Mythical creatures like humans. Mmm-hmmm."
    Lo "Not only are the towns you move into unique, but the inhabitants are, too. There are a variety of traits that get randomized, both in looks and personality."
    Lo "There are many things you can do, but it's very open-ended and you can live your life there however you want to."

    menu:
        "Sounds boring.":
            $ renpy.pause (0.5)

            Lo relieved "Well, I guess you're not part of the target audience, then."
            $ lorem1mood -= 1

        "That sounds interesting.":
            $ renpy.pause (0.5)

            Lo normal "It is! At least, I hope others feel the same way about it."

        "That sounds like my kind of game.":
            $ renpy.pause (0.5)

            Lo think "Oh, really?"
            Lo happy "I couldn't ask for a better compliment than that!"
            $ lorem1mood += 1


    c "What other mythical creatures are there besides humans?"
    Lo think "I haven’t worked that out yet, but humans alone give us a lot of material to work with."
    c "How so?"
    Lo normal "The question of the mythical human can be tackled in a variety of ways. There are many different interpretations of what humans are like."
    c "For example?"
    Lo happy "In general, the mythical human can be divided into three categories: Firstly, the human as a physical creature; secondly, the human as a non-physical entity; and thirdly, the human as a spiritual being."
    c "Let's start with the physical aspects."
    Lo normal "Sure. Since one of our myths tells us that the human who created us eventually turned into a dragon, there is a lot of room for interpretation as to how similar humans actually are to dragons."
    Lo think "I can see you don't have wings, but most of us are able to create fire in some way, or at least have a breath weapon. How about you?"


    menu:
        "I don't have a breath weapon, unless you count my morning breath.":
            Lo "I don't think that counts."

        "I can rub two sticks together to make fire. Does that count?":
            $ renpy.pause (0.5)

            Lo normal "Not really. Having hands that are dextrous enough to do that is remarkable, though."
            $ lorem1mood += 1
            show lorem think with dissolve

        "Of course. I can also move things with my mind.":
            $ renpy.pause (0.5)

            Lo happy "Really? That's amazing!"
            c "I was just kidding."
            Lo relieved "You shouldn't joke about things like that. This is serious."
            c "Alright."
            $ lorem1mood -= 1
            show lorem think with dissolve


    Lo "It is a bit strange, though, because our myths also say that you gave that ability to us."
    c "Interesting."
    Lo happy "Maybe it’s meant to be taken literally – meaning that when that ability was given to us, you lost it."
    c "Or maybe we never had it in the first place."
    c "Humans are known to have created a lot of things out of nothing. After all, we only needed to discover how to create and use fire, because we didn't have a natural ability to do so."
    c "We have a proverb that sums this up pretty well."
    Lo normal "What is it?"
    c "Necessity is the mother of invention."
    Lo think "So a lack of natural abilities drove innovation forward. What an interesting thought."
    c "Here's another thing: You may have many different images of humans, but in the end, only one can be right."
    c "It's also possible that what you've been led to believe about humans doesn't actually refer to us at all."
    Lo relieved "Are you implying that you aren't human?"
    c "No, I'm just saying that if you really had been in contact with humans before as your myths imply, they would need to belong to the same species as me, and thus be very similar to myself."
    c "If they aren't, then either they weren't humans at all, or have very different origins."
    Lo think "So you say there is a possibility that our humans and your humans may be something different altogether?"
    Lo happy "I suppose you are right in the way that our images of humans are very inconsistent. They certainly can't all be humans in the way that we would refer to a single species. The name should probably be reserved for yours."
    Lo normal "And we haven't even touched on the other two categories of humans."
    c "What did you call them again?"
    Lo happy "Non-physical human entities and spiritual humans."
    c "What's the difference?"
    Lo think "Honestly, the definitions get a bit muddled here. Going by conventional belief, a ghost could be a human who has died and thus changed into a different form. We would call this a spiritual human."
    Lo normal "An angel, on the other hand, would be classified as a non-physical entity."
    c "What do you know about angels?"
    Lo happy "Angels basically look like humans with wings. Their existence in ancient scripts was used to lend some credence to the theories about humans having become dragons."
    c "Because of the wings?"
    Lo "Exactly."
    c "But some of your dragon species don't have wings, either."
    Lo think "Yes. As I said, once you start delving into that kind of stuff, it all becomes very convoluted."
    c "When we met, you also told me something about a four-headed human."
    Lo normal "Right. With that we'd go into the realm of creatures that just don't make much sense at all."
    Lo think "Having four heads just seems unlikely from an evolutionary perspective."
    Lo "That might not really matter if we were talking about a non-physical entity or a spiritual being, though."
    c "So in the end, you have a lot of different ideas whose only connection to each other is that you use the word human to describe them in some way."
    Lo normal "And they share at least some basic characteristics. You fit those as well, by the way."
    c "What are they?"
    Lo think "You certainly are not a reptile like us, but you don't look like a conventional mammal either."
    c "We are mammals, though."
    Lo "Yes, but you are so different from other mammals we know that, ultimately, you are quite unique. We don't know any other sentient mammals."
    c "You've got a point there, I'll give you that."
    c "Strangely enough, we have plenty of human-like creatures in our mythologies as well."
    Lo happy "Oh, do tell!"
    c "You already mentioned ghosts, but some other ones include dwarves, giants, faeries and blemmyes."
    Lo normal "I think I've heard of most of these before, but what is a blemmyes?"
    c "Essentially, a blemmyes is a human without a head."
    Lo think "A human without a head? How does that work? How do they eat?"
    c "Instead of a head, they just have all their facial features on their chest."
    Lo relieved "That's a rather weird mental image."
    c "There are also a lot of half-creatures that share some characteristics with humans and other animals."
    Lo think "Like merhumans?"
    c "Sure."
    c "Lastly, there are creatures that are said to be able to shapeshift into human form."
    c "Strangely enough, some of our dragon myths said they could shapeshift into humans or that certain countries’ royalty are descended from dragons."
    Lo normal "That would imply that they are genetically compatible with humans."


    menu:
        "I guess.":
            pass

        "Apparently.":
            pass

        "Sounds gross.":
            $ lorem1mood -= 1


    $ renpy.pause (0.5)

    Lo think "Sounds rather outlandish, if you ask me. We certainly can't shapeshift like that."


    menu:
        "I suppose that's why they're just myths.":
            $ renpy.pause (0.5)

            Lo normal "Right. To be fair, we do have a lot of myths that seem quite out there as well compared to what you're like."

        "Are you sure?":
            $ renpy.pause (0.5)

            Lo happy "To be fair, I never tried. Hang on."
            Lo think "..."
            Lo normal "Did it work?"
            c "Nope, still a dragon."
            Lo sad "Awww."


    Lo think "Anyway, how come you know so much about myths?"

    c "All part of being an ambassador. Not only did I learn about dragon myths in order to compare them to what you're like, but I also studied myths about creatures that are similar to humans so I could find out how similar they were to yours."
    Lo happy "Well, you're doing an excellent job so far. And it's bound to help me a lot with my game as well."
    c "You're going to put all of that into the game?"
    Lo normal "Let's just say it gives me some excellent material to work with."
    c "I thought you wanted to give an accurate portrayal of humans, not just collect myths."
    Lo think "One species will certainly be modeled after you, but that doesn't mean we can't introduce some variety with the others."
    Lo happy "People will love it if we also bring some of the more unusual myths to life."
    c "I see."
    Lo normal "But since we also want each of the normal human characters to be unique, I'd like to know how much variety there really is within your species."
    Lo think "I've seen Reza before, so comparing him to you already gives me a bit of an idea - but how far do these differences go, exactly?"
    Lo "When we arrived here, you asked me if I was old enough to drink. That leads me to believe that your average human must be a lot taller."
    c "That's true. You could say Reza would be about average for an adult."
    c "Not that it would be impossible to get a good deal bigger than him or even smaller than you, but those cases are rather rare and usually the result of medical conditions."
    Lo normal "I see, I see."
    Lo "What about colors? Are there any humans who are blue like me?"
    c "Not really. There is a certain spectrum of skin colors that can be lighter or darker, but so far I've seen a lot more variety in the dragons here."
    c "We do have quite a number of different eye colors, though."
    Lo think "Interesting."
    c "As for things that aren't immediately visible, we also have different blood types, but I assume you know about that."
    Lo normal "We certainly have those as well."
    c "Some people even believe your blood type influences your personality."
    Lo think "That, on the other hand, is news to me."
    c "Anything else you want to know?"
    Lo relieved "Phew, we already got so much. I'll have to think about if and how we can work all this into the game."
    c "Have you worked on any other games before?"
    Lo normal "I worked on a few small projects during the course of my studies and also interned at a studio before. This is on a completely different level, though."
    c "How so?"
    Lo happy "It's my game, so I'm the one calling the shots here. It's a very different thing than just making a few graphics when you're part of a bigger team, for sure."
    c "I see. How long exactly have you been working on this?"
    Lo think "Phew. Must be several months now. I've got everything planned out and a lot of the groundwork has already been done."
    Lo normal "The most difficult things are the characters themselves, and to make sure all of the details are accurate."
    c "Of course."
    c "Have you shown the game to other people yet?"
    Lo happy "Sure! Feedback is a very important part of the development process, so I regularly gather ideas and opinions from others. I even made a website to do this!"
    c "And what do they say?"
    Lo think "All kinds of things, really. Sometimes it's hard to decide which ones have a good point and which can be disregarded."
    Lo normal "Overall, it seems there are many people who are looking forward to play my game, though."
    c "How many are we talking about?"
    Lo "I don't know, exactly. The counter on my website only tracks the number of visits, so I don’t actually know how many different people there are."
    c "What if it doesn't work out?"
    Lo think "What do you mean?"
    c "Well, you're investing a certain amount of time and money into making this game. Ideally, you would make back your investment and hopefully get some profit on top of that."
    Lo normal "If the goal is to make money, sure. However, I just wanted to try my hand at doing something like this. If some people are going to enjoy the end result, that's great."
    Lo happy "Don't forget that I'll also have made something that I can put on my resume. At the very least, it'll have been a good learning experience."
    c "With that attitude, I suppose you really don't have anything to lose."
    Lo think "I can always look for another job, and maybe I'll end up working at a game studio, but I think once I've started doing something like that, I might not get this opportunity again."
    c "So it's now or never, huh?"
    Lo normal "In a nutshell, yes."
    c "And that all works out with your courier job?"
    Lo happy "Sure. I can support myself this way and am not really under any pressure, since I don't have any deadlines to keep."

    menu:
        "Seems like you know what you're doing.":
            Lo "I'd like to think so!"

            $ lorem1mood += 1

        "Deadlines are a good way to ensure something gets done, though.":
            $ renpy.pause (0.5)

            Lo think "You're right about that. It's something where balance is important, I think. I set deadlines for myself, but I don't have to worry about the project breaking down if I don't meet certain milestones at a certain time."


    c "What kind of tools are you using to make it? If I consider what some of your species look like, I'm having a hard time imagining how the bigger ones could program a game."
    Lo normal "While we do have devices tailored to each individual species, I can't deny that my dextrous hands make it a lot easier compared to some of the others."
    Lo "One downside is that I have to keep my nails short, or else using the keyboard gets a bit cumbersome."
    c "I imagine you'd have to be careful with those while working as a courier, anyway."
    Lo relieved "You're right about that. One wrong move and you've suddenly shredded the letter you were just going to hand to someone."

    menu:
        "That sounds unpleasant.":
            pass

        "You should be more careful.":
            $ lorem1mood -= 1


    $ renpy.pause (0.5)

    Lo normal "Luckily, that kind of thing doesn't really happen to me anymore."
    Lo "Not only because of the shorter nails, but once you've worked there for a while, you just learn to be more careful."
    Lo think "It's a bit sad not to have them as a natural letter opener anymore, though."
    Lo normal "And it's not just for me. Some people ask me to open their letters for them, since doing that on their own can be difficult for some of the less dextrous and older ones."
    c "Have you been working as a courier for long?"
    Lo happy "I just got this job a few months ago, but I had a part-time summer job at the post office when I was growing up."
    Lo normal "My species is perfectly suited for the job, so they were glad to have me on board."

    menu:
        "I can see why.":
            pass

        "Why is that?":
            pass

        "Oh, really?":
            pass


    $ renpy.pause (0.5)

    Lo happy "Of course, being able to fly is a big plus. My size means I can't deliver any big packages, but I often get assigned to urgent letters that have to be delivered as soon as possible."
    Lo think "Huh, it's getting late. Maybe we should leave it at that for today."
    c "Yeah, I should probably head back to my apartment before it gets too dark."
    Lo happy "I got more than enough material to work with. Thanks a lot!"


    if lorem1mood >= 7:

        Lo think "Maybe I could convince you to meet me again some other time?"
        Lo normal "I'd like to get some pictures of you for reference."
        play sound "fx/scribblex.ogg"
        c "Alright, sure. Here's my number."
        Lo happy "I can't thank you enough for doing this. You've been a huge help!"
        c "Don't worry about it."
        c "I really have to get going now, so maybe I'll see you next time."
        Lo "Sure! Ciao!"
        c "Take care."

        stop music fadeout 2.0

        $ renpy.pause (0.5)

        $ loremstatus = "good"
        $ loremscenesfinished = 1
        $ persistent.lorem1skip = True

        if lbd_demo_mode:
            jump lbd_demo_ending

        return

    #    if chapter4unplayed == False:
    #        jump chapter4chars

    #    elif chapter3unplayed == False:
    #        jump chapter3chars

    #    elif chapter2unplayed == False:
    #        jump chapter2chars

    #    else:
    #        jump chapter1chars


    elif lorem1mood >= 1:
        c "Don't worry about it. I'll just consider it a public service."
        Lo normal "Honestly, I'm incredibly grateful for the opportunity, especially after nearly getting denied by Sebastian when I met you."
        c "Just make the best of it."
        Lo happy "I certainly will!"
        c "I really have to get going now, so maybe I'll see you some other time."
        Lo normal "Sure! Have a good night."
        c "Take care."

        stop music fadeout 2.0

        $ renpy.pause (0.5)

        $ loremstatus = "neutral"
        $ loremscenesfinished = 1
        $ persistent.lorem1skip = True

        if lbd_demo_mode:
            jump lbd_demo_ending

        return

        #if chapter4unplayed == False:
    #        jump chapter4chars

    #    elif chapter3unplayed == False:
    #        jump chapter3chars

    #    elif chapter2unplayed == False:
    #        jump chapter2chars
    #    else:
    #        jump chapter1chars

    else:
        c "Don't worry about it. I'll just consider it a public service."
        Lo normal "Thank you for your time. Really."
        Lo sad "I-I promise I won't bother you again."
        c "What are you talking about?"
        Lo relieved "Well, I can't help but feel like you still thought this was a waste of time."
        c "I have to admit, I was kinda annoyed about the whole thing. I guess it showed."
        Lo shy "Don't get me wrong, I'm still incredibly grateful that you stuck around until the end. I'm just saying it won't happen again."
        c "Okay."
        c "I really should be going now."
        Lo "Take care."
        c "Yeah, you too."

        stop music fadeout 2.0

        $ renpy.pause (0.5)

        $ loremstatus = "bad"
        $ loremscenesfinished = 1

        if lbd_demo_mode:
            jump lbd_demo_ending

        return

    #    if chapter4unplayed == False:
    #        jump chapter4chars
#
#        elif chapter3unplayed == False:
#            jump chapter3chars

#        elif chapter2unplayed == False:
#            jump chapter2chars

#        else:
#            jump chapter1chars
