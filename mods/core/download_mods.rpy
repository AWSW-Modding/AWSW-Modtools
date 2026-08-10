# modmenu entrance stuff
init -1 python:
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
                    # (mod_url, name, author, description, image) (for github)
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
        def __init__(self, modlist, page_size=6, filter_map=None, use_steam=True):
            """Manages the modscreen's displayed modlist, including paging, searching and filtering.

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

            self._filter_funcs = filter_map
            self._filter_activity = {name: None for name in filter_map.iterkeys()}

            self.use_steam = use_steam

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
                        fulter_func, add_args = self._filter_funcs[name]
                        if fulter_func(entry, add_args) != status:
                            passed = False
                            break
                if passed:
                    result_contents.append(entry)

            self._filtered_modlist = result_contents
#             _refresh_modlist(self, self.use_steam)

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


    def _modmenu_get_recursive_deps(dep_map, reverse_dep_map, strict=True):
        """Generate a recursive dependency map from the simple forward and reverse dependency maps

        :param dep_map: mapping from mod_id to iterable(mod_id), from each mod to it's dependencies
        :param reverse_dep_map: reverse mapping, from each mod to is users. used for efficiency
        :param strict: if True (default), raise KeyError on dependencies which do not appear as keys in dep_map. if False, they are treated as mods without dependencies
        :return mapping from mod_id to set(mod_id), recursive mod mapping
        :raises KeyError when strict=True and a mod has a dependency not in the mapping
        :raises ValueError when a circular dependency is detected
        """
        result = {}
        if strict:
            unfulfilled_deps = {mod_id: set(child_list) for mod_id, child_list in dep_map.iteritems()}
        else:
            checked_deps = dep_map.keys()
            unfulfilled_deps = {mod_id: set(child_list).intersection(checked_deps) for mod_id, child_list in dep_map.iteritems()}
        all_fulfilled = {mod_id: dep_map[mod_id] for mod_id, unfulfilled_list in unfulfilled_deps.iteritems() if not len(unfulfilled_list)}
        unfulfilled_deps = {mod_id: child_list for mod_id, child_list in unfulfilled_deps.iteritems() if mod_id not in all_fulfilled} # remove fulfilled mods
        while len(all_fulfilled):
            for mod_id, child_list in all_fulfilled.iteritems():
                # add entry to dependency map
                if strict:
                    recursive_deps = reduce(set.union, (dep_map[dep_id] for dep_id in child_list), set())
                else:
                    recursive_deps = reduce(set.union, (dep_map.get(dep_id, set()) for dep_id in child_list), set())
                result[mod_id] = set(child_list).union(recursive_deps)

                # update that they're fulfilled
                for use_id in reverse_dep_map[mod_id]:
                    unfulfilled_deps[use_id].remove(mod_id)

            all_fulfilled = {mod_id: dep_map[mod_id] for mod_id, unfulfilled_list in unfulfilled_deps.iteritems() if not len(unfulfilled_list)}
            unfulfilled_deps = {mod_id: child_list for mod_id, child_list in unfulfilled_deps.iteritems() if mod_id not in all_fulfilled}


        # all missing are circular dependencies. this should really never happen...
        circular_deps = set(dep_map.iterkeys()) - set(result.iterkeys())
        if circular_deps:
            raise ValueError("Circular dependency detected regarding these mods: {}".format(tuple(circular_deps)))

        return result


    class Modchanges:
        def __init__(self, base_modlist):
            """A class holding the full modlist, along with functionality to request to install or uninstall a mod.

            :param base_modlist: The vendor modlist for this class
            """

            self._modlist = {mod.id: mod for mod in base_modlist}
            self._add_map = {}
            self._dependant_add_map = Counter()
            self._remove_map = {}
            self._installed_dependant_map = Counter() # equivalent of _dependant_add_map used to keep track when a mod is safe to delete

            # setup recursive dependency maps
            forward_dep_map = {mod_id: set(mod.child_list) for mod_id, mod in self._modlist.iteritems()}
            reverse_dep_map = {mod_id: set() for mod_id in self._modlist}
            for mod_id, child_list in forward_dep_map.iteritems():
                for child_key in child_list:
                    if child_key not in reverse_dep_map:
                        reverse_dep_map[child_key] = set()
                    reverse_dep_map[child_key].add(mod_id)

            # Fixup forward_dep_map to include missing keys from reverse_dep_map as _modmenu_get_recursive_deps is annoying about them
            missing_keys = set(reverse_dep_map.keys()) - set(forward_dep_map.keys())
            forward_dep_map.update({key: set() for key in missing_keys})

            self._dependency_map = _modmenu_get_recursive_deps(forward_dep_map, reverse_dep_map, strict=False)
            self._r_dependency_map = _modmenu_get_recursive_deps(reverse_dep_map, forward_dep_map, strict=False)

            self._reset_installed_dependant_map()


        def _reset_installed_dependant_map(self):
            self._installed_dependant_map.clear()

            for mod_id in self._modlist:
                if self.is_mod_installed(mod_id):
                    self._installed_dependant_map += Counter(self._dependency_map[mod_id])


        def get_mod(self, mod_id):
            return self._modlist[mod_id]

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
            """
            if not dependency:
                return self._add_map
            result = self.get_added_dependencies(missing=True)
            result.update(self._add_map)
            return result

        def get_removed_mods(self, dependency=True):
            """Get all mods selected for removal, optionally depending on dependency coherence
            :param dependency: if True (default), only returns mods which have no remaining dependency after removal (whether existing or added). if False, all mods requesting removal will be returned
            """
            if not dependency:
                return self._remove_map
            return {mod_id: item for mod_id, item in self._remove_map.iteritems() if self.is_mod_removable(mod_id)}

        def get_added_dependencies(self, missing=False):
            """Get all added mod dependencies.
            :param missing: if True, only include missing (as in, not installed) dependencies. if False (default), include all dependencies
            """
            if missing:
                result = {}
                for mod_id in self._dependant_add_map.iterkeys():
                    mod_name = self.get_mod(mod_id).name
                    if not _modmenu_is_mod_installed(mod_id, mod_name):
                        result[mod_id] = mod_name
                return result
            return {mod_id: self.get_mod(mod_id).name for mod_id in self._dependant_add_map.iterkeys()}

        def get_installed_dependencies(self):
            return {mod_id for mod_id in self._installed_dependant_map.iterkeys()}


        def is_mod_added(self, mod_id, dependency=True):
            """Is mod_id selected for addition, or optionally will be installed.
            :param dependency: if True (default), returns True if mod_id is selected or is an uninstalled dependency of a selected mod. if False, only returns True if mod_id is selected for addition
            """
            return mod_id in self.get_added_mods(dependency)

        def is_mod_dependency(self, mod_id):
            return mod_id in self.get_added_dependencies()

        def is_mod_removed(self, mod_id, dependency=True):
            """Is mod_id selected for removal, or optionally will be removed.
            :param dependency: if True (default), returns True only if mod_id is selected and can be safely removed by dependency logic. if False, returns True if mod_id is selected for removal
            """
            return mod_id in self.get_removed_mods(dependency)

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

        def is_mod_removable(self, mod_id):
            """Can a mod be removed without breaking dependency constraints. this decides if a remove_mod call will produce a visible effect"""
            return mod_id not in self._installed_dependant_map and mod_id not in self._dependant_add_map


        def add_mod(self, mod_id):
            print "adding mod:", mod_id
            is_installed = self.is_mod_installed(mod_id)

            if is_installed and mod_id in self._remove_map: # Added, then removed this session
                self._remove_map.pop(mod_id)
                self._installed_dependant_map += Counter(self.get_mod_dependencies(mod_id))
            elif not is_installed and mod_id not in self._add_map: # Not added yet, and not an existing mod being reinstated
                self._add_map[mod_id] = self.get_mod(mod_id).name
                self._dependant_add_map += Counter(self.get_mod_dependencies(mod_id))
            # else: nothing to do...

        def remove_mod(self, mod_id, filename=""):
            print "removing mod:", mod_id, filename
            is_installed = self.is_mod_installed(mod_id)

            if not is_installed and mod_id in self._add_map:
                self._add_map.pop(mod_id)
                self._dependant_add_map -= Counter(self.get_mod_dependencies(mod_id))
            elif is_installed and mod_id not in self._remove_map:
                self._remove_map[mod_id] = (self.get_mod(mod_id).name, filename)
                self._installed_dependant_map -= Counter(self.get_mod_dependencies(mod_id))

        def clear_added_mods(self):
            self._add_map.clear()
            self._dependant_add_map.clear()

        def clear_removed_mods(self):
            self._remove_map.clear()
            self._reset_installed_dependant_map()

        def clear_mods(self):
            self.clear_added_mods()
            self.clear_removed_mods()


    # Vendor modfolder functions
    def _steam_get_modfolder(mod_id, mod_name):
        return str(mod_id)

    def _github_get_modfolder(mod_id, mod_name):
        return mod_name


