import renpy.parser
import renpy.ast as ast
import renpy

from modloader import modast
from modloader.modclass import Mod, loadable_mod


@loadable_mod
class AWSWMod(Mod):

    def mod_info(self):
        return ("rename_MC", "v1.0", "AdamJ1664")


    def mod_load(self):

        enable = False
        enable = True

        if enable:
            rpyCode =  'screen mainmenubutton_mymod:\n'\
                        '    imagebutton '\
                                'xpos 70 '\
                                'ypos 115 '\
                                'auto "ui/rnmc_%s.png" '\
                                'action [Start("start_mod_rnmc"), Play("audio", "se/sounds/open.wav")] '\
                                'hovered Play("audio", "se/sounds/select.ogg") '\
                                'at RNMC_title_slide'


            rv = renpy.parser.parse("RPDummy", rpyCode)

            targetDisp = None
            for e in rv:
                if isinstance(e, renpy.ast.Init):
                    targetDisp = e.block[0].screen.children[0]

            modast.get_slscreen("preferences").children.append(targetDisp)

    def mod_complete(self):
        pass


###------Our custom method for skipping a certain number of scenes
    def skip_scenes(self, node, skip, max_search=10000):
        skipped = 0

        for _ in range(1, max_search):
            node = node.next

            if node and isinstance(node, ast.Scene):
                if skipped == (skip - 1):
                    return node

                skipped += 1

        return None

    def skip_scenes_node_num(self, node, skip, num_back, max_search=10000):
        skipped = 0
        pre = [None] * num_back
        counter = 0
        looped = False

        for _ in range(1, max_search):
            pre[counter] = node
            counter += 1

            if counter == num_back:
                counter = 0
                looped = True

            node = node.next

            if node and isinstance(node, ast.Scene):
                if skipped == (skip - 1):
                    if looped:
                    	if counter + 1 == num_back:
                    		return pre[0]
                    	else:
                    		return pre[counter]
                    else:
                    	return pre[counter]

                    return pre[0]

                skipped += 1

        return None

    def skip_scenes_node_one(self, node, skip, max_search=10000):
        skipped = 0

        for _ in range(1, max_search):
            pre = node
            node = node.next

            if node and isinstance(node, ast.Scene):
                if skipped == (skip - 1):
                    return pre

                skipped += 1

        return None
