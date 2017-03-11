import renpy
import renpy.ast as ast
import renpy.sl2.slast as slast
import renpy.python
import os
import string

def sprnt(str):
    print(str.encode('utf-8'))

rot13_dec = string.maketrans( 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm",
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz")

class ASTHook(ast.Node): # Don't instantiate ASTHook directly. Ren'py assigns a serial number to each node which is used internally for the call stack and other things. We emulate that functionality in the base class. 
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
    def __init__(self, base):
        self.base = base
        searchStr = string.translate("Fur pybfrq ure rlrf nf n fvatyr grne ena qbja ure snpr. V zbirq gb jvcr vg sebz ure, naq pbhyq nyernql srry gur jnezgu qenvavat sebz Vmhzv'f obql. Fur jnf qrnq.", rot13_dec)
        self.TrueEndingPostIzumi = self.base.findSay(searchStr)
        
    def getPostTrueEndingIzumiScene(self):
        return self.TrueEndingPostIzumi

    def hookPostTrueEnding(self, node): 
        #fincall = self.base.searchPostNode(endsay, ast.Call, 500)
        #print(type(endsay.next.next).__name__.encode('utf-8'))
        fincall = self.getPostTrueEndingIzumiScene().next
        return self.base.call_hook(fincall, node)
        
    def hookPostEvilEnding(self, node):
        return None
        
    def hookRouteEnding(self, route):
        return None
        
    def getEndingPickerMenu(self):
        ch5 = ml.findlabel("chapter5")
        menu_node = self.base.searchPostNode(ch5, ast.Menu, 500)
        menu_hooks = self.base.getMenuHook(menu_node)
        
        return menu_hooks
        
        
class AWSWMenuHook():
    def __init__(self, menu, base):
        if not isinstance(menu, ast.Menu):
            raise AssertionError("MenuHook not instantiated with a Menu node!")
            
        self.menu = menu
        self.base = base
        self.oldItems = menu.items[:]
        
    def deleteItem(self, item):
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
    def __init__(self, base):
        self.base = base
        self.hooks = []
        
        altMenuLabs = ["chap2altmenua1", "chap2altmenub1", "chap3altmenua1", "chap3altmenub1", "chap4altmenua1", "chap4altmenub1"]
        self.altMenus = [] # I'm not sure what I want to do about this yet.
        for lab in altMenuLabs:
            self.altMenus.append(base.findlabel(lab).next)
        
        chmenus = base.findMenu(["Meet with Anna."]) # Choice was 100% unbiased thanks
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
        if isinstance(dest_node, ast.Node):
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.call_hook(hkPt2, dest_node)
        else:
            for (hkPt, hkPt2) in self.InitAnswPoints:
                self.base.hook_opcode(hkPt2, dest_node)
        
    def addRoute(self, title, routeHook, condition="True"): 
        for menu in self.ChapterMenus:
            hook = self.base.getMenuHook(menu)
            self.hooks.append(hook)
            hook2 = hook.addItem(title, None, condition)
            
            def call_func(hook):
                rv = renpy.game.context().call(routeHook.name, return_site=self.base.findlabel('_mod_fixjmp').name)
                hook.chain(rv)
            hook2.hook_func = call_func
            
            
    def hookChapterChange(self, hook):
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
        self.base.call_hook(self.CH1Hook, hook)
            

class AWSWModBase:
    #See display/screen.py
    
    
    def __init__(self):
        self.endingHooks = AWSWEndingHooks(self)
        self.nameSerial = 1
        self.homeHook = AWSWHomeHook(self)
    
    def getscreen(self, scr):
        return renpy.display.screen.get_screen_variant(scr) # Returns renpy.display.screen.Screen object
    
    def getsls(self, scr): # Shorthand for getting the SLScreen class
        return self.getscreen(scr).ast
    
    def findlabel(self, lab):
        return renpy.game.script.lookup(lab)
        
    def hook_opcode(self, node, func): #todo, check if a hook already exists at this point and make everything a bit more cohesive
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
        hook = self.call_hook(node, dest_node, func)
        hook.next = ret_node
        return hook
        
    def call_hook(self, node, dest_node, func=None):
        hook = self.hook_opcode(node, None)
        def call_func(hook):
            if func:
                func(hook)
            rv = renpy.game.context().call(dest_node.name, return_site=hook.__oldNext.name)
            hook.chain(rv)
            
            
        hook.hook_func = call_func
        return hook
        
    def hooklabel(self, lab, func):
        ASTLabel = self.findlabel(lab)
        return self.hook_opcode(ASTLabel, func)
        
    def unhooklabel(self, lab):
        found_node = self.findlabel(lab)
        if isinstance(found_node, ASTHook):
            found_node.fromOp.next = found_node.next
        
    def searchPostNode(self, node, type, maxBeforeFailure=200):
        for i in range(1,maxBeforeFailure): # Search 200 opcodes by default now. we don't want to exhaust resources by searching the entire tree.
            node = node.next
            #node_type = node.__class__.__name__
            #sprnt(node_type)
            if node:
                if isinstance(node, type):
                    return node
            
            else:
                return None
                
    def searchPostNodeCB(self, node, func, maxBeforeFailure=200):
        for i in range(1,maxBeforeFailure):
            node = node.next
            if node:
                ret = func(node)
                if ret:
                    return node
            else:
                return None
                
    def DisableSCache(self):
        def remove_s_cache():
            return
        renpy.sl2.slast.load_cache = remove_s_cache
        
    def DisableBCache(self):
        def remove_b_cache():
            return
        renpy.game.script.init_bytecode = remove_b_cache
        
    def nullPyexpr(self, scr, comp): # Given a screen, will completely remove an if statement and the child nodes.
        for i in scr.children:
            if isinstance(i, slast.SLIf):
                for cond, block in i.entries:
                    if cond == comp:      
                        block.children = []
                        return True
        return False
        
    def hookScreen(self, scr):
        scrObj = self.getscreen(scr)
        
        return None
        
    def findMenu(self, needle): # This will parse the entire AST to hopefully find a menu that matches the specification.
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
                            #for i, (label, condition, block) in enumerate(node.items):
                                #sprnt(label)
                            retlist.append(node)
                    elif label == needle:
                        retlist.append(node)
                            
        return list(set(retlist))
        
    def findSay(self, needle): # Searches the entire AST for a say statement.
        stmts = renpy.game.script.all_stmts            
        
        for node in stmts:
            if isinstance(node, ast.Say) and node.what == needle:
                return node
                
        return None
        
    def addMenuOption(self, menu, option, node):
        menu.items.append((option, "True", [node])) # Adding a dialogue option.
        return None
        
    def getMenuHook(self, menu):
        return AWSWMenuHook(menu, base)
        
    def getHomeHook(self):
        return self.homeHook
        
    def stepOp(self, node, num):
        for i in range(0, num):
            node = node.next
            while(node and isinstance(node, ASTHook)):
                node = node.next
        return node
        
    def setRGlobal(self, key, val):
        renpy.python.store_dicts["store"][key] = val
        
    def getRGlobal(self, key):
        store = renpy.python.store_dicts["store"]
        if key in store:
            return store[key]
        
    def findByLineNumber(self, ln, file): # This is a bad idea and only should be used as a last resort. 
        # Every node has self.filename and self.linenumber populated. We can use this as rudimentary verification, or as a last resort. Changes to the game may break this if you base off of line number.
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
        stmts = renpy.game.script.all_stmts            
        
        for node in stmts:
            if isinstance(node, ast.Python) and node.code.source == code:
                return node

base = AWSWModBase()
