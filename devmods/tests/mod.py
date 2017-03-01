import modlib
import renpy.ast as ast
from modlib import sprnt

ml = modlib.base
h = ml.getHomeHook()
e = ml.getEndingHooks()

# These are my bootleg unit tests. They'll let you know whether something's gone wrong due to a code change. 

h.addAnswerMachineScene(ml.findlabel("tests_2b"))

h.addAnswerMachineCheckHook(ml.findlabel("tests_1")) # Testing answering machine functionality
h.addAnswerMachineScene(ml.findlabel("tests_2"))

h.addAnswerMachineCheckHook(ml.findlabel("tests_1b")) # Make sure additional hooks work as well

h.addAnswerMachineScene(ml.findlabel("tests_2c"))

hook = e.hookPostTrueEnding(ml.findlabel("tests_3")) # Check for post true ending functionality

h.hookChapterChange(ml.findlabel("tests_4")) # Chapter change testing

def hook_4b(hook, lab):

    return False
h.hookChapterChange(hook_4b) # Chapter change testing

test_scr = ml.getscreen("main_menu")
if test_scr is None:
    raise AssertionError("Main_menu not found")
    
test_scr_ast = ml.getsls("main_menu")
if test_scr is None:
    raise AssertionError("Main_menu ast not found")
   
say_test = ml.findSay("Do you have something similar where you come from?")
if not isinstance(say_test, ast.Say):
    raise AssertionError("findSay failure.")
    
test_menu = ml.findMenu(["Scream.", "Accept.", "Reject."])
if len(test_menu) == 0:
    raise AssertionError("No menu")
    
test_menu_hook = ml.getMenuHook(test_menu[0])
test_menu_hook.setConditional("Scream.", "False")
test_menu_hook.deleteItem("Reject.")

test_menu_hook.addItem("Test", test_menu_hook.getOptionCode("Accept.")[0])

ml.call_hook(ml.findlabel("start"), ml.findlabel("tests_6"))


ml.findByLineNumber(1, "AWSWMod")