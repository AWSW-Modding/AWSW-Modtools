label anna_post_true_entry:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    jump anna_post_true_entry
                
    # Post true ending, the game locks all player interaction. We need to re-enable the UI controls to allow the play to play the scene.
    
    $ can_cont = True
    $ restore_ui()
    stop music fadeout 1.0 # These stop any music or sounds that are playing. 
    stop sound fadeout 1.0 
    
    scene black with fade # Fade to black
    $ renpy.pause (1.0) # Halt execution for 1.0 second. This will make the game sit at the black screen for 1 second before fading in np3 (look at images.rpy for the image IDs)
    scene np3 with fade # np3 is mapped to a specific cg file in the game. It is defined as "image np3 = 'bg/out/np/np3.jpg'"
    play music "mx/anna4.ogg" fadein 1.0 # Play some music with a fade in time of 1 second. 
    $ renpy.pause (1.0)
    
    # 'm' is the narrator character. This makes a text box with no name appear on the screen. 
    m "The last few hours felt like a dream or a memory of a dream I had many times before. Reza was dead, and both worlds were safe - for now. No doubt it would all make sense in the morning but now I just wanted to get home and get some rest. Anna and I walked back to town from the portal, together."
    show anna normal with dissolve # The show instruction, well, shows a character. See images.rpy in the AWSW code for the whole list (you'll need these).
    $ renpy.pause(0.5)
    An "What are you going to do now?" # An is the identifier for anna's character object. Once again, defined in images.rpy. This is a Say instruction.
    c "I don't know. It seems like I've got everything right this time so I won't have to do it all over again. If I have to, I will. But a part of me just wants to continue on and see what happens."
    
    # This changes Anna's expression to the second following keyword (smirk) when the say instruction fires off. 
    An smirk "Great. I'll have to put up with you even more?" # this allows us to change a character's expression. It persists until another instruction that specifies a different expression. 
    m "She was trying her best to sound sarcastic but I saw a smirk on her scaly lips."
    c "I guess you will."
    An normal "I don't know what I'll do. I still don't know if I'll be pardoned. I know what Bryce said, but he can only do so much if the courts decide I'm guilty."
    c "I don't think they'll arrest you. You may have broken the law, but it was for the greater good. Not everyone can see that, but I think enough people will."
    An "It would be ironic to be stuck in prison while a comet hit."
    m "Her expression changed, like the full realization of what she just said hit her."
    An sad "Are you really sure it will happen?"
    
    menu:
        "I don't know.":
            c "I don't know. But I know it will be bad."
        "Yes.":
            c "Yes. I learned about the comet in school. When it hits, it will destroy your ecosystem. It will throw enough debris into the air it will block out the sun and freeze the planet in a winter that lasts a decade. Everything heavier than a kilogram will starve to death in a year."
    
    An normal "Well... if it turns out I don't make it, I was glad to have known you for this short time. I was serious when I said you're the person I hate the least."
    c "I have to say, I barely hate you at all at this point."
    An smirk "Same here."
    m "I thought about something that had been bugging me for the last few days."
    
    c "Seriously. Sneaking onto that farm and eating freshly-killed meat was the best first date I've ever been on. But the night we spent together... that wasn't just a one-off thing, was it? Were you just looking to do something spontaneous or did you really want to?"
    
    # Change Anna's expression back to normal, otherwise the previously set one would persist. 
    An normal "If I'm going to be honest, it was a bit of both. There was just so much going on at that point I don't think I was in my right mind. It was spontaneous, but I don't regret it. Do you?"
    
    # 'c' is the MC. 
    c "No. The idea would have been unthinkable when I arrived here a week ago. But now, getting to know you... I don't know. But I'm just wondering, isn't that sort of thing frowned upon here? What would people think?"
    An "Humans have never been here before, so how could people have an opinion on something that's never happened before? A relationship between two different dragon species is unusual, but not unheard of. It's not illegal, if that's what you're thinking. But really, even if they did care, would you?"
    
    # A menu. Each option is indented, followed by a colon. Anything indented after the choice will be executed if the choice is picked. After all choice-specific instructions are ran, the game will skip down below the menu.
    menu:
        "I guess you're right.": 
            c "I guess you're right. It doesn't matter."
            An "If anything, they'd be jealous. Remember, humans are worshiped in our society. A week ago, humans were mythical creatures, and now, a few dozen people have met you."
            c "And now, one person even gets to date me."
            An smirk "And that person is very lucky, indeed."
        "But I represent humanity as a whole.":
            c "But I represent humanity as a whole. I have to put on a good impression for my side as well."  
            An "What do you mean? Do humans not like us?"
            c "It's not that they don't like you. On Earth, dragons are revered. It's just the thought of being romantically involved with one is just weird. Remember, where I come from, humans are the only sentient animals. Dating another species would be seen as disgusting."
            An disgust "And you don't want to be associated with a dumb animal. Right, I get it."
            m "She started to turn off to the side and leave. I held on to her hand, gently but firmly."
            c "But I don't agree with them. You may not be human, but you're still a person, just as much as I am."
        "But I'm a public figure here.":
            c "But I'm a public figure here. People might not care what a stranger does, but everyone here recognizes me. I have to hold a higher standard."
            An "So what, you're afraid of what other people think?"
            c "That's not what I meant. I just have to gauge public opinion on this, and I have to do it subtly."
            An "I didn't know you cared so much about public opinion. I thought you were above that."
            c "It's not just my opinion. I'm serving as humanity's ambassador. I can't put my desires above the success of my mission."
            An disgust "And I thought you were different. I was wrong about you. You're just like Emera. Were you lying about curing cancer, too?"
            c "Of course not, Anna, I would never lie about something like that. I'm on an important mission, so I can't just do whatever I want, or be with the people I like."
    
    # The game skips to here after running all the choice-specific instructions. 
    An face "I'm not a fan of politics if you haven't noticed. It's just a group of people trying to guess what everyone else wants, and at the same time, lying about what they themselves want. When you first came here I thought you'd be like one of {i}them{/i}. A selfish, corrupt bureaucrat. But..."
    An smirk "...you're different."
    m "She made a warm, honest smile that was infectious. It was an expression I had seen on her face all too rarely."
    c "I guess I was just able to see something that others didn't."
    An normal "Sorry. I know I'm not the easiest person to deal with sometimes. Nobody else has given me a chance, and you've given me plenty. I know I don't deserve it."
    c "You do. You just don't know it yet, and I want to show you."
    An smirk "You always know what to say."
    
    menu:
        "I guess that's why I was chosen to be humanity's ambassador.":
            An normal "How do you do it? How do you get along with people so well?"
            c "I don't know. I think it's because I try to look at the good things in life and I'm just honest with people, and along the way, I just try to be nice. You'd be surprised how far that gets you."
            An "I guess I should try, now that I know I'm going to be sticking around for a bit longer. Before, I didn't really care how people saw me. I figured I'd either die or I'd invent a cure for cancer, then people would have to respect me, even if they didn't like me."
            
        "That's my job.":
            An normal "Are you like this around everyone?"
            c "I get along with almost everyone. There are a few people that don't like me but there's nothing I can do about them."
            An sad "But how do I know you're being honest with me now? Part of politics is lying. Everyone knows that. Emera plays the political game so well you can never tell whether she's speaking her mind or simply regurgitating popular opinion."
            c "But I actually like you. I'm not just trying to get something out of you."
            An normal "Do you promise?"
            c "I promise."

    An "Is everything just politics to you?"
    c "Not everything. Being with you isn't. That's why I like it."
    An sad "Nobody likes being with me."
    c "I do. When I'm with you I can forget about the problems between our two species, and my mission, even if it's only for a few hours. When I'm with you I get to relax."
    An normal "But you didn't come here to make friends. If your mission is so important, why are you wasting time with me at all?"
    c "Part of my mission is to learn about your kind, and in order to do that, I have to get to know your species. If all I wanted to do was interview people, I could have spent time with anyone."
    An sad "What do you mean, anyone?"
    
    menu:
        "Remy.":
            c "I thought about the huge amount of information at his disposal. He could get me access to potentially all of the knowledge of your species."
            
        "Adine.":
            c "She meets dozens of new people every day so she's an ambassador in her own way. If we worked together I thought we'd be more effective."
         
        "Bryce.":
            c "As the chief of police, he's in a position of authority. With him, I could get access to people and places I might not otherwise have, and it would be a political step up from a simple ambassador. I'd have authority of my own."
            
        "Lorem.":
            c "I can only meet so many people myself. Everyone else's experience with humans would have been through media. Lorem was crafting a story based on humans, and I thought if I could work with him, I could influence dragonkind's perception of humans however I wanted."
            
    c "But in the end, it wasn't a political decision. It was an emotional one. I chose to be with you because I like you. I saw something in you, something that I don't think others do. Something that I don't think even you saw."
    An normal "What did you see?"
    m "The dragon stepped close to me. Her eyes were wide and I could see the row of streetlights in them, glowing faintly like a line of fireflies. Her eyes were filled with something I hadn't seen in them before: hope. The words gushed out before I knew they were coming."
    c "I saw potential. That you could be something great if only somebody could show you. I thought that person could be me. You're brilliant and skilled, but hopelessly independent and stubborn. You know how people underestimate you, but I think you underestimate yourself."
    c "You're going to change the world, Anna, if only you believe in yourself and realize your true potential. But you won't get far without someone to support you. I thought I could help you. You're a better friend than any I've met here, and I thought you might become even more. Do you think it... do you think {i}we{/i} could happen?" 

    scene np4 with dissolve
    $ renpy.pause(1.0)
    m "Anna was quiet for a bit and the only sounds were our footsteps. My shoes thunked against the path and her scaly claws clinked as they struck pebbles in the path."
    show anna normal with dissolve
    An "I think we can be more."
    An "We'll see what we become."
    scene np5e with dissolve
    $ renpy.pause(1.0)
    m "I hadn't realized it, but we had arrived at my doorstep. I wondered if I should invite her in. I wanted to, but so far she hadn't given me any indication she felt the same way. Luckily she broke the tension."
    show anna normal with dissolve
    An "You said cancer was cured in your world. How do they do it?"
    
    menu:
        "I'm not a doctor.":
            c "I'm not a doctor, so I don't know the process exactly. I just know that if the cancer is detected early enough, it's almost never fatal. If I got cancer, I'd be worried, but I wouldn't lose sleep over it. I'm not going to pretend it's 100%% guaranteed to work, but you still have a chance."
            
        "They give you lots of drugs.":
            c "They give you a lot of drugs, and if they find tumours there's radiation and surgery involved. From what I've heard, the process is unpleasant, but it's better than dying. I don't know how easy it will be with your different biology, but you still have a chance."
            
    stop music fadeout 4.0
    play sound "fx/door/handle.wav"
    $ renpy.pause(1.0)
    scene black with fade
    $ renpy.pause(4.0)

    #play sound "fx/door/doorclose3.wav"
    return # Return to wherever we came from. It could be the main menu for testing, or back to the rest of the true ending. 