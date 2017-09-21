label adine_shopping:


$ c = DynamicCharacter ("persistent.player_name", color=persistent.playercolor, callback=rolly)
$ player_name = persistent.player_name

stop music fadeout 2.0
scene black with dissolveslow

$ renpy.pause (1.0)

#scene 1: apartment

nvl clear
window show

n "Spending the day babysitting Amely had been interesting. I had to care for some children back in my former life, but watching  Amely made me realize just how much energy those little dragons had. She actually reminded me of of a large dog. If you didn't entertain them and keep them occupied, you would probably come back to a half-destroyed house."
n "I had a free day with Adine today, though. It didn't seem like the Ministry had figured out my current diplomatic status. I doubted they knew that the teleporter was no longer functional. They would learn of that during the debriefing tomorrow, though. I would be testifying in front of an entire council!"
n "... I would have been fine never seeing the inside of a courtroom ever again, to be honest, but I had to honor my role as Ambassador until the very end."

nvl clear
n "They would surely revoke many of my privileges after discovering that I was stuck here forever. I would probably lose my apartment, my escorts, and my ability to purchase almost anything without cost."
n "I don't mind doing honest work, but to lose all of those amenities stung. Luckily, after having dinner with Adine last night, an idea came to mind. I had checked my government-issued card last night, and sure enough, it still had a bottomless credit limit."
n "I just hope Adine doesn't make our frivolous spending too obvious..."

window hide
    
$ renpy.pause (0.8)
show adineapt at Pan((0,233),(0,233),0.0) with dissolve

play sound "fx/knocking1.ogg"
$ renpy.pause(3.0)

Ad "Coming!"

$ renpy.pause(1.0)
play sound "fx/door/door_open.wav"
$ renpy.pause(1.0)
show adine normal with dissolve

play music "mx/basicguitar.ogg" fadein 2.0

Ad "Oh, [player_name]! You're early!"
    
menu:
    "I had a few minutes to spare.":

        Ad "Is that so? Well, you probably had to do a lot less ever since the portal was closed off."
        
    "I had to make sure Amely didn't come back to destroy your apartment.":

        Ad giggle "Oh, please! She wasn't that bad yesterday! And I did warn you not to pick her up by the belly..."

    "Early dragon gets the worm, as they say.":

        $ renpy.pause (0.5)
        
        Ad "The early dragon gets the worm?"
        
        c "Back in our world, they say that the early bird gets the worm."

        Ad think "But what's a bird?"

        c "It's a small winged animal, like a runner but capable of flight. They evolved from dinosaurs, apparently."
        
        Ad giggle "I just hope I don't evolve into something like that!"

Ad normal "Oh, hold on! I forgot something. I'll be back in a second."

hide adine normal with dissolve

play sound "fx/cabinet.ogg"

$ renpy.pause (3.5)

show adine normal b with dissolve

Ad "I almost forgot my goggles! You can never leave home without them."

c "Oh, are you taking me for a ride today?"

Ad "No, silly! It's not like I could carry you, anyways. I don't think I can carry that much..."

c "Maybe I should start reading those weight-loss magazines you always get in the mail."

Ad giggle b "I don't mean it like that! You're fine just the way you are."

Ad think b "But now that you mention it, you never did tell me what we're doing today."

c "Well, I have that hearing tomorrow with the council. I have to tell them that I won't be able to make it back to my own world. After that, they'll probably take my apartment and everything else they gave me when I first came here."

Ad disappoint b "Oh, no... what will you do?"

c "We'll worry about that later. But first, about what we're doing today..."

#m "I rummaged through my pockets, pulling out the black credit card that I first received as an ambassador."

#c "This has no spending limit that I know of. They'll probably take it from me tomorrow, but..."

#$ renpy.pause (0.5)

#Ad normal b "But for today..."

#c "Let's see how high we can make this thing go."

nvl clear

stop music fadeout 2.0

scene black with dissolveslow

#scene 2: store
$ renpy.pause (2.0)

show store at Pan ((0,233),(0,233),0.0) with dissolve

play music "mx/jazzy.ogg" fadein 2.0

m "Last night I had a glimpse at what Adine typically ate. Unless you considered ramen noodles sustenence, there wasn't much in the way of actual nutrition. A trip to the grocery store should set her kitchen straight."

show zhong normal c with dissolve

Zh "Ah, if it isn't Adine and [player_name]! Good morning!"

c "Good morning to you too, Zhong."

play sound "fx/wheels.ogg"

m "I retrieved a grocery cart from the entrance and wheeled it over to the two dragons."

$ renpy.pause(1.5)

show zhong normal c at right with ease

show adine b disappoint flip at left with dissolve

Ad "Ah... [player_name], I don't think we'll be needing the cart. I'm only buying a few things..."

c "Zhong, we'll come to you if we have any questions, alright?"

Zh "Of course, [player_name]. Just let me know and I'll do my best to help."

hide zhong normal c with dissolve

show adine b disappoint flip at center with ease

Ad b sad flip "[player_name], I don't think you understand. I... can't afford much in here."

show adine b sad flip

c "I know Adine, I know. We had dinner last night... I'll just say that it's what I lived on in my college days."

stop music fadeout 1.0

show adine frustrated b flip with dissolve

$ renpy.pause(1.0)

Ad "Then why would you bring me here? You know I don't have the money for it, and-"

m "I held up a finger to Adine's mouth. In hindsight, she probably could have bitten my hand right off, but it quieted her for now."

c "Let me show you something, Adine."

play music "mx/funness.ogg" fadein 2.0

m "I rummaged in my pockets for my wallet. I pulled out a credit card, glossy black surface gleaming under the lights. It instantly caught her attention."

c "Do you know what this is?"

Ad think b flip "Hmm... it's a credit card. I've never seen one like that before, though."

c "It's a black card. Remy gave this to me on my first night here."

Ad "A black card? What's so special about it?"

c "It has no spending limit that I know of. Absolutely none at all."

Ad "No limit? That sounds impossible. What's the catch?"

c "Be an ambassador, I guess. If you're from another world, they tend to treat you pretty nicely."

Ad "An ambassador, huh...? But you have that hearing tomorrow. Are you going to tell them about how you can't go back?"

c "I can't lie to them. They'll probably just disable the card after all of that. But..."

$ renpy.pause(1.5)

Ad "But for today..."

Ad normal b flip "[player_name], are you saying what I think you're saying?"

$ renpy.pause(0.75)

Ad think b flip "But we can't just waste money like that. A lot of dragons pay taxes, and we'd be abusing their charity."

c "You should remember that we managed to save all of dragonkind from extinction. I'm sure no one would mind us borrowing a bit here and there."

Ad "..."

$ renpy.pause(0.75)

Ad normal b flip "I guess you're right. Besides, it's been a while since I've had actual food."

c "We should get going before you eat everything in sight. Come on."

hide adine 
$ adine_produce_available=True
$ adine_meats_available=True
$ adine_dry_available=True
$ adine_drinks_available=True
$ adine_wellness_available=True
$ grocery_sections_played=0

play sound "fx/system3.wav"

s "There are three meal options that you can cook for Adine. Be sure to pick the appropriate ingredients."

jump grocery_sections

