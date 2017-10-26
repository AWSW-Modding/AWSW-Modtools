import graphviz
import renpy.ast as ast
import sys
from modast import find_say, find_label

def create_graph(filename="script"):
    sys.setrecursionlimit(200000)
    dot = graphviz.Digraph()
    start = find_say("Detecting user profile.{cps=2}..{/cps}{w=2.0}{nw}")
    nodes = create_nodes(start, dot, [])
    draw_nodes(nodes, dot)
    dot.format = "svg"
    dot.render(filename, view=True)
    sys.exit()

def draw_nodes(nodes, dot, prev=None, next=None):
    print "draw nodes", len(nodes)
    for i, (prev, node, next) in enumerate(get_next(nodes, prev=prev, next=next)):
        if isinstance(node, ast.Jump):
            dot.edge(str(id(node)), str(id(find_label(node.target))))
            continue
        if isinstance(node, dict):
            for label, block in node.items():
                if block:
                    draw_nodes(block, dot, prev=node, next=next)
                    dot.edge(str(id(prev)), str(id(block[0])), label=label)
                    if isinstance(block[-1], ast.Jump):
                        dot.edge(str(id(prev)), str(id(find_label(block[-1].target))), label=label)
                    else:
                        dot.edge(str(id(block[-1])), str(id(next)))
                else:
                    dot.edge(str(id(prev)), str(id(next)), label=label)
            dot.edge(str(id(node)), str(id(next)))
        if next is None:
            continue
        if isinstance(node, (ast.Say, ast.Label, ast.Jump, ast.Call)) and \
           isinstance(next, (ast.Say, ast.Label, ast.Jump, ast.Call)):
            dot.edge(str(id(node)), str(id(next)))

def create_nodes(node, dot, labels, end_node=None):
    nodes = []
    if isinstance(node, (ast.Say, ast.Label, ast.Jump, ast.Call)):
        nodes.append(node)
    if isinstance(node, ast.Say):
        dot.node(str(id(node)), node.what)
    if isinstance(node, ast.Label):
        if node.name in labels:
            return []
        dot.node(str(id(node)), "Label: "+node.name)
        labels.append(node.name)
    if isinstance(node, ast.Call):
        dot.node(str(id(node)), "Call: "+node.label)
    if isinstance(node, ast.Menu):
        menu = {}
        for _label, _condition, block in node.items:
            if block is not None:
                menu[_label] = create_nodes(block[0], dot, labels, block[-1])
        dot.node(str(id(menu)), "End Menu")
        nodes.append(menu)
    if isinstance(node, ast.If):
        menu = {}
        dot.node(str(id(menu)), "End If")
        for _condition, block in node.entries:
            menu[_condition] = create_nodes(block[0], dot, labels, block[-1])
        if any(menu.values()):
            nodes.append(menu)
    if isinstance(node, ast.While):
        menu = [node, create_nodes(block[0], dot, labels, block[-1])]
        dot.node(str(id(menu)), "While: "+node.condition)
        nodes.append(menu)
    if node.next and node is not end_node:
        nodes.extend(create_nodes(node.next, dot, labels, end_node))
    if isinstance(node, ast.Jump):
        dot.node(str(id(node)), "Jump: "+node.target)
        if node.target not in labels:
            nodes.extend(create_nodes(find_label(node.target), dot, labels, end_node))
    return nodes

def get_next(lst, prev=None, next=None):
    for i, item in enumerate(lst):
        yield ([prev]+lst)[i], item, (lst+[next])[i+1]