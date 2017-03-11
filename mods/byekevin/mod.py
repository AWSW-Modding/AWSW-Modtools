import modlib
import renpy
import renpy.ast as ast

ml = modlib.base


found = ml.searchPostNode(ml.findlabel("c4hatchery"), ast.Scene, 20)
hook = ml.hook_opcode(found, None)
hook.chain(ml.searchPostNode(found, ast.Scene))

mainscr = ml.getsls('main_menu')
ml.nullPyexpr(mainscr, 'persistent.playedkevin')

eHooks = ml.getEndingHooks()
true_search = eHooks.getPostTrueEndingIzumiScene()

def kevinCB(node):
    if node.next is not None and isinstance(node.next, renpy.ast.Show) and node.next.imspec[0][0] == 'meetingkevin':
        return True

kevin_credits = ml.searchPostNodeCB(true_search, kevinCB, 800)
kevin_credits.chain(ml.searchPostNode(kevin_credits, ast.Scene)) # Show and with are separate instructions.