label grocery_sections:
    if grocery_sections_played==0:
            play sound "fx/steps/clean2.wav"
            $ adine_meats_available=False
            $ grocery_sections_played+=1
            jump grocery_section_meats    
    if grocery_sections_played<5:
        menu:
            c "(Which aisle?)"

            "Produce" if adine_produce_available:
                play sound "fx/steps/clean2.wav"
                $ adine_produce_available=False
                $ grocery_sections_played+=1
                jump grocery_section_produce
                
            "Dry Goods" if adine_dry_available:
                play sound "fx/steps/clean2.wav"
                $ adine_dry_available=False
                $ grocery_sections_played+=1
                jump grocery_section_dry
                
            "Drinks" if adine_drinks_available:
                play sound "fx/steps/clean2.wav"
                $ adine_drinks_available=False
                $ grocery_sections_played+=1
                jump grocery_section_drinks

            "Health \& Wellness" if adine_wellness_available:
                play sound "fx/steps/clean2.wav"
                $ adine_wellness_available=False
                $ grocery_sections_played+=1
                jump grocery_section_wellness
    else:
    
        jump grocery_done
        
label grocery_section_wellness:
    m "I steered the cart down the health and wellness section. Just like before, there were all the pills and supplement lining the walls, but now you had your own personal dragon guide to explain them all for you."
    show adine normal b with dissolve
    m "She stopped in front of a bunch of yellow boxes and picked one up. There was a blue dragon showing off her shining body on the cover, gaudy lens flare effects plastered all over her scales."
    Ad "This is my favorite! It's a scale cleaner. You just squeeze the paste out and scrub it into your scales. I usually use it before air shows so that others can see me sparkling in the sky. It's really good for your visual score."
    m "She stared at the price, then at the box. I still didn't have a firm grasp on dragon currency, but the number was way higher than anything else I've seen before."
    play sound "fx/box.wav"
    $ renpy.pause(1.5)
    m "In the blink of an eye, she dropped three or four boxes into the cart."
    Ad "There, that should do it."
    c "Are you sure you don't need more? This is probably the only time you'll get them for free."
    Ad "I think it's enough. One tube is good for a whole year. But I haven't used it in forever. You wouldn't mind helping me with it tonight, right?"
    m "We walked further down the aisle. She explained everything: pills that increased firebreathing range, patches that eased sore wings..."
    Ad "... and these are dragon contraceptives. I don't know if humans have something similar to this, but they're used to make sure that dragons don't get pregnant after having sex."
    c "Adine, I think I kn-"
    Ad "They're really stretchy and flexible sleeves. You wrap them around your-"
    c "Adine."
    Ad giggle b "Oh, [player_name], I'm sorry! I've just had to explain the concept to adolescents so many times. You {i}do{/i} know what a condom is, right?"
    menu:
        "We had those back in our world, too":
            Ad normal b "That's not too surprising. Mating probably works in a very similar way between humans."
            c "Some things never change, it seems. We still had the courtship and song-and-dance that I've seen dragons do here, too."
            Ad "It's funny how much humans and dragons share. That just makes me believe that humans created us even more, like the legends say."
            c "Of course, dating evolved in our society over the course of thousands of years. Women used to have no say in who their partner was, and even until recently it was improper to consummate your love until marriage."
            Ad "Was there ever a time when dating outside of your species was a question?"
            c "Outside of our species...? Not really, mostly because it never progressed that far. The furthest we ever got with biological experimentation on humans was nanomachines and cybernetics. We feared playing with genetics on that level."
            Ad "Oh, I see. It hasn't really gotten that far for us, either. We haven't had another intelligent species here before we discovered humans actually existed."
            c "Thanks for the compliment, I think."
            Ad giggle b "Of course it's a compliment! You are only one of two humans I've seen so far, but still..."
            
        "Condoms? Can you demonstrate for me?":

            Ad giggle b "Don't be silly! Or are you being serious...?"
            $ renpy.pause(1.5)
            Ad normal b "Wait, [player_name], I... you...?"
            m "She looked around furtively before opening one of the boxes. Her claws quickly ripped open one of the foil squares inside, holding up a rubber circle."
            Ad "So this is a condom. It's made out of latex, a really stretchy type of rubber. You have to wrap it around like this."
            m "Her claws grabbed one of the bananas in the cart, bringing it up to eye level. She spread the condom wide, draping it down the fruit inch by inch."
            Ad "It's very important to make sure it's nice and tight. And you have to inspect it, too! If there's holes in the condom, it's unusable."
            show zhong normal c flip at left with dissolve

            show adine normal b at right with ease
            

            Zh "Excuse me, but I couldn't help but notice what you were doing to that banana. You do intend to buy it, right?"
            
            Ad giggle b "I'm sorry. I was just showing [player_name] here how to..."
            
            Zh "... I see. I'll leave you two be, then."
            
            hide zhong with dissolve
                        
        "I don't really find them necessary.":
            Ad normal b "That's no good, [player_name]. That's how you get unwanted pregnancies at a young age. Then the mother lays the egg, and either the father runs off or she finds out she can't take care of it by herself."
            Ad disappoint b "Then she brings the egg to the orphanage and leaves it for us to discover in the morning, and we're left to care for it. Then after a couple years, you get a little dragon asking who their mommy and daddy are, and..."
            Ad frustrated b "I don't get how that happens! How can a mother be so callous, to give birth and just decide to toss the egg like it's yesterday's leftovers?! That's a dragon {i}life{/i} they're throwing away."
            c "Adine..."
            Ad disappoint b "... sorry, [player_name]. It's just that there are so many orphans and so few dragons willing to give them a home. Sometimes it makes me feel hopeless..."
            c "You're doing the best you can, Adine. Everyone knows that. How many of those kids don't know your name?"
            $ renpy.pause(1.5)
            Ad normal b "Yeah, you're right. It's just that I'd adopt every last one of them if I could, you know?"
            c "Amely might get jealous."
            Ad normal b "She likes all of her friends! Well, some of them..."
            
    hide adine with dissolve
    
    m "The two of you complete the aisle with your dignity still intact, thankfully. You do notice that the basket seems to be a box heavier after that unfortunate talk. Did Adine...?"
    jump grocery_sections
    
label grocery_section_meats:
    m "I figured we should go to the meat second first before anything else."
    m "Just like in my previous life, the butcher was located in the back of the store. The more I looked around, the more this reminded me of a store in our pre-solar flare civilization."
    m "I passed by the meat displays once before, but I can't help but marvel at the selection. Despite all of the different varieties of meats, I did have something in mind, though..."
    show adine normal b with dissolve
    Ad "Doesn't seem like there's anyone here... hello? Anyone back there?"
    show zhong normal c at right with dissolve
    show adine normal b flip at left with ease
    Zh "Ah, sorry. The regular butcher's out for the day, but I can help you two. What are you looking for?"
    m "We peered down into the glass display. All the meat was red and fresh, as if they had stocked it just this morning. We'd probably buy some meat for Adine to use through the week, but I was looking specifically for a single type of meat to cook with tonight."
    $ adine_fish_available=True
    $ adine_ground_mouflon_available=True
    $ adine_mouflon_available=True
    menu:
        "Ground mouflon (hamburgers)":
            c "Those mouflon steaks look pretty red. Are they fresh?"
            Zh "Of course! One of the farmers just dropped off a delivery this morning. He did complain about being a mouflon short, though..."
            Ad "A mouflon short? No one would actually steal a mouflon in this town, right?"
            c "Maybe they were hungry. Dragons can eat meat raw, right?"
            Ad "Yeah, we can. You have to be pretty hungry, though. They have a gamey taste when uncooked."
            Zh "So how many will you take?"
            c "Can you grind them? We'll take two if you can. The ones in the back, with lots of fat on them."
            Zh "Certainly. Give me one moment."
            m "Zhong took the two freshest-looking steaks and walked them back to a grinder. Within a minute, he hefted a bag of meat up to the scales and taped a label to it."
            Ad "You never did mention what you were making tonight, [player_name]."
            c "Don't worry about it. Well, it has mouflon in it, of course, but I'd be giving too much away if I told you now."
            Ad giggle b flip "Alright, alright. I trust you know what you're doing."
            $ adine_ground_mouflon_available=False

        "Mouflon steak (mouflon stew))":
            c "Those mouflon steaks look pretty red. Are they fresh?"
            Zh "Of course! One of the farmers just dropped off a delivery this morning. He did complain about being a mouflon short, though..."
            Ad "A mouflon short? No one would actually steal a mouflon in this town, right?"
            c "Maybe they were hungry. Dragons can eat raw meat, right?"
            Ad "Yeah, we can. You have to be pretty hungry, though. They have a gamey taste when raw."
            Zh "So how many will you take?"
            c "I think we'll take two steaks. It should be enough for what we're having tonight."
            Ad "You never did mention what that would be, [player_name]."
            c "Don't worry about it. Well, it has mouflon in it, of course, but I'd be giving too much away if I told you now."
            Ad giggle b flip "Alright, alright. I trust you know what you're doing."
            $ adine_mouflon_available=False
         
        "Fish (fish tacos and salsa)":
            c "I'm looking to get some fish, but I think Adine probably knows more than I do about it."
            Zh "No problem. Good timing on your part, actually. We had some fliers bring some fresh fish in from the coast this morning."
            Ad "Really? Wow, they do look fresh!"
            m "I couldn't help but watch with interest as Adine picked out the fish, commenting on their color and tapping on the glass every so often. Her tipped tail quivered very so often, as if the fish on ice were still prey to be hunted."
            Ad "Those two right there! They look the freshest. No, not that one. Above it. There!"
            c "What kind of fish did you pick?"
            Ad "I picked a coastal fish, something you'd find close to shore. It's a white fish, very delicate and light in taste. I figured that you liked what we caught out at the beach, so I just got more."
            c "Sounds like it's good for grilling, then."
            Ad "You never did mention what what you were making tonight, [player_name]."
            c "Don't worry about it. Well, it has fish in it, of course, but I'd be giving too much away if I told you now."
            Ad giggle b flip "Alright, alright. I trust you know what you're doing." 
            $ adine_fish_available=False
    hide zhong with dissolve
    hide adine with dissolve
    jump grocery_sections

