init python:
    renpy.music.register_channel("modmenu_music", "music", True)

    def modmenu_name_cleaner(name):
        try:
            name = unicode(name, "utf8")
        except TypeError:
            pass
        name = name.replace("-", " ")
        name = name.replace("_", " ")
        return u''.join(val.upper() if i == 0 or name[i-1] == u' ' else val for i, val in enumerate(name))


    style.modmenu_select_btn = Style(style.default)
    style.modmenu_select_btn.background = "#0000009B"
    style.modmenu_select_btn.hover_background = "#ffffff9B"

    #new way
    #style.modmenu_select_btn.xminimum = 190
    #style.modmenu_select_btn.yminimum = 50

    #old way
    style.modmenu_select_btn.xminimum = 425
    style.modmenu_select_btn.yminimum = 125
    style.modmenu_select_btn.xalign = 0.5
    style.modmenu_select_btn.yalign = 0.5
    #style.modmenu_select_btn.ypadding = 5
    style.modmenu_select_btn_text.xalign = 0.5
    style.modmenu_select_btn_text.yalign = 0.5
    style.modmenu_select_btn_text.size = 34
    style.modmenu_select_btn_text.color = "#FFFFF0"
    style.modmenu_select_btn_text.selected_color = "#FFFFF0"
    style.modmenu_select_btn_text.antialias = True
    style.modmenu_select_btn_text.font  = "TitilliumWeb-Bold.ttf"
    style.modmenu_select_btn_text.drop_shadow = None
    style.modmenu_select_btn_text.justify = True
    style.modmenu_select_btn_text.text_align = 0.5

    style.modmenu_content_btn = Style(style.default)
    style.modmenu_content_btn.background = "#0000009B"
    style.modmenu_content_btn.hover_background = "#ffffff9B"
    style.modmenu_content_btn.xminimum = 240
    style.modmenu_content_btn.yminimum = 50
    style.modmenu_content_btn.xalign = 0.5
    style.modmenu_content_btn.yalign = 0.5
    style.modmenu_content_btn.ypadding = 5

    ###-----Scrollbar------
    style.modmenu_select_slider = Style(style.default)
    style.modmenu_select_slider.top_bar = "ui/modselect_bar_full.png"
    style.modmenu_select_slider.bottom_bar = "ui/modselect_bar_empty.png"
    style.modmenu_select_slider.thumb = "image/ui/settings/thumb.png"
    style.modmenu_select_slider.thumb_offset = 20
    style.modmenu_select_slider.thumb_shadow = None
    style.modmenu_select_slider.bar_vertical = True
    style.modmenu_select_slider.bar_invert = True
    style.modmenu_select_slider.xmaximum = 64
    style.modmenu_select_slider.ymaximum = 750
    style.modmenu_select_slider.yalign = 0.5
    style.modmenu_select_slider.xpos = 0.005
    style.modmenu_select_slider.left_gutter = 20
    style.modmenu_select_slider.right_gutter = 20

    style.modmenu_content_slider = Style(style.default)
    style.modmenu_content_slider.bottom_bar = "ui/modcontent_bar_empty.png"
    style.modmenu_content_slider.top_bar = "ui/modcontent_bar_full.png"
    style.modmenu_content_slider.thumb = "image/ui/settings/thumb.png"
    style.modmenu_content_slider.bar_vertical = True
    style.modmenu_content_slider.bar_invert = True
    style.modmenu_content_slider.thumb_offset = 20
    style.modmenu_content_slider.thumb_shadow = None
    style.modmenu_content_slider.ymaximum = 331
    style.modmenu_content_slider.xmaximum = 34
    #style.modmenu_select_slider.xalign = 0.5
    style.modmenu_content_slider.top_gutter = 20
    style.modmenu_content_slider.bottom_gutter = 20


    from renpy.display.im import Image
    from renpy.ui import Wrapper
    import re
    import urllib2

    class ImageURL(Image):
        """
        This image manipulator loads an image from a url.
        """
        def load(self, unscaled=False):
            import pygame
            from cStringIO import StringIO
            from urllib2 import urlopen
            from renpy.display.im import cache

            url_f = urlopen(self.filename)
            virtual_f = StringIO(url_f.read())

            cache.add_load_log(self.filename)
            if unscaled:
                surf = renpy.display.pgrender.load_image_unscaled(virtual_f, self.filename)
            else:
                surf = renpy.display.pgrender.load_image(virtual_f, self.filename)
            return self.modify_surf(surf)

        def predict_files(self):
                return [self.url]

        def modify_surf(self, surf):
            return surf


    class ScaledImageURL(ImageURL):
        def modify_surf(self, surf):
            return renpy.display.pgrender.transform_scale(surf, (190, 190))

    class ModmenuContentImageURL(ImageURL):
        def modify_surf(self, surf):
            return renpy.display.pgrender.transform_scale(surf, (220, 220))


    ImageURL = Wrapper(ImageURL)
    ScaledImageURL = Wrapper(ScaledImageURL)
    ModmenuContentImageURL = Wrapper(ModmenuContentImageURL)

    style.download_mods = Style(style.default)

    def internet_on():
        try:
            urllib2.urlopen('http://github.com', timeout=5)
        except urllib2.URLError:
            return False
        return True


