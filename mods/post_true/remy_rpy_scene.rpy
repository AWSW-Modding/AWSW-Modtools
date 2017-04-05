label remy_post_true_bootstrap:
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    jump remy_post_true_entry

label remy_post_true_entry:
    $ remy_post_mood = 0
    call _mod_fixui
    stop music fadeout 1.0
    stop sound fadeout 1.0
    
    scene black with fade
    $ renpy.pause (1.0)
    scene np3 with fade
    #play music "mx/_.ogg" fadein 1.0
    $ renpy.pause (1.0)
    
    m "The last few hours felt like a dream, or a memory of a dream I had many times before. Izumi was dead, Reza was captured, and both worlds were safe - for now. No doubt it would all make sense in the morning but now I just wanted to get home and get some rest. Remy and I walked back to town from the portal, together."
    show remy normal with dissolve
    $ renpy.pause(0.5)
    Ry "What are you going to do now?"
    c "I don't know. It seems like I've got everything right this time so I won't have to do it all over again. If I have to, I will. But a part of me just wants to continue on and see what happens."
    Ry "What do you mean, this time? Do you remember what happened in different timelines?"
    c "Not very well. But well enough this feels like everything's in place."
    Ry "I don't know if it's just me, but it feels better somehow. It feels right."
    c "That's good. How are you and Amely doing?"
    Ry smile "She finally started talking. It took a few days but once she started she didn't stop. I think she had been silent for so long all her thoughts were bubbling up inside her and they finally burst out. It's funny, sometimes she narrates what I'm doing: \"Remy is opening the cupboard, he's looking inside, now he's getting plates out.\" In an odd way, her voice voice reminds me of..."
    show remy sad with dissolve
    m "Remy trailed off and looked away. The only sound was our footsteps, the even and steady patter of his paws against the gravel. It sounded like someone tapping against a desk while they're waiting for something. When Remy looked back his voice was steady but eyes were bright and glassy."
    $ renpy.pause(1.0)
    scene np4 with dissolve
    $ renpy.pause(1.0)
    show remy normal with dissolve
    Ry normal "When you go back in time, how far back can you go?"
    c "Only as far back as when the portal was built. And I would need to know the spacetime coordinates of that location."
    Ry "What do you mean, coordinates? Does the portal move?"
    c "Yes, in spacetime. The Earth itself is moving, so if you went back or forward in time to this location, you'd end up floating in space."
    Ry "I see. Is there anyway of finding out the coordinates of a given date?"
    c "Probably, that's how they sent me back here in the first place. But I don't know how. The first time, the coordinates were loaded into the portal's computer before I arrived, and every time after that, Izumi loaded it."
    Ry "The dragon nodded. He looked like he was deep in thought. His front claw wandered to his tie and gently touched it."
    
    menu:
        "You can't use it to go back in time, if you're wondering.":
            Ry "I just thought, if it was possible..."
            c "It's not. Even if there was someone who could figure out the coordinates, they wouldn't want you messing with the past."
            Ry "I suppose that's for the best."
            c "It is. There's no telling what might happen once people start messing with the distant past."
            
        "You'll just have to deal with the present now.":
            c "If you can go back as many times as you 	want, what's the value in the present moment? Why bother doing anything if you can just go 	back and redo it?"
            Ry "I suppose that's true, in a way."
            c "It's what I've learned. I don't know how many times I've met you for the first time. After a while the experience is diminished."
            
    c "I know what you're thinking but it's just not worth it."
    Ry "You've never done anything you regret? Something you want to go back and try again?"
    c "Sure. But I don't want to risk it unless I have to."
    Ry normal "You've gone back how many dozens or hundreds of times?"
    c "When I did it, it's worth the risk."
    Ry angry "Worth the risk to who?"
    c "To humanity, and to dragonkind. Not just one person."
    Ry "Do you know how many times I've thought about saving her? I dreamed about being able to go back. I dreamed about how I could have saved her had I just {i}been by her side{/i} instead of abandoning her when she needed me most." with Shake((0, 0, 0, 0), 2, dist=10)
    Ry "Do you have any idea how many sleepless nights I've spent looking at that picture of her, just weeping and wishing I could go into the picture? One time I broke the glass frame and cut myself because I was holding it so hard."
    Ry "Eventually I had enough. I thought if I couldn't be with her in this life, I could in another.  A week ago, I bought a rope. I tied it in a noose and hung it from my ceiling. I only stopped because-"
    c "Adine phoned you and asked if you wanted to adopt Vara."
    Ry sad "W-what? Did she tell you?"
    c "No, I told her you were looking to adopt. I know she called you because in another timeline, I didn't tell you about Adine's work at the orphanage. In that timeline, you killed yourself."
    c "I was going to take a PDA to you at work. You weren't there, so I went to your house to drop it off and I saw you hanging from the ceiling. I must have remembered that timeline because in this one, there was a voice telling me to tell you about the adoption in the back of my mind. Now I know why."
    Ry "..."
    c "You can't change the past, Remy. I wish I could help you bring her back, but you can't. If we went back that far, it would completely destabilize this timeline and all the work I've done here, all the hundreds of deaths I've died, would be for nothing. I'm sorry, but she's gone and you'll never get her back."
    Ry "I could at least try."
    c "In one timeline, Vara died. She snuck out and followed us to the portal and was shot by Reza. I don't even know what I did to prevent that this time. "
    c "If we went back to save your fiancee, you might not have been there to greet me when I came out of the portal. Then I'd never met you and I never would have had a reason to help you go back and save her. Major changes like that can cause paradoxes we don't even understand."
    Ry normal "I suppose you're right, of course."
    c "She must have really been something for you to care so much."
    Ry "She was. I can't describe her in words. Even trying would be an injustice to her. I could quote a song or recite a poem but it wouldn't describe what I felt when I saw her. But I don't want to bore you with that."
    
    menu:
        "Thanks.":
            Ry sad "Sorry."
            $ remy_post_mood -= 1
            
        "It's okay. I like listening to you.":
            Ry "Amelia was the one I could always talk to. She was the only constant in the constantly changing world. No matter how badly I was treated at work, I could always come home and see her, and instantly feel better. I think it's fair to say she was the only person in the world I liked."
            Ry sad "When she died it was like I had been hollowed out and left to dry. I've never got over it and I don't think I ever will. I tried to forget her and I couldn't."
            c "What did you do?"
            
        "It's good to get it off your chest.":
            c "Clearly this is something you've been holding inside you for a long time. It's not healthy to keep it inside you."
            Ry "I know. I've always known that. But it's not like anyone cares or listens."
            c "I care. Tell me."
            $ remy_post_mood += 1
            
    
    Ry sad "Ever since I lost her, I've always wanted to escape, to just stop being who I was. The only time I wasn't depressed was when I was asleep. When I went to bed, I looked forward to getting away from the world, even if it was just for eight hours at a time, and I dreaded waking up."
    Ry "Other times, I immersed myself in novels. Some of the best one are the ones I left in your apartment. Being able to lose myself in a book was the closest thing I had to being someone else. Then I found videogames. The one you played in my office, I liked it because I could lose myself in that world."
    Ry "Because there, I wasn't Remy the librarian. I was a hero. The characters liked me. But as soon as I turned it off I saw my own reflection looking back at me and I remembered it was nothing more than a fantasy."
    c "I'm sorry. I didn't realize it was that important to you."
    Ry normal "Don't be sorry, it shouldn't have been that important. It's just a stupid videogame. But when I played it, I could actually make accomplishments. Even if they were as insipid and useless as watching a number increase on a screen."
    Ry "It felt like I had achieved something, even if I knew it as artificial as the in-game sprites. And the harder it was, the more accomplished I felt. That's why I was so angry when you ruined my progress. I felt I had lost hundreds of hours of my life, and realizing that made me realize what a useless waste of time it was."
    c "If it entertains you, it's not a waste of time."
    Ry "But it didn't even entertain me. It was just endless grinding, simple combos and memorizing where to click on a screen. I just played it to lose myself and to pretend I was accomplishing something even though I knew it was artificial. Even though I knew it was just a story."
    c "Sometimes stories can have truths in them, even if they're just a metaphor. They can be more true than the reality that we live in."
    Ry "I guess that's true. I haven't touched it since adopting Amely. I guess I didn't need to. You helped me more than you might think. You gave me hope after I thought I would never have it again."
    c "I'm just doing my job."
    Ry "This goes beyond that, doesn't it? You came here to represent your species, not give individuals life advice."
    c "I came here to help people, and that's what I'm doing."
    Ry "I appreciate it. Although it doesn't really matter anymore, does it?"
    c "What do you mean?"
    m "Remy stopped and looked up at the night sky. Somewhere among the thousands of bright points was the comet that would kill every dragon on Earth unless we did something to prevent it."
    Ry "It's really going to hit, isn't it?"
    c "Yes. And it will-"
    Ry sad "No, don't tell me. I don't even want to know what's going to happen."
    c "You'll get through the portal."
    Ry normal "You say that as if you know if for sure."
    c "I'm humanity's ambassador, I can bring whoever I want. I'll try to bring as many people through as I can, but I'll make sure you come with me first."
    Ry "Why would you choose me?"
    $ joke_response = False
    
