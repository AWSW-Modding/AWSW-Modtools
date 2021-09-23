"""This file is free software under the MIT license"""
from modloader import modinfo


class Mod(object):
    """The Mod class

    This is supposed to act like a superclass for mods.
    Execution order is as follows:
    :meth:`mod_load` -> :meth:`mod_complete`
    """
    def mod_info(self):
        """Get the mod info
        
        Mod class has to either override this function or contain class attributes `name`, `version`, `author` and optionally `nsfw`.

        Returns:
            A tuple with the name, version, author, and (optionally) if the mod is NSFW
        """
        return (self.name, self.version, self.author, self.nsfw if hasattr(self.__class__, "nsfw") else False)

    def mod_load(self):
        """Executes when the mod is loaded

        This is where you put patcher code.

        See Also:
            :meth:`mod_complete`
        """
        raise NotImplementedError("Mod load isn't overriden")

    def mod_complete(self):
        """Executes when all mods are loaded

        This method is useful for dependency loading but can be left empty otherwise
        """
        raise NotImplementedError("Mod complete isn't overriden")


def loadable_mod(modclass):
    """Annotation to add a Mod subclass to the mod list

    Args:
        modclass (Mod): The Mod class, not an instance of the Mod class

    Raises:
        Exception: If the given class is not a subclass of Mod
    """
    if not issubclass(modclass, Mod):
        raise Exception("Class must be a subclass of Mod")

    mod = modclass()

    modinfo.add_mod(mod.mod_info()[0], mod)
