###--------------------init stuff--------------------
init python:
    #All the python code for the arcade game

    persistent.showautoforwardbutton = True

    renpy.music.register_channel("cpswright", "sfx", False)

    def get_screen_var(screen, name):
        cs = renpy.get_screen(screen)
        if cs is not None:
            return cs.scope[name]

    def lbd_narr_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            s = get_screen_var("say", "what")

            if s:
                intervals = []
                words = s.split()
                #speed = float(_preferences.text_cps)
                speed = float(lbd_arch_fstnarr_cps)
                for w in words:
                    intervals.append((len(w)+1)/speed) # We add 1 to account for spaces...
                renpy.show_screen("silly_timers", intervals, "sfx/arc/narr.wav")

        elif event == "slow_done":
            renpy.hide_screen("silly_timers")

    def lbd_slwnarr_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            s = get_screen_var("say", "what")

            if s:
                intervals = []
                words = s.split()
                #speed = float(_preferences.text_cps)
                speed = float(lbd_arch_char_cps)
                for w in words:
                    intervals.append((len(w)+1)/speed) # We add 1 to account for spaces...
                renpy.show_screen("silly_timers", intervals, "sfx/arc/narr.wav")

        elif event == "slow_done":
            renpy.hide_screen("silly_timers")

    def lbd_ronan_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            s = get_screen_var("say", "what")

            if s:
                intervals = []
                words = s.split()
                #speed = float(_preferences.text_cps)
                speed = float(lbd_arch_char_cps)
                for w in words:
                    intervals.append((len(w)+1)/speed) # We add 1 to account for spaces...
                renpy.show_screen("silly_timers", intervals, "sfx/arc/ronan.wav")

        elif event == "slow_done":
            renpy.hide_screen("silly_timers")

    def lbd_buddy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            s = get_screen_var("say", "what")

            if s:
                intervals = []
                words = s.split()
                #speed = float(_preferences.text_cps)
                speed = float(lbd_arch_char_cps)
                for w in words:
                    intervals.append((len(w)+1)/speed) # We add 1 to account for spaces...
                renpy.show_screen("silly_timers", intervals, "sfx/arc/buddy.wav")

        elif event == "slow_done":
            renpy.hide_screen("silly_timers")

    def lbd_wolf_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            s = get_screen_var("say", "what")

            if s:
                intervals = []
                words = s.split()
                #speed = float(_preferences.text_cps)
                speed = float(lbd_arch_char_cps)
                for w in words:
                    intervals.append((len(w)+1)/speed) # We add 1 to account for spaces...
                renpy.show_screen("silly_timers", intervals, "sfx/arc/deep.wav")

        elif event == "slow_done":
            renpy.hide_screen("silly_timers")

    def lbd_damage(mini, maxi, multi=False):
        damage = renpy.random.randint(mini, maxi)

        if multi:
            if multi == 2:
                #10% chance
                if renpy.random.randint(1, 10) == 1:
                    damage = (damage * 3)
                else:
                    damage = (damage * multi)
            else:
                damage = (damage * multi)

        return damage


    # arcade cheating
    class arcadeListener(renpy.Displayable):

        def __init__(self, target):

            renpy.Displayable.__init__(self)

            import pygame

            # The label we jump to when the code is entered.
            self.target = target

            # This is the index (in self.code) of the key we're
            # expecting.
            self.state = 0

            # The code itself.
            self.code = [
                pygame.K_UP,
                pygame.K_UP,
                pygame.K_DOWN,
                pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_b,
                pygame.K_a,
                ]

        # This function listens for events.
        def event(self, ev, x, y, st):
            import pygame

            # We only care about keydown events.
            if ev.type != pygame.KEYDOWN:
                return

            #If key is not on list
            if ev.key != self.code[self.state]:
                self.state = 0
                return

            # cont
            self.state += 1

            # If we are at the end of the code, then call the target label in
            # the new context. (After we reset the state machine.)
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)

            return

        # Return a small empty render, so we get events.
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)

    store.arc_cheat_listener = arcadeListener('konami_code')

    def arc_cheat_overlay():
        ui.add(store.arc_cheat_listener)

    def init_arc_listener():
        config.overlay_functions.append(arc_cheat_overlay)

    def remove_arc_listener():
        config.overlay_functions.remove(arc_cheat_overlay)


