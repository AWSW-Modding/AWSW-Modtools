# modmenu entrance stuff
init -1 python:
    class EntranceStates:
        INTERNET = "internet"
        INTERNET_FAILED = "internet_failed"
        MODLIST = "modlist"
        MODLIST_FAILED = "modlist_failed"
        DONE = "done"

    class ModmenuEntranceLoadManager:
        """ Keeps the DynamicDisplayable at the heart of the modmenu_entrance aligned with the actual modlist loading.
        This uses the ScreenValueContainer paradigm with the set and clear methods. as such, the __init__ is empty.
        """

        def __init__(self):
            self.use_steam = False

            self._state = EntranceStates.INTERNET
            self._state_lock = threading.Lock()

            self._result = None
            self._exception = None
            self._done_signal = threading.Event() # Used to gate access to these two. a lock is not necessary as they are only accessible after being set for the last time.

            self.disabled = threading.Event() # I've had issues with calls coming after a transition was supposed to take effect, so this allows me to disable the screen under those cases.

            self._running_thread = None

        def set(self, use_steam):
            self.use_steam = use_steam

            self._state = EntranceStates.INTERNET

            self._result = None
            self._exception = None
            self._done_signal.clear()

            self.disabled.clear()

            self._running_thread = threading.Thread(target=self._load_modlist, args=(self.use_steam,))
            self._running_thread.daemonic = True
            self._running_thread.start()

        def clear(self):
            self.use_steam = False

            self._state = EntranceStates.INTERNET

            self._result = None
            self._exception = None
            self._done_signal.clear()

            self.disabled.clear()
            self._running_thread = None


        def set_state(self, state):
            with self._state_lock:
                self._state = state

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

screen modmenu_entrance(use_steam):
    modal True

    add ScreenValueContainerClearer()

    default load_manager = ModmenuEntranceLoadManagerContainer.get("load_manager", use_steam)

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

    # modmenu search stuff
    import modmenu_search
    import time

    class ModscreenModlistManager:
        def __init__(self):
            """ Manages the modscreen's displayed modlist, including paging, searching and filtering.
            This uses the ScreenValueContainer paradigm with the set and clear methods. as such, the __init__ is empty.
            """
            self._base_modlist = []
            self._reordered_modlist = []
            self._filtered_modlist = []

            self._current_page = 1
            self._page_size = 1

            self._query = ""
            self._author_query = ""

            self._filter_funcs = {}
            self._filter_activity = {}

            self.use_steam = False

        def set(self, modlist, page_size=6, filter_map=None, use_steam=True):
            """
            :param modlist: The base modlist to manage
            :param page_size: The page size of each mod page
            :param filter_map: mapping from name (str) to (filter_func, add_args): the initial filter types which are available. if None (default), the initial filter map is empty
            """
            if page_size <= 0:
                raise ValueError("page_size={} must be positive!".format(page_size))

            if filter_map is None:
                filter_map = {}

            self._base_modlist = modlist
            self._reordered_modlist = modlist
            self._filtered_modlist = modlist

            self._current_page = 1
            self._page_size = page_size

            self._query = ""
            self._author_query = ""

            self._filter_funcs = dict(filter_map) # This can be changed within this class (and we don't want to copy it each time), so we must copy it here to avoid unwanted side effects
            self._filter_activity = {name: None for name in filter_map.iterkeys()}

            self.use_steam = use_steam

        def clear(self):
            # The lists may be external, so they should not be cleared in place. the dicts can't be, so they are.
            self._base_modlist = []
            self._reordered_modlist = []
            self._filtered_modlist = []

            self._filter_funcs.clear()
            self._filter_activity.clear()

        def get_current_page(self):
            return self._current_page

        def get_page_size(self):
            return self._page_size

        def get_max_page(self):
            return int(math.ceil(len(self.get_current_modlist()) / float(self.get_page_size()))) # float is used to force accurate division so the ciel actually does its job

        def get_query(self):
            return self._query

        def get_author_query(self):
            return self._author_query

        def is_filter_active(self, name):
            """Return filter name's activity. see set_filter_active for how filter activity is defined"""
            return self._filter_activity[name]

        def get_filter_func(self, name):
            return self._filter_funcs[name]


        def get_base_modlist(self):
            """Get the base modlist, upon which all paging, searching and filtering is done"""
            return self._base_modlist

        def get_current_modlist(self):
            """Get the searched and filtered modlist"""
            return self._filtered_modlist

        def get_current_modlist_page(self):
            page_size = self.get_page_size()
            page = self.get_current_page()
            return self.get_current_modlist()[page_size*(page - 1) : page_size*page] # Pages are 1-indexed but lists are 0-indexed, so 1 is subtracted from page# to match them


        def set_current_page(self, page_num):
            self._current_page = min(max(page_num, 1), self.get_max_page()) # clamp

        def move_current_page(self, amount):
            self.set_current_page(self.get_current_page() + amount)

        def set_page_size(self, page_size):
            if page_size <= 0:
                raise ValueError("page_size={} must be positive!".format(page_size))
            self._page_size = page_size

        def set_query(self, query):
            self._query = query
            self._apply_search()

        def set_author_query(self, query):
            self._author_query = query
            self._apply_search()

        def set_filter_active(self, name, active):
            """Set activity status of filter of name name
            :param name: The name in the name map of the filter to set
            :param active: The activity status to set. True filters out False results, False filters out True results, and None is disabled"""
            print "setting filter \"{}\" to".format(name), active
            self._filter_activity[name] = active
            self._apply_filters()

        def register_filter(self, name, func, add_args=tuple()):
            """Register a new filter func with the name name
            :param name: the name of the new filter
            :param func: the filter function. must take a mod tuple as its first argument, and the rest of the arguments (if present) must match add_args
            :param add_args: an iterable of additional arguments for func, which are added to each call to it. default empty tuple, which adds no arguments.
            :raises KeyError if name is already present"""
            if name in self._filter_funcs:
                raise KeyError("\'{}\' is already registered".format(name))

            self._filter_funcs[name] = (func, add_args)
            self._filter_activity[name] = None


        def _apply_search(self):
            """apply the new search to the modlist"""
            s_time = time.time()
            if self._query.strip() or self._author_query.strip(): # There's no reason to reorder the modlist if no search has been done.
                self._reordered_modlist = modmenu_search.sort_best(self._query, self.get_base_modlist(), author_query=self._author_query)
            else:
                self._reordered_modlist = self.get_base_modlist()
            print "Search took: {:.5}".format(time.time() - s_time) # Hopefully this never goes above 0.3
            self._apply_filters()

        def _apply_filters(self):
            result_contents = []

            for entry in self._reordered_modlist:
                passed = True
                for name, status in self._filter_activity.iteritems():
                    if status is not None:
                        filter_func, add_args = self._filter_funcs[name]
                        if filter_func(entry, add_args) != status:
                            passed = False
                            break
                if passed:
                    result_contents.append(entry)

            self._filtered_modlist = result_contents

    def _modmenu_do_then_refresh(func, modlist_manager, mod_changes, use_steam):
        """A wrapper which calls func and then refreshes the modlist display. necessary for searchbars, as they don't accept Actions"""
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            finally:
                _refresh_modlist(modlist_manager, mod_changes, use_steam)

        return inner



