
label TLAMaverickCafe:

    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - TLAMaverick - Cafe"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - TLAMaverick - Cafe"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - TLAMaverick - Cafe"

    else:
        $ save_name = "Chapter 1 - TLAMaverick - Cafe"

m "It took us a while to get to the cafe. Maverick was still keeping eye on me, making sure i am not going to fool him any way."

scene cafe with dissolvemed

m "When we arrived, Maverick took a seat next to one of the tables, while i took a seat in front of him."

show maverick normal with dissolve

c "So...anything you would like to eat?"

Mv "Steak..."

show maverick at Position(xpos = 0.7) with ease

show adine normal b flip at left with easeinleft

Ad "Hello, may I take your order?"

c "Yes, two steaks for us, please."

Ad "Rare, medium rare or well done?"

menu:
    "Rare.":
        Ad "Is that everything?"
        $ steak = "Rare"
    "Medium rare.":
        Ad "Is that everything?"
        $ steak = "Medium rare"    
    "Well done.":
        Ad "Is that everything?"
        $ steak = "Well done"
    "Raw.":
        Mv blush "..."
        $ TLAMaverickpoints += 1
        Ad "Is that everything?"
        $ steak = "raw"
    
c "Yes, thank you."

hide adine with easeoutleft

if steak == "raw":
      show maverick blush at center with ease
      Mv blush "I..love raw steak..."
      c "We humans don't eat them raw usually, but i want to give it a try this time."
      show maverick nice with dissolve

else:
  show maverick at center with ease
  Mv normal "Also steak, huh?"
  c "Yeah, i thought i will give it a try."

Mv "So, if i may ask. Why did you come here? Be honest."

menu:
    "To save my kind.":
        Mv "Hah...typical talk. Reza was the same."
        jump TLAMaverickFoodReady
    "I've always wanted to see a real dragon.":
        Mv "Oh, really? Why though?"   
        jump TLAMaverickChoiceOne
    "I am not sure.":
        Mv "Heh...you don't even know why are you here."
        jump TLAMaverickFoodReady

label TLAMaverickFoodReady:

show maverick normal with dissolve

show maverick at Position(xpos = 0.7) with ease

show adine normal b flip at left with easeinleft

Ad "Your order is ready."

c "Thank you."

play sound "fx/dishes.wav"

m "Dragon put two plates on the table before dissapearing."

hide adine with easeoutleft

show maverick at center with ease

m "Maverick, not waiting anymore, took his whole steak in his teeth, before throwing it up and swallowing whole at once."

c "..."

Mv "What? I was hungry..."

menu:
    "Nothing. It's fine.":
        Mv nice "..."
    "It was cute.":
        Mv blush "Y..you really think that?"   
        c "Yes."
        $ TLAMaverickpoints += 1  
    "[[Say nothing.]":
        Mv normal "..."

m "I took my steak in my hands, biting a piece off before chewing on it. Maverick was watching me closely as i was consuming my food."

m "It was longer then Maverick, but after some bites i finished my steak."

c "It was really tasty."

m "Maverick, probably bored by my speed of eating laid his head on the table."

Mv "Finished already?"

c "Yeah..."

m "He looked up at me, his red eyes watching my face when i was looking down at him."

menu:
    "It's getting late, i should go and make raport on Police Station.":
        jump TLAMaverickGoAway
    "[[Pet him.]":
        jump TLAMaverickGoAwayPet
    "[[Kiss his snout.]":
        jump TLAMaverickGoAwayKiss