###--------------------Extra sprite's--------------------
image lorem cry = "char/lorem/lorem_cry.png"
image lorem cry flip = im.Flip("char/lorem/lorem_cry.png", horizontal=True)
image lorem drunk = "char/lorem/lorem_drunk.png"
image lorem drunk flip = im.Flip("char/lorem/lorem_drunk.png", horizontal=True)
image scientist-a normal = "char/a_neutral.png"
image scientist-a normal flip = im.Flip("char/a_neutral.png", horizontal=True)
image scientist-a mad = "char/a_mad.png"
image scientist-a mad flip = im.Flip("char/a_mad.png", horizontal=True)
image scientist-a happy = "char/a_happy.png"
image scientist-a happy flip = im.Flip("char/a_happy.png", horizontal=True)

image scientist-m normal = "char/m_normal.png"
image scientist-m normal flip = im.Flip("char/m_normal.png", horizontal=True)
image scientist-m mad = "char/m_mad.png"
image scientist-m mad flip = im.Flip("char/m_mad.png", horizontal=True)
image scientist-m happy = "char/m_happy.png"
image scientist-m happy flip = im.Flip("char/m_happy.png", horizontal=True)


###--------------------Optional Sideface's--------------------
init 200:
    if "AWSW_Sidefaces" in modinfo.modlist:
        image side lorem cry = Image("sdf/lorem_cry.webp", xalign=0.01, yalign=1.0)
        image side lorem cry flip = Image("sdf/lorem_cry.webp", xalign=0.01, yalign=1.0)
        image side lorem drunk = Image("sdf/lorem_drunk_side.webp", xalign=0.01, yalign=1.0)
        image side lorem drunk flip = Image("sdf/lorem_drunk_side.webp", xalign=0.01, yalign=1.0)

###--------------------Scenes--------------------
image forestevening = "bg/forest_evening.jpg"
image insidetrain = "bg/train_one.jpg"
image trainstation = "bg/train_station_noon.jpg"
image trainstation-dusk = "bg/train_station_almost_dusk.jpg"
image trainstation-night = "bg/train_station_night.jpg"
image outsidestation = "bg/Auditorium_Outside_Noon.jpg"
image arcade_bg = "bg/arcade.jpg"
image medieval_day = "bg/medieval_path_daye.jpg"
image lbd_panorama1 = "bg/pano/panorama1.jpg"
image lbd_panorama2 = "bg/pano/panorama2.jpg"
image lbd_panorama3 = "bg/pano/panorama3.jpg"
image lbd_kimberland_town = "bg/kimberland_town.jpg"
image underpass = "bg/the_glorious_underpass_day.jpg"
image dark-allyway = "bg/deep_dark_fantasy2.jpg"
image kimberland_evening = "bg/kimberland_hub_night.jpg"
image kimberland_trainstation = "bg/kimberland_trainstation.jpg"
image town_road_b = "bg/4_road_b.jpg"
image fancy_class_carriage = "bg/1st_class_carriage.jpg"
image lorem-train-cg = "cgp/final-resize.jpg"
image bridge_keeper = "bg/bridge_keeper.jpg"
image visiting_ipsum = "bg/oriental_day.jpg"
image visiting_ipsum_night = "bg/oriental_night.jpg"
image lbd_battle_background = "arch/battle background.jpg"

###--------------------Random Shit--------------------
image lime_achievement:
    "ui/lime_achievement.png"
    subpixel True
    ycenter 0.0
    xcenter 1.0
    xoffset -119
    yoffset -46.5
    alpha 0.0

    on appear:
        yoffset -46.5 alpha 0.0

    on show:
        linear 0.5 yoffset 46.5 alpha 1.0

    on hide:
        linear 0.5 yoffset -46.5 alpha 0.0


###--------------------Animated Scenes--------------------
#========From 3==========
image lbd_pano32:
    subpixel True

    contains:
        parallel:
            "bg/pano/panorama2.jpg"
            xoffset -1920
            linear 1.2 xoffset 0

    contains:
        parallel:
            "bg/pano/panorama3.jpg"
            linear 1.2 xoffset +1920

#========From 2==========
image lbd_pano21:
    subpixel True

    contains:
        parallel:
            "bg/pano/panorama1.jpg"
            xoffset -1920
            linear 1.2 xoffset 0

    contains:
        parallel:
            "bg/pano/panorama2.jpg"
            linear 1.2 xoffset +1920

image lbd_pano23:
    subpixel True

    contains:
        parallel:
            "bg/pano/panorama3.jpg"
            xoffset +1920
            linear 1.2 xoffset 0

    contains:
        parallel:
            "bg/pano/panorama2.jpg"
            linear 1.2 xoffset -1920

#========From 1==========
image lbd_pano12:
    subpixel True

    contains:
        parallel:
            "bg/pano/panorama2.jpg"
            xoffset +1920
            linear 1.2 xoffset 0

    contains:
        parallel:
            "bg/pano/panorama1.jpg"
            linear 1.2 xoffset -1920


