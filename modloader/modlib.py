"""The modding library.

This file contains all the functions needed to modify and extend AwSW.

This file is free software under the GPLv3 license.
"""
import renpy
import renpy.ast as ast
import renpy.python
import os
import string

import modloader

def imports():
    # Unfortunately importing renpy.sl2.slast is impractical because
    # it eventually tries to import a Cython-compiled file.
    global slast
    import renpy.sl2.slast as slast

if not modloader.building_documentation:
    imports()

def sprnt(string):
    """Print an encoded string to stdout

    This function is not like your standard print function. Rather, it encodes the string in UTF-8 to avoid Unicode errors

    Args:
        string (str): The string to be printed
    """
    print(string.encode('utf-8'))

rot13_dec = string.maketrans( 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

class ASTHook(ast.Node): # Don't instantiate ASTHook directly. Ren'py assigns a serial number to each node which is used internally for the call stack and other things. We emulate that functionality in the base class. 
    """A custom :class:`renpy.ast.Node` that acts as a hook between other node objects.

    Note:
        Don't instantiate this class directly. Ren'Py uses an internal serial for the call stack and other uses. This class emulates that at the base class.

    Attributes:
        hook_func: A function that's called when the node is executed. If the function returns a non-None value, the next node will be skipped.
    """

    def execute(self):
        ast.statement_name("hook")
        ret = None
        if self.hook_func:
            ret = self.hook_func(self)
        if not ret:
            self.exec_continue()

    def exec_continue(self):
        ast.next_node(self.next)

    def unhook(self):
        self.fromOp.next = self.__oldNext

class AWSWEndingHooks():
    """The ending hooks for the game.
    """

    def __init__(self, base):
        """Initialize a new ending hook class

        This function is also responsible for finding the true-ending post-Izumi node

        Args:
            base (AWSWModBase): An instance of the AWSWModBase class
        """
        self.base = base
        searchStr = string.translate("Fur pybfrq ure rlrf nf n fvatyr grne ena qbja ure snpr. V zbirq gb jvcr vg sebz ure, naq pbhyq nyernql srry gur jnezgu qenvavat sebz Vmhzv'f obql. Fur jnf qrnq.", rot13_dec)
        self.TrueEndingPostIzumi = self.base.findSay(searchStr)

    def getPostTrueEndingIzumiScene(self):
        """Get the post-true Izumi's tear scene

        Returns:
            A :class:`renpy.ast.Say` node object.
        """
        return self.TrueEndingPostIzumi

    def hookPostTrueEnding(self, node):
        """Hook ``node`` to the post-true ending node

        Returns:
            An :class:`ASTHook` instance
        """
        fincall = self.getPostTrueEndingIzumiScene().next
        return self.base.call_hook(fincall, node)

    def hookPostEvilEnding(self, node):
        """Hook ``node`` to the post-evil ending node

        Todo:
            Program this.
        """
        return None

    def hookRouteEnding(self, route):
        # What is this function?
        return None

    def getEndingPickerMenu(self):
        """Get Chapter 5's menu on who to go to the fireworks.

        Get an instance of :class:`AWSWMenuHooks` for use of making new choices on who to go to the festival with.

        Returns:
            An instance of :class:`AWSWMenuHooks`
        """
        ch5 = ml.findlabel("chapter5")
        menu_node = self.base.searchPostNode(ch5, ast.Menu, 500)
        menu_hooks = self.base.getMenuHook(menu_node)

        return menu_hooks


class AWSWMenuHook():
    """A hook class for editing a specific menu
    """

    def __init__(self, menu, base):
        """Make a hook class for the specific ``menu`` object

        Args:
            menu (renpy.ast.Menu): The Menu node to be hooked
            base (AWSWModBase): An instance of the mod base class
        """
        if not isinstance(menu, ast.Menu):
            raise AssertionError("MenuHook not instantiated with a Menu node!")

        self.menu = menu
        self.base = base
        self.oldItems = menu.items[:]

    def deleteItem(self, item):
        # TODO: Describe what the hell is happening here.
        self.getItems()[:] = [(lab, cond, block) for i, (lab, cond, block) in enumerate(self.getItems()) if lab != item]
        return None

    def getItem(self, item):
        for obj in self.getItems():
            if obj[0] == item:
                return obj

    def getOptionCode(self, item):
        obj = self.getItem(item)
        return obj[2]

    def getItems(self):
        return self.menu.items

    def setConditional(self, item, newCond):
        for i, (lab, cond, block) in enumerate(self.getItems()):
            if lab == item:
                self.menu.items[i] = (lab, newCond, block)
                return True
        return False

    def addItem(self, label, hook, condition="True"):
        if isinstance(hook, ast.Node):
            self.getItems().append((label, condition, [hook])) # Adding a dialogue option.
            return None
        else:
            node = ASTHook(("AWSWMod", 1))
            node.fromOp = self.menu
            node.hook_func = hook
            node.name = "AWSWModOp_" + str(self.base.nameSerial)
            self.base.nameSerial += 1
            self.getItems().append((label, condition, [node]))
            return node

    def addItemCall(self, label, usr_hook, condition="True"):
        hook = self.addItem(label, None, condition)

        def call_func(hook):
            rv = renpy.game.context().call(usr_hook.name, return_site=self.menu.next.name)
            hook.chain(rv)

        hook.hook_func = call_func

class AWSWHomeHook():
    """Hook the menu found in the player's apartment.
    """

    def __init__(self, base):
        """Hook the hooks in the appropriate places.

        Args:
            base (AWSWModBase): An instance of the mod base class
        """
        self.base = base
        self.hooks = []

        altMenuLabs = ["chap2altmenua1", "chap2altmenub1", "chap3altmenua1", "chap3altmenub1", "chap4altmenua1", "chap4altmenub1"]
        self.altMenus = [] # I'm not sure what I want to do about this yet.
        for lab in altMenuLabs:
            self.altMenus.append(base.findlabel(lab).next)

        chmenus = base.findMenu(["Meet with Bryce."]) # Choice was 100% unbiased thanks
        chmenus[:] = [node for node in chmenus if node not in self.altMenus]
        self.ChapterMenus = chmenus



        stmts = renpy.game.script.all_stmts

        for node in stmts:
            if isinstance(node, ast.Python) and node.code.source == "brycebar = False":
                self.CH1Hook = node

        answToHook = ["chapter2chars", "chapter3chars", "chapter4chars"]
        closure_val = ""
        def nodeCB(node):
            if isinstance(node, ast.Python) and node.code.source == closure_val:
                return True

        self.InitAnswPoints = []
        for lab in answToHook:
            closure_val = "playmessage = False"
            labNode = base.findlabel(lab)
            hkPt = base.searchPostNodeCB(labNode, nodeCB)
            base.call_hook(hkPt, base.findlabel('_mod_fixansw')) # New mods will be inserted BEFORE this node, so we'll be alright. 
            closure_val = "remyavailable = True"
            hkPt2 = base.searchPostNodeCB(labNode, nodeCB)

            self.InitAnswPoints.append((hkPt, hkPt2))

    def addAnswerMachineCheckHook(self, dest_node):
        """Change the answering machine's output.

        Return true if the dialog should pop up and return false if it shouldn't.

        Args:
            dest_node: Can be either a :class:`renpy.ast.Node` or a function.
        """
        if isinstance(dest_node, ast.Node):
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.call_hook(hkPt, dest_node)
        else:
            for (hkPt, hkPt2) in self.InitAnswPoints:
               def det_func(hook):
                    ret = False
                    if dest_node:
                        ret = dest_node(hook)
                    if ret:
                        self.base.setRGlobal('playmessage', True)

               hook = self.hook_opcode(hkPt, dest_node)

    def addAnswerMachineScene(self, dest_node):
        """Add a hook before the answering machine plays

        Args:
            dest_node: Can be either a :class:`renpy.ast.Node` or a function. Called after the machine check returns true
        """
        if isinstance(dest_node, ast.Node):
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.call_hook(hkPt2, dest_node)
        else:
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.hook_opcode(hkPt2, dest_node)

    def addRoute(self, title, routeHook, condition="True"):
        """Add a route to the chapter menu

        The route will only appear if the condition evaluate to true.

        Args:
            title (str): The human-readable menu option
            routeHook (Node): The :class:`renpy.ast.Node` object to change to
            condition (str): The Python string to evaluate if the option should appear
        """
        for menu in self.ChapterMenus:
            hook = self.base.getMenuHook(menu)
            self.hooks.append(hook)
            hook2 = hook.addItem(title, None, condition)

            def call_func(hook):
                rv = renpy.game.context().call(routeHook.name, return_site=self.base.findlabel('_mod_fixjmp').name)
                hook.chain(rv)
            hook2.hook_func = call_func


    def hookChapterChange(self, hook):
        """Hook a change of the chapters

        Args:
            hook: A :class:`renpy.ast.Node` object or function
        """
        chapterLabs = ["chapter2", "chapter3", "chapter4"]

        if isinstance(hook, ast.Node):
            for lab in chapterLabs:
                self.base.call_hook(base.findlabel(lab), hook, None)

            self.base.call_hook(self.CH1Hook, hook, None)
        else:
            for lab in chapterLabs:
                def ch_id(hook2):
                    if hook:
                        hook(hook2, lab)
                self.base.hooklabel(lab, ch_id)

            def ch_id(hook2):
                if hook:
                    hook(hook2, lab)

            self.base.hook_opcode(self.CH1Hook, ch_id)

    def hookChapter1(self, hook):
        """Hook a node to the start of Chapter 1

        Args:
            hook (Node): The node to hook
        """
        self.base.call_hook(self.CH1Hook, hook)


class AWSWModBase:
    """The modding framework base.

    This class contains all the base functions needed to edit the AST, screens, and screen language.

    Attributes:
        endingHooks (AWSWEndingHooks): An instance of the :class:`AWSWEndingHooks`.
        homeHook (AWSWHomeHook): An instance of the :class:`AWSWHOmeHook`
    """

    def __init__(self):
        self.endingHooks = AWSWEndingHooks(self)
        self.nameSerial = 1
        self.homeHook = AWSWHomeHook(self)

    def getscreen(self, scr):
        """Get a screen based off of its name

        Args:
            scr (str): The screen's name

        Returns:
            A :class:`renpy.display.screen.Screen` object
        """
        return renpy.display.screen.get_screen_variant(scr) # Returns renpy.display.screen.Screen object

    def getsls(self, scr):
        """Get the SLScreen based off of its name

        Args:
            scr (str): The screen's name

        Returns:
            A :class:`renpy.sl2.slast.SLScreen` object
        """
        return self.getscreen(scr).ast

    def findlabel(self, lab):
        """Find a label based off of its name

        Args:
            lab (str): The label's name

        Returns:
            A :class:`renpy.ast.Label` object
        """
        return renpy.game.script.lookup(lab)

    def hook_opcode(self, node, func):
        """Hook ``func`` to ``node``

        Args:
            node (Node): The node object for the function to hook
            func (function): The function to be executed when the node is executed

        Todo:
            Check if a hook already exists and make the code more cohesive

        Returns:
            An :class:`ASTHook` object
        """
        next_statement = node.next

        hook = ASTHook(("AWSWMod", 1)) # hooking hooks breaks
        hook.fromOp = node
        node.next = hook
        hook.chain(next_statement)
        hook.__oldNext = next_statement
        hook.hook_func = func
        hook.name = "AWSWModOp_" + str(self.nameSerial)
        self.nameSerial += 1
        renpy.game.script.namemap[hook.name] = hook

        return hook

    def jump_ret(self, node, dest_node, ret_node, func=None):
        """Hook ``func`` to ``node`` and once executed, redirect execution to
            ``dest_node`` and allow ``ret_node`` to be executed after
            ``dest_node`` returns.

        Args:
            node (Node): The node to hook
            dest_node (Node): The node to go after ``node`` is executed
            ret_node (Node): The node that is executed after ``dest_node`` returns
            func (function): The function hook

        Returns:
            An :class:`ASTHook` object
        """
        hook = self.call_hook(node, dest_node, func)
        hook.next = ret_node
        return hook

    def call_hook(self, node, dest_node, func=None):
        """Hook ``func`` to ``node`` and once executed, redirect execution to
            ``dest_node``

        Args:
            node (Node): The node to hook
            dest_node (Node): The node to go after ``node`` is executed
            func (function): The function hook

        Returns:
            An :class:`ASTHook` object
        """
        hook = self.hook_opcode(node, None)
        def call_func(hook):
            if func:
                func(hook)
            rv = renpy.game.context().call(dest_node.name, return_site=hook.__oldNext.name)
            hook.chain(rv)


        hook.hook_func = call_func
        return hook

    def hooklabel(self, lab, func):
        """Hook a function to a label

        Args:
            lab (renpy.ast.Label): The label
            func (function): The function to be hooked

        Returns:
            An :class:`ASTHook` object
        """
        ASTLabel = self.findlabel(lab)
        return self.hook_opcode(ASTLabel, func)

    def unhooklabel(self, lab):
        """Unhook hooks from a label

        Args:
            lab (str): The label's name
        """
        found_node = self.findlabel(lab)
        if isinstance(found_node, ASTHook):
            found_node.fromOp.next = found_node.next

    def searchPostNode(self, node, type, maxBeforeFailure=200):
        """Search for a specific type of node.

        Args:
            node (Node): The node to start the search
            type (Node): The node *class*, not an instance of a class, to search for
            maxBeforeFailure (int): The number of nodes to search before giving up
        """

        for i in range(1,maxBeforeFailure): # Search 200 opcodes by default now. we don't want to exhaust resources by searching the entire tree.
            node = node.next
            if node:
                if isinstance(node, type):
                    return node

            else:
                return None

    def searchPostNodeCB(self, node, func, maxBeforeFailure=200):
        # TODO: What does CB stand for?
        for i in range(1,maxBeforeFailure):
            node = node.next
            if node:
                ret = func(node)
                if ret:
                    return node
            else:
                return None

    def DisableSCache(self):
        """Disable SLAst's load cache
        """
        #TODO: Rename function
        def remove_s_cache():
            return
        renpy.sl2.slast.load_cache = remove_s_cache

    def DisableBCache(self):
        """Disable bytecode cache
        """
        #TODO: Rename function
        def remove_b_cache():
            return
        renpy.game.script.init_bytecode = remove_b_cache

    def nullPyexpr(self, scr, comp):
        """Remove an if statement and its branches

        Args:
            scr (Screen): The screen object to iterate over
            comp (str): String comparison for
        """
        for i in scr.children:
            if isinstance(i, slast.SLIf):
                for cond, block in i.entries:
                    if cond == comp:
                        block.children = []
                        return True
        return False

    def hookScreen(self, scr):
        #TODO: Determine usage
        scrObj = self.getscreen(scr)
        return None

    def findMenu(self, needle):
        """Find a menu based off of a menu choice

        This searches the entire AST tree to find the menu choice. If it still cannot find it, it returns None

        Args:
            needle (str): The menu choice to look for

        Returns:
            A list of menus.
        """
        stmts = renpy.game.script.all_stmts
        multiSearch = False
        if isinstance(needle, list):
            multiSearch = True

        needle2 = None
        retlist = []
        for node in stmts:
            if isinstance(node, ast.Menu):
                if multiSearch:
                    needle2 = needle[:]
                for i, (label, condition, block) in enumerate(node.items):
                    if multiSearch:
                        for stri in needle2:
                            if stri == label:
                                needle2.remove(stri)
                        if len(needle2) == 0:
                            retlist.append(node)
                    elif label == needle:
                        retlist.append(node)
        return list(set(retlist))

    def findSay(self, needle): # Searches the entire AST for a say statement.
        """Find a :class:`renpy.ast.Say` node based on what is said

        This searches the entire AST tree for the specified statement.
        If none is found the function returns None.

        Args:
            needle (str): The said statement

        Returns:
            A :class:`renpy.ast.Node` node.
        """
        stmts = renpy.game.script.all_stmts

        for node in stmts:
            if isinstance(node, ast.Say) and node.what == needle:
                return node

        return None

    def addMenuOption(self, menu, option, node):
        """Add a dialog option to a given menu

        Args:
            menu (Menu): A menu to append the option
            option (str): The option name to add to the menu
            node (Node): The node to execute after
        """
        menu.items.append((option, "True", [node])) # Adding a dialogue option.
        return None

    def getMenuHook(self, menu):
        return AWSWMenuHook(menu, base)

    def getHomeHook(self):
        return self.homeHook

    def stepOp(self, node, num):
        """Get the ``num`` nodes after ``node``

        Note:
            This skips :class:`ASTHook` nodes

        Args:
            node (Node): The node to start searching from
            num (int): The number of nodes to skip

        Returns:
            A :class:`renpy.ast.Node` object
        """
        for i in range(0, num):
            node = node.next
            while(node and isinstance(node, ASTHook)):
                node = node.next
        return node

    def setRGlobal(self, key, val):
        """Set a Ren'Py global

        Ren'Py globals can be used during execution of rpy.

        Args:
            key (str): The dictionary key
            val: The value of the dictionary object
        """
        #TODO: Rename this function
        renpy.python.store_dicts["store"][key] = val

    def getRGlobal(self, key):
        """Get a Ren'Py global

        Args:
            key (str): The dictionary key

        Returns:
            The value put into the key or None if it doesn't exist
        """
        #TODO: Rename this function
        store = renpy.python.store_dicts["store"]
        if key in store:
            return store[key]

    def findByLineNumber(self, ln, file):
        """Find a node by line number and file

        Note:
            Due to the fact that line numbers can change between versions, this only should be used as a last resort.

        Args:
            ln (int): The line number
            file (str): The file name

        Returns:
            The node or None if it doesn't meet the criteria provided
        """
        stmts = renpy.game.script.all_stmts

        for node in stmts:
            base, nfile = os.path.split(node.filename)
            nf = nfile or os.path.basename(base)
            if node.linenumber == ln and nf == file:
                return node
        return None

    def getEndingHooks(self):
        return self.endingHooks

    def searchPeakIf(self, node, type, maxBeforeFailure=200, skip=0):
        """Search recursively for a node type.

        This enters if statement blocks in order to find your specified node type

        Args:
            node (Node): The starting node
            type (Node): A *subclass*, not an instance, of a :class:`renpy.ast.Node` object
            maxBeforeFailure (int): How many nodes to iterate through before giving up

        Returns:
            A :class:`renpy.ast.Node` object or None if not found
        """
        for i in range(1,maxBeforeFailure):
            if node:
                if isinstance(node, ast.If):
                    for condition, block in node.entries:
                        if block and skip <= 0:
                            skip -= 1
                            cand = self.searchPeakIf(block[0], type, 20)
                            if cand:
                                return cand

                        else:
                            skip -= 1


                elif isinstance(node, type):
                    return node

            else:
                return None
            node = node.next

    def findPyStatement(self, code):
        """Find a specific Python node in the entire AST

        Args:
            code (str): The Python code to search for

        Returns:
            The Python node
        """
        stmts = renpy.game.script.all_stmts

        for node in stmts:
            if isinstance(node, ast.Python) and node.code.source == code:
                return node

if not modloader.building_documentation:
    base = AWSWModBase()
