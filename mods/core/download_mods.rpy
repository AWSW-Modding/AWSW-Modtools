screen modmenu_download:
    modal True

    window id "modmenu_download" at alpha_dissolve:
        style "nvl_window"

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

        style.download_mods = Style(style.default)

        # (modid, name, author, description, image
        from modloader.modconfig import github_downloadable_mods
        contents = github_downloadable_mods()

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

    window id "close":
        style "download_mods"
        imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Hide("modmenu_download", transition=dissolve), Play("audio", "se/sounds/close.ogg"), Show("modmenu")] hovered Play("audio", "se/sounds/select.ogg", Show("modmenu"))



screen modmenu_install_confirm(modid, modname) tag smallscreen2:
    modal True
    python:
        from modloader.modconfig import download_github_mod

    window id "modmenu_install_confirm" at popup2:
        style "alertwindow"

        hbox xalign 0.5 yalign 0.8:
            spacing 250
            textbutton "Yes" action [Hide("modmenu_install_confirm"), Play("audio", "se/sounds/close.ogg"), lambda download_github_mod=download_github_mod, modname=modname, modid=modid: download_github_mod(modname, modid), Show("modmenu_download")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"
            textbutton "No" action [Hide("modmenu_install_confirm"), Show("modmenu_download"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "yesnobutton"

        label "Are you sure you want to install [modname]?":
            style "yesno_prompt"
            text_style "yesno_prompt_text"