label grocery_section_produce:
    m "Adine practically radiated happiness at seeing the fresh produce, going from display to display and picking up fruits just to examine them."
    show adine normal b with dissolve
    Ad "The fruits here are always so fresh! Here!"
    m "She pressed a banana into my hands. It was firm and fresh, yellow and perfectly ripe for eating. It was tempting to taste it right there in the store. The color of her scales shared an uncanny resemblance with the banana. I then found myself staring down at her tail, and yet another comparison began to form in my mind..."
    $ renpy.pause(1.5)
    Ad annoyed b "... don't say it."
    c "How did you know what I was going to say?"
    Ad normal b "Let's just say I had a hunch."
    menu:
        "But it's true!":
            Ad giggle b "All I'll say is that you're lucky we're in public."
        "Why would you suspect such a thing?":
            Ad normal b "I wouldn't be suspicious if somebody didn't attempt to play with my tail in the shower."
        "Did your tarot cards tell you that?":
            Ad annoyed b "They're used for actual predictions, not little things like this."
    Ad normal b  "Anyways, I'll take care of the fruit. You go get the vegetables."
    m "She waved her claws at me, shooing me off before she began her crusade on the entire fruits section. Adine sure loves fruit, that's for sure..."
    hide adine with dissolve
    play sound "fx/steps/clean2.wav"
    m "For a carnivorous species, dragons sure enjoyed to grow produce. There was no noticable difference between here and the supermarkets back in my world... when they still existed, of course. The only difference I could spot were some coniferous vegetables. They were probably Jurassic-era plants, nothing I really wanted to take a risk with."
    m "I was able to pick out some more familiar vegetables. The biggest problem was that I couldn't take one of everything. Adine and I had to walk the groceries back, after all."
    $ produce_pick=0
    $ adine_onion_available=True
    $ adine_tomato_available=True
    $ adine_lettuce_available=True
    $ adine_potato_available=True
    $ adine_carrot_available=True
    $ adine_jalapeno_available=True
    $ adine_tomato_counter=0
    jump produce_pick_section

label produce_pick_section:
    if produce_pick<3:
        menu: 
            m "I could reasonably take three of these back..."
            "Onions" if adine_onion_available:
                c "(I never thought I'd be thinking this, but Adine's pretty cute, especially for a dragon. Every once in a while I stop and ponder it, but now that I'm probably going to end up living with her, it's becoming harder and harder to ignore.)"
                c "(What would it be like if I tried to approach her? We already had some time in the shower, though I don't know whether that was just dragon culture or something else. I'm not terribly interested in asking her point-blank, either.)"
                c "(But what if she really meant something? And we ended up together somehow? That would be interesting.)"
                c "(It would just be a shame if these onions ended up tearing us apart.)"
                $ adine_onion_available=False
                $ produce_pick+=1
                
            "Tomatoes" if adine_tomato_available:
                $ adine_tomato_available=False
                $ produce_pick+=1
                c "(These tomatoes are remarkably fresh, bright-red without a hint of a bruise. I don't remember the last time I've seen tomatoes so perfect. Growing them in the post-solar flare environment back home proved to be challenging.)"
                c "(I had to feel it in my hand. It was firm, heavy, and smelled very earthy. It was a shame I couldn't grab more than a few.)"
                c "(There were smaller ones, too, in little plastic cages of about ten or so. There was no way anyone would notice one missing, right?)"
                $ renpy.pause(1.0)
                c "(I looked around before opening one of the boxes. Before Zhong could see, I had palmed a single cherry tomato. I popped it into my mouth a second later, letting it roll about before squeezing it between my teeth."
                c "(As expected, it held for a second before squirting in my mouth. The sweetness wasn't overwhelming, and the sourness bit at my taste buds ever so slightly. It was a good blend of flavors and texture, and I ate the rest of it in an instant."
                c "(The box was still there, with so many more tomatoes... but I had to resist taking more. It would be embarassing to get caught by Zhong.)"
                #if adine_tomato_counter<10:
                    #c "I looked down to see an empty cage of tomatoes. Had I eaten them all? Hopefully Zhong hadn't seen..."
                    #menu:
                        #"Eat another one":
                            #c "I looked around again before popping another one in my mouth. These were so good!"
                            #$ adine_tomato_counter+=1
                        #"Put the box down":
                            #c "I sighed and put the box back down. No sense in getting caught, right?"
                        
            "Lettuce" if adine_lettuce_available:
                c "(Knock, knock!)"
                c "(Who's there?)"
                c "(Lettuce.)"
                c "(Lettuce who?)"
                c "(Lettuce in. It's cold out here!)"
                c "..."
                $ adine_lettuce_available=False
                $ produce_pick+=1
                
            "Potatoes" if adine_potato_available:
                c "(It was nice to see such a familiar sight. Potatoes formed the backbone of our food supply back home. They were easy to grow, high in calories, and stayed fresh for a really long time. Without them, we probably would have starved a long time ago.)"
                c "(Of course, the thought of eating potatoes every day was not apeeling at all. We had to mash them into our meals, even if we would rather eat dirt than another one of those awful things.)"
                c "(Without seasoning, the sheer blandness of a potato cannot be overstatered. If we had even a bit of salt or pepper, or even chili flakes, the meal would stand in starch contrast to just a regular old potato.)"
                c "(... I may have retained some anxiety from those bleak days.)"
                $ adine_potato_available=False
                $ produce_pick+=1
                
            "Carrots" if adine_carrot_available:
                c "(The carrots were placed away from most of the vegetables. I guess you could say all the other veggies were scarrot of them.)"
                $ adine_carrot_available=False
                $ produce_pick+=1
                
            "Jalapenos" if adine_jalapeno_available:
                $ adine_jalapeno_available=False
                $ produce_pick+=1
                c "(Do dragons taste spiciness the way we do? In a past life, I remember Anna being able to breathe fire through some chemical mixture.)"
                c "(But that's more temperature hotness than actual spiciness. Given how they understand the use of seasonings and garnishes, dragons must have some developed some sort of palette for spicy foods.)"
                c "(I'll be sure to ask Adine later tonight. I hope she just doesn't get defensive and ask me \"How would you like if I got jalapeno business?\" or something like that.)"
                
        jump produce_pick_section
    else:
        if adine_ground_mouflon_available==False:
            if adine_tomato_available==False and adine_lettuce_available==False and adine_onion_available==False:
                jump post_produce_pick
            else:
                c "(... are these the right ingredients for a hamburger? We aren't having any fries, so I don't need potatoes. I should go back and double check...)"
                $ adine_onion_available=True
                $ adine_tomato_available=True
                $ adine_lettuce_available=True
                $ adine_potato_available=True
                $ adine_carrot_available=True
                $ adine_jalapeno_available=True
                $ produce_pick=0
                jump produce_pick_section

        elif adine_mouflon_available==False:
            if adine_carrot_available==False and adine_onion_available==False and adine_carrot_available==False:
                jump post_produce_pick
            else:
                c "(Are these the right ingredients for a stew? I know I need onions, potatoes, and carrots. I should go back and double check...)"
                $ adine_onion_available=True
                $ adine_tomato_available=True
                $ adine_lettuce_available=True
                $ adine_potato_available=True
                $ adine_carrot_available=True
                $ adine_jalapeno_available=True
                $ produce_pick=0
                jump produce_pick_section
                
        elif adine_fish_available==False:
            if adine_onion_available==False and adine_tomato_available==False and adine_jalapeno_available==False:
                jump post_produce_pick
            else:
                c "(Are these the right ingredients for some salsa? I know I need onions, tomatoes, and jalapenos. I should go back and double check...)"
                $ adine_onion_available=True
                $ adine_tomato_available=True
                $ adine_lettuce_available=True
                $ adine_potato_available=True
                $ adine_carrot_available=True
                $ adine_jalapeno_available=True
                $ produce_pick=0
                jump produce_pick_section