init -1 python:
    import sys
    import math
    import traceback
    import threading
    from collections import Counter

    import modloader
    from modloader import modconfig, steamhandler_extensions


    def is_modlist_loaded():
        return modconfig.steam_modlist_preloader.is_loaded()

    # modlist error stuff
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

    # Ensure error screens are available, as we may need them
    if not renpy.exports.has_screen("_modlist_errors"):
        renpy.load_module("modloader/patch_errorhandling_screens")



    def _refresh_modlist(modlist_manager, mod_changes, use_steam):
        renpy.hide_screen('modmenu_paged_modlist')
        renpy.show_screen('modmenu_paged_modlist', contents=modlist_manager.get_current_modlist_page(), mod_changes=mod_changes, use_steam=use_steam)
        renpy.restart_interaction()


    # modchange lists methods
    def _modmenu_is_mod_installed(mod_id, mod_name):
        """Is mod actually installed on the computer, regardless of modmenu status."""
        return str(mod_id) in modinfo.get_mod_folders() or str(mod_name) in modinfo.get_mod_folders()

    def _reverse_mapping(mapping):
        """Reverses a mapping from keys to sets of keys

        :param mapping: mapping from keytype to iterable(valuetype), from each key to its mapping set
        :return mapping from valuetype to set(keytype), from each value to its source keys
        """
        result = {}

        for k, v_list in mapping.iteritems():
            print "k={}, v_list={}".format(k, v_list)
            for v in v_list:
                print "v={}".format(v)
                if v not in result:
                    result[v] = set()
                result[v].add(k)
        return result


    def _modmenu_get_recursive_deps(dep_map, reverse_dep_map=None, strict=True):
        """Generate a recursive dependency map from the simple forward and reverse dependency maps

        :param dep_map: mapping from mod_id to iterable(mod_id), from each mod to it's dependencies
        :param reverse_dep_map: reverse mapping, from each mod to is users. used for efficiency. If None (the default), the reversed map is generated.
        :param strict: if True (default), raise KeyError on dependencies which do not appear as keys in dep_map. if False, they are treated as mods without dependencies
        :return mapping from mod_id to set(mod_id), recursive mod mapping
        :raises KeyError when strict=True and a mod has a dependency not in the mapping
        :raises ValueError when a circular dependency is detected
        """
        if reverse_dep_map is None:
            reverse_dep_map = _reverse_mapping(dep_map)

        result = {}
        if strict:
            outer_deps = set(reverse_dep_map.iterkeys()) - set(dep_map.iterkeys())
            if outer_deps:
                raise KeyError("Dependencies {} are not present in the dependency map".format(list(outer_deps)))

            unresolved_deps = Counter({mod_id: len(child_list) for mod_id, child_list in dep_map.iteritems()})
        else:
            present_deps = dep_map.keys()
            unresolved_deps = Counter({mod_id: len(set(child_list).intersection(present_deps)) for mod_id, child_list in dep_map.iteritems()})

        _next_all_unresolved = Counter() + unresolved_deps
        all_resolved = unresolved_deps.most_common()[len(_next_all_unresolved):]
        unresolved_deps = _next_all_unresolved
        while len(all_resolved):
            for mod_id, _ in all_resolved:
                # add entry to dependency map
                child_list = dep_map[mod_id]
                if strict:
                    recursive_deps = reduce(set.union, (result[dep_id] for dep_id in child_list), set())
                else:
                    recursive_deps = reduce(set.union, (result.get(dep_id, set()) for dep_id in child_list), set())
                result[mod_id] = set(child_list).union(recursive_deps)

                # update that they're resolved
                unresolved_deps.subtract(reverse_dep_map.get(mod_id, tuple()))

            _next_all_unresolved = Counter() + unresolved_deps
            all_resolved = unresolved_deps.most_common()[len(_next_all_unresolved):]
            unresolved_deps = _next_all_unresolved


        # all missing are circular dependencies. this should really never happen...
        circular_deps = set(unresolved_deps.iterkeys())
        if circular_deps:
            raise ValueError("Circular dependency detected regarding these mods: {}".format(tuple(circular_deps)))

        return result


    def _default_vendor_filename_func(mod_id, mod_name):
        return mod_name

    class Modchanges:
        def __init__(self):
            """A class holding the full modlist, along with functionality to request to install or uninstall a mod.
            This uses the ScreenValueContainer paradigm with the set and clear methods. as such, the __init__ is empty.
            """

            self._modlist = {}
            self._add_map = {}
            self._remove_map = {}
            self._requested_add_dependency_counts = Counter() # Used to forbid removals of dependencies of present mods by keeping count of them
            self._installed_dependency_counts = Counter()
            self._vendor_filename_func = _default_vendor_filename_func

            self._dependency_map = {}
            self._r_dependency_map = {}


        def set(self, base_modlist, vendor_filename_func=_default_vendor_filename_func):
            """
            :param base_modlist: list[ModlistEntry], The vendor modlist for this class.
            :param vendor_filename_func: func from (mod_id, mod_name) to str, used for removal of mods in accordance with modconfig.remove_mod rules. creates filename for that method.
            """

            self._modlist = {mod.id: mod for mod in base_modlist}
            self._vendor_filename_func = vendor_filename_func

            self._dependency_map = {mod_id: set(mod.child_list) for mod_id, mod in self._modlist.iteritems()}
            self._dependency_map = _modmenu_get_recursive_deps(self._dependency_map, strict=False)

            # Make all valid keys available, then set the ones that have parents
            self._r_dependency_map = {k: set() for k in self._dependency_map.iterkeys()}
            self._r_dependency_map.update(_reverse_mapping(self._dependency_map))

            self._reset_installed_dependency_counts()

        def clear(self):
            self._modlist.clear()
            self._add_map.clear()
            self._remove_map.clear()
            self._requested_add_dependency_counts.clear()
            self._installed_dependency_counts.clear()
            self._vendor_filename_func = _default_vendor_filename_func
            self._dependency_map.clear()
            self._r_dependency_map.clear()


        def _reset_installed_dependency_counts(self):
            self._installed_dependency_counts.clear()

            for mod_id in self._modlist:
                if self.is_mod_installed(mod_id):
                    self._installed_dependency_counts += Counter(self._dependency_map[mod_id])


        def get_mod(self, mod_id):
            return self._modlist[mod_id]

        def get_mod_name(self, mod_id):
            return self._modlist[mod_id].name

        def get_mod_by_name(self, mod_name):
            result = [mod for mod in self._modlist.itervalues() if mod.name == mod_name]
            if not result:
                raise ValueError("mod \"{}\" not present in modlist".format(mod_name))
            return result[0]

        def get_mod_dependencies(self, mod_id):
            return self._dependency_map[mod_id]

        def get_mod_parents(self, mod_id):
            return self._r_dependency_map[mod_id]


        def get_added_mods(self, dependency=True):
            """Get all mods selected for addition, optionally along with their uninstalled dependencies
            :param dependency: if True (default), result also includes all uninstalled dependencies of the selected mods. if False, only mods specifically added will be included
            :return set[mod_id] of added mods
            """
            result = set(self._add_map.iterkeys())
            if dependency:
                result = result.union(mod_id for mod_id in self._requested_add_dependency_counts.iterkeys() if not self.is_mod_installed(mod_id))
            return result

        def get_add_modmap(self, dependency=True):
            """Get modconfig.apply_mod_changes add_modmap appropriate value given the mods selected for addition.
            This will return the same modlist as self.get_added_mods, formatted in a way appropriate for use as the add_modmap parameter of the modconfig.apply_mod_changes function.
            :param dependency: if True (default), result also includes all uninstalled dependencies of the selected mods. if False, only mods specifically added will be included
            :return dict[mod_id: mod_name] of added mods, which can be directly used in apply_mod_changes as the add_modmap parameter
            """
            result = dict(self._add_map)
            if dependency:
                result.update(self._get_add_modmap_deps())
            return result

        def get_removed_mods(self, dependency=True):
            """Get all mods selected for removal, optionally depending on dependency coherence
            :param dependency: if True (default), only returns mods which have no remaining dependency after removal (whether existing or added). if False, all mods requesting removal will be returned
            :return set[mod_id] of removed mods
            """
            if not dependency:
                return set(self._remove_map.iterkeys())
            return {mod_id for mod_id in self._remove_map.iterkeys() if self.is_mod_removable(mod_id)}

        def get_remove_modmap(self, dependency=True):
            """Get modconfig.apply_mod_changes remove_modmap appropriate value given the mods selected for removal.
            This will return the same modlist as self.get_removed_mods, formatted in a way appropriate for use as the remove_modmap parameter of the modconfig.apply_mod_changes function.
            :param dependency: if True (default), only returns mods which have no remaining dependency after removal (whether existing or added). if False, all mods requesting removal will be returned
            :return dict[mod_name: filename] of removed mods, which can be directly used in apply_mod_changes as the remove_modmap parameter
            """
            if not dependency:
                return {mod_name: filename for mod_name, filename in self._remove_map.itervalues()}
            return {mod_name: filename for mod_id, (mod_name, filename) in self._remove_map.iteritems() if self.is_mod_removable(mod_id)}

        def _get_add_modmap_deps(self):
            """Get add_modmap entries for add list dependencies, avoiding already installed mods
            :return dict[mod_id: mod_name] of added mod dependencies, in the format of the add_modmap parameter of the modconfig.apply_mod_changes function
            """
            result = {}
            for mod_id in self._requested_add_dependency_counts.iterkeys():
                mod_name = self.get_mod_name(mod_id)
                if not _modmenu_is_mod_installed(mod_id, mod_name):
                    result[mod_id] = mod_name
            return result




        def is_mod_added(self, mod_id, dependency=True):
            """Is mod_id selected for addition, or optionally will be installed.
            :param dependency: if True (default), returns True if mod_id is selected or is an uninstalled dependency of a selected mod. if False, only returns True if mod_id is selected for addition
            """
            return mod_id in self.get_added_mods(dependency=dependency)

        def is_mod_removed(self, mod_id, dependency=True):
            """Is mod_id selected for removal, or optionally will be removed.
            :param dependency: if True (default), returns True only if mod_id is selected and can be safely removed by dependency logic. if False, returns True if mod_id is selected for removal
            """
            return mod_id in self.get_removed_mods(dependency=dependency)

        def is_all_dependencies_available(self, mod_id):
            """Are all of mod_id's dependencies present in the modlist"""
            return all((dep_id in self._modlist) for dep_id in self._dependency_map[mod_id])


        def is_mod_installed(self, mod_id):
            """Version of _modmenu_is_mod_installed which matches the rest of the functions here"""
            mod = self.get_mod(mod_id)
            return _modmenu_is_mod_installed(mod_id, mod.name)

        def is_mod_present(self, mod_id, dependency=False):
            """Will the mod be installed once the modmenu changes have been applied
            :param mod_id: the mod id to check presence
            :param dependency: if False (default), ignore dependency install for this calculation. if True, then include such case"""
            return (self.is_mod_installed(mod_id) and not self.is_mod_removed(mod_id, dependency)) or self.is_mod_added(mod_id, dependency)

        def is_mod_dependency(self, mod_id):
            """Is this mod a dependency of a present mod. semantically equivalent to not self.is_mod_removable(mod_id)"""
            return mod_id in self._installed_dependency_counts or mod_id in self._requested_add_dependency_counts

        def is_mod_removable(self, mod_id):
            """Can a mod be removed without breaking dependency constraints. this decides if a remove_mod call will produce a visible effect"""
            return not self.is_mod_dependency(mod_id) and self.is_mod_installed(mod_id)


        def add_mod(self, mod_id):
            print "adding mod: " + str(mod_id)
            is_installed = self.is_mod_installed(mod_id)

            if is_installed and mod_id in self._remove_map: # Installed removed mod being reinstated
                self._remove_map.pop(mod_id)
                self._installed_dependency_counts += Counter(self.get_mod_dependencies(mod_id))
            elif not is_installed and mod_id not in self._add_map: # Not added yet, and not an existing mod being reinstated
                self._add_map[mod_id] = self.get_mod_name(mod_id)
                self._requested_add_dependency_counts += Counter(self.get_mod_dependencies(mod_id).intersection(self._modlist.keys()))
            # else: nothing to do...

        def remove_mod(self, mod_id):
            print "removing mod: " + str(mod_id)
            is_installed = self.is_mod_installed(mod_id)

            if not is_installed and mod_id in self._add_map: # Added mod being removed
                self._add_map.pop(mod_id)
                self._requested_add_dependency_counts -= Counter(self.get_mod_dependencies(mod_id))
            elif is_installed and mod_id not in self._remove_map: # Installed mod being removed
                mod_name = self.get_mod_name(mod_id)
                self._remove_map[mod_id] = (mod_name, self._vendor_filename_func(mod_id, mod_name))
                self._installed_dependency_counts -= Counter(self.get_mod_dependencies(mod_id))

        def clear_added_mods(self):
            self._add_map.clear()
            self._requested_add_dependency_counts.clear()

        def clear_removed_mods(self):
            self._remove_map.clear()
            self._reset_installed_dependency_counts()

        def clear_mods(self):
            self.clear_added_mods()
            self.clear_removed_mods()


    # Vendor modfolder functions
    def _steam_get_modfolder(mod_id, mod_name):
        return str(mod_id)

    def _github_get_modfolder(mod_id, mod_name):
        return mod_name


