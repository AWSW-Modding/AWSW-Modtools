label adine_post_true_bootstrap:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ player_name = persistent.player_name
    
    jump adine_post_true_entry

label adine_post_true_entry:
    $ adine_post_mood = 0

    $ adinestagename = persistent.adinestagename
    $ can_cont = True
    $ restore_ui()
    stop music fadeout 1.0
    stop sound fadeout 1.0 
    
    scene black with fade
    $ renpy.pause (1.0) 
    scene np3 with fade
    play music "mx/adine3.ogg" fadein 1.0
    $ renpy.pause (1.0)
    
    m "The last few hours felt like a dream, or a memory of a dream I had many times before. Izumi was dead, Reza was captured, and both worlds were safe - for now. No doubt it would all make sense in the morning but now I just wanted to get home and get some rest. Adine and I walked back to town from the portal, together. "
    show adine normal with dissolve
    $ renpy.pause(0.5)
    Ad "So what are you gonna to do now, [player_name]?"
    c "I don't know. It seems like I've got everything right this time so I won't have to do it all over again. If I have to, I will. But a part of me just wants to continue on and see what happens."
    Ad "I hope you can stay."
    c "Me too."
    m "I noticed she kept looking up at the night sky. Above us, the dusty cloud of the Milky Way stretched from horizon to horizon. Countless stars twinkled in the firmament, as if someone had spilled sugar across a black tabletop."
    c "Are you thinking you'd rather be flying?"
    Ad "No, I like walking with you. I was just wondering which one is the comet."
    
    menu:
        "I don't know.":
            c "I don't know. If I took a picture tonight and tomorrow night I could compare them and see which one moved. But it wouldn't help."
            Ad "And you really know it's going to hit?"
            
        "The one on the left.":
            m "She smiled faintly but still didn't look in my direction."
            Ad "I guess it wouldn't help knowing."
            $ adine_post_mood += 1
            
    Ad "You know, I never really looked up at the sky like this. I mean, I've seen it before, but I didn't really think about what's really up there."
    c "We can sit down and look if you'd like. I'm not in a hurry."
    m "There was a park bench close by and we sat down next to each other. The night was cool and since we weren't moving anymore, I shivered. Adine shifted and draped a wing over my shoulders. It was thin but soft as a leather jacket, and surprisingly warm. Her gesture was perfectly natural, like it was something she'd do without thinking."
    menu:
        "Put your arm around her.":
            $ hugged_adine = True
            m "I put my arm around her shoulders. I could feel the individual scales under my fingers, and 	warmth radiating through the bulge of her flight muscles under them. She didn't say anything but I saw the corner of her mouth curl up in a little smile as she gazed upwards."
            $ adine_post_mood += 1
        
        "Do nothing.":
            $ hugged_adine = False
            c "We sat together and it was a while before she spoke."
            
    Ad "Is there any way we could survive it? By hiding in caves or underground?"
    c "Not for long. You might be able to survive the initial blast but not the winter after. When I learned about the comet in school I heard it kicked up so much dust and rocks it blocked out the sun for years. Almost nothing will survive."
    Ad sad "Do we have any chance of stopping it?"
    c "I don't know. If not, we'll have to evacuate everyone through the portal. But if the generators continue working, we should be able to send people through continuously."
    Ad normal "As long as the children from the orphanage make it, I'll be happy."
    c "The limiting factor is mass, so smaller, younger dragons would be prioritized, so you don't have to worry about them. And someone has to take care of them, so you'd definitely have a spot."
    Ad "And there's going to be space for us on the other side?"
    c "We'll find something for you. As long as you can make yourself useful, you'll be accepted. You're skilled enough you can find work."
    Ad annoyed "I guess you need waitresses too, right?"
    c "Actually, I was thinking you would make a good ambassador for your kind."
    Ad normal "Really? But I don't have any experience in that."
    c "Sure you do. It's not that much different from what you do at your job. You're already good at listening to what people need, you try to help them, and just be polite and understanding. That's all I do, and it's worked out pretty well for me so far."
    Ad "I guess that's true. Still, it seems pretty important."
    c "You don't have to, just keep it in mind. Out of everyone I've met, I thought you'd be the best for it."
    Ad "If I said no, who else would you chose?"
    
    menu:
        "Remy.":
            c "He's already used to working with the public, even if they're not nice to him. He has a lot of knowledge at his disposal so that would be useful too."
        "Anna.":
            c "She works in the scientific field, and her research would be invaluable to us. There may be something she learned that we haven't figured out yet, or something we knew and lost."
        "Bryce.":
            c "Even if he's not the most subtle person here, people respect him. He can get things done, here, or in my world."
        "Lorem.":
            c "He's crafting a story based on humans so he's done a lot of research. I'd say he 	knows more about humanity than anyone else here besides me."
            
    c "But I figured you're better at communicating with people, and you're more honest than any politician I've ever met. I think you could help our two species live together."
    Ad "If I could, I think I would like to. I don't know if I'd be up to the responsibility, but I'd try my best. I'd definitely owe you."
    
    menu:
        "Don't worry about it.":
            c "You'd be doing me a favour just by working with me. I could use 	your help."
            Ad "I hope I can do a good job, then. "
        "I accept cash or credit.":
            c "You're so silly, [player_name]!"
            $ adine_post_mood += 1
    
    Ad "But really, you don't know how much that means to me. I never really made anything of myself besides earning enough to survive. I always wanted to make a difference, but I never imagined I'd be doing something as important as this. You even talked me out of doing that flying competition. I could have seriously hurt myself."
    Ad sad "I could have died!"
    c "It's partly my fault. You crashed the first time when I was there. If I wasn't, you might not have."
    Ad giggle "You must have distracted me! Maybe I was showing off for you."
    c "Still, I feel partly to blame."
    Ad normal "I don't think it's really your fault at all. Don't blame yourself over what's out of your control. Nobody can tell what's going to happen in the future."
    c "I guess I shouldn't. See, I told you you'd be a good ambassador. You're good at talking to people."
    Ad "Unless you {i}could{/i} have foreseen that, if you're really from the future? Maybe you've done all this before."
    c "Maybe, but when it happened I didn't remember it."
    Ad "I still don't think I understand it."
    c "Neither do I, and I've done it who knows how many times. All I know is that there are multiple timelines, and I did them all one after another. But I've never done this. I've never got this far before."
    Ad "So I could do something completely random and you wouldn't see it coming!"
    m "There was a playfulness in her eyes. It was the look a child has when they know they're up to no good."
    c "I guess not."
    
    if hugged_adine:
        m "Before I could react, she leaned forward and kissed the tip of my nose."
    else:
        m "She pulled her wing closed so I was pushed towards her chest. She put her wings over my head like a big yellow tent and tousled my hair until I broke free."

    Ad giggle "I bet you didn't expect that!"
    c "No, I didn't."
    m "When I looked at her we were close enough I could see the stars reflected in her eyes. Suddenly she pulled away."
    Ad normal "I guess we should get going."
    m "We got up and continued along our path."
    Ad "What else would I do in your world?"
    
    menu:
        "That will take up all your time.":
            Ad "Really? I'd like to have some time to help the orphanage."
            c "We'll have to find someone else to run it."
            Ad sad "I don't know if I'd even want to, then."
            $ adine_post_mood -= 1
            
        "You can run the orphanage on my world as well.":
            c "Besides, I'm sure there are plenty of humans that would be willing to adopt a dragon child. Heck, I would."
            Ad "Really? Do you have one in mind you'd like?"
            c "I don't know yet."
            Ad "Whichever one you chose, I'm sure they would love you! Everyone else here does."
            
        "Flying.":
            c "We don't have many vehicles, so a flyer like you would be valued. I think you could make a good living just delivering equipment across the city. It might not have much glory in it, but you'll be helping. You could even restart that flying competition."
            Ad "Oh! Do you think humans would want to watch that?"
            c "I'm sure they would, The Amazing [adinestagename]."
            $ adine_post_mood += 1
            
    c "No matter what, you'll be able to keep yourself busy."
    Ad normal "I wonder how humans will react when they see me."
    c "They'll probably say, \"Oh! It's a dragon!\" every time, and you'll know what I felt when I first arrived here."
    Ad "Ha! I guess that would get annoying after a while."
    c "It wasn't when {i}you{/i} said it."
    m "I hadn't realized it, but we had arrived at my doorstep. I wondered if I should invite her in. I wanted to, but so far she hadn't given me any indication she felt the same way. Luckily she broke the tension."
    Ad "What are the beaches like in your home?"
    c "Not as nice as here, but it's basically the same deal. Why do you ask?"
    Ad "One of theses days you'll have to teach me how to build a sandcastle. And we can enter a competition together!"
    c "I'm looking forward to that."
    
    if persistent.seashells:
        Ad "I put those seashells you gave me on my bookshelf. They're very pretty."
        c "They suit you, then."
        Ad giggle "Really? You think I'm pretty?"
        c "Of course I do. Who wouldn't?"
        Ad normal "Does it matter that I'm a dragon?"
        c "Not to me."
        
    $ ply_fl = player_name[:1]
    Ad "We could call our creation \"A[ply_fl]COF\"."
    c "What? What's that?"
    Ad "Adine and [player_name]'s Castle of Friendship!"
    
    menu:
        "Am I just your friend? I thought we were more than that.":
            Ad "What do you mean?"
            c "Where I come from, friends usually don't shower together. That's only for couples."
            Ad annoyed "Where you come from, people wear clothes."
            c "You took off your goggles."
            Ad "They would fog up otherwise."
            c "I guess I misinterpreted it."
            Ad "I guess so."
            $ adine_post_mood -= 2
            
        "Hopefully our real friendship lasts longer than the sandcastle.":
            Ad "I'm sure it will."
            
    
    m "She stepped back and glanced down at the key in my hand, then at my front door."