label post_produce_pick:
    "There, that should do it! I returned to Adine three bags heavier. The sheer amount of fruit in her basket seemed to placate her for now."
    show adine normal b with dissolve
    if adine_tomato_available==False:
        Ad "You know that you're supposed to eat the food {i}after{/i} you pay for it, right?"
        c "I had to sample the tomatoes to make sure they were worth buying."
        if adine_tomato_counter>3:
            Ad "Usually you should be able to get a sense of what they taste like after just a couple."
            c "I need to sample as many as possible to make sure none of them were defective."
            Ad giggle b "I just hope Zhong didn't catch you, silly."
        else:
            Ad "Oh, I see. I'm guilty of that too sometimes. It's too good to resist, isn't it?"
        Ad normal b "Anyways, I got everything I want! Apples, bananas, peaches, mangos, grapes, lemons..."
    else:
        Ad "Well, I got everything I want! Apples, bananas, peaches, mangos, grapes, lemons..."
    c "Enough for two dragons?"
    Ad "Yeah! Enough for two dragons! Wait..."
    c "I'll try my best to keep up with you, then."
    Ad giggle b "You better! I won't have any of these going bad on my watch."
    jump grocery_sections
    hide adine with dissolve

label grocery_section_drinks:
    m "Bottles upon bottles line the shelves around you, a menagerie of spirits, wines, and beers in hundreds of different colors."
    c "Any particular selection you're fond of?"
    show adine normal b with dissolve
    Ad "No, not really. I don't drink very often."
    c "Could I ask why?"
    Ad think b "Well, I usually never have the time or the money for it. That, and flying while drunk is really reckless."
    c "Flying drunk? What happens if you fly drunk?"
    Ad normal b "It's not something you should do, even if you're just trying it out. You can crash and break your wings, or even worse, crash into someone else mid-air."
    c "You know, we used to have something similar back in my world. Humans used to drive cars for transportation. Imagine something like this cart, except larger with an engine inside of it."
    Ad normal b "So a type of vehicle? Must have taken a while to get somewhere without flight or anything like that."
    c "We had vehicles that could fly, too, but they were larger and more expensive. And cars weren't slow, either."
    Ad "You think I'd be able to beat one of these cars in a race?"
    menu:
        "Not in your dreams!":
            c "Cars were built to go very fast, faster than any dragon I've seen. There used to be racing competitions for who could drive the fastest, actually."
            Ad think b "It sounds interesting, but I think I'd have to see it to believe it."
        "You'd probably give them a hard time":
            c "Some cars were built for performance, but a lot of cars were just used for everyday driving around town. You could probably fly faster than those regular cars."
            Ad "You think so? Maybe I'd be useful as a flying car. Did those exist in your world?"
            c "It's funny you ask that. Humanity had dreamt about a flying car for a whole century, but we've never actually made a usable one."
        "Easily!":
            c "Oh, it wouldn't even be a contest! You'd blow a car away in any sort of competition."
            Ad "You think so? You can tell the truth, you know. There's no way that humans designed something that wasn't fast."
            c "You'd be surprised at how slow humans can make things, Adine."
    c "But anyways, these cars were manually driven. When you're drunk, it's not easy to drive as well. Drunk drivers often crashed their cars, usually killing themselves or other innocent people."
    Ad b sad "That's horrible..."
    c "And it was worse because sometimes the drunk driver would end up hitting a person on the street, or even another car full of people. In the worst cases, none of them would survive."
    Ad "That's definitely worse than two dragons colliding. Sometimes they both end up dying, but it's never more than those two."
    c "But that's not to say alcohol is bad, though. It's a voluntarily bad choice to just drive or fly right after drinking."
    Ad "No, that's true. You just have to be careful after drinking, that's all..."
    c "Well, we're not driving or flying tonight, so we should definitely get something. What do you think?"
    Ad b think "I don't know... I'm not very good at drinks. Besides, wine with ramen doesn't sound too appetizing."
    c "So a good wine, then. And before you ask, I promise that we're not having ramen tonight."
    Ad normal b "Is that so? That's a relief. Well, how about this one?"
    m "She picked out a bottle of red wine and handed it to me. I took a good look at the label and tried to hide my frown. This was the same wine that Remy had stocked my apartment with."
    c "Maybe not this one. How about..."
    m "Remy said he picked the second-cheapest wine, right? I scanned through the numbers, trying to find... the second most expensive wine. It would probably throw some numbers off on the receipt, but that didn't really matter to me."
    c "Let's get this one instead. Remy told me it was pretty good."
    Ad "Remy? Well, if there's a dragon that knows his wines, it would be him..."
    m "She took the bottle of red wine and set it down in the cart. Hopefully the drink would make the time after dinner more entertaining."
    hide adine with dissolve
    jump grocery_sections
    
