"""Get and modify nodes in the AST tree

This file is free software under the GPLv3 license
"""
import os

import renpy
from renpy import ast

import modloader

def _imports():
    # pylint: disable=invalid-name
    global slast
    from renpy.sl2 import slast

if not modloader.BUILDING_DOCUMENTATION:
    _imports()

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
    for _ in range(1, max_depth):
        node = node.next
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
    for _ in range(1, max_depth):
        node = node.next
        if node and isinstance(node, ast.Node) and func(node):
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
        if isinstance(child, slast.SLIf):
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


def find_python_statement(statement):
    """Find a specific Python node in the entire AST

    Args:
        statement (str): The Python statement to look for

    Returns:
        The Python node if found, None if not
    """
    for node in renpy.game.script.all_stmts:
        if isinstance(node, ast.Python) and node.code.source == statement:
            return node
    return None
