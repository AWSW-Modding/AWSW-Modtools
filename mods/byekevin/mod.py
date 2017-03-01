import modlib
import renpy
import renpy.ast as ast

ml = modlib.base


found = ml.searchPostNode(ml.findlabel("c4hatchery"), ast.Scene, 20)
hook = ml.hook_opcode(found, None)
hook.chain(ml.searchPostNode(found, ast.Scene))

mainscr = ml.getsls('main_menu')
ml.nullPyexpr(mainscr, 'persistent.playedkevin')
