
label TLAMaverickChoiceOne:

    if chapter4unplayed == False:
        $ save_name = "Chapter 4 - TLAMaverick - Cafe"

    elif chapter3unplayed == False:
        $ save_name = "Chapter 3 - TLAMaverick - Cafe"

    elif chapter2unplayed == False:
        $ save_name = "Chapter 2 - TLAMaverick - Cafe"

    else:
        $ save_name = "Chapter 1 - TLAMaverick - Cafe"

menu:
    "Beacause dragons are awesome!":
        Mv "Heh..."
    "Because dragons are cute and lovely.":
        Mv blush "..."
        $ TLAMaverickpoints += 1  
jump TLAMaverickFoodReady


label TLAMaverickGoAway:

Mv "Sure."

$ renpy.pause (1.0)

Mv blush "Thanks for today..."

c "No problem. Bye Maverick!"

Mv nice "Bye." 

jump TLAMaverickEnd

label TLAMaverickGoAwayPet:

if TLAMaverickpoints >= 2:
 
     Mv blush "Murr..."
     
     c "Did you just...?"
     
     Mv nice "Shut up and continue..."
     
     m "I smiled, seeing Maverick that enjoy pets."
     
     m "After some time have passed, i stopped."
     
     Mv blush "That was...nice. You should go now, it's getting late."
     
     c "Yeah...Mav...Thank you. For today."
     
     Mv nice "My pleasure."

else:

 show maverick rage with dissolve
 
 play music "mx/termination.ogg" fadein 2.0
 
 $ renpy.pause (1.0)
 
 Mv rage "What the hell are you thinking about?"

 Mv rage "You think i am some kind of pet?!"

 m "Maverick roared loudly and left cafe, clearly not happy for petting him."

 hide maverick with easeoutleft
jump TLAMaverickEnd

label TLAMaverickGoAwayKiss:

if TLAMaverickpoints >= 3:
 
   play sound "fx/kiss.wav"
   $ renpy.pause(1.0)
 
   Mv blush "Did you just...?"
   
   c "Yes i did. Hope you don't mind."
   
   Mv nice "..."
   
   Mv nice "No i don't. Actually..."
   
   play sound "fx/kiss.wav"
   
   m "He moved his head to my face, leaving a kiss on my cheek."
   
   Mv blush "You should go now, it's getting late."
   
   c "Y..yeah...Thanks Mav."
   
   Mv nice "My pleasure, sweetie."

else:

  play sound "fx/kiss.wav"
  $ renpy.pause(1.0)
   
  show maverick rage with dissolve
 
  play music "mx/termination.ogg" fadein 2.0
 
  $ renpy.pause (1.0)
 
  Mv rage "What the hell are you thinking about?"

  Mv rage "You think you can just kiss me whenever you want?!"

  m "Maverick roared loudly and left cafe, clearly not happy for kissing him."
 
  hide maverick with easeoutleft
  
jump TLAMaverickEnd

label TLAMaverickEnd:

show blackbg with dissolvemed

$ renpy.pause (1.0)

if not persistent.playedTLAMaverick:

    $ persistent.playedTLAMaverick = True

nvl clear

window hide

show TLAMaverickCredits with dissolvemed

s "Congratulations! You finished TLAMaverick mod made by Keegen."

s "Moving to menu..."

$ renpy.pause (2.0)