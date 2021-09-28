"""This file is free software under the MIT license"""
from modloader import modinfo


class Mod(object):
    """The Mod class

    This is supposed to act like a superclass for mods.
    Execution order is as follows:
    :meth:`mod_load` -> :meth:`mod_complete`
    """
    
    def __init__(self):
        """Forwards compatibity between mod_info function and class attributes"""
        
        cls = self.__class__
        
        # check if the class doesn't override mod_info
        if cls.mod_info == Mod.mod_info:
            # check mandatory attributes
            if not hasattr(cls, "name"):
                raise Exception("Mod must specify the class attribute `name`.")
            if not hasattr(cls, "version"):
                raise Exception("Mod must specify the class attribute `version`.")
            if not hasattr(cls, "author"):
                raise Exception("Mod must specify the class attribute `author`.")
            if not hasattr(cls, "nsfw"):
                cls.nsfw = False
            if not hasattr(cls, "dependencies"):
                cls.dependencies = []
        else:
            # cannot have both mod_info and class attributes
            if hasattr(cls, "name"):
                raise Exception("Mod name can only be defined either by class attribute or mod_info function, not both.")
            if hasattr(cls, "version"):
                raise Exception("Mod version can only be defined either by class attribute or mod_info function, not both.")
            if hasattr(cls, "author"):
                raise Exception("Mod author can only be defined either by class attribute or mod_info function, not both.")
            if hasattr(cls, "nsfw"):
                raise Exception("Mod nsfw tag can only be defined either by class attribute or mod_info function, not both.")
            
            # set class attributes from mod_info
            mi = self.mod_info()
            cls.name = mi[0]
            cls.version = mi[1]
            cls.author = mi[2]
            cls.nsfw = mi[3] if len(mi) >= 4 else False
            cls.dependencies = []
        
        # check if class attributes have valid types
        assert isinstance(cls.name, (str, unicode))
        assert isinstance(cls.version, (str, unicode))
        assert isinstance(cls.author, (str, unicode))
        assert isinstance(cls.nsfw, bool)
        assert isinstance(cls.dependencies, (list, tuple))
        
    def mod_info(self):
        """Get the mod info
        
        Mod class has to either override this function or contain class attributes `name`, `version`, `author` and optionally `nsfw`.

        Returns:
            A tuple with the name, version, author, and (optionally) if the mod is NSFW
        """
        return (self.name, self.version, self.author, getattr(self.__class__, "nsfw", False))

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