init python:
    # screen variable container code
    _SVC_LISTING_SCOPE_KEY = "_must_clear"
    class ScreenValueContainer:
        """
        Multiton interface for managing complex types which are values within Renpy screen.

        Renpy (for some reason) keeps a live reference to every value that appears in a variable in one of it's screens (it seems to be related to bindings?),
          This will cause memory leaks if that value is reference counted and the screen is reopened... which includes... almost everything...
        For values that are not supposed to survive after a screen is closed, we therefore don't want to create a fresh object on every screen show.
        This is what this interface is for:
          it can get the value we need to hold using the get() method, then clear it on screen hide relying on the ScreenValueContainerClearer object.
          objects are created once, then cleared and reused when the screen is reopened.
        This way, repeated entrances to these screens cannot leak these values, and they can safely be cleared when the screen is hidden.

        :param var_type: The type of object this manages. that object type must be constructable with no arguments, and have a clear() method with no arguments to clear it's contents.
        :param set_method (default "set"): The name of the method of var_type which is used to set the instances value

        The clear method is managed by ScreenValueContainerClearer, and must be named "clear".
        """

        def __init__(self, var_type, set_method="set"):
            self._var_type = var_type
            self._instances = {} # Mapping[(screen_name, var_name): instance] for reusable instances
            self._set_method = set_method

        def get(self, name, *args, **kwargs):
            """ Set the held value, using parameters defined by the screen.
            Usually called when showing the screen, though this method can be more flexible.

            :param name: the name of the variable within this multiton. should generally match the variable's name within the screen

            Additional arguments are passed to the variable type's set method, as defined in the __init__ method.
            """
            cscr = renpy.current_screen()
            key = (cscr.screen_name[0], name)


            if key not in self._instances:
                self._instances[key] = self._var_type()

            result = self._instances[key]
            getattr(result, self._set_method)(*args, **kwargs)

            if name not in cscr.scope[_SVC_LISTING_SCOPE_KEY]:
                cscr.scope[_SVC_LISTING_SCOPE_KEY][name] = result

            return result

    class ScreenValueContainerClearer(renpy.Displayable):
        """
        Ensures ScreenValueContainer's inner values get cleared properly at screen hide.
        If a screen uses any ScreenValueContainers, an instance of this type must be added (using the `add` command) before any ScreenValueContainer.get calls are made.
        This then ensures that all ScreenValueContainer inner values used within the screen are cleared on screen hide.
        """

        def __init__(self):
            super(renpy.Displayable, self).__init__()
            cscr = renpy.current_screen()
            if _SVC_LISTING_SCOPE_KEY not in cscr.scope:
                cscr.scope[_SVC_LISTING_SCOPE_KEY] = {}
            return

        def render(self, width, height, st, at):
            return renpy.display.render.Render(0, 0)

        def set_transform_event(self, event):
            if event == "hide":
                cscr = renpy.current_screen()
                for to_clear in cscr.scope[_SVC_LISTING_SCOPE_KEY].itervalues():
                    to_clear.clear()
                cscr.scope[_SVC_LISTING_SCOPE_KEY].clear()

    class SettableSet(set):
        """set subclass compatible with ScreenValueContainer.
        set_to method required as dicts dont have a valid one
        """
        def set_to(self, other):
            # Come on... set.set would be ridiculous
            self.clear()
            return self.update(other)

    class SettableClearableList(list):
        """dict subclass compatible with ScreenValueContainer.
        set and clear methods required as lists dont have valid ones
        """
        def set(self, other):
            self[:] = other

        def clear(self):
            self[:] = []


    ModmenuEntranceLoadManagerContainer = ScreenValueContainer(ModmenuEntranceLoadManager, set_method="set")
    ModscreenModlistManagerContainer = ScreenValueContainer(ModscreenModlistManager, set_method="set")
    ModchangesContainer = ScreenValueContainer(Modchanges, set_method="set")
    SetContainer = ScreenValueContainer(SettableSet, set_method="set_to")
    ListContainer = ScreenValueContainer(SettableClearableList, set_method="set")




