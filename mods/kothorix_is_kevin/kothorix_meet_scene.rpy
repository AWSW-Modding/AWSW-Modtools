#This mod was supposed to be a bit of fun and practice but it's turned into something bigger and meta.
#This is more than a little bit pointless, I never even used this :3
label Kothorix_mod_bootstrap:
  
    $ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
    $ lorem2unplayed = False
    $ remy1unplayed = False
    $ exampleroute_scene = 0 
    $ MeetKothorix = 0 
    $ KothorixDated = 0
    $ toPortal = False

    #the jump the meat of the mod
    jump Kothorix_mod

#Used to initialize variables needed to date Kothorix, because who wouldn't want to.
label KothorixDate_init:
        #I don't know what this does but I'm too scared to get rid of it
    $ exampleroute_scene = 0 
        #Variable used to see if player has met with Kothorix, Set to 1 when the player brings eggs to hatchery
    $ MeetKothorix = 0 
        #This is set to one when the player plays the Kothorix date scene
    $ KothorixDated = 0 
    return

#Actual meat of the mod
label Kothorix_mod:
    
    #some variables, I hope this doesn't ruin everything
    $ askipsum = False
    $ askremy = False
    $ toPortal = False


    stop music fadeout 2.0 
    stop sound fadeout 2.0 
    
    #Scene had to take place in town3 as for some reason the game flashed that scene for a bit
    $ renpy.pause (0.5)
    scene town3
    play music haze fadein 1.0
    $ renpy.pause (2.0)
    
    #Lines pulled from the met Kevin scene, only difference is the music
    m "I was on my way to the hatchery when I heard a voice call out to me."
    "???" "Hello there!"
    m "I turned around to see an unfamiliar face before me."
    
    show kothorix normal with dissolve
    $ renpy.pause(1.0) 
    Kx "Hey, look at that. It's the human that's almost as famous as I am."
    Kx normal crossed "My name is Kothorix, and I am sure you are aware."
    
    menu: 
        #in kothorix's world someone not knowing who he is, is impossible
        "Never heard of you.":
            Kx displeased "It can tell jokes, too? I've always thought humans were serious creatures."
            Kx normal "Perhaps you would like to introduce yourself."
            
        #Player char pretends to have heard of kothorix for his own Vanity
        "Oh wow i-it's you.":
            Kx "Yes, yes. Please refrain from \"fan-girling\" all over me." 
            
    c "Well, my name is [player_name]. It's good to meet you."
    
    #For the one person that named their human kothorix, XD
    if player_name == "Kothorix":
        Kx displeased "I'm not sure how to feel about that. I've worked hard to give my name a good reputation." 
        c "Likewise, I hope you haven't tarnished my own."
        Kx unamused point "It's times like these that I have to remind myself that imitation is the greatest form of flattery."
        c "..."
    elif player_name == "Adam": #A bit of ego stroking and vanity
        Kx hey you "Hey modmaster, nice to finally met you. I am really excited for this mod."
    elif player_name == "Cryoraptor": #my partner in crime
        Kx eyes closed "Cryoraptor."
        Kx yuno "Y U NO keep mod secret!!!!!" #This is because he leaked info about the mod, XP. I think a horrifying image is punishment enough for such a crime
        
    c "I haven't seen a dragon of your kind. Feathered wings and scales? I take it that you don't come from around here."
    Kx normal crossed "Well spotted. Very few dragons have feather wings, so having them marks one as truly exceptional. The townsfolk don't call me the \"Scaly with Angel Wings\" for nothing, you know." #Multiple times in VC kothorix referred to himself as a Scaly with Angel wings it had to be included.
    Kx "I come from a nearby city. You know how it goes: girls, booze, and too much attention. I end up running to this getaway town to let off some steam. But now, with you and Reza, it seems like I can’t get a break."
    Kx sad down "I don't know if more people are flooding in here because of me, you, or that portal..." #He's still thinking that he's important
    Kx somber face "Sadly, with access to the portal restricted, people are forced to bug me." 
    
    menu:
        #He up's and leaves to go to the portal really fast because he wants to go there but not say that he wants to go there
        "Would you like to visit the portal?":
            $ toPortal = True
            Kx thinking "I just said that access is restricted. How do we get up there?"
            c "I'm an ambassador, so they are not going to stop me."
            Kx thinking "Well, I suppose it would get me out of town for a while. However, let's not stay too long. I don't want my fans to think that some horrible fate has befallen me."
            
            scene black with dissolveslow
            $ renpy.pause (0.5)
            window show

            #It's only when I wrote this part did I realize just how empty this game world is. Yo Saunders simple lines like that ain't hard to include
            n "While we walked towards the portal, I noticed that Kothorix preferred to take the more populated streets."
            n "He waved at several passing people. No one seemed sure if they knew him or not."
            n "A young child ran up to me and shyly asked to \"shake my hand,\" saying that it was a human tradition. While she literally shook my hand, I noticed that Kothorix was waving his mane in a fruitless effort to get attention."
            
            scene black with dissolve
            window hide

            scene np1x at Pan  ((200,200), (450,100), 6.0) with dissolveslow
            $ renpy.pause (3.5)

            c "There it is in all its glory."
            show kothorix normal with dissolve
            
            #I'm proud of this line
            Kx "It's an amazing device, isn't it? How many years has it sat here, only to remain tall, proud and untouched by age? Huh, I guess it and I may have a few things in common."
            Kx thinking "Say, do you have any idea how this works?"
            
            menu:
                "No idea.":
                    c "I have no idea where to start with such a thing."
                    
                #This option appears if you have done the second date with Lorem, it's only then do we met Ipsum.
                #Depending on your status with Lorem you get slightly different dialogue  
                "Ipsum may know." if lorem2unplayed == False:
                    $ askipsum = True
                    if loremstatus == "bad":
                        c "Ipsum is interested in the portal, since he gets a huge nerdgasm when talking about it."
                        Kx thinking "Ipsum? Who's he?"
                        c "He's Lorem's roommate. You know, the little blue postman?"
                        Kx normal "Oh! I know Lorem. He's the... {w=0.7}{nw}"
                        Kx somber face "Nevermind."
                        c "What is it? I hope something humiliating."
                        Kx disgusted "I'm not answering that!"
                    else:
                        c "Ipsum has a strong interest in the portal. He told me a lot about how it could work, but most of it went over my head."
                        Kx thinking "Ipsum? Who's he?"
                        c "He's Lorem's roommate. You know, the little blue postman?"
                        Kx normal "Oh! I know Lorem. He's the... {w=0.7}{nw}"
                        Kx somber face "Nevermind."
                        c "What? Is something wrong?"
                        Kx somber face "Nothing's wrong, but people often treat him badly over it."
                        Kx sad down "As the police would well and truly know, considering how many times he's had to call them."
                    
                #Date Remy once for this option.
                "Remy may know." if remy1unplayed == False:
                    $ askremy = True
                    c "Remy might be able to point you in the right direction."
                    #date Remy 3 times for this text to appear.
                    if remy3unplayed == False:
                        c "He might have a personal interest in the portal considering his old job."
                        Kx normal "Interesting."
                    
                    Kx normal "Where can I find him?"
                    c "He works at the library."
                    Kx "I forgot that Remy works there. I don't get visit the library often."
            
            Kx normal crossed "What was it like going through the portal?"
            c "At first, I was worried that something might go wrong. I assume that's a normal reaction."
            c "Other than that, I saw a lot of flashing images. It was difficult to distinguish them apart."
            Kx thinking "Alright. Did you feel any different once you crossed over?"
            menu:
                "No.":
                    c "Just dizzy and exhausted."
                    
                #Kothorix commented multiple times that the portal heals you for some unexplained reason and gave the neutral ending as an example
                #Have gotten the neutral ending for this option to appear.
                "There is one thing..." if persistent.neutralending == True:
                    c "There used to be a wound on my arm, but it appears to be gone now."
                    Kx wtf "Gone?"
                    c "It seems that way. I really can't explain how."
                    if askremy == True:                    
                        Kx thinking "I'll have to remember that when talking to Remy."
                    elif askipsum == True:
                        Kx thinking "I'll have to remember that when talking to Ipsum."
                    else:
                        Kx thinking "I'll have to remember that."
                        
                       
            Kx normal crossed "It's really calming here. Almost too calm, I might add."
            c "Well, it should be, considering the view, but I can't help but feel tense."
            Kx "I thought there would be a guard around. Why is no one here?"
            c "They are all busy right now, so I guess no one is available to keep watch."
            Kx "We should probably head back before my fans think I'm dead."
            c "..."
            c "Alright, let's go."
            
            scene black with dissolveslow
            $ renpy.pause (2.0)
            scene town3 with dissolve
            
            #Now we are back in town
            show kothorix normal crossed with dissolve
            Kx "Considering your limited but privileged time in my presence, I'll break my \"No Signatures\" rule."
         
            #The card sliding across the screen was an idea ripped from Blackgate, but the implementation had to be different due to this game having multiple resolutions 
            m "He pulled out his wallet, which contained several copies of his business card. He handed one to me."
            show card at truecenter with moveinright
            m "It was an autographed photo that displayed his arrogant face."
            hide card with moveoutleft
      
            c "Uh, thanks?"
            Kx "Don't mention it. You should consider yourself lucky."
    
            menu:
                "Hey, why don't you come over?":
                    Kx disgusted "And fornicate with you? Absolutely not."
                    Kx displeased "I already get to pick from the best dragonesses. Do you not see them?"
                    m "There was a noticeable lack of females around us."
                    Kx uninterested distance "Sorry to disappoint, but I don't fall for the first human who makes an advance on me. Good day to you!"
            
                "Well, it's been nice meeting you.":
                    Kx "It's nice meeting someone who isn't trying to get me into their bed. And with that..." 
                    Kx hey you "I'm Kothorix and you have a rawrnderful day!"
        
        #This is to cut the scene short, if player doesn't want to talk to Kothorix    
        "That's a shame.":
            Kx sad down "Indeed it is. Will there ever be an escape from the fan-girling?" 
            c "Let's hope not."
            Kx normal "Indeed."

            Kx "Considering your limited but privileged time in my presence, I'll break my \"No Signatures\" rule." 
         
            m "He pulled out his wallet, which contained several copies of his business card. He handed one to me."
            show card at truecenter with moveinright
            m "It was an autographed photo that displayed his arrogant face."
            hide card with moveoutleft
      
            c "Uh, thanks?"
            Kx "Don't mention it. You should consider yourself lucky."
            
            menu:
                "Hey, why don't you come over?":
                    Kx disgusted "And fornicate with you? Absolutely not."
                    Kx displeased "I already get to pick from the best dragonesses. Do you not see them?" 
                    m "There was a noticeable lack of females around us."
                    Kx uninterested distance "Sorry to disappoint, but I don't fall for the first human who makes an advance on me. Good day to you!"
            
                "It's been nice meeting you.":
                    Kx "It's nice meeting someone who isn't trying to get me into their bed. And with that..."
                    Kx hey you "I'm Kothorix and you have a rawrnderful day!"

    nvl clear
    $ MeetKothorix = 1
    stop music fadeout 2.0
    scene black with fade
    $ renpy.pause(1.0)
    play music "mx/elegant.ogg" fadein 1.0

    return