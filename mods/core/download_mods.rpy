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


    import modmenu_search
    import time

    def set_query(value):
        curr_screen_scope = renpy.current_screen().scope
        curr_screen_scope["query"] = value
        search_modlist(value, curr_screen_scope["author_query"])
        return

    def set_author_query(value):
        curr_screen_scope = renpy.current_screen().scope
        curr_screen_scope["author_query"] = value
        search_modlist(curr_screen_scope["query"], value)
        return


    def search_modlist(query, author_query=""):
        print "searching with {}, {}".format(query, author_query)

        # As renpy input doesn't allow for additional variables to this method, I've had to resort to this cursed thing
        curr_screen_scope = renpy.current_screen().scope
        modlist = curr_screen_scope["contents"]
        page = curr_screen_scope["current_page"]
        page_size = curr_screen_scope["PAGE_SIZE"]
        use_steam = curr_screen_scope["use_steam"]

        s_time = time.time()
        if query.strip() or author_query.strip(): # There's no reason to reorder the modlist if no search has been done.
            reordered_modlist = modmenu_search.sort_best(query, modlist, author_query=author_query)
        else:
            reordered_modlist = curr_screen_scope["contents"]
        print "Search took: {:.5}".format(time.time() - s_time) # Hopefully this never goes above 0.3

        curr_screen_scope["search_order_contents"] = reordered_modlist
        _refresh_modlist_page(page, page_size, reordered_modlist, use_steam)
        renpy.restart_interaction()

        return


init -1 python:
    import sys
    import math
    import traceback
    import threading

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

    class EntranceStates:
        INTERNET = "internet"
        INTERNET_FAILED = "internet_failed"
        MODLIST = "modlist"
        MODLIST_FAILED = "modlist_failed"
        DONE = "done"

    class ModmenuEntranceLoadManager:
        """Keeps the DynamicDisplayable at the heart of the modmenu_entrance aligned with the actual modlist loading."""

        def __init__(self, use_steam):
            self.use_steam = use_steam

            self._state = EntranceStates.INTERNET
            self._state_lock = threading.Lock()

            self._result = None
            self._exception = None
            self._done_signal = threading.Event() # Used to gat access to these two. a lock is not necessary as they are only accessible after being set for the last time.

            self.disabled = threading.Event() # I've had issues with calls coming after a transition was supposed to take effect, so this allows me to disable the screen under those cases.

            self._running_thread = threading.Thread(target=self._load_modlist, args=(self.use_steam,))
            self._running_thread.daemonic = True
            self._running_thread.start()

        def set_state(self, state):
            with self._state_lock:
                self._state = state
            return

        def get_state(self):
            with self._state_lock:
                return self._state


        def get_modlist(self):
            self._done_signal.wait()
            if self._exception is not None:
                raise self._exception
            return self._result


        def _load_modlist(self, use_steam):
            if internet_on():
                self.set_state(EntranceStates.MODLIST)
                try:
                    # (modid, name, author, description, image) (for github)
                    # (id, name, author, desc, image) (for steam)
                    if use_steam:
                        from modloader.modconfig import steam_downloadable_mods as download_mods
                    else:
                        from modloader.modconfig import github_downloadable_mods as download_mods

                    self._result = download_mods()
                    self.set_state(EntranceStates.DONE)
                except Exception as e:
                    self._exception = e
                    self._exception.traceback = sys.exc_info()[2]
                    self.set_state(EntranceStates.MODLIST_FAILED)
            else:
                print "Internet failed"
                self.set_state(EntranceStates.INTERNET_FAILED)

            self._done_signal.set()
            return

    _dots = 1
    _MAX_DOTS = 3

    def _cycle_dots():
        global _dots, _MAX_DOTS
        _dots = (_dots % _MAX_DOTS) + 1
        return _dots


    def _modmenu_entrance_transition_to(screen, load_manager, **kwargs):
        """As transitioning out of the modmenu entrance without issues requires setting a few things, this helps ensure it is done correctly"""
        renpy.show_screen(screen, **kwargs)
        renpy.hide_screen('modmenu_entrance')
        load_manager.disabled.set()
        renpy.restart_interaction()
        return

    _modmenu_entrance_cancelled = False

    def _modmenu_entrance_progress(st, at, load_manager, use_steam):
        state = load_manager.get_state()
        if load_manager.disabled.is_set(): # Multi-calls made the transitions occur multiple times, causing screens which don't close properly. this prevents that.
            if state == EntranceStates.DONE and not _modmenu_entrance_cancelled:
                return Text("Modlist load done, showing modmenu..."), None
            return Text(""), None

        print "{:.4}".format(st), state

        if state == EntranceStates.INTERNET:
            t = Text("Connecting to network{}".format("." * _cycle_dots()))
            return t, 1.5
        elif state == EntranceStates.INTERNET_FAILED:
            _modmenu_entrance_transition_to('modmenu_nointernet', load_manager)
            return Text("Network connection failed!"), None
        elif state == EntranceStates.MODLIST:
            t = Text("Loading modlist{}".format("." * _cycle_dots()))
            return t, 1.0
        elif state == EntranceStates.MODLIST_FAILED:
            if use_steam:
                _ensure_modlist_okay(strict=True) # This will fail
            else:
                try:
                    load_manager.get_modlist() # This will fail
                except Exception as exception:
                    modloader.report_modlist_errors("An error has occurred in trying to load the steam mod list.\n"
                                        "Error raised:\n"
                                        + "".join(traceback.format_exception(type(exception), exception, exception.traceback))
            )
            return Text("Modlist load failed!"), None
        else: # state == EntranceStates.DONE
            contents = load_manager.get_modlist()
            _modmenu_entrance_transition_to('modmenu_paged', load_manager, contents=contents, use_steam=use_steam)
            return Text("Modlist load done, showing modmenu..."), None


    def _enter_modmenu(use_steam):
        renpy.show_screen('modmenu_entrance', use_steam=use_steam)
        return



    # Paging methods
    def _get_slice_lims_from_page(page, page_size):
        return page_size * (page - 1), page_size * page # Pages are 1-indexed but lists are 0-indexed, so 1 is subtracted from page# to match them

    def _refresh_modlist_page(page, page_size, modlist, use_steam):
        start, end = _get_slice_lims_from_page(page, page_size)
        renpy.hide_screen('modmenu_paged_modlist')
        renpy.show_screen('modmenu_paged_modlist', contents=modlist[start:end], use_steam=use_steam)
        return


    _modmenu_mods_to_add = {}
    _modmenu_mods_to_remove = set()

    def _modmenu_add_mod(mod_id, mod_name):
        print "adding mod:", mod_id, mod_name
        if mod_id in _modmenu_mods_to_remove:
            _modmenu_mods_to_remove.discard(mod_id)
        else:
            _modmenu_mods_to_add[mod_id] = mod_name
        return

    def _modmenu_remove_mod(mod_id):
        print "removing mod:", mod_id
        if mod_id in _modmenu_mods_to_add:
            _modmenu_mods_to_add.pop(mod_id)
        else:
            _modmenu_mods_to_remove.add(mod_id)
        return

    def _modmenu_get_added_mods():
        return _modmenu_mods_to_add

    def _modmenu_get_removed_mods():
        return _modmenu_mods_to_remove

    def _modmenu_is_mod_added(mod_id):
        return mod_id in _modmenu_mods_to_add

    def _modmenu_is_mod_removed(mod_id):
        return mod_id in _modmenu_mods_to_remove



