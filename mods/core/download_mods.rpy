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

    from modloader.preload import Preload

    def load_mod_image(url):
        """
        Loads the image data from given url. The resulting data is a str containing the image data
        """
        return urllib2.urlopen(url).read()

    mod_image_preloader = Preload(load_mod_image, 5) # 5 threads is plenty

    def _preload_mod_images(modlist, error):
        if error is not None:
            print "Definitely can't preload this..."
            return
        image_urls = [entry[4] for entry in modlist]
        for url in image_urls:
            mod_image_preloader.load(url)
        return


    class ImageURL(Image):
        """
        This image manipulator loads an image from a url.
        """
        def load(self, unscaled=False):
            from cStringIO import StringIO
            from renpy.display.im import cache

            virtual_f = StringIO(mod_image_preloader.get(self.filename))

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


    # Preload steam modlist, so we don't wait for it when we try to open the mod browser
    if internet_on() and modloader.has_steam():
        modconfig.steam_modlist_preloader.load()


init -1 python:
    import math
    import traceback

    import modloader
    from modloader import modconfig, steamhandler_extensions


    def is_modlist_loaded():
        return modconfig.steam_modlist_preloader.is_loaded()

    def _ensure_modlist_okay(strict=False):
        """Wait until the steam modlist is loaded, then check for errors and report any that have been detected.
        :parameter strict: default (False) only reports severe errors. if set to True, all errors are reported"""
        try:
            modconfig.steam_modlist_preloader.get()
            return
        except steamhandler_extensions.CacheWriteError as exception:
            # CacheWriteError have a special error screen, as they're more severe
            modloader.report_modlist_errors("The steam modlist cache file write has failed.  "
                                        "This should never happen under normal circumstances, and may cause the game to crash or not open.  "
                                        "If you're seeing this, please report it to the developers of the Modtools, or on the fan discord, "
                                        "preferably with a screenshot.\n"
                                        "Page cache location: \"{}\"\n".format(steamhandler_extensions.get_instance().get_page_cache_dir())
                                        + "Error raised:\n"
                                        + "".join(traceback.format_exception(type(exception), exception, exception.cause_traceback))
            )
        except OSError as exception:
            # These may happen if the page cache dir gets messed up
            modloader.report_modlist_errors("The steam modlist cache file usage has failed.  "
                                        "This generally means that the page cache directory has been messed up, which will cause issues with the in-game mod browser.  "
                                        "If you're seeing this, please report it to the developers of the Modtools, or on the fan discord, "
                                        "preferably with a screenshot.\n"
                                        "Page cache location: \"{}\"\n".format(steamhandler_extensions.get_instance().get_page_cache_dir())
                                        + "Error raised:\n"
                                        + "".join(traceback.format_exception(type(exception), exception, exception.traceback))
            )
        except Exception as exception:
            if strict:
                modloader.report_modlist_errors("An error has occurred in trying to load the steam mod list.\n"
                                            "Error raised:\n"
                                            + "".join(traceback.format_exception(type(exception), exception, exception.traceback))
                )
        return

    # Ensure error screens are available, as we may need them
    if not renpy.exports.has_screen("_modlist_errors"):
        renpy.load_module("modloader/patch_errorhandling_screens")

    def _mod_check_internet_downloader(use_steam):
        if internet_on():
            # (modid, name, author, description, image) (for github)
            # (id, name, author, desc, image) (for steam)
            if use_steam:
                from modloader.modconfig import steam_downloadable_mods as download_mods
                _ensure_modlist_okay(strict=True)
            else:
                from modloader.modconfig import github_downloadable_mods as download_mods

            contents = download_mods()
            renpy.show_screen('modmenu_paged', contents=contents, use_steam=use_steam)
        else:
            renpy.show_screen('modmenu_nointernet')


    # Paging methods
    def _get_slice_lims_from_page(page, page_size):
        return page_size * (page - 1), page_size * page # Pages are 1-indexed but lists are 0-indexed, so 1 is subtracted from page# to match them

    def _refresh_modlist_page(page, page_size, modlist, use_steam):
        start, end = _get_slice_lims_from_page(page, page_size)
        renpy.hide_screen('modmenu_paged_modlist')
        renpy.show_screen('modmenu_paged_modlist', contents=modlist[start:end], use_steam=use_steam)
        return



