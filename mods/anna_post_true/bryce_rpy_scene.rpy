label bryce_post_true_bootstrap:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ player_name = persistent.player_name
    jump bryce_post_true_entry

label bryce_post_true_entry:
    $ bryce_post_mood = 0
    call _mod_fixui
    stop music fadeout 1.0
    stop sound fadeout 1.0
    
    scene black with fade
    $ renpy.pause(1.0)
    scene np3 with fade
    #play music "mx/_.ogg" fadein 1.0
    $ renpy.pause(1.0)
    
    m "The last few hours felt like a dream, or a memory of a dream I had many times before. Izumi was dead, Reza was captured, and both worlds were safe - for now. No doubt it would all make sense in the morning but now I just wanted to get home and get some rest. Bryce and I walked back to town from the portal, together."
    show bryce normal with dissolve
    $ renpy.pause(0.5)
    
    Br "So what's next for you?"
    c "I don't know. It seems like I've got everything right this time so I won't have to do it all over again. If I have to, I will. But a part of me just wants to continue on and see what happens. What about you?"
    Br "All I know is I'm going to go home and have a drink or three. I need it."
    
    menu:
        "(Say nothing)":
            Br "Hold on. I'm pretty sure I'm out. I had my last few beers the other day. I don't suppose you have more of that wine at your place?"
            c "I might still have a few bottles left."
            Br "Alright!"
            
            menu:
                "(Say nothing)":
                    Br "Assuming you want me to come over, of course."
                
                "I didn't invite you.":
                    Br "Oh. I just assumed, after that one night, you wanted to..."
                    c "Is that what you want? Just to use me for entertainment and alcohol?"
                    Br "Hey, I was just asking. If you want to be alone, I understand."
                    $ bryce_post_mood -= 1
                    
        "I think I will too.":
            Br "Alright! I'm out of beer at my place at the moment but the liquor store by my place is open till midnight."
            m "I looked at my watch. It was just after one in the morning."
            Br "Damn! I don't suppose you have any at your place?"
            c "I think we drank the last bottle the other night. "
            $ bryce_post_mood += 1
            
    Br "Although, maybe not. Hell, I can go without drinking for one night. We both know I drink too much. I know you know too, even if you're too polite to say anything."
    Br "You were right earlier, when you asked if people at my job noticed. Once you said that, I started paying attention. Whenever someone mentioned alcohol, they'd look in my direction. I just never paid attention before."
    c "I can't tell you what to do."
    m "The dragon looked at me and for a second it looked like he was going to ask me something but was too ashamed. So I asked him what I thought he was thinking."
    c "Are there any programs or groups that help people deal with this here?"
    Br "If there are, I haven't heard of them. I never looked though, I can handle it on my own."
    
    menu:
        "There's no shame in asking for help.":
            c "You needed my help during the investigation and 	nobody judged you for it. If you need help of a more personal nature I could help with that too."
            $ bryce_post_mood -= 1
            
        "If you could, you would have already.":
            Br "Hey, what I do in my spare time is none of your business."
            c "True, but if you're going to be in my world, among my people, you have to act a certain way. Otherwise they'll judge you for it."
            Br "And what if I don't give a damn what they think?"
            c "If I bring you through the portal, you're partly my responsibility. If you want to stay here, you can."
            $ bryce_post_modd -= 1
            
        "Whatever works for you, I guess. Do you have any hobbies that distract you from wanting to drink?":
            Br "Building that model ship helped. At first I found it frustrating that I couldn't keep my claws steady or see the tiny stupid parts. But if I was sober, I could just barely do it, so it's a good excuse not to drink."
    
    m "He was silent for a while and I could tell he was deep in thought. For the first time, I wondered how old he was. If he had hair it would surely be graying."
    Br "But it's the only thing that helps. Sometimes it's the only way to keep the dreams away. You don't know what it's like, dealing with what I had to deal with every day."
    Br "I deal with the worst that dragonkind has to offer. I see murderers, thieves and rapists. Drug overdoses and suicides. Nearly every day."
    
    menu:
        "You're right.":
            c "I've only been here a week and I've seen only a few crimes."
            
        "Actually, I do know what it's like.":
            c "My world isn't like this. We don't have pretty little towns where everyone knows each other and gets along. We have one city and it's walled off, and if it wasn't, people would come in, steal everything we have, and kill everyone they met."
            c "I've seen people murdered in the streets for their shoes. I've seen families kill one of their children and eat it so the others could survive."
            Br "Damn, [player_name], I'm sorry. I didn't know. I mean I knew it was bad, but not that bad."
            c "Nobody does. If we really told everyone how bad it was, your people could take advantage of us."
            c "That's why we need those generators. Something as simple as electricity makes a world of difference in a world where we have useful, lifesaving technology lying around but nothing to power it with."
            
    Br "I guess your people really do need our help, then."
    c "We do. An experienced police chief would be an extremely valuable asset to us. Even without your experience, a dragon like yourself is strong enough to help with manual labour."
    Br "Was there anyone else you thought of bringing?"
    
    menu:
        "Remy.":
            c "He's a scholar. There's a huge amount of information at his disposal, information humanity might have lost, or not discovered in the first place."
            
        "Adine.":
            c "Being a flyer is helpful. Even something as menial as delivering packages would help us."
            
        "Anna.":
            c "She's a scientist, and a doctor. She knows how to operate medical equipment and make diagnoses. There's almost nothing we would value more than that. "
            
        "Lorem.":
            c "I know Lorem was working on a story about humans, and he wanted my input. I thought I could use him to influence dragonkind's perception of humans however I wanted."
            
        "Nobody but you.":
            pass
            
        
    c "I'll make sure you'll be allowed through the portal. You're useful enough. The only limitation is mass, so you won't be able to bring much with you"
    Br flirty "Can I bring my Fun Basket?"
    c "I'm sure the Chief of Police can bring whatever he-"
    Br normal "Oh, shit. I think I forgot it at the park where we watched the fireworks. I really hope nobody found it."
    c "Why, what was inside it?"
    Br flirty "Uh... stuff."
    c "What kind of stuff?"
    Br "You know... things we might have used."
    
    menu:
        "We'd better go look for it, then.":
            c "You never know when that stuff comes in handy."
            Br normal "I think it could come in handy tonight."
            c "That sounds like a fun night."
            $ bryce_post_mood += 1
            
        "I'm sure it'll be there in the morning.":
            c "If it contains what I think it contains, nobody will touch it."
    scene np4 with dissolve
    $ renpy.pause(1.0)
    m "We were both silent for a while and the only sound was our footsteps. Each of his footfalls was a dull thud like the beat of a drum. He stopped and looked up at the night sky."
    show bryce normal with dissolve
    Br normal "So it's really going to hit, isn't it? And it's going to kill all of us?"
    
    menu:
        "Yes, it will.":
            c "And there's nothing you can do."
            
        "Not all at once.":
            c "The impact itself will only kill everyone within a few hundred miles, but it will wreak havoc on your ecosystem. The debris will block out the sun for years. Some dragons may survive by feeding off the corpses of whatever is left. But eventually, yes. I'd say in two years, there won't be a single living dragon left on earth."
            
    Br "Well, there's still work to do around here until then. We have to figure out what to do with your friend Reza."
    
    menu:
        "Reza is not my friend.":
            Br "I know. And he's not your responsibility, either, so don't feel guilty for what he did. I've seen good people go bad. Their family and friends always feel responsible, but the choice was theirs alone."
        
        "We'll have to let my people decide what to do with him.":
            Br "What do you think will happen to him?"
            c "He'll probably just be executed or exiled from the city, which is nearly the same thing. We don't really have the spare resources to feed and care for someone in prison."
    
    Br "We'll have to arrange an escort or something so he doesn't get attacked on the way to the portal. There are a lot of people who'd like to see him dead because of what he's done."
    
    menu:
        "It's a shame we have to take him.":
            Br "I know. But he's still an ambassador and therefore has diplomatic immunity."
            c "I think he forfeited his diplomatic immunity when he shot Maverick and murdered three people."
            Br "Still, he's in our custody now."
            
        "I think we should just leave him here to die.":
            Br stern "And he'd deserve it. But you never know what kind of mischief he'd get up to alone here. It's not worth it the risk."
            $ bryce_post_mood -= 1
            
    c "What do you think will happen to Anna?"
    Br normal "I'll keep my word. Tomorrow I'll write up an official pardon outlining the fact that she admitted to her transgression against the law, but due to her valued contribution to society, her crimes are forgiven."
    c "That sounded very official."
    Br "I'm only quoting the forms."
    c "Do you write a lot of pardons?"
    Br "No, but I've always wanted to."
    c "Are they hard to get?"
    Br "They're only given out when someone does a very important deed, like saving multiple people. Why do you ask?"
    c "I thought it was just for when you can't understand someone."
    Br "What?"
    c "I beg your pardon?"
    Br "..."
    Br laugh "HA! Good one. Actually, that was terrible."
    c "You still laughed."
    Br normal "True. Anyways, we'll see about Emera. I'm sure I can convince her."
    Br flirty "I can be very convincing when I want to."
    
    menu:
        "Yes you can.":
            Br normal "I managed to convince you."
            c "The wine helped."
            $ bryce_post_mood += 1
       
        "Are the two of you seeing each other?":
            Br normal "Only at work. I didn't know if I should make a move in case, you know. There might be someone else I'm interested in."
            c "Do I know this person?"
            Br "Pretty well, I'd say."
            c "Well, whoever it is, I'm sure they'd be happy to be with you."
            
    c "Can I ask you a question?"
    Br "Alright."
    
    $ post_choice_dict = {}
    