screen modmenu_entrance(use_steam):
    modal True

    default load_manager = ModmenuEntranceLoadManager(use_steam)

    frame id "modmenu_entrance" at alpha_dissolve:
        add "image/ui/ingame_menu_bg3.png"

        add "image/ui/ingame_menu_bg_light.png" at ingame_menu_light

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
                    Hide("modmenu_entrance", transition=dissolve),
                    Stop("modmenu_music", fadeout=1.0),
                    Play("music", "mx/menu.ogg", fadein=1.0),
                    Play("audio", "se/sounds/close.ogg"),
                    Function(load_manager.disabled.set),
                    SetVariable("_modmenu_entrance_cancelled", True)]

            xpos 0.94
            ypos 0.02

        add DynamicDisplayable(_modmenu_entrance_progress, load_manager, use_steam):
            xalign 0.5
            yalign 0.5

    on "show" action SetVariable("_modmenu_entrance_cancelled", False)



screen modmenu_paged(contents, use_steam):
    modal True

    default current_page = 1
    default PAGE_SIZE = 6
    $ MIN_PAGE = 1 # Do note, modpage numbers are 1-indexed
    $ MAX_PAGE = int(math.ceil(len(contents) / float(PAGE_SIZE)))

    default search_order_contents = contents
    default query = ""
    default author_query = ""

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
                    Hide("modmenu_entrance", transition=dissolve),
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
                        Function(_refresh_modlist_page, max(current_page-5, MIN_PAGE), PAGE_SIZE, search_order_contents, use_steam=use_steam)
                       ]
                sensitive (current_page > 1)

            textbutton "-":
                xalign 0.4
                ycenter 0.5
                keysym "mousedown_4"
                action [SetScreenVariable("current_page", current_page-1),
                        Function(_refresh_modlist_page, current_page-1, PAGE_SIZE, search_order_contents, use_steam=use_steam)
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
                        Function(_refresh_modlist_page, current_page+1, PAGE_SIZE, search_order_contents, use_steam=use_steam)
                        ]
                sensitive (current_page < MAX_PAGE)

            textbutton "+5":
                xalign 0.8
                ycenter 0.5
                # Also tried to bind this to shift+scroll, but it didn't work...
                action [SetScreenVariable("current_page", min(current_page+5, MAX_PAGE)),
                        Function(_refresh_modlist_page, min(current_page+5, MAX_PAGE), PAGE_SIZE, search_order_contents, use_steam=use_steam)
                        ]
                sensitive (current_page < MAX_PAGE)

        textbutton "Download status Placeholder":
            background "#0000009B"
            hover_background "#ffffff9B"
            xpos 1855
            ypos 990
            xanchor 1.0
            yanchor 1.0

            xsize 425
            ysize 125
