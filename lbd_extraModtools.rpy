init python:
    from modloader import modinfo

    def is_koth_mod_db():
        if (renpy.python.store_dicts["store"].get("lbd_dev_debug", False) == True):
            return (mts_yes_no_prompt("(Debug) Is the koth mod installed?"))

        else:
            for mod_name in modinfo.modlist:
                if mod_name == "Kothorix_mod":
                    return True

            return False

    def is_koth_mod():
        for mod_name in modinfo.modlist:
            if mod_name == "Kothorix_mod":
                return True

        return False

    def bldfrombootstrap():
        store = renpy.python.store_dicts["store"]
        if "bldfrombootstrap" in store:
            return True

        return False
