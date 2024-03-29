"""Get and modify nodes in the AST tree

This file is free software under the MIT license
"""
import os
import string

import renpy
from renpy import ast


def get_screen(scr, nodes=None):
    """Get a screen based off of its name

    Args:
        scr (str): The screen's name
        nodes (list): A list of screen variants. If None, default to all screens

    Returns:
        A :class:`renpy.display.screen.Screen` object
    """
    return renpy.display.screen.get_screen_variant(scr, nodes)


def get_slscreen(scr, nodes=None):
    """Get a screen's executable based off of its name

    Args:
        scr (str): The screen's name
        nodes (list): A list of screen variants. If None, default to all screens

    Returns:
        A :class:`renpy.display.screen.Screen` object
    """
    return get_screen(scr, nodes).ast


def find_label(label):
    """Find a label based off of its name

    Args:
        label (str): The label's name

    Returns:
        A :class:`renpy.ast.Label` object
    """
    return renpy.game.script.lookup(label)


def find_jump_target(target_label, one=True):
    """Find a jump node (all if one is False) which is bound to the target_label

    Args:
        target_label (str): The target label's name

    Returns:
        Union[Node, List[Node]]
    """
    results = []
    for node in renpy.game.script.all_stmts:
        if isinstance(node, ast.Jump) and node.target == target_label:
            if one:
                return node
            results.append(node)
    return results


def search_for_node_type(node, type_, max_depth=200):
    """Search for a specific type of node

    Args:
        node (Node): The node to start the search
        type_ (class): The node class, not an instance of the class, to search for
        max_depth (int): The number of nodes to search before giving up
            Defaults to 200. The higher the number, the slower the process

    Returns:
        A :class:`renpy.ast.Node` object if a match occurs or None if no match occurs
    """
    while max_depth >= 1:
        if isinstance(node, ASTHook):
            node = node.old_next
        else:
            node = node.next
            max_depth -= 1
        if node:
            if isinstance(node, type_):
                return node
        else:
            return None


def search_for_node_with_criteria(node, func, max_depth=200):
    """Search for a node and check with ``func``

    If ``func`` returns a truthy value, return the node. Else, skip it

    Args:
        node (Node): The node to start the search
        func (function): Function to check for the given node. Given one argument,
            node (of type :class:`renpy.ast.Node`), which is the node that is at the current depth.
            Do not make the functions complex or it will slow down the game significantly.
        max_depth (int): The number of nodes to search before giving up
            Defaults to 200. The higher the number, the slower the process

    Returns:
        A :class:`renpy.ast.Node` object if a match occurs or None if no match occurs
    """
    while max_depth >= 1:
        if isinstance(node, ASTHook):
            node = node.old_next
        else:
            node = node.next
            max_depth -= 1
        if node:
            if func(node):
                return node
        else:
            return None


def remove_slif(scr, comparison):
    """Remove a block (equivalent to a Node) from a :class:`renpy.sl2.slast.SLIf` object

    Args:
        scr (SLScreen): The SLScreen node to start the search
        comparison (str): The comparison string for the expression

    Returns:
        True if removed, False if not
    """
    for child in scr.children:
        if isinstance(child, renpy.sl2.slast.SLIf):
            for condition, block in child.entries:
                if condition == comparison:
                    block.children = []
                    return True
    return False


def find_menu(needle):
    """Find menus based off a single menu choice

    This searches the entire AST tree to find the menu choice.

    Args:
        needle: The menu choice to look for. If needle is a string, search for
            the string. If needle is a list of strings, the program automatically
            enters multisearch mode

    Returns:
        A list of matching menus
    """
    matching_menus = []

    # Ensure that needle is a list
    if isinstance(needle, str):
        needle = [needle]

    for node in renpy.game.script.all_stmts:
        if isinstance(node, ast.Menu):
            for label, _, _ in node.items:
                if label in needle:
                    matching_menus.append(node)

    # Ensure there are no duplicate menus
    return list(set(matching_menus))


def find_say(needle):
    """Find a :class:`renpy.ast.Say` node based on what is said

    This searches the entire AST tree for the specified statement.

    Args:
        needle (str): The statement to search for

    Returns:
        A :class:`renpy.ast.Node` node
    """
    for node in renpy.game.script.all_stmts:
        if isinstance(node, ast.Say) and node.what == needle:
            return node
    return None


