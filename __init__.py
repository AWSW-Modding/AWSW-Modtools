import renpy.parser
import renpy.ast as ast

from modloader import modast
from modloader.modclass import Mod, loadable_mod


@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Lorem's_better_date-Demo", "v0.1", "AdamJ1664")


    def mod_load(self):
        ### Leave comments with 3 '#' as comments, they are just for explanation.
        ### Bootstrap Setup.
        ### Really just dev testing your mod. This puts a button on your main menu which will short-cut you to your mod.
        Bootstap_label = "lbd_lorem1_bootstrap"                      ### <-- Enter the name of your bootstrap label
        main_menu_button = True                 ### <-- Set to "True" to show the button and set to "False" to hide the button


        ### Inject your mod code here
        ### Plug in 5 values and the result is:
        ### the game will jump from a set point to your code and then return to another set point

        jump_from_label = ""                    ### <-- In-game label you want to jump from
        jump_from_scene = 4                     ### <-- Scene of the label you want to jump from, represented as a number

        return_to_label = ""                    ### <-- In-game label you want to return to once your code is finished
        return_to_scene = 2                    ### <-- Scene of the label you want to return to, represented as a number

        startlabel_yourmod = ""                 ### <-- Beginning label of your mod


        ###\/\/\/\/\/You can ignore the stuff below \/\/\/\/\/













###--------------------------------------------------The label we are jumping from--------------------------------------------
        if not jump_from_label == "":
            ### This is the node of the label from the label name you entered above.
            ### We need this for hooking to the desired scene
            from_label_node = renpy.game.script.lookup(jump_from_label)

            ### This is for setting up the scene we are jumping from
            if not jump_from_scene == 0:
                ### If we are skipping any scenes

                from_scene_node = self.skip_scenes_up(from_label_node, jump_from_scene, 1)


            else:
                ### if we are not skipping scenes
                ### Often this will start near the beginning of the label after the game set's the savefile name

                from_scene_node = modast.search_for_node_type(from_label_node, ast.Scene, 100)

                #If no scene is found a search is done for any node at the start of the label
                if from_scene_node == None:
                    from_scene_node = modast.search_for_node_type(return_label_node, ast.Node, 200)

###--------------------------------------------------The label we are returning to -----------------------------------------------
        if not return_to_label == "":
            ### This is the node of the label from the label name you entered above.
            ### We need this for hooking to the desired scene
            return_label_node = renpy.game.script.lookup(return_to_label)


            ### This is for setting up the scene we are returning to
            if not return_to_scene == 0:
                ### If we are skipping any scenes

                return_scene_node = self.skip_scenes(return_label_node, return_to_scene)

            else:
                ### if we are not skipping scenes
                ### Often this will start near the beginning of the label after the game set's the savefile name

                return_scene_node = modast.search_for_node_type(return_label_node, ast.Scene, 100)

                #If no scene is found a search is done for any node at the start of the label
                if return_scene_node == None:
                    return_scene_node = modast.search_for_node_type(return_label_node, ast.Node, 200)

###--------------------------------------------------The label of your mod we are jumping to -------------------------------------
        if not startlabel_yourmod == "":
            mod_label_node = renpy.game.script.lookup(startlabel_yourmod)


###--------------------------------------------------Calling our code ------------------------------------------------------------
        if jump_from_label != "" and return_to_label != "" and startlabel_yourmod != "" :
            modast.call_hook(from_scene_node, mod_label_node, None, return_scene_node)

        elif jump_from_label != "" and startlabel_yourmod != "" :
            modast.call_hook(from_scene_node, mod_label_node, None)

        ###------------------------------------------From documentation ----------------------------------------------------------
             ###https://scrlys.github.io/AWSW-Modtools/_modules/modloader/modast.html#call_hook

###--------------------------------------------------Our code to put the "my mod" button on the main menu ------------------------
        if main_menu_button:
            rpyCode =  'screen mainmenubutton_mymod:\n'\
                        '    imagebutton '\
                                'xalign 0.95 '\
                                'yalign 0.88611111 '\
                                'idle "ui/lbd_demo_btn_idle.png" '\
                                'hover "ui/lbd_demo_btn_hover.png" '\
                                'selected "ui/lbd_demo_btn_hover.png" '\
                                'action [Start("' + Bootstap_label + '"), Play("audio", "se/sounds/open.wav")] '\
                                'hovered Play("audio", "se/sounds/select.ogg") '

            rv = renpy.parser.parse("RPDummy", rpyCode)

            targetDisp = None
            for e in rv:
                if isinstance(e, renpy.ast.Init):
                    targetDisp = e.block[0].screen.children[0]

            modast.get_slscreen("main_menu").children.append(targetDisp)


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

    def skip_scenes_up(self, node, skip, num_back, max_search=10000):
        skipped = 0
        pre = [None] * num_back
        counter = 0

        for _ in range(1, max_search):
            pre[counter] = node
            counter = counter + 1

            if counter == num_back:
                counter = 0

            node = node.next

            if node and isinstance(node, ast.Scene):
                if skipped == (skip - 1):
                    return pre[0]

                skipped += 1

        return None

    def skip_scenes_up_1(self, node, skip, max_search=10000):
        skipped = 0
        #pre = ""

        for _ in range(1, max_search):
            pre = node
            node = node.next

            if node and isinstance(node, ast.Scene):
                if skipped == (skip - 1):
                    return pre

                skipped += 1

        return None
