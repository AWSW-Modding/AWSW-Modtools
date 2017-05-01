#Defining assets in a differnt file  made it easier for me to make a WIP demo, my files are kept in a differnt directory 
#I spent sooooooo long getting the kothorix spirtes right, I was always more than a bit off in each one, they all had to edited to fit a std size
#Declare Images
image kothorix normal = "char/kothorix/happy_face-arms.png"
image kothorix normal crossed ="char/kothorix/happy_face.png"
image kothorix normal crossed distance ="char/kothorix/happy_face_side.png"
image kothorix displeased ="char/kothorix/um_face.png"
image kothorix disgusted ="char/kothorix/ugh_face.png"
image kothorix sad down ="char/kothorix/sad_down.png"
image kothorix somber face ="char/kothorix/somber_face.png"
image kothorix uninterested distance ="char/kothorix/uninterested distance.png"
image kothorix hey you ="char/kothorix/hey_you.png"
image kothorix thinking ="char/kothorix/thinking.png"
image kothorix unamused point ="char/kothorix/unamused_point.png"
image kothorix unamused point_distance ="char/kothorix/unamused-point-side.png" 
image kothorix wtf ="char/kothorix/wtf.png"
image kothorix yuno ="char/kothorix/yuno.png"
image kothorix eyes closed ="char/kothorix/eyes_closed.png"
image kothorix ramble ="char/kothorix/ramble.png"
image kothorix ramble face ="char/kothorix/ramble_face.png"

#Darker images
image kothorix normal dk = im.Recolor("char/kothorix/happy_face-arms.png", 240, 240, 250, 255)
image kothorix normal crossed dk =im.Recolor("char/kothorix/happy_face.png", 240, 240, 250, 255)
image kothorix normal crossed distance dk =im.Recolor("char/kothorix/happy_face_side.png", 240, 240, 250, 255)
image kothorix displeased dk =im.Recolor("char/kothorix/um_face.png", 240, 240, 250, 255)
image kothorix disgusted dk =im.Recolor("char/kothorix/ugh_face.png", 240, 240, 250, 255)
image kothorix sad down dk =im.Recolor("char/kothorix/sad_down.png", 240, 240, 250, 255)
image kothorix somber face dk =im.Recolor("char/kothorix/somber_face.png", 240, 240, 250, 255)
image kothorix uninterested distance dk =im.Recolor("char/kothorix/uninterested distance.png", 240, 240, 250, 255)
image kothorix hey you dk =im.Recolor("char/kothorix/hey_you.png", 240, 240, 250, 255)
image kothorix thinking dk =im.Recolor("char/kothorix/thinking.png", 240, 240, 250, 255)
image kothorix unamused point dk =im.Recolor("char/kothorix/unamused_point.png", 240, 240, 250, 255)
image kothorix unamused point_distance dk =im.Recolor("char/kothorix/unamused-point-side.png" , 240, 240, 250, 255)
image kothorix wtf dk =im.Recolor("char/kothorix/wtf.png", 240, 240, 250, 255)
image kothorix yuno dk =im.Recolor("char/kothorix/yuno.png", 240, 240, 250, 255)
image kothorix eyes closed dk =im.Recolor("char/kothorix/eyes_closed.png", 240, 240, 250, 255)
image kothorix ramble dk =im.Recolor("char/kothorix/ramble.png", 240, 240, 250, 255)
image kothorix ramble face dk =im.Recolor("char/kothorix/ramble_face.png", 240, 240, 250, 255) 

#Flipped Images
image kothorix normal flip = im.Flip("char/kothorix/happy_face-arms.png", horizontal=True)
image kothorix normal crossed flip =im.Flip("char/kothorix/happy_face.png", horizontal=True)
image kothorix normal crossed distance flip =im.Flip("char/kothorix/happy_face_side.png", horizontal=True)
image kothorix displeased flip =im.Flip("char/kothorix/um_face.png", horizontal=True)
image kothorix disgusted flip =im.Flip("char/kothorix/ugh_face.png", horizontal=True)
image kothorix sad down flip =im.Flip("char/kothorix/sad_down.png", horizontal=True)
image kothorix somber face flip =im.Flip("char/kothorix/somber_face.png", horizontal=True)
image kothorix uninterested distance flip =im.Flip("char/kothorix/uninterested distance.png", horizontal=True)
image kothorix hey you flip =im.Flip("char/kothorix/hey_you.png", horizontal=True)
image kothorix thinking flip =im.Flip("char/kothorix/thinking.png", horizontal=True)
image kothorix unamused point flip =im.Flip("char/kothorix/unamused_point.png", horizontal=True)
image kothorix unamused point_distance flip =im.Flip("char/kothorix/unamused-point-side.png", horizontal=True)
image kothorix wtf flip =im.Flip("char/kothorix/wtf.png", horizontal=True)
image kothorix yuno flip =im.Flip("char/kothorix/yuno.png", horizontal=True)
image kothorix eyes closed flip =im.Flip("char/kothorix/eyes_closed.png", horizontal=True)
image kothorix ramble flip =im.Flip("char/kothorix/ramble.png", horizontal=True)
image kothorix ramble face flip =im.Flip("char/kothorix/ramble_face.png", horizontal=True)

