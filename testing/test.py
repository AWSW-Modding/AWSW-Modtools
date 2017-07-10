import renpy
import renpy.display.screen
import renpy.sl2.slast
import renpy.ast

from modloader import modast


def test_get_screen():
    result = modast.get_screen("screen_test_get_screen")
    return result is not None and isinstance(result,
            renpy.display.screen.Screen)


def test_get_slscreen():
    result = modast.get_slscreen("screen_test_get_screen")
    return result is not None and isinstance(result,
            renpy.sl2.slast.SLScreen)


def test_find_label():
    result = modast.find_label("label_test_find_label")
    return result is not None and isinstance(result, renpy.ast.Label)


def test_search_for_node_type():
    result = modast.search_for_node_type(
            modast.find_label("label_test_find_label"), renpy.ast.Menu)
    return result is not None and isinstance(result, renpy.ast.Menu)


def test_search_for_node_with_criteria():
    def bryce_say(node):
        return isinstance(node, renpy.ast.Say) and node.who == "Br"

    result = modast.search_for_node_with_criteria(
            modast.find_label("label_test_find_label"), bryce_say)
    return result is not None and isinstance(result, renpy.ast.Say)


def test_remove_slif():
    sl = modast.get_slscreen("screen_test_get_screen")
    result = modast.remove_slif(sl, "persistent.test")
    return result and len(sl.children[0].entries[0][1].children) == 0


def test_find_menu_single():
    result = modast.find_menu("Yes you are!")
    return result is not None and isinstance(result, list)


def test_find_menu_multi():
    result = modast.find_menu(["Yes you are!", "Of course!"])
    return result is not None and isinstance(result, list)


def test_find_say():
    result = modast.find_say("This should not be displayed")
    return result is not None and isinstance(result, renpy.ast.Say) \
            and result.who == "c"


def test_add_menu_option():
    menu = modast.find_menu("Yes you are!")[0]
    modast.add_menu_option(menu, "No you aren't",
            modast.find_label("label_extra"))
    return len(menu.items) == 3


def test_find_in_source_code():
    # TODO: Fix this, it fails
    result = modast.find_in_source_code(16, "test.rpy")
    return result is not None and isinstance(result, renpy.ast.Label)


def test_find_python_statement():
    result = modast.find_python_statement("this_is_a_very_unique = \"variable\"")
    return result is not None


def test_tests():
    list_of_tests = [test_get_screen, test_get_slscreen,
                     test_find_label, test_search_for_node_type,
                     test_search_for_node_with_criteria, test_remove_slif,
                     test_find_menu_single, test_find_menu_multi,
                     test_find_say, test_add_menu_option,
                     test_find_in_source_code, test_find_python_statement]

    for test in list_of_tests:
        try:
            success = test()
        except Exception, e:
            success = False
            print e

        if success:
            print "[+] {}".format(test.__name__)
        else:
            print "[-] {}".format(test.__name__)
