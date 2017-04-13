"""The modding library.

This file contains all the functions needed to modify and extend AwSW.

This file is free software under the GPLv3 license.
"""
import string

import renpy
import renpy.python
from renpy import ast

import modloader
from modloader import modast

ROT13 = string.maketrans(
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")


def sprnt(str_):
    """Print an encoded string to stdout

    Encode the string in UTF-8 before printing it out to stdout
    This helps avoid Unicode errors

    Args:
        string (str): The string to be printed
    """
    print str_.encode('utf-8')

class AWSWEndingHooks(object):
    """The ending hooks for the game"""

    def __init__(self, base_):
        """Initialize a new ending hook class

        This function is also responsible for finding the true-ending post-Izumi node

        Args:
            base_ (AWSWModBase): An instance of the AWSWModBase class
        """
        self.base = base_
        # pylint: disable=line-too-long
        search_str = string.translate("Fur pybfrq ure rlrf nf n fvatyr grne ena qbja ure snpr. V zbirq gb jvcr vg sebz ure, naq pbhyq nyernql srry gur jnezgu qenvavat sebz Vmhzv'f obql. Fur jnf qrnq.", ROT13)
        self.post_izumi_node = modast.find_say(search_str)

    def get_post_izumi_node(self):
        """Get the post-true Izumi's tear scene

        Returns:
            A :class:`renpy.ast.Say` node object.
        """
        return self.post_izumi_node

    def hook_post_true_ending(self, node):
        """Hook ``node`` to the post-true ending node

        Returns:
            An :class:`ASTHook` instance
        """
        fincall = self.get_post_izumi_node().next
        return self.base.call_hook(fincall, node)

    def hook_post_evil_ending(self, node):
        """Hook ``node`` to the post-evil ending node

        Todo:
            Program this.
        """
        # pylint: disable=unused-argument, no-self-use
        return None

    def hook_route_ending(self, route):
        # What is this function?
        # pylint: disable=missing-docstring, no-self-use, unused-argument
        return None

    def get_ending_picker_menu(self):
        """Get Chapter 5's menu on who to go to the fireworks.

        Get an instance of :class:`AWSWMenuHooks` for use of making
        new choices on who to go to the festival with.

        Returns:
            An instance of :class:`AWSWMenuHooks`
        """
        ch5 = self.base.findlabel("chapter5")
        menu_node = self.base.searchPostNode(ch5, ast.Menu, 500)
        menu_hooks = self.base.get_menu_hook(menu_node)

        return menu_hooks


class AWSWHomeHook(object):
    """Hook the menu found in the player's apartment."""

    def __init__(self, base_):
        """Hook the hooks in the appropriate places.

        Args:
            base_ (AWSWModBase): An instance of the mod base class
        """
        self.base = base_
        self.hooks = []

        alt_menu_labels = ["chap2altmenua1", "chap2altmenub1", "chap3altmenua1",
                           "chap3altmenub1", "chap4altmenua1", "chap4altmenub1"]
        self.alt_menus = [] # I'm not sure what I want to do about this yet.
        for lab in alt_menu_labels:
            self.alt_menus.append(modast.find_label(lab).next)

        chapter_menus_ = modast.find_menu(["Meet with Bryce."]) # Choice was 100% unbiased thanks
        chapter_menus_[:] = [node for node in chapter_menus_ if node not in self.alt_menus]
        self.chapter_menus = chapter_menus_

        stmts = renpy.game.script.all_stmts

        for node in stmts:
            if isinstance(node, ast.Python) and node.code.source == "brycebar = False":
                self.chapter_1_hook = node

        #TODO: Understand what this variable name is
        # pylint: disable=invalid-name
        answToHook = ["chapter2chars", "chapter3chars", "chapter4chars"]
        closure_val = ""

        # pylint: disable=missing-docstring
        def nodeCB(node):
            if isinstance(node, ast.Python) and node.code.source == closure_val:
                return True

        #TODO: Understand what this variable name is
        self.InitAnswPoints = []
        for lab in answToHook:
            closure_val = "playmessage = False"
            labNode = modast.find_label(lab)

            #TODO: This is returning None
            hkPt = modast.search_for_node_with_criteria(labNode, nodeCB)
            print type(hkPt)

            # New mods will be inserted BEFORE this node, so we'll be alright.
            self.base.call_hook(hkPt, modast.find_label('_mod_fixansw'))
            closure_val = "remyavailable = True"
            hkPt2 = modast.search_for_node_with_criteria(labNode, nodeCB)

            self.InitAnswPoints.append((hkPt, hkPt2))

    def addAnswerMachineCheckHook(self, dest_node):
        """Check if the answering machine's output.

        Return true if the dialog should pop up and return false if it shouldn't.

        Args:
            dest_node: Can be either a :class:`renpy.ast.Node` or a function.
        """
        #TODO: Figure out what the variable names mean
        # pylint: disable=invalid-name
        if isinstance(dest_node, ast.Node):
            for (hkPt, _) in self.InitAnswPoints:
                self.base.call_hook(hkPt, dest_node)
#        else:
#            for (hkPt, hkPt2) in self.InitAnswPoints:
#                #TODO: Figure out what this closure does
#                # It's not called on anywhere
#                # pylint: disable=missing-docstring, unused-variable
#                def det_func(hook):
#                    ret = False
#                    if dest_node:
#                        ret = dest_node(hook)
#                    if ret:
#                        self.base.setRGlobal('playmessage', True)
#
#                # Why is this even here? We don't use ``hook`` after this
#                #hook = self.hook_opcode(hkPt, dest_node)

    def addAnswerMachineScene(self, dest_node):
        """Add a hook before the answering machine plays

        Args:
            dest_node: Can be either a :class:`renpy.ast.Node` or a
                function. Called after the machine check returns true
        """
        #TODO: Change the variable names
        # pylint: disable=invalid-name
        if isinstance(dest_node, ast.Node):
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.call_hook(hkPt2, dest_node)
        else:
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.hook_opcode(hkPt2, dest_node)

    def add_route(self, title, route_hook, condition="True"):
        """Add a route to the chapter menu

        The route will only appear if the condition evaluate to true.

        Args:
            title (str): The human-readable menu option
            route_hook (Node): The :class:`renpy.ast.Node` object to change to
            condition (str): The Python string to evaluate if the option should appear
        """
        for menu in self.chapter_menus:
            hook = self.base.get_menu_hook(menu)
            self.hooks.append(hook)
            hook2 = hook.addItem(title, None, condition)

            def call_func(hook):
                #TODO: What does rv stand for?
                # pylint: disable=invalid-name
                rv = renpy.game.context().call(route_hook.name,
                                               return_site=self.base.findlabel('_mod_fixjmp').name)
                hook.chain(rv)
            hook2.hook_func = call_func


    def hook_chapter_change(self, hook):
        """Hook a change of the chapters

        Args:
            hook: A :class:`renpy.ast.Node` object or function
        """
        chapter_labels = ["chapter2", "chapter3", "chapter4"]

        if isinstance(hook, ast.Node):
            for lab in chapter_labels:
                self.base.call_hook(self.base.findlabel(lab), hook, None)

            self.base.call_hook(self.chapter_1_hook, hook, None)
        else:
            #TODO: Determine which ch_id is actually being used
            # pylint: disable=function-redefined
            for lab in chapter_labels:
                def ch_id(hook2):
                    if hook:
                        hook(hook2, lab)
                self.base.hooklabel(lab, ch_id)

            #TODO: What does lab mean here?
            # pylint: disable=undefined-loop-variable, function-redefined
            def ch_id(hook2):
                if hook:
                    hook(hook2, lab)

            self.base.hook_opcode(self.chapter_1_hook, ch_id)

    def hook_chapter_1(self, hook):
        """Hook a node to the start of Chapter 1

        Args:
            hook (Node): The node to hook
        """
        self.base.call_hook(self.chapter_1_hook, hook)


#TODO: Reduce the amount of public methods
# pylint: disable=too-many-public-methods
class AWSWModBase(object):
    """The modding framework base.

    This class contains all the base functions needed to edit the AST, screens, and screen language.

    Attributes:
        ending_hooks (AWSWEndingHooks): An instance of the :class:`AWSWEndingHooks`.
        home_hook (AWSWHomeHook): An instance of the :class:`AWSWHOmeHook`
    """

    def __init__(self):
        self.ending_hooks = AWSWEndingHooks(self)
        self.name_serial = 1
        self.home_hook = AWSWHomeHook(self)

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

        hook = modast.ASTHook(("AWSWMod", 1)) # hooking hooks breaks
        hook.from_op = node
        node.next = hook
        hook.chain(next_statement)
        hook.old_next = next_statement
        hook.hook_func = func
        hook.name = "AWSWModOp_" + str(self.name_serial)
        self.name_serial += 1
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
        #TODO: Determine what this function does
        # pylint: disable=missing-docstring
        def call_func(hook):
            # pylint: disable=invalid-name
            if func:
                func(hook)
            rv = renpy.game.context().call(dest_node.name, return_site=hook.old_next.name)
            hook.chain(rv)


        hook.hook_func = call_func
        return hook

    def hooklabel(self, label, func):
        """Hook a function to a label

        Args:
            label (renpy.ast.Label): The label
            func (function): The function to be hooked

        Returns:
            An :class:`ASTHook` object
        """
        node_label = modast.find_label(label)
        return self.hook_opcode(node_label, func)

    def unhooklabel(self, label):
        """Unhook hooks from a label

        Args:
            label (str): The label's name
        """
        #TODO: Determine if method should be a static function
        # pylint: disable=no-self-use
        found_node = modast.find_label(label)
        if isinstance(found_node, modast.ASTHook):
            found_node.from_op.next = found_node.next

    def disable_slast_cache(self):
        """Disable SLAst's load cache"""
        #TODO: Determine if method should be a static function
        # pylint: disable=no-self-use
        renpy.sl2.slast.load_cache = lambda *_: None

    def disable_bytecode_cache(self):
        """Disable bytecode cache"""
        #TODO: Determine if method should be a static function
        # pylint: disable=no-self-use
        renpy.game.script.init_bytecode = lambda *_: None

    def get_menu_hook(self, menu):
        """Get the equivalent :class:`AWSWMenuHook` object

        Returns:
            The equivalent :class:`AWSWMenuHook` object
        """
        #TODO: Determine whether method should be static function
        # pylint: disable=no-self-use
        return modast.MenuHook(menu, base)

    def get_home_hook(self):
        """Get the home hook class

        Returns:
            The :class:`AWSWHomeHook` object
        """
        return self.home_hook

    def get_node_from_location(self, node, location):
        """Get the ``location``th node after ``node``

        Note:
            This skips :class:`ASTHook` nodes

        Args:
            node (Node): The starting search node
            location (int): The number of nodes to skip

        Returns:
            A :class:`renpy.ast.Node` object
        """
        #TODO: Determine whether method should be static function
        # pylint: disable=no-self-use
        for _ in range(0, location):
            node = node.next

            # Effectively skip the ASTHook nodes by continuing on
            while node and isinstance(node, modast.ASTHook):
                node = node.next
        return node

    def set_renpy_global(self, key, val):
        """Set a Ren'Py global

        Ren'Py globals can be used during execution of rpy.

        Args:
            key (str): The dictionary key
            val: The value of the dictionary object
        """
        #TODO: Determine whether method should be static function
        # pylint: disable=no-self-use
        renpy.python.store_dicts["store"][key] = val

    def get_renpy_global(self, key):
        """Get a Ren'Py global

        Args:
            key (str): The dictionary key

        Returns:
            The value put into the key or None if it doesn't exist
        """
        #TODO: Determine whether method should be static function
        # pylint: disable=no-self-use
        store = renpy.python.store_dicts["store"]
        if key in store:
            return store[key]

    def get_ending_hooks(self):
        """Get the ending hook class

        Returns:
            An instance of :class:`AWSWEndingHooks`
        """
        return self.ending_hooks

    def search_peak_if(self, node, type_, max_depth=200, skip=0):
        """Search recursively for a node type.

        This enters if statement blocks in order to find your specified node type

        Args:
            node (Node): The starting node
            type_ (Node): A *subclass*, not an instance, of a :class:`renpy.ast.Node` object
            maxBeforeFailure (int): How many nodes to iterate through before giving up

        Returns:
            A :class:`renpy.ast.Node` object or None if not found
        """
        # Simplify this pyramid
        # pylint: disable=too-many-nested-blocks
        for _ in range(1, max_depth):
            if node:
                if isinstance(node, ast.If):
                    for _, block in node.entries:
                        if block and skip <= 0:
                            skip -= 1
                            cand = self.search_peak_if(block[0], type_, 20)
                            if cand:
                                return cand

                        else:
                            skip -= 1


                elif isinstance(node, type_):
                    return node

            else:
                return None
            node = node.next


if not modloader.BUILDING_DOCUMENTATION:
    # Determine if this should be a constant
    # pylint: disable=invalid-name
    base = AWSWModBase()