label post_bryce_menu:
    menu:
        "Do you think Anna was justified in what she did?" if 0 not in post_choice_dict:
            Br "I'm not sure of the extent of what she did, so I can't make judgments."
            c "Do you think she's lying? Or she did more than what she told us?"
            Br "No, I mean I wasn't really paying attention to her story. Once she started talking about her childhood I kind of zoned out."
            c "Don't you have to hear stories from victims all the time?"
            Br "Yeah, but Naomi usually writes it down and I read over the stuff I missed."
            $ post_choice_dict[0] = True
            jump post_bryce_menu
            
        "How do you take off your badge?" if 1 not in post_choice_dict:
            c "Can you even reach?"
            Br "Like this!"
            m "The great dragon leaned forward and shook his head. The badge on its chain fell to the ground and he picked it up with his teeth."
            Br "Ftill wouw we easier wiwf has."
            c "What?"
            m "He flipped his head back and the badge fell back into place around his neck."
            Br "It still would be easier with hands."
            c "Keep on practising your shipbuilding and you'll get better at it."
            $ bryce_post_mood += 1
            $ post_choice_dict[1] = True
            jump post_bryce_menu
            
        "Do you ever build model spaceships?" if 2 not in post_choice_dict:
            Br "What's a spaceship?"
            c "It's like a regular ship but it flies in space."
            Br "Do you have those where you come from?"
            c "We used to."
            Br "Where did you go?"
            c "We went to the Moon more than a century ago."
            $ post_choice_dict[2] = True
            jump post_bryce_menu
        
            
        "What would you do if you knew you couldn't get through the portal?" if 3 not in post_choice_dict:
            Br "I'd probably be swamped with work. If the world was ending there would be anarchy. But in all honesty, I'd probably just drink and fuck the rest of my short life away."
            c "That's as good a plan as any."
            $ post_choice_dict[3] = True
            jump post_bryce_menu
            
        "That was it.":
            if len(post_choice_dict) == 0:
                Br "Uh, okay."
                
    scene np5e with dissolve
    $ renpy.pause(1.0)
    m "I hadn't realized it, but we had arrived at my doorstep. I wondered if I should invite him in. I wanted to, but so far he hadn't given me any indication he felt the same way. Luckily he broke the tension."
    show bryce normal with dissolve
    Br "Are you going to invite me in or what?"
    
    menu:
        "Of course.":
            c "You didn't think I'd make you walk home alone, did you?"
            Br flirty "Who needs a fun basket when you have your own fun package?"
            $ bryce_post_mood += 1
            
        "I don't think so.":
            Br "Really? I could help you sleep."
            c "Really, I'm okay. Thanks."
        
    stop music fadeout 4.0
    play sound "fx/door/handle.wav"
    $ renpy.pause(1.0)
    scene black with fade
    $ renpy.pause(4.0)
    
    return