###--------------------Animated imagebuttons--------------------
#Arcade icon
image arcadeicon-idle:
    subpixel True
    zoom 0.5
    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/arcadeiconcabinet.png")

image arcadeicon-Selected:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/arcadeiconcabinet_selected.png")

image arcadeicon-insensitive_idle:
    subpixel True
    zoom 0.5
    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/arcadeiconcabinet.png")

    contains:
        arciconBackground("ui/kimberland_icon_no.png")

image arcadeicon-insensitive_Selected:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/arcadeiconcabinet_selected.png")

    contains:
        arciconBackground("ui/kimberland_icon_no.png")

#Medieval Icon
image medievalicon-idle:
    subpixel True
    zoom 0.5
    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/medevial_idle.png")#

image medievalicon-selected:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/medevial_selected.png")

image medievalicon-insensitve_idle:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/medevial_idle.png")

    contains:
        arciconBackground("ui/kimberland_icon_no.png")

image medievalicon-insensitve_selected:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    contains:
        arciconLogo("ui/medevial_selected.png")

    contains:
        arciconBackground("ui/kimberland_icon_no.png")

#Park Icon
image parkicon-idle:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

    #contains:
    #    arciconLogo("ui/medevial_idle.png")#

image parkicon-selected:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

        # contains:
        #    arciconLogo("ui/medevial_selected.png")

image parkicon-insensitve_idle:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

 #    contains:
 #        arciconLogo("ui/medevial_idle.png")

    contains:
        arciconBackground("ui/kimberland_icon_no.png")

image parkicon-insensitve_selected:
    subpixel True
    zoom 0.5

    contains:
        arciconBackground("ui/kimberland_icon_bg.png")

 #    contains:
 #        arciconLogo("ui/medevial_selected.png")

    contains:
        arciconBackground("ui/kimberland_icon_no.png")


###--------------------AUDIO--------------------
define audio.case3 = "music/Anjigami (Case 3).opus"
define audio.fort_severn = "music/Fort-Severn.opus"
define audio.battle1 = "music/day 15.opus"
define audio.battle2 = "music/day 20.opus"
define audio.battle3 = "music/day 24.opus"
define audio.battle4 = "music/day 27.opus"
define audio.onesix = "music/One Six.opus"
define audio.battle_both_live = "music/Cruising-Back-in-Time.opus"
define audio.battle_one_lives = "music/Still-of-Morning_Looping.opus"
define audio.medieval_day_music = "music/day 26.opus"
define audio.kimberland_town_music = "music/Ballooning_Looping.opus"
define audio.calmer_times = "music/Calmer-Times-Ahead_looping.opus"
define audio.desert_wind = "music/04 Desert Wind.opus"
define audio.lbd_seasons_change = "music/Seasons-Change.opus"
define audio.lbd_case1 = "music/Elk Lake (Case 1).opus"
define audio.lbd_train_ambiance = "music/inside-a-train.opus"

###--------------------Sound Effects--------------------
define audio.tainwhistle = "sfx/train-whistle.ogg"
#define audio.typewriter = "sfx/typewriter.ogg"
#define audio.keyboard = "sfx/vintage-keyboard.ogg"
define audio.lbd_coin = "sfx/insert_coin.opus"
define audio.lbd_stock_slap = "sfx/stock_slap.wav"
define audio.lbd_slap = "fx/slap1.wav"
define audio.lbd_pencil_writing = "sfx/pencil-writing.opus"


###--------------------Charactors--------------------
define lime45 = Character("PerfectLime45", color="#CAFF00", image="plime45")
define Db = Character("Debug manager", color="#A8A8A8")
define Dm = Character("Demo Manager", color="#A8A8A8")
define scia = Character("Scientist-A", color="#6A4372", image="scientist-a")
define scim = Character("Scientist-M", color="#4B726E", image="scientist-m")
define Bridgekeeper = Character("Bridgekeeper", color="#fff")

image side plime45 = Image("char/side_lime.webp", xalign=0.01, yalign=1.0, yoffset=-10)

init -20:
    $ lbd_arch_char_cps = 35
    $ lbd_arch_fstnarr_cps = 45