screen modmenu_paged(contents, use_steam):
    modal True

    add ScreenValueContainerClearer()

    if use_steam:
        $ _get_modfolder = _steam_get_modfolder
    else:
        $ _get_modfolder = _github_get_modfolder

    default mod_changes = ModchangesContainer.get("mod_changes", contents, vendor_filename_func=_get_modfolder)

    python:
        filter_map = {"install": (lambda mod, mod_changes: mod_changes.is_mod_installed(mod.id), mod_changes),
                      "select":  (lambda mod, mod_changes: mod_changes.is_mod_added(mod.id, dependency=False) or mod_changes.is_mod_removed(mod.id, dependency=False), mod_changes),
                      "present": (lambda mod, mod_changes: mod_changes.is_mod_present(mod.id, dependency=True), mod_changes),
                  }


    default modlist_manager = ModscreenModlistManagerContainer.get("modlist_manager", contents, filter_map=filter_map, use_steam=use_steam)


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
                action [Function(modlist_manager.move_current_page, -5),
                        Function(_refresh_modlist, modlist_manager, mod_changes, use_steam)
                       ]
                sensitive (modlist_manager.get_current_page() > 1)

            textbutton "-":
                xalign 0.4
                ycenter 0.5
                keysym "mousedown_4"
                action [Function(modlist_manager.move_current_page, -1),
                        Function(_refresh_modlist, modlist_manager, mod_changes, use_steam)
                       ]
                sensitive (modlist_manager.get_current_page() > 1)

            # renpy seems to not like calling things in the string formatting...
            $ _page_num = modlist_manager.get_current_page()
            $ _max_page = modlist_manager.get_max_page()
            label "Page #[_page_num]/[_max_page]":
                xalign 0.5
                ycenter 0.5
                text_size 40

            textbutton "+":
                xalign 0.6
                ycenter 0.5
                keysym "mousedown_5"
                action [Function(modlist_manager.move_current_page, 1),
                        Function(_refresh_modlist, modlist_manager, mod_changes, use_steam)
                        ]
                sensitive (modlist_manager.get_current_page() < modlist_manager.get_max_page())

            textbutton "+5":
                xalign 0.8
                ycenter 0.5
                # Also tried to bind this to shift+scroll, but it didn't work...
                action [Function(modlist_manager.move_current_page, 5),
                        Function(_refresh_modlist, modlist_manager, mod_changes, use_steam)
                        ]
                sensitive (modlist_manager.get_current_page() < modlist_manager.get_max_page())

        # As we wish to include dependencies in both calculations, we use the non-selection methods
        $ n_added_mods = len(mod_changes.get_added_mods())
        $ n_removed_mods = len(mod_changes.get_removed_mods())

        if n_added_mods:
            if n_removed_mods:
                $ apply_button_prefix = "Apply"
                $ apply_button_postfix = "(+{}, -{})".format(n_added_mods, n_removed_mods)
            else:
                $ apply_button_prefix = "Install"
                $ apply_button_postfix = "({})".format(n_added_mods)
        else:
            if n_removed_mods:
                $ apply_button_prefix = "Uninstall"
                $ apply_button_postfix = "({})".format(n_removed_mods)
            else:
                $ apply_button_prefix = "No mods selected..."
                $ apply_button_postfix = ""

        textbutton "[apply_button_prefix] [apply_button_postfix]":
            background "#0000009B"
            hover_background "#ffffff9B"
            insensitive_background "#3f3f3fFF"
            xpos 1855
            ypos 990
            xanchor 1.0
            yanchor 1.0

            xsize 425
            ysize 125
            action [Function(print, "added:", mod_changes.get_added_mods(), "\nremoved:", mod_changes.get_removed_mods()),
                    Show("modmenu_apply_confirm", mod_changes=mod_changes, use_steam=use_steam)]
            sensitive bool(n_added_mods) or bool(n_removed_mods)

    # Searchbars
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
                    changed _modmenu_do_then_refresh(modlist_manager.set_author_query, modlist_manager, mod_changes, use_steam)


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
                    changed _modmenu_do_then_refresh(modlist_manager.set_query, modlist_manager, mod_changes, use_steam)
        key "K_ESCAPE" action [SetScreenVariable("focus_query_input", False), SetScreenVariable("focus_author_query_input", False)]
        key "K_TAB" action [ToggleScreenVariable("focus_author_query_input"),
                            If(focus_author_query_input,
                               ToggleScreenVariable("focus_query_input"),
                               SetScreenVariable("focus_query_input", False))]

    # Filter buttons
    hbox:
        xpos 510
        ypos 10
        xanchor 0.0
        yanchor 0.0
        xsize 250
        ysize 110

        spacing 10

        vbox:
            xalign 0.0
            ycenter 0.5
            xsize 200
            spacing 6

            # For some reason 'label' and 'text' text components insisted on being ever so slightly larger than necessary, which made everything look misaligned
            textbutton "Installed":
                background "#00000000"
                text_size 24
                ysize 32
                xalign 0.0

            textbutton "Selected":
                background "#00000000"
                text_size 24
                ysize 32
                xalign 0.0

            textbutton "To be installed":
                background "#00000000"
                text_size 24
                ysize 32
                xalign 0.0

        vbox:
            xalign 1.0
            ycenter 0.5
            spacing 6

            $ _im_size = 30

            for filter_name in ["install", "select", "present"]:

                $ _status = modlist_manager.is_filter_active(filter_name)
                imagebutton:
                    if _status is True:
                        idle im.Scale("ui/nsfw_chbox-checked.png", _im_size, _im_size)
                    elif _status is False:
                        idle im.Scale("ui/nsfw_chbox-crossed.png", _im_size, _im_size)
                    else: # _status is None
                        idle im.Scale("ui/nsfw_chbox-unchecked.png", _im_size, _im_size)

                    action    [Function(modlist_manager.set_filter_active, filter_name, If(_status is True, None, True)),
                               Function(_refresh_modlist, modlist_manager, mod_changes, use_steam)
                              ]
                    alternate [Function(modlist_manager.set_filter_active, filter_name, If(_status is False, None, False)),
                               Function(_refresh_modlist, modlist_manager, mod_changes, use_steam)
                              ]


    on "show" action [Function(_refresh_modlist, modlist_manager, mod_changes, use_steam),
                      Function(_preload_mod_images, contents, None),
                      Function(im.cache.clear) # I tended to get 'out of memory' errors on this menu, so we use this precaution
                      ]

    on "hide" action [Function(mod_image_preloader.clear), # Cleanup after ourselves
                      Function(im.cache.clear),
                      Function(modmenu_search.clear_cache),
                      Function(mod_changes.clear_mods),
                     ]