def find_all_hide(hide_name):
    """Find a list of :class:`renpy.ast.Hide` nodes based on a string

    This searches the entire AST tree for the all the instances of the specified statement.

    Args:
        hide_name (str): The string to search in Hide nodes

    Returns:
        A list of :class:`renpy.ast.Node` nodes
    """
    # Make a list so we can store all applicable nodes in
    result = []

    # Loop over every node in the game
    for node in renpy.game.script.all_stmts:
        # Ignore non-Hide nodes
        if isinstance(node, ast.Hide):
            # Compare the search string and the object the node is hiding
            # Note: The comma makes it a one-element tuple, which impsec is
            if node.imspec[0] == (hide_name,):
                result.append(node)

    return result  # Return the list


def find_all_show(show_name):
    """Find a list of :class:`renpy.ast.Show` nodes based on a string

    This searches the entire AST tree for the all the instances of the specified statement.

    Args:
        show_name (str): The string to search in Show nodes

    Returns:
        A list of :class:`renpy.ast.Node` nodes
    """
    rtn = []
    for node in renpy.game.script.all_stmts:
        if isinstance(node, ast.Show):
            if node.imspec[0] == (show_name,):
                rtn.append(node)
    return rtn


def add_menu_option(menu, option, node):
    """Add a dialog option to a given menu

    Args:
        menu (Menu): The menu to modify
        option (str): The option's text
        node (Node): The node to execute if the node is selected
    """
    menu.items.append((option, "True", [node]))


def find_in_source_code(line_number, file_name):
    """Find a node by line number and file name

    Note:
        Line numbers and file names can change between versions. Use the
        function as a last resort only.

    Args:
        line_number (int): The line number
        file_name (str): The file name

    Returns:
        The node or None if it doesn't meet the criteria provided
    """
    for node in renpy.game.script.all_stmts:
        head, tail = os.path.split(node.filename)
        node_file_name = tail or os.path.basename(head)
        if node.linenumber == line_number and node_file_name == file_name:
            return node
    return None


def find_python_statement(statement, all=False):
    """Find a specific Python node in the entire AST

    Args:
        statement (str): The Python statement to look for
        all (bool): If you want to return all such python statements or just one. Defaults to False.

    Returns:
        The Python node if found, None if not
        Or a list of nodes which satisfy the conditions
    """
    rtn = []
    for node in renpy.game.script.all_stmts:
        if isinstance(node, ast.Python) and node.code.source == statement:
            if all:
                rtn.append(node)
            else:
                return node
    if all:
        return rtn
    return None


