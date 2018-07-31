init python:
    if renpy.windows:
        import sys
        reload_mods = "modloader" in sys.modules
        import modloader
        modloader.main(reload_mods=reload_mods)