label grocery_section_dry:
    show adine normal b with dissolve
    Ad "I think I've been down here too many times..."
    m "I looked around the aisle. Dried and preserved foods surrounded me - chips, fruits, nutrient bars, cereals, and, of course, ramen. Ramen cups, ramen bowls, ramen blocks... all instant, of course. The variety in ramen stunned me."
    Ad "This store has the best selection in this town. They have all of my favorite flavors. Mushroom, shimp, roast mouflon, spicy..."
    c "Spicy's a flavor?"
    Ad "Of course spicy's a flavor! It says so on the packaging here. See?"
    m "The more I watched her, the more fanatic her expression became. She stared at the plastic packaging to the point where I expected her to drool a bit."
    c "Why don't you get the bowls? These ones seem really cheap."
    Ad "That's exactly why I get them. Also, you can't season the microwavable ones that well. If you get the ramen blocks, you can do a lot of things with them! Add boiled eggs, scrambled eggs,  broccoli, chopped onions, steamed fish, bits of mouflon..."
    c "The best is when you make your own broth and pour scrambled eggs into it right before turning off the heat. That way, the egg's much softer when you begin eating it."
    Ad "Really? I'll have to try that sometime. How do you know about ramen, anyways?"
    menu:
        "Old college days":
            c "I lived off of ramen in my college days too. Money was scarce, especially for a student like me, so I had to get creative."
            Ad "So like my situation right now, then! We should exchange more ramen recipes when we get the chance."
        "Scavenging after the flare":
            c "After the solar flare, all of our means of food production were disrupted or destroyed. We had to scavenge for any type of food we can, especially ones that didn't perish."
            Ad "That's horrible, but fortunate, too. I never would have thought that you would live off of ramen in a world like that."
            c "We did what we had to do to survive. Thankfully, eating ramen was one of the more innocent things I did back then."
            Ad "Hopefully you didn't have to do anything too drastic then."
    Ad "But for right now, I'm getting as many of these as possible."
    play sound "fx/box.wav" 
    m "My jaw dropped as she took a wing and slid it over a shelf, shoving at least twenty packets fall into the cart. Then another row... then..."
    c "Adine, the meteor's passed. We aren't trying to stock a doomsday shelter."
    Ad giggle b "I know, I know [player_name]! It's just that I probably won't have this opportunity anytime soon, so I have to make the most of it."
    c "But there are other dried foods besides ramen, you know. Besides, we have to walk all of this home."
    Ad normal b "Great idea! We can get all of these and lots of other snacks too! Look, fish-flavored crackers! The kids at the orphanage love them. You have to try them!"
    m "I found myself unable to escape her claws as she dragged me down the aisle, pointing out many, many of her \"absolute favorite\" snacks..."
    m "But before we exited the aisle, I remembered that I had to pick something up from here. What was it again?"
    jump pick_bread_item
    
label pick_bread_item:
    menu:
        "Hamburger buns":
            if adine_ground_mouflon_available==False:
                m "I grabbed a bag of hamburger buns and tried to stuff it among the mountain of bags Adine made in the cart."
            else:
                c "(Was this the right thing to get? We're not having hamburgers tonight...)"
                jump pick_bread_item
        "Corn tortillas":
            if adine_fish_available==False:
                m "I grabbed a bag of tortillas and tried to stuff it among the mountain of bags Adine made in the cart."
            else:
                c "(Was this the right thing to get? We're not having fish tacos tonight...)"
                jump pick_bread_item

        "Mouflon broth":
            if adine_mouflon_available==False:
                m "I grabbed several cans of mouflon broth and tried to stuff them among the mountain of bags Adine made in the cart."
            else:
                c "(Was this the right thing to get? We're not having stew tonight...)"
                jump pick_bread_item
    hide adine with dissolve
    jump grocery_sections

label grocery_done:
    m "By the time we were done, the cart was stuffed to the brim. Adine practically vibrated with excitement, so enamored by the sheer quantity of food that I wondered if she forgot how to blink."
    show adine normal b with dissolve
    Ad "Just look at all of this! I don't think I'll be going hungry for a while. And we even have plenty of snacks for the kids, too. Can you really buy all of this?"
    menu:
        "Don't worry":
            c "Don't worry about it. There's no way that we won't be able to buy all of this as long as I have the black card."
        "If they haven't disabled my card yet":
            c "I'm sure that they haven't disabled the card yet. If they have, I'll just go to the Ministry and have them activate it again. I'm still allowed that right, I think."
        "Only with a secret password": 
            c "Well, Adine, I... I don't think I was entirely truthful with you."
            Ad "What do you mean?"
            c "This card also needs a passphrase spoken to it before it's usable. There's a voice recorder embedded inside it."
            Ad think b "Really? That's really odd. Do you know what the passphrase is?"
            c "Yeah, but you need to say it. It doesn't register my voice all the time for some reason."
            Ad normal b "Alright. What is it?"
            c "You have to say, \"I'm a banana dragon with a banana phone tail.\""
            $ renpy.pause(1.5)
            Ad "..."
            Ad "You are very lucky we are in public right now."
            c "This card doesn't work until you say it."
            Ad "Ugh..."
            c "Well?"
            Ad annoyed b "Fine..."
            Ad "I'm a banana dragon with a banana phone tail. There, satisfied?"
            c "Perfect. Now this card should work."
            Ad normal b "Just wait until we get back to the apartment, [player_name]."
    m "We rolled the cart to the checkout line. Zhong was there waiting for us, of course."
    show adine normal b flip at left with ease   
    show zhong normal c at right with dissolve
    Zh "Just about ready, [player_name]?"
    c "Yeah, I'd say so. Thanks for helping us out at the butcher earlier."
    Zh "My pleasure. Planning to throw a party?"
    c "Something like that. The meteor just passed, so there's reason to celebrate."
    Zh "That is true, [player_name]. Bryce and the others are holding a beach party very soon. Both of you can come by if you want."
    m "The goods flew through his claws and over the barcode scanner. The number on the screen grew higher and higher by the second."
    Zh "And that'll all come out to... wow. Will that be cash or card?"
    m "I handed him the black government-issued card. He stared at it with skepticism for a moment, but then swiped it into his terminal."
    $ renpy.pause(1.25)
    play sound "fx/system.wav"
    $ renpy.pause(.75)
    Zh "Looks like the payment's cleared. If you could just sign here..."
    play sound "fx/scribblex.ogg"
    $ renpy.pause(1)
    Zh "... and that'll be it. Here's your receipt. This is a lot to bag up, and I don't want to have you and Adine make two trips to carry everything back. Oh - since you two live close, feel free to borrow the cart. Just be sure to return it later."
    c "Don't worry, I'll bring it back. Shouldn't be more than half an hour at most. Let's get going, Adine."
    Ad "Yeah, we should be getting back. Thanks, Zhong."
    hide zhong with dissolve
    hide adine with dissolve
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    jump apartment_cooking
    