ROT13 = string.maketrans(
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")


class ASTHook(ast.Node):
    """A custom :class:`renpy.ast.Node` that acts as a hook between
        other node objects.

    Note:
        Don't instantiate this class directly. Ren'Py uses an
        internal serial for the call stack and other uses. This
        class emulates that at the base class.

    Attributes:
        hook_func: A function that's called when the node is executed.
                If the function returns a non-None value, the next
                node will be skipped.
        from_op: The original node before hooking
        old_next: The original next node before hooking was done
        tag: Unique tag appended to the name of the node. 
                Use in situation, when it's possible for the player to save
                the game during the execution of the hook function to ensure 
                name consistency between saves.
    """
    _serial = 1

    def __init__(self, loc, hook_func_=None, from_op_=None, tag=None):
        super(ASTHook, self).__init__(loc)

        self.hook_func = hook_func_
        self.from_op = from_op_
        self.old_next = None
        
        # Node which is expected to come next if the hook function runs successfully
        # This value doesn't change the behaviour, only provides information about the hook
        self.expected_next = None

        # Create a unique name
        if tag:
            self.name = "AWSWModOp_" + tag
        else:
            self.name = "AWSWModOp_" + str(ASTHook._serial)
            ASTHook._serial += 1
        renpy.game.script.namemap[self.name] = self

    def execute(self):
        """Execute hook after node is called"""
        ast.statement_name("hook")
        ret = None
        if self.hook_func:
            ret = self.hook_func(self)

        if not ret:
            self.exec_continue()
    
    # Sets the expected next node when chaining
    def chain(self, next):
        self.next = next
        self.expected_next = next

    def exec_continue(self):
        """Continue"""
        ast.next_node(self.next)

    def unhook(self):
        """Remove the hook"""
        self.from_op.next = self.old_next


class MenuHook(object):
    """A hook class for editing a specific menu"""

    def __init__(self, menu_, base_):
        """Make a hook class for the specific ``menu_`` object

        Args:
            menu_ (renpy.ast.Menu): The Menu node to be hooked
            base_ (AWSWModBase): An instance of the mod base class
        """
        if not isinstance(menu_, ast.Menu):
            raise AssertionError("MenuHook not instantiated with a Menu node!")

        self.menu = menu_
        self.base = base_
        # Copy the menu.items list, not a reference to it
        self.old_items = menu_.items[:]

    def delete_item(self, label):
        """
        Delete a choice from the menu

        Args:
            label (str): The label to search for
        """
        # choice[0] is the choice's label
        self.get_items()[:] = [choice for choice in self.get_items() if choice[0] != label]

    def get_item(self, label):
        """Get a choice from the menu

        Args:
            label (str): The label to search for

        Returns:
            A three-element tuple where the format is (label, condition, block).
            Label is the visible label given to the user, condition is a Python statement that determines whether or not to show the choice, and block is SL code
        """
        # obj[0] is the choice's label
        for choice in self.get_items():
            if choice[0] == label:
                return choice

    def get_option_code(self, label):
        """Get a choice's SL code from the menu

        Args:
            choice (str): The choice to get
        """
        # choice[2] is the choice's SL code
        choice = self.get_item(label)
        return choice[2]

    def get_items(self):
        """Get all the items in the menu

        Returns:
            A list of three-element tuples where the format is (label, condition, block), where
            label is the visible label given to the user,
            condition is a Python statement that determines whether or not to show the choice, and
            block is SL code
        """
        return self.menu.items

    def set_conditional(self, item, new_cond):
        """Change the conditional statement for ``item``

        Returns:
            True if successful and False if not
        """
        for i, (label, _, block) in enumerate(self.get_items()):
            if label == item:
                self.menu.items[i] = (label, new_cond, block)
                return True
        return False

    def add_item(self, label, hook, condition="True"):
        """Add a new choice to the menu

        Args:
            label (str): The option's label

            hook: Either a :class:`renpy.ast.Node` or a function to be
                    executed after the menu choice has been selected

            condition (str): A Python string to evaluate to determine
                    whether or not the choice should be shown

        Returns:
            None if ``hook`` is a :class:`renpy.ast.Node` or a
            :class:`ASTHook` if ``hook`` is a function
        """
        if isinstance(hook, ast.Node):
            self.get_items().append((label, condition, [hook])) # Adding a dialogue option.
            return None

        node = ASTHook(("AWSWMod", 1))
        node.from_op = self.menu
        node.hook_func = hook
        self.get_items().append((label, condition, [node]))
        return node

    def add_item_call(self, label, usr_hook, condition="True"):
        #TODO: Determine what this does
        # pylint: disable=missing-docstring, invalid-name
        hook = self.add_item(label, None, condition)

        def call_func(hook):
            rv = renpy.game.context().call(usr_hook.name, return_site=self.menu.next.name)
            hook.chain(rv)

        hook.hook_func = call_func

    def set_item(self, item, new_block):
        """Change the statement for ``item``

        Returns:
            True if successful and False if not
        """
        for i, (label, condition, _) in enumerate(self.get_items()):
            if label == item:
                self.menu.items[i] = (label, condition, new_block)
                return True
        return False


def hook_opcode(node, func, tag=None):
    """Hook ``func`` to ``node``

    Args:
        node (Node): The node object for the function to hook
        func (function): The function to be executed when the node is executed
        tag (string): Unique tag of the hook. (See attributes of ASTHook for more details.)

    Todo:
        Check if a hook already exists and make the code more cohesive

    Returns:
        An :class:`ASTHook` object
    """
    # Keep a copy of the node's original next node
    next_statement = node.next

    # Make a new ASTHook and hook it to the node
    # The tuple is in the format (filename, filenumber)
    # This is used by the renpy stacktrace
    hook = ASTHook(("AWSWMod", 1), func, node, tag)
    if isinstance(node, ast.Label):
        node.next = hook
    else:
        node.chain(hook)

    # Put the original next node to the hook node
    # Also keep a copy of the original next node in the hook node, allowing us to unhook it
    hook.chain(next_statement)
    hook.old_next = next_statement

    return hook


def call_hook(node, dest_node, func=None, return_node=None, tag=None):
    """Hook ``func`` to ``node`` and once executed, redirect execution to
        ``dest_node``

    Args:
        node (Node): The node to hook
        dest_node (Node): the node to go after ``node`` is executed
        func (function): The function to call
        tag (string): Unique tag of the hook. (See attributes of ASTHook for more details.)

    Returns:
        An :class:`ASTHook` object
    """
    hook = hook_opcode(node, None, tag)

    def call_function(hook):
        # pylint: disable=missing-docstring
        if func:
            rtn = func(hook)
            if rtn:
                return rtn

        #TODO: Better understand this line
        label = renpy.game.context().call(dest_node.name,
                return_site=hook.old_next.name if return_node is None else
                return_node.name)
        hook.chain(label)

    hook.hook_func = call_function
    hook.expected_next = dest_node
    return hook


def unhook_label(label):
    """Unhook a hook from a label

    Args:
        label (str): The label's name
    """
    #TODO: Test this
    found_node = find_label(label)
    if isinstance(found_node, ASTHook):
        found_node.from_op.next = found_node.next


def disable_slast_cache():
    """Disable SLAst's load cache"""
    renpy.sl2.slast.load_cache = lambda *_: None


def disable_bytecode_cache():
    """Disable bytecode cache"""
    renpy.game.script.init_bytecode = lambda *_: None


def get_node_after_nodes(node, location):
    """Get the ``location``th node after ``node``

    Note:
        This skips :class:`ASTHook` nodes

    Args:
        node (Node): The starting search node
        location (int): The number of nodes to skip

    Returns:
        A :class:`renpy.ast.Node` object
    """
    for _ in range(0, location):
        node = node.next

        # Effectively skip the ASTHook nodes by continuing on
        while node and isinstance(node, ASTHook):
            node = node.next
    return node


def get_renpy_global(key):
    """Get a Ren'Py global

    Args:
        key (str): The dictionary key

    Returns:
        The value put into the key or None if it doesn't exist
    """
    store = renpy.python.store_dicts["store"]
    if key in store:
        return store[key]


def set_renpy_global(key, val):
    """Set a Ren'Py glboal

    Ren'Py globals can be used during execution of rpy.

    Args:
        key (str): The dictionary key
        val (str): The value of the dictionary object
    """
    renpy.python.store_dicts["store"][key] = val


def jump_ret(node, dest_node, return_node, func=None):
    """Hook ``func`` to ``node`` and once executed, redirect execution to
        ``dest_node`` and allow ``return_node`` to be executed after
        ``dest_node`` returns

    Args:
        node (Node): The node to hook
        dest_node (Node): The node to go after ``node`` is executed
        return_node (Node): The node that is executed after ``dest_node`` returns
        func (function): The function hook

    Returns:
        An :class:`ASTHook` object
    """
    return call_hook(node, dest_node, func, return_node)


def jump_if_ret(node, dest_node, condition, return_node=None):
    """If ``condition`` is true, just from ``node`` to ``dest_node``.
    Regardless of ``condition``, then jump to ``return_node``.

    Args:
        node (Node): The node to hook
        dest_node (Node): The node to go after ``node`` is executed
        condition (str): The condition to jump to ``dest_node``
        return_node (Node): The node that is executed after ``dest_node`` returns

    Returns:
        An :class:`ASTHook` object
    """
    def func(hook):
        rtn = renpy.python.py_eval(condition)
        if rtn:
            ast.next_node(hook.old_next)
        return rtn
    return jump_ret(node, dest_node, return_node, func)


def hook_label(label, func):
    """Hook a function to a label

    Args:
        label (renpy.ast.Label): The label
        func (function): The function to be hooked

    Returns:
        An :class:`ASTHook` object
    """
    node_label = find_label(label)
    return hook_opcode(node_label, func)