screen modmenu_paged_modlist(contents, mod_changes, use_steam):

    add ScreenValueContainerClearer()

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

            $ mod_button_text_extras = ListContainer.get("mod_button_text_extras", [])
            for mod in contents:
                $ mod_id = mod.id
                $ child_list = mod.child_list
                $ mod_button_text = modmenu_name_cleaner(mod.name)

                if len(mod_button_text) > 21:
                    #if mod_button_text is greater than 21 characters, decrease size of font by 5
                    if len(mod_button_text) <= 25:
                        $ mod_button_text = "{size=-5}" + mod_button_text + "{/size}"

                    #if mod_button_text is greater than 25 characters, decrease size of font by 10
                    else:
                        #if mod_button_text is greater than 30 characters, decrease size of font by 10 and cut all text after 30 places
                        $ mod_button_text = mod_button_text[:30]
                        $ mod_button_text = "{size=-10}" + mod_button_text + "{/size}"

                $ mod_button_text_extras.clear()

                if mod_changes.is_mod_installed(mod_id):
                    $ mod_button_text_extras.append("Installed")
                    if mod_changes.is_mod_removed(mod_id, dependency=False):
                        if mod_changes.is_mod_removable(mod_id):
                            $ mod_button_text_extras.append("Removed")
                        else:
                            $ mod_button_text_extras.append("{s}Removed{/s}")
                elif mod_changes.is_mod_added(mod_id, dependency=False):
                    $ mod_button_text_extras.append("Added")
                    if not mod_changes.is_all_dependencies_available(mod_id):
                        $ mod_button_text_extras.append("Missing")

                if mod_changes.is_mod_dependency(mod_id):
                    $ mod_button_text_extras.append("Dependency")

                if mod_button_text_extras:
                    $ mod_button_status_text = ", ".join(mod_button_text_extras)
                    if len(mod_button_status_text) >= 25:
                        $ mod_button_text += "\n{size=-10}("
                    else:
                        $ mod_button_text += "\n{size=-5}("
                    $ mod_button_text += mod_button_status_text  + "){/size}"

                # format: "\n{size=-5}(eff, eff, eff){/size}"

                textbutton "[mod_button_text]":
                    style "modmenu_select_btn"
                    # Recolor the button if involved with add/remove/dependency lists
                    if mod_changes.is_mod_removed(mod_id, dependency=False):
                        if mod_changes.is_mod_removable(mod_id):
                            background "#7f00009B"
                            hover_background "#ff7f7f9B"
                        else:
                            background "#7f3f009B"
                            hover_background "#ffbf7f9B"
                    elif mod_changes.is_mod_installed(mod_id):
                        background "#001f3f9B"
                        hover_background "#003f7f9B"
                    elif mod_changes.is_mod_added(mod_id, dependency=False):
                        if not mod_changes.is_all_dependencies_available(mod_id):
                            background "#7f7f00CF"
                            hover_background "#ffff7fCF"
                        else:
                            background "#007f009B"
                            hover_background "#7fff7f9B"
                    elif mod_changes.is_mod_dependency(mod_id):
                        background "#007f3f9B"
                        hover_background "#7fffaf9B"


                    action [Hide("modmenu_mod_content"),
                            Show("modmenu_mod_content",
                                 mod=mod,
                                 mod_changes=mod_changes,
                                 use_steam=use_steam,
                                 ),
                            Play("audio", "se/sounds/open.ogg")]

                    alternate [If(mod_changes.is_mod_present(mod_id, dependency=False),
                                   Function(mod_changes.remove_mod, mod_id),
                                   Function(mod_changes.add_mod, mod_id)),
                               Play("audio", "se/sounds/open.ogg")]
                              ]




