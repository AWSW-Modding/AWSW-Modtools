import modinfo

class Mod():
    """The Mod class

    This is supposed to act like a superclass for mods.
    """
    def mod_info(self):
        """Get the mod info

        Returns:
            A tuple with the name, version, and author
        """
        raise Exception("Mod info isn't overriden")

def loadable_mod(clazz):
    """Annotation to add a Mod subclass to the mod list

    Args:
        clazz (Mod): The Mod class
    """
    mod = clazz() # Create a new instance of the class
    modinfo.add_mod(mod.mod_info()[0], mod)