#             xalign 0.0
#             yalign 0.0
            action [Function(print, "added:", _modmenu_get_added_mods(), "\nremoved:", _modmenu_get_removed_mods())]

    hbox:
        xpos 65
        ypos 10
        xanchor 0.0
        yanchor 0.0
        xsize 425
        ysize 70

        spacing 10

        vbox:
            xalign 0.0
            ycenter 0.5
            xsize 75
            spacing 6

            # For some reason 'label' and 'text' text components insisted on being ever so slightly larger than necessary, which made everything look misaligned
            textbutton "Author:":
                background "#00000000"
                text_size 24
                ysize 32
                xalign 0.0

            textbutton "Mod:":
                background "#00000000"
                text_size 24
                ysize 32
                xalign 0.0

        vbox:
            xalign 0.0
            ycenter 0.5
            spacing 6

            default focus_query_input = False
            default focus_author_query_input = False

            # input components aggressively capture focus, to the point where you can't use more than one of them in a single screen.
            #  a button is used to circumvent this, as it is a container that can itself hold focus, so it is able to intercept the aggressive behaviour.
            button:
                background If(focus_author_query_input, "#FFFFFFCD", "#000000CD")
                hover_background If(focus_author_query_input, "#BFBFFFCD", "#000040CD")
                activate_sound None
                key_events focus_author_query_input
                action [ToggleScreenVariable("focus_author_query_input"), SetScreenVariable("focus_query_input", False)]
                xfill True
                ysize 32
                xpadding 0

                input:
                    color If(focus_author_query_input, "#000", "#FF7F00")
                    xalign 0.0
                    ycenter 0.5
                    size 24
                    pixel_width 320 # While the horizontal space is supposed to be 340, The inputs have a tendency to drop down a row...
                    changed set_author_query


            button:
                background If(focus_query_input, "#FFFFFFCD", "#000000CD")
                hover_background If(focus_query_input, "#BFBFFFCD", "#000040CD")
                activate_sound None
                key_events focus_query_input
                action [ToggleScreenVariable("focus_query_input"), SetScreenVariable("focus_author_query_input", False)]
                xfill True
                ysize 32
                xpadding 0

                input:
                    color If(focus_query_input, "#000", "#FFFF00")
                    xalign 0.0
                    ycenter 0.5
                    size 24
                    pixel_width 320
                    changed set_query
        key "K_ESCAPE" action [SetScreenVariable("focus_query_input", False), SetScreenVariable("focus_author_query_input", False)]
        key "K_TAB" action [ToggleScreenVariable("focus_author_query_input"),
                            If(focus_author_query_input,
                               ToggleScreenVariable("focus_query_input"),
                               SetScreenVariable("focus_query_input", False))]


    on "show" action [Function(_refresh_modlist_page, current_page, PAGE_SIZE, contents, use_steam=use_steam),
                      Function(_preload_mod_images, contents, None),
                      Function(im.cache.clear) # I tended to get 'out of memory' errors on this menu, so we use this precaution
                      ]

    on "hide" action [Function(mod_image_preloader.clear), # Cleanup after ourselves
                      Function(im.cache.clear),
                      Function(modmenu_search.clear_cache),
                     ]



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

                if (str(modid) in modinfo.get_mod_folders() or _modmenu_is_mod_added(modid)) and not _modmenu_is_mod_removed(modid):
                    textbutton "Uninstall":
                        ycenter 0.5
                        action [Function(_modmenu_remove_mod, modid),
#                         Show("modmenu_remove_confirm_2", modname=name, filename=str(modid)),
                                Play("audio", "se/sounds/open.ogg")]
                        style "modmenu_content_btn"
                        text_style "modmenu_select_btn_text"
                        text_size 40

                else:
                    textbutton "Install":
                        ycenter 0.5
                        action [Function(_modmenu_add_mod, modid, name),
#                         Show("modmenu_install_confirm", modid=modid, modname=name, use_steam=use_steam),
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
