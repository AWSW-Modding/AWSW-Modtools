import modinfo

class Mod():
    """The Mod class

    This is supposed to act like a superclass for mods.
    Execution order is as follows:
    mod_load -> mod_complete
    """
    def mod_info(self):
        """Get the mod info

        Returns:
            A tuple with the name, version, and author
        """
        raise Exception("Mod info isn't overriden")

    def mod_load(self):
        """Executes when a mod is loaded

        This is where you put special renpy code
        Other mods may not be fully loaded yet. If you want this functionality, see mod_complete
        """
        pass

    def mod_complete(self):
        """Executes when all mods are loaded"""
        pass

def loadable_mod(clazz):
    """Annotation to add a Mod subclass to the mod list

    Args:
        clazz (Mod): The Mod class

    Raises:
        Exception: If the given class is not a subclass of Mod
    """
    if not issubclass(clazz, Mod):
        raise Exception("Class must be a subclass of Mod")

    mod = clazz() # Create a new instance of the class
    mod_name, _, _ = mod.mod_info() # Get just the mod name
    mod.mod_load() # Load the mod
    modinfo.add_mod(mod_name, mod)