###--------------------Arcade Characters--------------------
define r = Character('Ronan',
                    color="#CD0000",
                    window_background="archspeachbox",
                    who_font="Munro.ttf",
                    who_antialias=False,
                    what_font="Munro.ttf",
                    what_color="#FFFFF0",
                    what_drop_shadow=None,
                    what_antialias=False,
                    what_kerning=2,
                    what_justify=True,
                    what_slow_cps=lbd_arch_char_cps,
                    callback=lbd_ronan_voice,
                    window_left_padding=10,
                    window_left_margin=80,
                    window_right_padding=10,
                    window_right_margin=80,
                    window_top_padding=20,
                    window_top_margin=10,
                    ctc="ctcanimation",
                    ctc_position="fixed")

define w = Character('Draco',
                    color="#B5B5B5",
                    window_background="archspeachbox",
                    who_font="Munro.ttf",
                    who_antialias=False,
                    what_font="Munro.ttf",
                    what_color="#FFFFF0",
                    what_antialias=False,
                    what_drop_shadow=None,
                    what_kerning=2,
                    what_justify=True,
                    what_slow_cps=lbd_arch_char_cps,
                    callback=lbd_wolf_voice,
                    window_left_padding=10,
                    window_left_margin=80,
                    window_right_padding=10,
                    window_right_margin=80,
                    window_top_padding=20,
                    window_top_margin=10,
                    ctc="ctcanimation",
                    ctc_position="fixed")

define narr = Character(
                    window_background="archspeachbox",
                    what_font="Munro.ttf",
                    what_color="#FFFFF0",
                    what_antialias=False,
                    what_drop_shadow=None,
                    what_kerning=2,
                    what_justify=True,
                    what_slow_cps=lbd_arch_fstnarr_cps,
                    callback=lbd_narr_voice,
                    window_left_padding=10,
                    window_left_margin=80,
                    window_right_padding=10,
                    window_right_margin=80,
                    window_top_padding=20,
                    window_top_margin=10,
                    ctc="ctcanimation",
                    ctc_position="fixed")

#slower Narrator
define slwnarr = Character(
                    window_background="archspeachbox",
                    what_font="Munro.ttf",
                    what_color="#FFFFF0",
                    what_antialias=False,
                    what_drop_shadow=None,
                    what_kerning=2,
                    what_justify=True,
                    what_slow_cps=lbd_arch_char_cps,
                    callback=lbd_slwnarr_voice,
                    window_left_padding=10,
                    window_left_margin=80,
                    window_right_padding=10,
                    window_right_margin=80,
                    window_top_padding=20,
                    window_top_margin=10,
                    ctc="ctcanimation",
                    ctc_position="fixed")

define slnarr = Character(
                    window_background="archspeachbox",
                    what_font="Munro.ttf",
                    what_color="#FFFFF0",
                    what_antialias=False,
                    what_drop_shadow=None,
                    what_kerning=2,
                    what_justify=True,
                    what_slow_cps=lbd_arch_char_cps,
                    window_left_padding=10,
                    window_left_margin=80,
                    window_right_padding=10,
                    window_right_margin=80,
                    window_top_padding=20,
                    window_top_margin=10,
                    ctc="ctcanimation",
                    ctc_position="fixed")

define lb = Character('Little Buddy',
                    color="#0074C6",
                    window_background="archspeachbox",
                    who_font="Munro.ttf",
                    who_antialias=False,
                    what_font="Munro.ttf",
                    what_color="#FFFFF0",
                    what_drop_shadow=None,
                    what_antialias=False,
                    what_kerning=2,
                    what_justify=True,
                    what_slow_cps=lbd_arch_char_cps,
                    callback=lbd_buddy_voice,
                    window_left_padding=10,
                    window_left_margin=80,
                    window_right_padding=10,
                    window_right_margin=80,
                    window_top_padding=20,
                    window_top_margin=10,
                    ctc="ctcanimation",
                    ctc_position="fixed")

###--------------------Arcade Misc things--------------------
image archspeachbox:
    "arch/textboxnew.png"
    yoffset -8
    xalign 0.5
    yanchor 0.5
    yalign 0.8

image ctcanimation:
    "textbox2.png"
    yoffset -10
    ypos 0.94
    xpos 0.95

    block:
        easeout_expo 0.2 yoffset 8
        0.1
        easein_expo 0.2 yoffset -8
        repeat

image battle_ending_scene:
    contains:
        "arch/bg/layer4.png"

    contains:
        subpixel True
        "arch/bg/layer3.png"

        yoffset 500
        linear 8.0 yoffset 0

    contains:
        subpixel True
        "arch/bg/layer2.png"

        block:
            xoffset 0
            linear 20.0 xoffset -1920

            repeat

    contains:
        "arch/bg/layer1.png"

    contains:
        "arch/bg/layer0.png"
        alpha 0.5
        0.3
        linear 4.0 alpha 0.0