label apartment_cooking:
    play music "mx/jazzy.ogg" fadein 2.0

    show adineapt at Pan((0,233),(0,233),0.0) with dissolve
    m "After all of the trouble, we finally managed to get all of the groceries into her apartment. Luckily, it was on the bottom floor. I wouldn't have envied whoever had to carry those bags up an entire floor."
    play sound "fx/box.wav"
    show adine normal b with dissolve
    Ad "And... there! That should do it! Managed to close the fridge. And to think there was nothing in there the last time I checked, too."
    c "And your cabinets are stuffed too. You probably won't go hungry for a while."
    Ad "Yeah!"
    $ renpy.pause(1)
    Ad think b "Unless I eat it all first..."
    c "You should leave some for the kids, at least. "
    Ad normal b "I'm kidding, silly! Well, maybe..."
    c "You probably won't be thinking that after tonight. All of the ingredients out on the counter, right?"
    Ad "Yeah, they're right here. What are you making, anyways?"
    if adine_ground_mouflon_available==False:
        c "We're going to make some of the best mouflon burgers you've ever had."
        Ad "The best? I've had some of my cafe's burgers, and they were pretty good sometimes."
        c "Let's see if I'm qualified to work at your cafe, then. I sound like I'm joking, but after tomorrow I'm not going to have any money..."
        Ad giggle b "I'm sure they'll set you up with some funding. But of course, you're welcome to work at my cafe if you'd like."
        c "Sounds like a plan. Well, let's do the onions first. We're going to want to get these grilled early. Can you cut them? They should be thin slices."
        show adine normal b at right with ease   
        Ad "Sure, one second."
        play sound "sfx/chopping.ogg"
        m "While she attended to the onions, I got the stove heated up. At least her kitchen was somewhat furnished, despite what the empty refridgerator and shelves suggested. High heat on the pan, a little bit of oil..."
        Ad "Done! Do I drop them in the pan?"
        c "Yeah. One by one, like that."
        show adine normal b at left with ease   
        play sound "sfx/sizzling_food.wav"
        c "While that's cooking, we'll go ahead and prepare the rest of the vegetables. Can you slice some tomatoes while I leaf the lettuce?"
        show adine normal b at right with ease   
        play sound "sfx/chopping.ogg"
        m "She handed me a bowl of neatly cut tomatoes. That, along with the lettuce, went to the side for later use. At that point, the smell of cooked onions began to fill the room."
        show adine normal b at left with ease   
        m "I turned around to take them off the pan, but Adine was a step ahead of me. She already had a spatula in her claws and yet another plate stacked with the grilled onions."
        Ad "I know a thing or two about cooking too, you know. These look pretty good!"
        c "Then you'll know what to do with the hamburger buns, then."
        m "As she took a pair of them out of the bag, I began to lay out the ground mouflon before me. It didn't take a minute before the aroma of toasting bread filled the room, and Adine was at my side again."
        show adine normal b at right with ease   
        c "So back at the market, I got the fattiest cuts. The more fat's in a burger, the better tasting it is. Not too sure about how it affects your figure, though."
        Ad "I'll try not to have too many. I have to make sure I weigh the right amount for my competitions. Acrobatics actually take a lot of balancing out."
        c "You might be trouble after eating one of these, then. Anyways, you're going to take the mouflon and form them into patties. You can do it with claws, right?"
        Ad "Let me try right here..."
        play sound "fx/knockheavy.ogg"
        Ad "... like this?"
        m "For a creature with claws like that, I was surprised to see how neatly she formed her patties. They were round - a bit rough around the edges, but definitely usable."
        c "Right, just like that. Here, make a couple more more, just like that. We're going to then season them with salt and pepper - here."
        play sound "fx/salt.ogg"
        c "Alright, let's get these cooking before they dry out. The bread should be toasted well enough now."
        m "She got out yet another set of plates, but these ones were more ornate than usual. We took the buns out of the pan and arranged them neatly - a pair for her and a pair for me."
        c "A little more oil, and..."
        Ad "I'll get it."
        show adine normal b at left with ease   
        play sound "sfx/sizzling_food.wav"
        m "She took the patties and transferred them over to the pan. The sound of sizzling mouflon immediately began to fill the room, and I almost salivated at the smell. I couldn't really imagine how Adine, let alone any dragon, resisted eating them right then and there."
        Ad "But there doesn't seem to be anything different about these burgers than what we make at the cafe. What makes these special?"
        c "There's one last trick to it."
        m "Thankfully, I had found some mustard in her refrigerator earlier. I took the bottle and gave the patties a generous squirt each."
        Ad "That's it?"
        c "Just wait for it."
        m "I let a couple more pass before I flipped the patties over. The moment that mustard-covered side hit the pan, Adine's eyes widened. A dragon's sense of smell was probably better than a humans, and the way the mustard and mouflon cooked was strong even for me."
        c "I'd say that's about it."
        Ad "Wow. Adding mustard does that much to the meat?"
        c "It surprised me at first, too. Just wait until you try it! But before that, I think these are just about ready."
        show adine normal b at right with ease   
        m "I didn't know how similar mouflon was to beef, but I assumed that medium-well was good enough for the meat. I layered the ketchup and mustard out on the bottom burger bun before placing two steaming patties right on top of it."
        m "While Adine began to build hers, I stacked on the other ingredients - the tomato first, then the lettuce, the the onion..."
        Ad "[player_name], how come you stack them like that? I see the cooks do it all the time, but I never figured it out."
        c "Have you ever had a burger that was just soggy and sloppy? With everything just falling out of it?"
        Ad think b "A few times. They were never really good."
        c "That's because the buns soaked all of the water out of the vegetables. If you stack them like this, you won't get any of your wet vegetables soaking into the bread."
        Ad normal b "Oh! That's pretty clever."
        show adine normal b at center with ease   
        m "A few moments later, we had our burgers prepared and ready to eat. We sat at the small table in the kitchen, and even though I was hungry, I just waited to see how Adine would react to the burger."
        m "She grabbed it in both claws, a couple streams of juices dripping onto the plate from the mouflon patty. Then she opened wide and took a bite without hesitation."
        play sound "fx/bite.ogg"
        Ad "..."
        c "Well? How is it?"
        Ad "This is great! It's so soft and juicy! And the mustard adds so much... I'm surprised."
        m "I took a bite of my own, letting all the juices run into my mouth. Mouflon was a bit more gamey than beef, but it was still very, very flavorful and soft. I reminded myself to try more recipes involving mouflon in the future."
        c "The mustard's a twist on the burger. It's certainly different than what you've had before, right?"
        Ad "You're right, this is different! Is this what humans ate regularly in your world?"
        c "That, and more. There were a lot of different variants. You could get chopped onions, peppers, and even an \"Animal Style\" burger where they fry your buns with mustard."
        Ad "..."
        c "If you want, I can show you how to make one."
        Ad "Could you... make me one right now?"
        c "Right now? But we just-"
        m "I guess I wasn't really watching carefully, but in the time I had talked, she had eaten most of her burger! I had barely gotten through half of mine."
        Ad giggle b "Please?"
        c "Okay, okay. One \"Animal Style\" burger coming right up. Just don't eat mine, alright?"
        hide adine with dissolve
        $ renpy.pause(1.25)
        show adineapt2 at Pan((0,233),(0,233),0.0) with dissolve
        m "..."
        m "I was surprised she was able to eat that much, but apparently dragons didn't have cooking as refined as ours. It made me feel a bit important to expose her to this sort of cusine."
        show adine normal b at center with dissolve
        Ad "That was really good! You'll have to show me how to cook it again so I remember."
        c "Not a problem, Adine. I'll show you other things I've learned how to cook, too. But for right now..."
        m "I went to the kitchen and picked out two wine glasses out of one fo the cabinets. Then I grabbed for the wine bottle on the kitchen before sitting back down with her."
        c "I know wine after a burger sounds odd, but I think we should treat ourselves tonight."
        jump adine_wine
        
    if adine_fish_available==False:
        c "When's the last time you had a taco? A really good one?"
        Ad "Well, our cafe doesn't really make tacos, so... I don't remember at all."
        c "Then now is the time. Do you know how to cook fish?"
        Ad "Of course! I hunt them all the time. It would be odd if I didn't know how to prepare them."
        c "Good. Can you get some grilled fish going?"
        show adine normal b at left with ease   
        m "As she attended to the stove, I laid out all of the necessary fruits and vegetables in front of me. Luckily, she had picked up a lot of fruit - mangos and lemons in particular. I'm not sure if dragons had invented mango salsa, but if they haven't, they'll know about it soon."
        play sound "sfx/sizzling_food.wav"
        show adine normal b at right with ease   
        m "Adine was by my side again, leaning over at the cutting board and knife I had found."
        Ad "Mangos? And onions and jalapenos and lemons?"
        c "We're going to be making some mango salsa. Mangodine salsa, maybe?"
        Ad giggle b "Please, [player_name]. The comparison to bananas is already enough."
        c "Just kidding, kidding. Here, dice the onions. I'll take care of the mango and jalapenos."
        show adine normal b at right with dissolve
        play sound "sfx/chopping.ogg"
        m "The more food we diced, the better that fish began to smell. Adine tended to it once every minute, leaving her work to make sure the fish wasn't burning. She seemed serious about being able to prepare the fish."
        m "I grabbed a bowl from a cabinet to slide my onions and jalapenos into. She followed suit, dumping in her diced mangos."
        c "Then we'll mix this up just a bit. Could you get a lemon? We need the juice from it."
        m "As I whisked the ingredients together with a spoon, she came back from a fridge with a lemon in hand."
        play sound "sfx/chopping.ogg"
        Ad "Here. Didn't your col- I mean, the other human have something to do with lemons?"
        c "Yeah. He used them for secret notes. I think he was passing notes back through the teleporter when that still existed."
        Ad "Secret notes? That's really sneaky of him."
        c "It's a very old spy trick. If you could squeeze some juice into the bowl here...?"
        Ad "Hold on one second. I think the fish is ready."
        show adine normal b at left with ease   
        c "I grabbed Adine a bowl while she got the fish off the stove. It smelled fresh and light - she definitely knew what she was doing! I had to resist just plucking one out of the bowl and sampling it."
        show adine normal b at right with ease   
        Ad "There we go. And now, the lemon."
        $ renpy.pause(1)
        c "There, that should do it."
        m "I gave the salsa a bit more mixing before giving Adine the spoon."
        c "Here, you should try this out. Mangodine salsa."
        play sound "fx/slap1.wav"
        show adine giggle b at right with dissolve
        $ renpy.pause(1)
        c "Okay, okay. Mango salsa."
        show adine normal b at right with dissolve
        m "She took a bit of it in the spoon and ate it."
        c "It's good! Sweet, but spicy, and it bites a bit too."
        m "I had to snatch the spoon from her claws before she dipped it back into the bowl."
        c "You can have more once we actually spread it on the tacos. I promise, it's better that way."
        Ad "Fine..."
        c "Get the pan going again. We'll need to toast these tortillas."
        show adine normal b at left with ease   
        m "I got the bag and tossed four tortillas out onto the pan. Thirty seconds later, I took them off and replaced them with four more. Eight tacos should be generous enough between the two of us."
        play sound "fx/dishes.wav"
        m "Adine had gotten a couple plates to lay out the tortillas. The fish came first, generous chunks placed on every taco. Then, I spooned the salsa out over each one of them."
        show adine normal b at center with ease   
        m "We sat at the small table in the kitchen, and even though I was hungry, I just waited to see how Adine would react to the tacos."
        m "She pinched the tortillas in between two of her claws and turned her head to the side to bite at it. I didn't realize how large dragon muzzles were until she ate half the taco in one bite."
        play sound "fx/bite.wav"
        $ renpy.pause(1.25)
        Ad "I've had fish tacos before, but the salsa makes it much better! It's that perfect balance of sweetness and spiciness, and the fish makes it so savory, too!"
        m "I bit into my own taco, and she was right! The fish was flakey and light, cooked expertly, and the salsa was bursting with flavor! Considering my past life, being able to taste fresh fruit like this was somethign else."
        c "Glad you like it. It's been a long time since I've made these, but it seems like I still have it. Maybe I can try making other types of salsas later."
        Ad "A lot of the fruit at Zhong's market is picked fresh. We're lucky that this town is near several farms."
        c "Gives more dragons more jobs, right? It's probably good for the-"
        m "I didn't realize it at the time, but she had cleaned her entire plate. Her head was pointed down at my remaining tacos - I was still working my way through the second one."
        c "Adine?"
        Ad giggle b "Oh! I'm sorry, [player_name]! It's just that, well, they were so good, and we're out of fish. So..."
        m "I couldn't hide a grin as I pushed my plate to her."
        c "You can have mine, too. I think you want them more than I do."
        m "Adine didn't say anything, but the way she pinched up another taco and ate it spoke for itself. It didn't surprise me that she would enjoy actual food, considering her ramen-fueled diet."
        m "I just sat there and finished my own food as she set out on her sixth taco. I was still a bit hungry, but seeing her reaction was worth it alone."
        hide adine with dissolve
        $ renpy.pause(1.25)
        show adineapt2 at Pan((0,233),(0,233),0.0) with dissolve
        m "..."
        m "I was surprised she was able to eat that much, but apparently dragons didn't have cooking as refined as ours. It made me feel a bit important to expose her to this sort of cusine."
        c "I know wine after fish tacos sounds odd, but I think we should treat ourselves tonight."
        jump adine_wine
        
    if adine_mouflon_available==False:
        c "We're going to be making a good mouflon stew. Something that'll last you for a while, at least"
        Ad "A stew? Is it good? I've actually only had ramen broth as soup."
        c "This tastes way different than ramen broth. It's much more richer and flavorful."
        Ad "Sounds good. But you must be making a lot of it, considering the all the ingredients you have out."
        c "It's definitely a lot of food. You'll be able to store it as leftovers... if you can figure out how to stop eating it."
        Ad "Will it be that good?"
        c "You dare doubt my cooking skills again?"
        Ad giggle b "Let's just see where this goes, silly."
        c "First, we'll need to take care of all the vegetables. If you could start dicing those potatoes for me, that would be great. And do you have a pot? A large one."
        show adine normal b at right with ease   
        Ad "Yeah, in the cupboard down there."
        play sound "sfx/chopping.ogg"
        m "As I took a can opener to all of the mouflon broth containers, the sound of chopping began to fill the room. I should have known Adine was fast, especially since she worked in a cafe for a living."
        play sound "fx/water1.ogg"
        m "There were enough cans of broth to fill the pot up almost to the top. We were definitely making a lot of stew today."
        Ad "Here are the potatoes. What's next?"
        c "The carrots and the onions. I'll prepare the mouflon while you cut those up."
        m "I unwrapped the paper meat package. Adine wasn't kidding - it definitely smelled pretty gamey. Surprisingly, it had the consistency of beef steaks when I cut through it. Honestly, if someone had handed me this and told me it was beef, I would have believed them."
        m "The ingredient bowls began to multiply. One for sliced onions, one for chopped carrots, yet another one for diced potatoes. And lastly, my own bowl for cubed mouflon"
        c "It's actually pretty simple from here. We just dump all of these ingredients into that broth and let it cook."
        Ad "That's it? I thought it would be more complicated than that."
        show adine normal b at left with ease   
        play sound "fx/splashes2.ogg"
        m "We poured bowl after bowl into the broth. We stared into the glossy surface as everything slowly sank to the bottom of the pot."
        c "The trick's all in the seasoning. Salt, pepper, garlic powder, bay leaves..."
        m "I measured out seasoning after seasoning, adding them all to the broth bit by bit. Adine apparently invested in a spice rack a while ago, but it had gathered dust..."
        Ad "How do you know how to mix all of them like that? I could never figure it out, and everything I made tasted overseasoned."
        c "Trial and error, mostly. I'll teach you all of the good combinations later. And lastly..."
        play sound "fx/pour.ogg"
        c "I picked up the bottle of wine Adine had left on the counter and uncorked it, pouring a cup or two of it in."
        Ad "Is this an alcoholic stew?"
        c "Alcoholic? No, the wine's just for flavoring. The alcohol burns off with heat, but you still get the richness and taste of the wine. It won't get you drunk."
        Ad "Oh, alright. I didn't realize that would happen."
        c "And I think we're done! One last thing's left..."
        Ad "What is it?"
        c "We wait for six hours."
        Ad "... six hours?"
        c "It'll take a while for everything to cook. More importantly, the flavors need time to blend together. Let's go to the park while the stew comes together."
        stop music fadeout 2.0
        scene black with dissolveslow
        $ renpy.pause(2)
        show adineapt2 at Pan((0,233),(0,233),0.0) with dissolve
        play sound "fx/door/door_open.wav"
        play music "mx/jazzy.ogg" fadein 2.0
        m "When we opened the door, a sheer wall of aroma hit us right then and there. Just the smell of that rich mouflon broth made me salivate."
        Ad "Is that the stew?"
        c "That's the stew, yes."
        play sound "fx/door/doorclose.ogg"
        m "Despite her eagerness, she didn't rush to the kitchen. The pot lid was steaming, but thankfully nothing seemed to have spilled out. I lifted it open and let the full aroma of the stew fill the kitchen."
        c "So now do you think the wait was worth it?"
        Ad "It smells really good. Hold on."
        play sound "fx/dishes.wav"
        show adine normal b at center with ease   
        m "I barely saw her retrieve two bowls from the cabinets, her motions so fast that she returned with a ladle in hand only a second later. She didn't even ask permission for getting the stew, filling her bowl to the brim."
        c "Are you that hungry? We had a light lunch."
        Ad "Just put this on the table. And this one, too!"
        m "I was just finished setting the first bowl down when she shoved another one into my hands. That one almost burned my hands before I set it down, too. I didn't realize that Adine could get so impatient, but that may have just been her hunger."
        m "We sat down at the table, and Adine laid out a fork and spoon for both of us."
        play sound "fx/slurp.ogg"
        Ad "This is really good! It's so rich!"
        m "She wasn't kidding. Maybe it was just not having eaten this kind of meal for a long time, but I could taste everything - the meatiness of the mouflon, the slight bite of the onions, the heartiness of the potatoes..."
        Ad "And this was all made from just combining a bunch of ingredients in a pot?"
        c "Yeah. Stews are pretty simple as far as foods go, but they just take a long time to cook. But once you do..."
        m "Adine seemed to have just been drinking the soup the entire time. All of the meats and vegetables were starting to form a little island at the center of her bowl."
        c "You shouldn't just drink the soup. The mouflon is just as tasty."
        Ad "But it tastes so good!"
        c "Try to get a bit of soup and a chunk of mouflon at the same time."
        m "I saw her spoon some meat out and eat it. Her eyes went wide, and soon she preoccupied herself with eating even more."
        Ad "The meat's so soft! It melted in my mouth so easily! And all of the vegetables have that mouflon taste to them, too."
        c "That's what happens when you let everything cook for so long together."
        Ad "But that easily?"
        c "That easily."
        play sound "fx/chair.wav"
        hide adine with dissolve
        m "She had completely cleaned her bowl! I wasn't even halfway through mine, but she was already ladling herself a second serving."
        c "Try not to eat the whole thing. Otherwise you won't have leftovers for the next few days."
        show adine normal b with dissolve
        Ad "I'll try my best not to, but no promises!"
        $ renpy.pause(1.25)
        m "..."
        m "I was surprised she was able to eat that much, but apparently dragons didn't have cooking as refined as ours. It made me feel a bit important to expose her to this sort of cusine."
        c "I know wine after soup like sounds odd, but I think we should treat ourselves tonight."
        jump adine_wine
        