label remy_post_menu1:
    menu:
        "I want to start a band with you called Remy and me." if not joke_response:
            c "I'm a pretty good guitarist, how are you at singing?"
            m "Remy looked at me as if he didn't know whether to laugh or not."
            Ry "Okay. I appreciate you trying to lighten the tension, but what's the real reason?"
            $ joke_response = True
            jump remy_post_menu1
            
        "That is the real reason." if joke_response:
            Ry "Well, I can't sing, and I've never learned an instrument."
            c "You can't come then."
            Ry "Be serious. This is important."
            c "I am serious."
            $ remy_post_mood -= 2
            
        "Because you're a lot more valuable than you realize.":
            c "Emera chose you because you're smart and useful. Even if she doesn't respect you, she still sees your value. I see it too, but I respect you as well. You're good at working with people."
            Ry "I've never been good with people."
            c "I think you are, but you've just forgotten. You managed to convince someone to marry you once. And you're already a good father even though you've only been doing it a few days. I think you have the potential to be a great person."
            $ remy_post_mood += 1
            
        "Because I like you.":
            c "Do I really need another reason?"
            Ry "Really? Do you mean as a friend, or something else?"
            $ remy_post_mood += 2
            
            menu:
                "Just as a friend.":
                    Ry sad "Oh. I guess that's fine, then."
                    Ry "I just thought..."
                    Ry "Never mind."
                    $ remy_post_mood -= 2
                    
                "I don't know yet.":
                    Ry "Well, maybe we can find out together. I don't want to be too forward but I have to say, I like spending time with you."
                    c "Maybe we should spend more time together."
                    Ry smile "That sounds like a good idea to me."
                    
                "As more than a friend.":
                    Ry "Really? I have to say, after I lost Amelia, I never thought I'd feel that way about someone again. At least not for a very long time. But..."
                    Ry shy "I guess we can be more than friends, if you want." # TODO: check that this is correct
                    $ remy_post_mood += 2
                    
    Ry normal "If you could work with anyone else, who would it be?"
    
    menu:
        "Anna.":
            c "I thought her scientific and medical knowledge would be valuable to humanity. It's something we're lacking and we desperately need."
        "Adine.":
            c "She works with different people every day, and that experience is helpful. If we worked together she'd be a great help."
        "Bryce.":
            c "He's already a respected figure here. If I allied myself with him, I'd look more legitimate. "
        "Lorem.":
            c "He's creating a story based on humans. I thought if we worked together, he could make it all the more accurate and interesting."
    
    c "But none of those people would be as good as you."
    scene np5e with dissolve
    $ renpy.pause(1.0)
    m "I hadn't realized it, but we had arrived at my doorstep. I wondered if I should invite him in. I wanted to, but so far he hadn't given me any indication he felt the same way. Luckily he broke the tension."
    show remy normal with dissolve
    Ry "Well, I guess I'll head home now."
    
    menu:
        "Okay, bye.":
            $ remy_post_mood -= 1
            $ renpy.pause(0.5)
            show remy normal flip
            $ renpy.pause(0.3)
            hide remy with easeoutright
            
        "Would you like to come inside?":
            Ry smile "Of course."
            
            
    play sound "fx/door/handle.wav"
    $ renpy.pause(1.0)
    scene black with fade
    $ renpy.pause(4.0)
    return