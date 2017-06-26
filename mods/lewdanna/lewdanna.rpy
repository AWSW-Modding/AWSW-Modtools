image anna blush = "cr/anna_blush.png"
image anna orgasm = "cr/anna_orgasm.png"
image anna blushpalm = "cr/anna_blushpalm.png"
image anna lipbite = "cr/anna_lipbite.png"

label a4romanceL:

        if not nsfwtoggle:
            return
        
        An smirk "Now stand still..."
            
        m "She effortlessly began to cut through the buttons of my shirt with her claw, all while giving me a sultry look."
            
        An smirk "It is certainly fun looking at you getting all hot and bothered by this."
            
        m "After making her way down to my pants, her expression changed to one of frustration."
            
        An face "Okay, I'm not even going to try to undo this. You do it."
            
        m "I quickly unbuckle my belt and drop the pants, underwear included."
            
        An smirk "Well look who's excited already."
            
        menu:
                "I can't help it, Anna. You're sexy.":
                
                    An smirk "Of course I am. I'm glad that you finally noticed."
                
                "Not like you'd have a reason to complain.":
                
                    An normal "Well, there's always room for improvement."

        m "With little hesitation, she began to give my shaft several tentative licks. I can only shudder in response." 

        An smirk "You haven't done this before, have you, [player_name]?"
            
        menu:
            "You are actually my first.":
                
                An blush "Better make it memorable, then, for both our sakes."
                
            "Y-yes.":
                
                An normal "That was a lame attempt at a lie." 
                    
                An smirk "It was kinda cute though."
                
            "Yes, but never with a dragon.":
                
                An blushpalm "Well that's obvious."

        m "With my member now fully erect, she slid up to lock eyes with me. Her eyes lit up with a lustful glare."
            
        An smirk "Let's see if humans are as great as people make them out to be."
            
        m "I grab my shaft and push the tip into Anna's slit."
            
        m "Anna wastes no time and begins to lower herself onto my length. Her insides felt hot and wet already..."
            
        c "Looks like I wasn't the only one getting excited."
            
        An lipbite "Oh, shut up."
        
        m "She only gives me a second, before lowering her hips down to let the real fun begin."
        
        c "F-fuck..."
        
        m "As I try to relax on the couch, she places her weight on my body, pinning me beneath her." 
        
        An smirk "I'll take over from here..."
        
        m "Just like that, she began to ride me at her own pace."
        
        m "I couldn't help but let out groans of pleasure."

        An blush "You'd better not finish before I do."
        
        c "I-I'll try not to."
        
        m "The riding only got more intense as it went on, her claws digging into my shoulders for support as she had her way with me."
        
        An lipbite "Ngh..."
        
        m "She bit her lip, as if holding herself back. But, her clutch on my shoulders and the intensity in which she rode me showed her true colors."
        
        c "A-Anna..."
        
        An lipbite "Not yet..."
        
        m "She sped up her movement even more, the sound of our sexes slapping filling the room."
        
        show anna orgasm with dissolve

        An "A-Almost t-there..." with Shake((0, 0, 0, 0), 2, dist=5)
        
        $ renpy.pause (1.0)
        
        show anna lipbite with dissolve
        
        m "As she lets out a roar and her slit clenches down on me, she reaches her peak while driving me to my own climax as well."

        $ renpy.pause (1.5)
        
        m "Soon we found ourselves riding the wave of pleasure to it's end, Anna's body laying on me as she panted in exhaustion."
        
        An blush "That wasn't half bad. You're actually better than Damion."
        
        c "Not sure how to take that..."
        
        An normal "Take it how you want. Now just let me rest for a bit. I'm beat..."
        
        $ renpy.pause (1.0)

        "She's just laying on me now... What should i do?"

        menu:
            "Hug her.":
                
                m "I wrap my hands around her as we laid on the couch. Seeing as she raised no objections I kept embracing her until i drifted into sleep."
                
                stop music fadeout 2.0
                
                scene black with fade
                
                play sound "fx/purr.ogg"
                
                $ renpy.pause (5.0)
                
            "Ignore her.":

                $ renpy.pause (0.5)
                
        $ mp.annaromance = True
        $ mp.save()

        $ annastatus = "good"

        $ annascenesfinished = 4

        stop sound fadeout 0.5
        
        stop music fadeout 2.0

        $ renpy.pause (0.5)

pass