label adine_wine:
        Ad "I don't mind at all. Just a glass, though. I don't drink much."
        play sound "fx/pouringwine.ogg"
        Ad "To what do we owe this to?"
        menu:
            "Saving the world!":
                Ad giggle b "It feels so silly saying it out loud, but it's true. To saving the world!"
            "Our friendship.":
                Ad "I'm definitely glad I got to know you like this. To our friendship."
            "Just a relaxing night.":
                Ad "Yeah, this has been really nice so far. To a relaxing night."
        play sound "fx/clink.ogg"
        show adine normal b
        c "The wine was much, much better than the one Remy bought. It tasted rich and earthy, and I let it sit in my mouth for just a minute."
        Ad "I haven't had wine in a long time, but this is really good. Maybe I should drink more often."
        c "Not too often, I hope."
        m "I took another sip, letting the warmth fill my mouth again. It felt smooth and relaxing, and I couldn't help but let out a content sigh."
        Ad "So I'm curious, [player_name]. Have you done something like this with any other dragon?"
        c "What do you mean?"
        Ad "Well, since you have that credit card, you can buy anything you want, right? Have you ever taken another dragon out like this?"
        menu:
            "Yes":
                Ad "I'm not surprised. Any human would be a celebrity around here, and there are a lot of dragons who are interested in humans."
                Ad "But either way, thank you for all of this. I've really wanted a break like this. This has been my best day in a really long time."
            "No":
                Ad "Really? I'm surprised. I thought dragons would be lining up just to be with you. But that makes my time with you that much more valuable, doesn't it?"
                Ad "..."
                Ad "Thank you for everything, really. It means a lot to me."
        play sound "fx/glassdown.wav"
        m "She finished the last of her glass, setting it down on the table a bit more unsteadily than before."
        Ad "Do you remember the scale polisher I bought today? It's been such a long time since I've used it. Could you... help me out with it?"
        menu:
            "Yes":      
                play sound "fx/chair.wav"
                m "We pushed away from the table, but before I could say anything, she approached me and wrapped me in a hug."
                play sound "sfx/bandage2.ogg"
                m "Her wings was leathery and warm as they wrapped around me. I didn't really have much room to move at all, considering that she was completely draped over my body. But I didn't want to - not right now, at least."
                m "I tried my best to raise my arms under her hold, and I got them somewhat around her body. That action seemed to give her confidence, and she laid her head on my shoulder for a moment."
                Ad "Humans are warm. Really warm. If I had known, I would have done this earlier."
                c "Perhaps you should do it more often in the future, then."
                Ad giggle b "Silly."
                m "We held but for a moment, and then she let go. I didn't really know how to read her expression, but all I knew was that it was the cutest a dragon could ever be."
                Ad "Let me get the polisher. I'll be in the bathroom."
                hide adine with dissolve
                m "She disappeared into the other room. I swirled the last of my wine in the glass before drinking the rest of it."
                m "I gave her a minute or so before I left as well. I remember where the bathroom was from my last visit here, so finding it wasn't a problem."
                stop music fadeout 2.0
                scene black with dissolveslow
                play sound "fx/door/door_open.wav"
                $ renpy.pause(1.0)
                c "Adine, I'm ready- ... oh."
                Ad "[player_name]?"
                c "I thought I was going to polish your scales, Adine."
                Ad "Well, you could do that, but you could also... well..."
                menu:
                    "Accept":
                        c "I wouldn't mind helping out at all. But first things first..."
                        jump adine_mod_credits
                    "Reject":
                        c "Adine, I, uh- I don't-"
                        Ad "It's alright, [player_name]. I, uh, didn't expect you to be interested, anyways..."
                        c "I'm sorry, Adine. I didn't know."
                        play sound "fx/door/doorclose.ogg"
                        jump adine_mod_credits
                    "Scream":
                        show bsod at Pan((0,0),(0,0),0.0)
            "No":
                Ad "Aw, alright. Maybe next time then. Hey, there's an episode of \"Humans\" on soon! Want to watch it with me?"
                c "What's the show about?"
                Ad giggle b "Take a guess."
                hide adine with dissolve
                m "With that, she led me to the living room. We grabbed a couple spots on her bed, and she showed me the bizarre nature of the show supposedly designed after us - or at least, how they saw us."
                m "Adine failed to mention that it was boring, though. It wasn't twenty minutes before we had just fallen asleep on each other, the food and wine we ate not helping at all..."
                scene black with dissolveslow
                jump adine_mod_credits
                
label adine_mod_credits:
    stop music fadeout 2.0
    $ renpy.pause (4)

    $ _game_menu_screen = None
    nvl clear
    n "Thanks for playing! Be sure to check out the other food options as well!"
    n "         -waveshine"
    $ renpy.pause (3)
    return