screen check_internet_downloader(use_steam):
    modal True

    if internet_on():
        python:
            # (modid, name, author, description, image) (for github)
            # (id, name, author, desc, image) (for steam)
            if use_steam:
                from modloader.modconfig import steam_downloadable_mods as download_mods
            else:
                from modloader.modconfig import github_downloadable_mods as download_mods

            contents = download_mods()
        use modmenu_download(contents=contents, use_steam=use_steam)
    else:
        use modmenu_nointernet()

screen modmenu_download(contents, use_steam):
    modal True

    frame id "modmenu_download" at alpha_dissolve:
        add "image/ui/ingame_menu_bg3.png"

        add "image/ui/ingame_menu_bg_light.png" at ingame_menu_light

        #Title
        text "MOD MENU":
            size 65
            xpos 0.5
            ypos 0.05
            xcenter 0.5
            yanchor 0.5
            font "Ardnas.otf"

        #Close Button
        imagebutton:
            idle "image/ui/close_idle.png"
            hover "image/ui/close_hover.png"
            action [Show("modmenu", transition=dissolve),
                    Hide("check_internet_downloader", transition=dissolve),
                    Hide("modmenu_mod_content", transition=dissolve),
                    Hide("modmenu_download", transition=dissolve),
                    Stop("modmenu_music", fadeout=1.0),
                    Play("music", "mx/menu.ogg", fadein=1.0),
                    Play("audio", "se/sounds/close.ogg")]

            xpos 0.94
            ypos 0.02

        frame:
            background None
            yminimum 900
            ymaximum 900
            xmaximum 425
            xminimum 425
            xpos 65
            ypos 90

            #button hieght 125
            vpgrid id "modselect_vp":

                yminimum 900
                ymaximum 900
                xmaximum 425
                xminimum 425

                cols 1
                spacing 30
                draggable True
                mousewheel True

                for modid, name, author, description, url in contents:
                    $ modname = modmenu_name_cleaner(name)

                    if len(modname) <= 21:
                        #if mod is installed
                        if str(modid) in modinfo.get_mod_folders():
                            $ modname = modname + "\n{size=-5}(Installed){/size}"
                        #if mod is not installed
                        else:
                            $ modname = modname

                    #if modname is greater than 21 characters, decrese size of font by 5
                    elif len(modname) <= 25:
                        #if mod is installed
                        if str(modid) in modinfo.get_mod_folders():
                            $ modname = "{size=-5}" + modname + "{/size}" + "\n{size=-5}(Installed){/size}"
                        #if mod is not installed
                        else:
                            $ modname = "{size=-5}" + modname + "{/size}"

                    #if modname is greater than 25 characters, decrese size of font by 10
                    else:
                        #if modname is greater than 30 characters, decrese size of font by 10 and cut all text after 30 places
                        if len(modname) > 30:
                            $ modname = modname[:30]

                        #if mod is installed
                        if str(modid) in modinfo.get_mod_folders():
                            $ modname = "{size=-10}" + modname + "{/size}" + "\n{size=-5}(Installed){/size}"
                        #if mod is not installed
                        else:
                            $ modname = "{size=-10}" + modname + "{/size}"


                    textbutton "[modname]":
                        style "modmenu_select_btn"

                        action [Hide("modmenu_mod_content"),
                                Show("modmenu_mod_content",
                                     modid=modid,
                                     name=unicode(name, "utf8"),
                                     author=unicode(author, "utf8"),
                                     description=unicode(description, "utf8"),
                                     url=url,
                                     use_steam=use_steam,
                                     transition=dissolve),
                                Play("audio", "se/sounds/open.ogg")]


        bar value YScrollValue("modselect_vp"):
            style "modmenu_select_slider"
            #yalign 0.95