###--------------------Arcade Character sprites--------------------
image koth_intro:
     Image(im.Recolor(Image(im.Sepia(im.Flip("arch/bonnar123.png", horizontal=True),)), 50, 50, 70, 255))
     alpha 0.0

     linear 4.0 alpha 1.0

     on hide:
        linear 1.0 alpha 0.0

image ronan_intro:
    Image(im.Recolor(Image(im.Sepia("arch/ronan5.png")), 50, 50, 70, 255))
    alpha 0.0

    linear 4.0 alpha 1.0

    on hide:
        linear 1.0 alpha 0.0

image buddy_intro:
    Image(im.Recolor((im.Sepia("arch/aidith1.png")), 50, 50, 70, 255))
    alpha 0.0

    linear 4.0 alpha 1.0

    on hide:
        linear 1.0 alpha 0.0

image kothsprite2:
    im.Flip("arch/bonnar123.png", horizontal=True)      #"arch/kothorix-sprite1.png"
    pause 0.8
    im.Flip("arch/bonnar223.png", horizontal=True)      #"arch/kothorix-sprite2.png"
    pause 0.8
    repeat

#image bonnarsprite2:
#    "arch/bonnar1.png"
#    pause 0.8
#    "arch/bonnar2.png"
#    pause 0.8
#    repeat

image ronansprite3:
    "arch/ronan5.png"
    pause 0.8
    "arch/ronan6.png"
    pause 0.8
    repeat

image aidithsprite2:
    "arch/aidith1.png"
    pause 0.8
    "arch/aidith2.png"
    pause 0.8
    repeat


###--------------------Transitions#--------------------
define dissolvegame = Dissolve(1.0, alpha=True)


###--------------------Tranforms--------------------
transform arciconBackground(child):
    ycenter 0.5
    xcenter 0.5
    yoffset 0
    child

transform arciconLogo(child):
    ycenter 0.5
    xcenter 0.5
    yoffset 0
    child
    time 0.4

    block:
        easeout_expo 1.2 zoom 0.8
        easein_expo 1.2 zoom 1.0
        repeat

transform panoButtons:
    alpha 0.0 zoom 0.5
    easein 0.8 alpha 1.0 zoom 1.0

    on hide:
        easeout 0.6 alpha 0.0 zoom 0.5

transform lorem_nav_trans:
    xpos -220
    ypos -220
    zoom 0.5
    alpha 0.0

    easein 1.2 zoom 1.0 alpha 1.0 ypos 0 xpos 0

    on hide:
        easeout 0.6 zoom 0.5 alpha 0.0 ypos -220 xpos -220

transform home_nav_trans:
    ycenter 1.0
    xcenter 1.0
    xpos 2030
    ypos -110
    zoom 0.5
    alpha 0.0

    easein 1.2 zoom 1.0 alpha 1.0 ypos 110 xpos 1810

    on hide:
        easein 0.6 zoom 0.5 alpha 0.0 ypos -110 xpos 2030

transform lbd_left_arrow_trans:
    ycenter 0.0
    xcenter 1.0
    xpos -110
    ypos 1190
    zoom 0.5
    alpha 0.0

    easein 1.2 zoom 1.0 alpha 1.0 ypos 970 xpos 110

    on hide:
        easeout 0.6 zoom 0.5 alpha 0.0  ypos 1190 xpos -110

transform lbd_right_arrow_trans:
    ycenter 0.0
    xcenter 1.0
    xpos 2030
    ypos 1190
    zoom 0.5
    alpha 0.0

    easein 1.2 zoom 1.0 alpha 1.0 ypos 970 xpos 1810

    on hide:
        easeout 0.6 zoom 0.5 alpha 0.0 ypos 1190 xpos 2030

transform lbd_battle_respawn:
    alpha 1.0
    0.1
    alpha 0.0
    0.1
    alpha 1.0
    0.1
    alpha 0.0
    0.1
    alpha 1.0
    0.15
    alpha 0.0
    0.15
    alpha 1.0
    0.2
    alpha 0.0
    0.2
    alpha 1.0




###--------------------Styles--------------------
init python:
    style.arcicon = Style(style.default)
    style.arcicon.background = None
    style.arcicon.xalign = 0.5
    style.arcicon.yalign = 0.5
    style.arcicon.xcenter = 0.5
    style.arcicon.ycenter = 0.5
    style.arcicon.left_margin = 0
    style.arcicon.right_margin = 0
    style.arcicon.bottom_margin = 0
    style.arcicon.top_margin = 0
    style.arcicon.left_padding = 0
    style.arcicon.right_padding = 0
    style.arcicon.bottom_padding = 0
    style.arcicon.top_padding = 0