screen modmenu_mod_content(mod, mod_changes, use_steam):
    $ mod_id = mod.id
    $ name = unicode(mod.name, "utf8")
    $ author = unicode(mod.author, "utf8")
    $ description = unicode(mod.desc, "utf8")
    $ url = mod.image_url


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
#         vbox xpos 0.72 ypos 0.21:
        vbox xpos 0.73 ypos 0.21:
            python:
                ModmenuContentImageURL(url)


        vbox xpos 0.275 ypos 0.21:
            null height 30

            text "Author: [author]" size 42

            null height 38

            hbox:
                text "Description:" size 42 ycenter 0.5

                null width 350

                if mod_changes.is_mod_present(mod_id, dependency=False):
                    textbutton "Uninstall":
                        ycenter 0.5
                        action [Function(mod_changes.remove_mod, mod_id),
                                Play("audio", "se/sounds/open.ogg")]
                        style "modmenu_content_btn"
                        text_style "modmenu_select_btn_text"
                        text_size 40

                else:
                    textbutton "Install":
                        ycenter 0.5
                        action [Function(mod_changes.add_mod, mod_id),
                                Play("audio", "se/sounds/open.ogg")]
                        style "modmenu_content_btn"
                        text_style "modmenu_select_btn_text"
                        text_size 40


            null height 32

            viewport id "modcontent_vp":
                #scrollbars "vertical"
                draggable True
                mousewheel True
                xminimum 1050
                xmaximum 1050
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
            xpos 1582
            #yalign 0.95

        # dependency area
        frame xpos 1632 ypos 0.21 xsize 280 ysize 290:
            background "#0000009B"
            xpadding 15

            vbox xsize 230 yfill True:
                text "Dependencies:" size 40

                viewport id "_dep_list" xfill True:
                    mousewheel "change"

                    vbox:
                        for dep_id in mod_changes.get_mod_dependencies(mod_id):
                            python:
                                dep_present = True
                                try:
                                    dep_name = mod_changes.get_mod(dep_id).name

                                    if mod_changes.is_mod_removed(dep_id, dependency=False):
                                        if mod_changes.is_mod_removable(dep_id):
                                            dep_color = "#ff1f1fFF"
                                            dep_hover = "#ff4f4fFF"
                                        else:
                                            dep_color = "#9f7f7fFF"
                                            dep_hover = "#7f5f5fFF"
                                    elif mod_changes.is_mod_installed(dep_id):
                                        dep_color = "#00bfffFF"
                                        dep_hover = "#007fbfFF"
                                    elif mod_changes.is_mod_added(dep_id, dependency=False):
                                        dep_color = "#bfff00FF"
                                        dep_hover = "#7fbf00FF"
                                    elif mod_changes.is_mod_dependency(dep_id):
                                        dep_color = "#00ffbfFF"
                                        dep_hover = "#00bf7fFF"
                                    else:
                                        dep_color = "#ffffffFF"
                                        dep_hover = "#bfbfbfFF"

                                except KeyError:
                                    dep_present = False
                                    dep_name = "<Missing>"
                                    dep_color = "#7f7f7fFF"
                                    dep_hover = "#afafafFF"

                            textbutton "[dep_name]":
                                background "#0000" # Clear background, as I don't wish there to be
                                padding (0, 0)
                                text_size 20
                                text_color dep_color
                                text_hover_color dep_hover

                                if dep_present:
                                    action [Hide("modmenu_mod_content"),
                                            Show("modmenu_mod_content",
                                                 mod=mod_changes.get_mod(dep_id),
                                                 mod_changes=mod_changes,
                                                 use_steam=use_steam,
                                                 ),
                                            Play("audio", "se/sounds/open.ogg")]

                                    alternate [If(mod_changes.is_mod_present(dep_id, dependency=False),
                                                   Function(mod_changes.remove_mod, dep_id),
                                                   Function(mod_changes.add_mod, dep_id)),
                                               Play("audio", "se/sounds/open.ogg")]
                                              ]



            bar value YScrollValue("_dep_list"):
                style "modmenu_content_slider"
                ysize 250
                yalign 1.0
                xalign 1.0
                unscrollable "hide"


        # parents area
        frame xpos 1632 ypos 0.497 xsize 280 ysize 290:
            background "#0000009B"
            xpadding 15

            vbox xsize 230 yfill True:
                text "Dependents:" size 40

                viewport id "_parent_list" xfill True:
                    mousewheel "change"

                    vbox:
                        for parent_id in mod_changes.get_mod_parents(mod_id):
                            python:
                                parent_present = True
                                try:
                                    parent_name = mod_changes.get_mod_name(parent_id)

                                    if mod_changes.is_mod_removed(parent_id, dependency=False):
                                        if mod_changes.is_mod_removable(parent_id):
                                            parent_color = "#ff1f1fFF"
                                            parent_hover = "#ff4f4fFF"
                                        else:
                                            parent_color = "#9f7f7fFF"
                                            parent_hover = "#7f5f5fFF"
                                    elif mod_changes.is_mod_installed(parent_id):
                                        parent_color = "#00bfffFF"
                                        parent_hover = "#007fbfFF"
                                    elif mod_changes.is_mod_added(parent_id, dependency=False):
                                        parent_color = "#bfff00FF"
                                        parent_hover = "#7fbf00FF"
                                    elif mod_changes.is_mod_dependency(parent_id):
                                        parent_color = "#00ffbfFF"
                                        parent_hover = "#00bf7fFF"
                                    else:
                                        parent_color = "#ffffffFF"
                                        parent_hover = "#bfbfbfFF"

                                except KeyError:
                                    parent_present = False
                                    parent_name = "<Missing>"
                                    parent_color = "#7f7f7fFF"
                                    parent_hover = "#afafafFF"

                            textbutton "[parent_name]":
                                background "#0000" # Clear background, as I don't wish there to be
                                padding (0, 0)
                                text_size 20
                                text_color parent_color
                                text_hover_color parent_hover

                                if parent_present:
                                    action [Hide("modmenu_mod_content"),
                                            Show("modmenu_mod_content",
                                                 mod=mod_changes.get_mod(parent_id),
                                                 mod_changes=mod_changes,
                                                 use_steam=use_steam,
                                                 ),
                                            Play("audio", "se/sounds/open.ogg")]

                                    alternate [If(mod_changes.is_mod_present(parent_id, dependency=False),
                                                   Function(mod_changes.remove_mod, parent_id),
                                                   Function(mod_changes.add_mod, parent_id)),
                                               Play("audio", "se/sounds/open.ogg")]
                                              ]

            bar value YScrollValue("_parent_list"):
                style "modmenu_content_slider"
                ysize 250
                yalign 1.0
                xalign 1.0
                unscrollable "hide"



