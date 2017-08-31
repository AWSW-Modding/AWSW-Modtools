init python:
    import modloader
    # Is true when reloading
    if renpy.loader.old_config_archives:
        modloader.main(reload_mods=True)