screen modmenu_mod_content(modid, name, author, description, url, use_steam):
    frame:
        add "ui/modcontent_frame.png":
            xoffset -10 yoffset 10 xpos 0.275 ypos 0.21

        #Handling long authornames
        if len(author) < 30:
            pass

        elif len(author) < 34:
            $ author = "{size=-5}" + author + "{/size}"

        elif len(author) < 41:
            $ author = "{size=-10}" + author + "{/size}"

        else:
            $ author = "{size=-10}" + author[:40] + "{/size}"



        $ subtitle = ((name.replace("-", " ")).replace("_", " ")).upper()

        #handling long modnames
        if len(subtitle) < 41:
            pass

        elif len(subtitle) < 51:
            $ subtitle = "{size=-8}" + subtitle + "{/size}"

        else:
            $ subtitle = "{size=-8}" + subtitle[:50] + "{/size}"

        #Title
        text "[subtitle]":
            size 45
            xpos 0.5
            ypos 0.155
            xcenter 0.5
            yanchor 0.5
            font "Ardnas.otf"

        #Mods image
        vbox xpos 0.72 ypos 0.21:
            python:
                ModmenuContentImageURL(url)


        vbox xpos 0.275 ypos 0.21:
            null height 30

            text "Author: [author]" size 42

            null height 38

            hbox:
                text "Description:" size 42 ycenter 0.5

                null width 350

                if str(modid) in modinfo.get_mod_folders():
                    textbutton "Uninstall":
                        ycenter 0.5
                        action [Show("modmenu_remove_confirm_2", modname=name, filename=str(modid)),
                                Play("audio", "se/sounds/open.ogg")]
                        style "modmenu_content_btn"
                        text_style "modmenu_select_btn_text"
                        text_size 40

                else:
                    textbutton "Install":
                        ycenter 0.5
                        action [Show("modmenu_install_confirm", modid=modid, modname=name, use_steam=use_steam),
                                Play("audio", "se/sounds/open.ogg")]
                        style "modmenu_content_btn"
                        text_style "modmenu_select_btn_text"
                        text_size 40


            null height 32

            viewport id "modcontent_vp":
                #scrollbars "vertical"
                draggable True
                mousewheel True
                xminimum 1100
                xmaximum 1100
                yminimum 355
                ymaximum 355

                python:
                    description = re.sub(r'\[[^]]*\]', '', description)
                    description = re.sub(r'\{[^}]*\}', '', description)
                    description = [i for i in description if i not in "[]{}"]
                text description

        bar value YScrollValue("modcontent_vp"):
            style "modmenu_content_slider"
            ypos 472
            xpos 1682
            #yalign 0.95


screen modmenu_install_confirm(modid, modname, use_steam) tag smallscreen2:
    modal True
    python:
        if use_steam:
            from modloader.modconfig import download_steam_mod as download_mod
        else:
            from modloader.modconfig import download_github_mod as download_mod

    add "image/ui/nvlscreen.png" at zoom_fade_in:
        xcenter 0.5 ycenter 0.5 size (1921, 1081) xoffset -1 yoffset -1

    window id "modmenu_install_confirm" at popup2:
        style "alertwindow"

        hbox xalign 0.5 yalign 0.8:
            spacing 250

            textbutton "Yes":
                action [Hide("modmenu_install_confirm"),
                        Play("audio", "se/sounds/close.ogg"),
                        lambda download_mod=download_mod, modname=modname, modid=modid: download_mod(modid, modname)]

                style "yesnobutton"

            textbutton "No":
                action [Hide("modmenu_install_confirm", transition=dissolve),
                        Play("audio", "se/sounds/close.ogg")]

                style "yesnobutton"

        label "Are you sure you want to install [modname]?":
            style "yesno_prompt"
            text_style "yesno_prompt_text"


screen modmenu_remove_confirm_2(modname, filename) tag smallscreen2:
    modal True
    python:
        from modloader.modconfig import remove_mod

    add "image/ui/nvlscreen.png" at zoom_fade_in:
        xcenter 0.5 ycenter 0.5 size (1921, 1081) xoffset -1 yoffset -1

    window id "modmenu_remove_confirm" at popup2:
        style "alertwindow"

        if modname == "Core":
            textbutton "Continue":
                action [Hide("modmenu_remove_confirm_2", transition=dissolve),
                        Play("audio", "se/sounds/close.ogg")]
                        hovered Play("audio", "se/sounds/select.ogg")
                style "yesnobutton"
                xalign 0.5
                yalign 0.8

            label "You cannot remove the Core mod.":
                style "yesno_prompt"

        else:
            hbox xalign 0.5 yalign 0.8:
                spacing 250
                textbutton "Yes":
                    action [Hide("modmenu_remove_confirm_2"),
                            Play("audio", "se/sounds/close.ogg"),
                            lambda remove_mod=remove_mod, modname=modname, filename=filename: remove_mod(modname, filename),
                            Show("modmenu_remove")]
                    style "yesnobutton"

                textbutton "No":
                    action [Hide("modmenu_remove_confirm_2"),
                            Play("audio", "se/sounds/close.ogg")]
                    style "yesnobutton"

            label "Are you sure you want to remove [modname]?":
                style "yesno_prompt"


screen modmenu_nointernet() tag smallscreen2:
    modal True
    python:
        #from modloader.modconfig import download_github_mod
        pass

    add "image/ui/nvlscreen.png" at zoom_fade_in:
        xcenter 0.5 ycenter 0.5 size (1921, 1081) xoffset -1 yoffset -1

    window id "modmenu_install_confirm" at popup2:
        style "alertwindow"

        hbox xalign 0.5 yalign 0.8:
            textbutton "OK.":
                action [Show("modmenu", transition=dissolve),
                        Hide("check_internet_downloader", transition=dissolve),
                        Play("audio", "se/sounds/close.ogg")]
                style "yesnobutton"

        label "No internet connection detected. Please connect to the internet and try again.\nIf you are connected, a proxy or firewall could be blocking requests or the update server is down":
            style "yesno_prompt"