transform _button_zoom:
    zoom 40.0 / 54.0


screen modmenu_apply_confirm(mod_changes, use_steam):
    modal True

    add ScreenValueContainerClearer()

    python:
        from modloader.modconfig import apply_mod_changes

        full_mods_to_add = SetContainer.get("full_mods_to_add", mod_changes.get_added_mods(dependency=True))
        selected_mods_to_remove = SetContainer.get("selected_mods_to_remove", mod_changes.get_removed_mods(dependency=False))

        selected_mods_to_add = SetContainer.get("selected_mods_to_add", mod_changes.get_added_mods(dependency=False))
        removable_mods_to_remove = SetContainer.get("removable_mods_to_remove", mod_changes.get_removed_mods(dependency=True))

    window id "modmenu_apply_confirm" at alpha_dissolve:
        add "#22589a"
        xfill True
        yfill True

        xpadding 0
        ypadding 0

        text "Are you sure you want to change these mods?":
            size 65
            xpos 0.5
            ypos 0.05
            xcenter 0.5
            yanchor 0.5
            font "Ardnas.otf"


        hbox: # Changelist
            ysize 700
            xsize 1800

            ypos 100
            xcenter 0.5
            yanchor 0.0

            fixed: # Added mods list: fixed is used to force list+scrollbar to stay within their region
                xalign 0.0
                xsize 850
                ymaximum 700

                vbox:
                    xsize 800
                    xalign 0.0

                    text "Added mods:":
                        size 50
                        ysize 100
                        xfill True

                    viewport id "_mod_add_list":
                        xfill True
                        mousewheel "change"

                        vbox:
                            spacing 5
                            xfill True

                            for mod_id in selected_mods_to_add:
                                $ mod_name = mod_changes.get_mod_name(mod_id)
                                hbox:
                                    spacing 20
                                    ysize 60

                                    imagebutton:
                                        idle "image/ui/close_idle.png" at _button_zoom
                                        hover "image/ui/close_hover.png"
                                        yalign 0.5

                                        action Function(mod_changes.remove_mod, mod_id)

                                    text mod_name:
                                        if len(mod_name) > 30:
                                            size 30
                                        xfill True
                                        ysize 60

                            if len(full_mods_to_add) > len(selected_mods_to_add):
                                null height 5
                                text "Including these dependencies:":
                                    size 50
                                null height 10

                                for mod_id in (full_mods_to_add - selected_mods_to_add):
                                    $ mod_name = mod_changes.get_mod_name(mod_id)
                                    hbox:
                                        spacing 20
                                        ysize 60

                                        text mod_name:
                                            if len(mod_name) > 30:
                                                size 30
                                            xfill True
                                            ysize 60

                vbar value YScrollValue("_mod_add_list"):
                    style "modmenu_select_slider"
                    xalign 1.0


            fixed: # Removed mods list: fixed is used to force list+scrollbar to stay within their region
                xalign 1.0
                xsize 850
                ymaximum 700

                vbox:
                    xsize 800
                    xalign 0.0

                    text "Removed mods:":
                        size 50
                        ysize 100
                        xfill True

                    viewport id "_mod_remove_list":
                        xfill True
                        mousewheel "change"

                        vbox:
                            spacing 5
                            xfill True
                            for mod_id in removable_mods_to_remove:
                                $ mod_name = mod_changes.get_mod_name(mod_id)
                                hbox:
                                    spacing 20
                                    ysize 60

                                    imagebutton:
                                        idle "image/ui/close_idle.png" at _button_zoom
                                        hover "image/ui/close_hover.png"
                                        yalign 0.5
                                        action Function(mod_changes.add_mod, mod_id)

                                    text mod_name:
                                        if len(mod_name) > 30:
                                            size 30
                                        xfill True
                                        ysize 60


                            if len(selected_mods_to_remove) > len(removable_mods_to_remove):
                                if not removable_mods_to_remove:
                                    text "---":
                                        xfill True
                                        ysize 60
                                null height 5
                                text "Removal suppressed:":
                                    size 50
                                null height 10

                                for mod_id in (selected_mods_to_remove - removable_mods_to_remove):
                                    $ mod_name = mod_changes.get_mod_name(mod_id)
                                    hbox:
                                        spacing 20
                                        ysize 60

                                        imagebutton:
                                            idle "image/ui/close_idle.png" at _button_zoom
                                            hover "image/ui/close_hover.png"
                                            yalign 0.5
                                            action Function(mod_changes.add_mod, mod_id)

                                        text mod_name:
                                            if len(mod_name) > 30:
                                                size 30
                                            xfill True
                                            ysize 60

                vbar value YScrollValue("_mod_remove_list"):
                    style "modmenu_select_slider"
                    xalign 1.0

        hbox: # Apply/Cancel buttons
            ysize 125
            xsize 1200

            ypos 990
            xcenter 0.5
            yanchor 1.0


            textbutton "Cancel":
                background "#0000009B"
                hover_background "#ffffff9B"

                xalign 0.0
                ycenter 0.5
                xsize 425
                ysize 125
                action [Hide("modmenu_apply_confirm", transition=dissolve),
                    Play("audio", "se/sounds/close.ogg"),
                    ]

            textbutton "Apply":
                background "#0000009B"
                hover_background "#ffffff9B"
                insensitive_background "#3f3f3fFF"

                xalign 1.0
                ycenter 0.5
                xsize 425
                ysize 125
                action [Function(apply_mod_changes,
                                 add_modmap=mod_changes.get_add_modmap(),
                                 remove_modmap=mod_changes.get_remove_modmap(),
                                 show_status_screen=True,
                                 reload_script=True,
                                 use_steam=use_steam),]
                sensitive bool(selected_mods_to_add) or bool(selected_mods_to_remove)


screen modmenu_nointernet() tag smallscreen2:
    modal True

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