screen modmenu_paged(contents, use_steam):
    modal True

    default current_page = 1
    default PAGE_SIZE = 6
    $ MIN_PAGE = 1 # Do note, modpage numbers are 1-indexed
    $ MAX_PAGE = int(math.ceil(len(contents) / float(PAGE_SIZE)))

    frame id "modmenu_paged" at alpha_dissolve:
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
                    Hide("modmenu_mod_content", transition=dissolve),
                    Hide("modmenu_paged_modlist", transition=dissolve),
                    Hide("modmenu_paged", transition=dissolve),
                    Stop("modmenu_music", fadeout=1.0),
                    Play("music", "mx/menu.ogg", fadein=1.0),
                    Play("audio", "se/sounds/close.ogg")]

            xpos 0.94
            ypos 0.02


        hbox id "page_number_hb":
            yminimum 425
            ymaximum 425
            xmaximum 900
            xminimum 900

            ypos 913
            xcenter 960
            yanchor 0.5


            textbutton "-5":
                xalign 0.2
                ycenter 0.5
                # Tried to bind this to shift+scroll, but it didn't work...
                action [SetScreenVariable("current_page", max(current_page-5, MIN_PAGE)),
                        Function(_refresh_modlist_page, max(current_page-5, MIN_PAGE), PAGE_SIZE, contents, use_steam=use_steam)
                       ]
                sensitive (current_page > 1)

            textbutton "-":
                xalign 0.4
                ycenter 0.5
                keysym "mousedown_4"
                action [SetScreenVariable("current_page", current_page-1),
                        Function(_refresh_modlist_page, current_page-1, PAGE_SIZE, contents, use_steam=use_steam)
                       ]
                sensitive (current_page > 1)

            label "Page #[current_page]/[MAX_PAGE]":
                xalign 0.5
                ycenter 0.5

                text_size 40

            textbutton "+":
                xalign 0.6
                ycenter 0.5
                keysym "mousedown_5"
                action [SetScreenVariable("current_page", current_page+1),
                        Function(_refresh_modlist_page, current_page+1, PAGE_SIZE, contents, use_steam=use_steam)
                        ]
                sensitive (current_page < MAX_PAGE)

            textbutton "+5":
                xalign 0.8
                ycenter 0.5
                # Also tried to bind this to shift+scroll, but it didn't work...
                action [SetScreenVariable("current_page", min(current_page+5, MAX_PAGE)),
                        Function(_refresh_modlist_page, min(current_page+5, MAX_PAGE), PAGE_SIZE, contents, use_steam=use_steam)
                        ]
                sensitive (current_page < MAX_PAGE)

    on "show" action [Function(_refresh_modlist_page, current_page, PAGE_SIZE, contents, use_steam=use_steam),
                      Function(_preload_mod_images, contents, None)]

    on "hide" action [Function(mod_image_preloader.clear)]



screen modmenu_paged_modlist(contents, use_steam):
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

            for modid, name, author, description, url in contents:
                $ modname = modmenu_name_cleaner(name)

                if len(modname) > 21:
                    #if modname is greater than 21 characters, decrease size of font by 5
                    if len(modname) <= 25:
                        $ modname = "{size=-5}" + modname + "{/size}"

                    #if modname is greater than 25 characters, decrease size of font by 10
                    else:
                        #if modname is greater than 30 characters, decrease size of font by 10 and cut all text after 30 places
#                         if len(modname) > 30:
                        $ modname = modname[:30]
                        $ modname = "{size=-10}" + modname + "{/size}"

                if str(modid) in modinfo.get_mod_folders():
                    $ modname = modname + "\n{size=-5}(Installed){/size}"


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
                                 ),
                            Play("audio", "se/sounds/open.ogg")]






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
                        Hide("modmenu_nointernet", transition=dissolve),
                        Stop("modmenu_music", fadeout=1.0),
                        Play("music", "mx/menu.ogg", fadein=1.0),
                        Play("audio", "se/sounds/close.ogg")]
                style "yesnobutton"

        label "No internet connection detected. Please connect to the internet and try again.\nIf you are connected, a proxy or firewall could be blocking requests or the update server is down":
            style "yesno_prompt"
