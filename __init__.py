from modloader import modinfo, modast
from modloader.modclass import Mod, loadable_mod
import renpy.parser as parser
import renpy.ast as ast

@loadable_mod
class AWSWMod(Mod):
    @staticmethod
    def mod_info():
        """Get the mod info
        Returns: a three element tuple containing the mod name, version and description
        """
        return ("FPS Counter", "v1.0", "muddyfish")

    @staticmethod
    def mod_load():

        # Initialise the FPS counter and show it during the splashscreen
        from_label_node = modast.find_label("splashscreen")
        fps_counter_label = modast.find_label("fix_fps")
        modast.call_hook(from_label_node, fps_counter_label, None)

        # It would get automatically hidden at the main menu normally
        # Re-enable it whenever the main menu is shown
        tocompile = """
        screen mainmenu_fps:
            python:
                store.suppress_overlay = False
        """

        compiled = parser.parse("FPSCounter", tocompile)
        target_display = None
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    target_display = child

        modast.get_slscreen('main_menu').children.append(target_display)

    @staticmethod
    def mod_complete():
        pass