#darker flipped images
image kothorix normal flip dk =im.Flip(im.Recolor("char/kothorix/happy_face-arms.png", 240, 240, 250, 255), horizontal=True)
image kothorix normal crossed flip dk =im.Flip(im.Recolor("char/kothorix/happy_face.png", 240, 240, 250, 255), horizontal=True)
image kothorix normal crossed distance flip dk =im.Flip(im.Recolor("char/kothorix/happy_face_side.png", 240, 240, 250, 255), horizontal=True)
image kothorix displeased flip dk =im.Flip(im.Recolor("char/kothorix/um_face.png", 240, 240, 250, 255), horizontal=True)
image kothorix disgusted flip dk =im.Flip(im.Recolor("char/kothorix/ugh_face.png", 240, 240, 250, 255), horizontal=True)
image kothorix sad down flip dk =im.Flip(im.Recolor("char/kothorix/sad_down.png", 240, 240, 250, 255), horizontal=True)
image kothorix somber face flip dk =im.Flip(im.Recolor("char/kothorix/somber_face.png", 240, 240, 250, 255), horizontal=True)
image kothorix uninterested distance flip dk =im.Flip(im.Recolor("char/kothorix/uninterested distance.png", 240, 240, 250, 255), horizontal=True)
image kothorix hey you flip dk =im.Flip(im.Recolor("char/kothorix/hey_you.png", 240, 240, 250, 255), horizontal=True)
image kothorix thinking flip dk =im.Flip(im.Recolor("char/kothorix/thinking.png", 240, 240, 250, 255), horizontal=True)
image kothorix unamused point flip dk =im.Flip(im.Recolor("char/kothorix/unamused_point.png", 240, 240, 250, 255), horizontal=True)
image kothorix unamused point_distance flip dk =im.Flip(im.Recolor("char/kothorix/unamused-point-side.png" , 240, 240, 250, 255), horizontal=True)
image kothorix wtf flip dk =im.Flip(im.Recolor("char/kothorix/wtf.png", 240, 240, 250, 255), horizontal=True)
image kothorix yuno flip dk =im.Flip(im.Recolor("char/kothorix/yuno.png", 240, 240, 250, 255), horizontal=True)
image kothorix eyes closed flip dk =im.Flip(im.Recolor("char/kothorix/eyes_closed.png", 240, 240, 250, 255), horizontal=True)
image kothorix ramble flip dk =im.Flip(im.Recolor("char/kothorix/ramble.png", 240, 240, 250, 255), horizontal=True)
image kothorix ramble face flip dk =im.Flip(im.Recolor("char/kothorix/ramble_face.png", 240, 240, 250, 255), horizontal=True) 

#Anna really mad
image anna furious ="char/anna/anna_really_mad.png"
image anna furious flip =im.Flip("char/anna/anna_really_mad.png", horizontal=True)

#Card's
image card ="card/cardsignedbig.png"
image callmecard ="card/callmecard.png"

#Scenes
image cafer ="backg/cafer.jpg"
image arcade ="backg/arcade.jpg"

#arcade sprites
image koth 1 ="arch/kothorix-sprite1.png" 
image koth 2 ="arch/kothorix-sprite2.png"
image genDrag 1 ="arch/bonnar1.png"
image genDrag 2 ="arch/bonnar2.png"
image wifeDrag ="arch/aaliyah1.png"

#arcade characters
define Ks = Character(None, window_background="textbox.png")
define Gd = Character(None, window_background="textbox.png")

#Define character
#define Kx = Character("Kothorix", color="#328EFF", image="kothorix")
define Kx = Character("Kothorix", color="#3F95FF", image="kothorix")

#The debug manager is a nice guy, he let's me know my fuck ups
define Db = Character("Debug Manager", color="#919191", image="")

#Define Audio - I didn't think it would work but it does, I havn't seen anyone define audio within renpy before
#Crinkles - Soundtrack from a box 16. 
define audio.haze = "sound/msc/haze.ogg"
define audio.alps = "sound/msc/alps.ogg"
define audio.bolt = "sound/msc/bolt.ogg"
define audio.terrace = "sound/msc/terrace.ogg"
#Pirate manners - Caps on, hats off
define audio.kothorixtheme = "sound/msc/kothorix_theme.ogg"
#Rick and morty reference
define audio.moonmen = "sound/msc/moonmen.mp3"

#sound effects
define audio.runawayfxkx = "sound/sfx/running-away.ogg"
define audio.dialout = "sound/sfx/dial_out_tone.ogg"
define audio.cuptable = "sound/sfx/cup_on_table.ogg"
define audio.silence = "fx/silence.ogg"
define audio.coin = "sound/sfx/insert_coin.ogg"
define audio.hitfail = "sound/sfx/hitfail.ogg"
define audio.lightning = "sound/sfx/lightningcrash.ogg"
define audio.slap = "fx/slap1.wav" 
define audio.bookopen = "sound/sfx/openbook.ogg" 
define audio.bookclose = "sound/sfx/closebook.ogg" 
define audio.champagne = "sound/sfx/champagne-pop-and-pour.ogg"
define audio.glass_bowl = "sound/sfx/glass_bowl_clank.ogg"     
define audio.glass_glass = "sound/sfx/glass_glass_clank.ogg"   

screen action_menu():
    tag menu

    frame:
        style_group "Test"
        xalign .25
        yalign .80
        
        hbox:
            textbutton _("Reason With") action Return (1)
            textbutton _("Attack") action Return (2)
            textbutton _("Cosmic Horror") action Return (3)

init -2:

    style Test:
        bar_vertical False

    style Test_frame:
        background "arch/textboxx.png"
        hover_background "arch/textboxx.png"
        selected_background "arch/textboxx.png"

    style Test_button:
        background "#0707A7"
        hover_background "#1578A5"
        selected_background "#71CDF7"
        right_margin 150
        left_margin 150
        top_margin 140
        outlines [(4, "#E0E0E1", absolute(0), absolute(0))]

    style Test_button_text:
        text_align 0.5
        size 60
        color "#FFFFF0"
        selected_color "#FFFFF0"
        antialias False
        font "Munro.ttf"