screen modmenu_paged(contents, use_steam):
    modal True

    default mod_changes = Modchanges(contents)

    python:
        filter_map = {"install": (lambda mod, mod_changes: mod_changes.is_mod_installed(mod.id), mod_changes),
                      "select":  (lambda mod, mod_changes: mod_changes.is_mod_added(mod.id, dependency=False) or mod_changes.is_mod_removed(mod.id, dependency=False), mod_changes),
                      "present": (lambda mod, mod_changes: mod_changes.is_mod_present(mod.id, dependency=True), mod_changes),
                  }

    default modlist_manager = ModscreenModlistManager(contents, filter_map=filter_map, use_steam=use_steam)


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
    if use_steam:
        $ _get_modfolder = _steam_get_modfolder
    else:
        $ _get_modfolder = _github_get_modfolder

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

                $ mod_button_text_extras = []

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
                    if mod_changes.is_mod_added(mod_id, dependency=False):
                        if not mod_changes.is_all_dependencies_available(mod_id):
                            background "#7f7f00CF"
                            hover_background "#ffff7fCF"
                        else:
                            background "#007f009B"
                            hover_background "#7fff7f9B"
                    elif mod_changes.is_mod_dependency(mod_id):
                        background "#007f3f9B"
                        hover_background "#7fffaf9B"
                    elif mod_changes.is_mod_removed(mod_id, dependency=False):
                        if mod_changes.is_mod_removable(mod_id):
                            background "#7f00009B"
                            hover_background "#ff7f7f9B"
                        else:
                            background "#7f3f009B"
                            hover_background "#ffbf7f9B"


                    action [Hide("modmenu_mod_content"),
                            Show("modmenu_mod_content",
                                 mod=mod,
                                 mod_changes=mod_changes,
                                 use_steam=use_steam,
                                 ),
                            Play("audio", "se/sounds/open.ogg")]

                    alternate [If(mod_changes.is_mod_present(mod_id, dependency=False),
                                   Function(mod_changes.remove_mod, mod_id, _get_modfolder(mod_id, mod.name)),
                                   Function(mod_changes.add_mod, mod_id)),
                               Play("audio", "se/sounds/open.ogg")]
                              ]




