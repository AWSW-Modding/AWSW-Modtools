screen modmenu_download:
    modal True

    window id "modmenu_download" at alpha_dissolve:
        style "nvl_window"
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("modmenu_download", transition=dissolve), Play("audio", "se/sounds/close.ogg"), Show("modmenu")] hovered Play("audio", "se/sounds/select.ogg", Show("modmenu")) xalign 1.1 yalign -0.1 at nav_button

    python:
        from renpy.display.im import Image
        from renpy.ui import Wrapper

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

                return surf

            def predict_files(self):
                    return [self.url]
        ImageURL = Wrapper(ImageURL)

        # (modid, name, author, description, image

        contents = [(123, "Test mod", "muddyfish", "A test mod with an extremely long, multiline description. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", "http://s-media-cache-ak0.pinimg.com/originals/42/41/90/424190c7f88c514a1c26a79572d61191.png") for i in range(10)]

    vpgrid:

        rows 1
        spacing 32
        draggable True
        mousewheel True

        scrollbars "horizontal"

        # Since we have scrollbars, we have to position the side, rather
        # than the vpgrid proper.
        side_yalign 0.5

        for modid, name, author, description, url in contents:
            vbox:
                xmaximum 500
                yminimum 600
                python:
                    ImageURL(url)
                text name
                text author
                textbutton "Install" action [Show("modmenu_install_confirm", modid=modid, modname=name), Play("audio", "se/sounds/open.ogg")] hovered Play("audio", "se/sounds/select.ogg")
                text description size 24



screen modmenu_install_confirm(modid, modname) tag smallscreen2:
    modal True

    window id "modmenu_install_confirm" at popup2:
        style "alertwindow"

        hbox xalign 0.5 yalign 0.8:
            spacing 250
            textbutton "Yes" action [Hide("modmenu_install_confirm"), Play("audio", "se/sounds/close.ogg"), Show("modmenu_download")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
            textbutton "No" action [Hide("modmenu_install_confirm"), Show("modmenu_download"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"

        label "Are you sure you want to install [modname]?":
            style "yesno_prompt"
            text_style "yesno_prompt_text"
