import modlib
from modlib import sprnt

ml = modlib.base

home_hook = ml.getHomeHook()

# Here's how this works:
# Calling addRoute will install a hook into every single instance* where the player can choose who to visit. "Test Route" is the title, and the ml.findlabel... code gets our entry point to the scene logic.
# The third argument ("exampleroutestatus >=...") is evaluated as a python expression every time the menu pops up. If it returns true, the option shows, otherwise the option does not. 
# We check for exmapleroute_status >= 1, which will return true as long as we're in good standing for this route, AND exampleroute_lastplayed  is less than mod_currentChapter
# First: we can break the logic up into to discrete sections- "exampleroute_status >= 1", "exampleroute_lastplayed < mod_currentChapter". Due to the the AND operator, both must return true for the statement as a whole to return true.
# If either in False, the menu option does not show. 
# Second: mod_currentChapter is a variable handled by the modloader. It will always be the integer value of the current chapter (Chapter 1: 1, Chapter 2: 2, etc)
# *There are some unhandled menus at the moment, particularly when there are more than 7 options on the menu, causing the player to get [[Show more options]]. This will be fixed ASAP. 
home_hook.addRoute("Test Route", ml.findlabel("exampleroute_entrypoint"), "exampleroute_status >= 1 and exampleroute_lastplayed < mod_currentChapter")


home_hook.hookChapter1(ml.findlabel("exampleroute_init")) # We need to set up our code at the beginning of every game. 