screen modmenu_mod_content(mod, mod_changes, use_steam):
    $ mod_id = mod.id
    $ name = unicode(mod.name, "utf8")
    $ author = unicode(mod.author, "utf8")
    $ description = unicode(mod.desc, "utf8")
    $ url = mod.image_url

    if use_steam:
        $ _get_modfolder = _steam_get_modfolder
    else:
        $ _get_modfolder = _github_get_modfolder

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
                        action [Function(mod_changes.remove_mod, mod_id, _get_modfolder(str(mod_id), name)),
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
        frame xpos 1632 ypos 0.21 xsize 280 ysize 600:
            background "#0000009B"
            xpadding 15

            vbox xfill True ymaximum 600:
                text "Dependencies:" size 40

                for dep_id in mod_changes.get_mod_dependencies(mod_id):
                    python:
                        try:
                            dep_name = mod_changes.get_mod(dep_id).name

                            if mod_changes.is_mod_installed(dep_id):
                                dep_color = "#ffffffFF"
                            elif mod_changes.is_mod_added(dep_id):
                                dep_color = "#bfff00FF"
                            else:
                                dep_color = "#00ffbfFF"

                        except KeyError:
                            dep_name = "<Missing>"
                            dep_color = "#7f7f7fFF"

                    text dep_name:
                        size 20
                        color dep_color



transform _button_zoom:
    zoom 40.0 / 54.0


screen modmenu_apply_confirm(mod_changes, use_steam):
    modal True
    python:
        from modloader.modconfig import apply_mod_changes

        mods_to_install = mod_changes.get_added_mods()
        mods_to_uninstall = mod_changes.get_removed_mods()
        n_mods_to_install = len(mods_to_install)
        n_mods_to_uninstall = len(mods_to_uninstall)

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

            $ mods_to_add_text = "\n".join(mods_to_install.itervalues())
            $ mods_to_remove_text = "\n".join(modname for modname, _ in mods_to_uninstall.itervalues())

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

                    vpgrid id "_mod_add_list":
                        cols 1
                        xfill True
                        mousewheel "change"

                        for mod_id, mod_name in mods_to_install.iteritems():
                            hbox:
                                spacing 20
                                ysize 60

                                if not mod_changes.is_mod_dependency(mod_id):
                                    imagebutton:
                                        idle "image/ui/close_idle.png" at _button_zoom
                                        hover "image/ui/close_hover.png"
                                        yalign 0.5

                                        action Function(mod_changes.remove_mod, mod_id) # As mod is guaranteed to be in the add list, we only need id to remove.

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

                    vpgrid id "_mod_remove_list":
                        cols 1
                        xfill True
                        mousewheel "change"

                        for mod_id, (mod_name, _) in mods_to_uninstall.iteritems():
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
                action [Function(apply_mod_changes, add_modmap=mods_to_install, remove_modmap=mods_to_uninstall, show_status_screen=True, reload_script=True, use_steam=use_steam),]
                sensitive bool(n_mods_to_install) or bool(n_mods_to_uninstall)


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
