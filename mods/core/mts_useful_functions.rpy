init -1 python:
    def mts_yes_no_prompt(string):
        ui.frame(xalign=0.5, yalign=0.5)
        ui.add("image/ui/menubg_options.png", at=popup_custom)
        ui.vbox(at=popup_custom)
        ui.null(height=30)

        ui.text(string,
                style="yesno_prompt_text",
                xcenter=0.5, ycenter=0.5)

        ui.null(height=50)
        ui.hbox(xcenter=0.5, ycenter=0.5)

        ui.textbutton("Yes",
                        clicked=[ui.returns(True), Play("audio", "se/sounds/yes.wav")],
                        hovered=[Play("audio", "se/sounds/select.ogg")],
                        style="yesnobutton")

        ui.null(width=250)

        ui.textbutton("No",
                        clicked=[ui.returns(False), Play("audio", "se/sounds/close.ogg")],
                        hovered=[Play("audio", "se/sounds/select.ogg")],
                        style="yesnobutton")
        ui.close()
        ui.close()

        return ui.interact()

    def mts_ok_prompt(string):
        ui.frame(xalign=0.5, yalign=0.5)
        ui.add("image/ui/menubg_options.png", at=popup_custom)
        ui.vbox(at=popup_custom)
        ui.null(height=30)

        ui.text(string,
                style="yesno_prompt_text",
                xcenter=0.5, ycenter=0.5)

        ui.null(height=50)
        ui.hbox(xcenter=0.5, ycenter=0.5)

        ui.textbutton("OK",
                        clicked=[ui.returns(True), Play("audio", "se/sounds/yes.wav")],
                        hovered=[Play("audio", "se/sounds/select.ogg")],
                        style="yesnobutton")

        ui.close()
        ui.close()

        return ui.interact()

    def mts_var_exists(var):
        if var in renpy.python.store_dicts["store"]:
            return True

        return False

    def mts_is_mod_installed(mod):
        for mod_name in modinfo.modlist:
            if mod_name == mod:
                return True

        return False

init -100 python:
    @renpy.pure
    class MTSSetPersistent(Action, FieldEquality):
        identity_fields = ['value']
        equality_fields = ['name']

        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __call__(self):
            setattr(persistent, self.name, self.value)
            renpy.save_persistent()
            renpy.restart_interaction()

        def get_selected(self):
            return getattr(persistent, self.name) == self.value


    @renpy.pure
    class MTSTogglePersistentBool(Action):
        def __init__(self, name):
            self.name = name

        def __eq__(self, other):
            if not isinstance(other, MTSTogglePersistentBool):
                return False
            return self.name == other.name

        def __call__(self):
            #if it's true
            if getattr(persistent, self.name):
                setattr(persistent, self.name, False)
                renpy.save_persistent()
                renpy.restart_interaction()

            #if it's False
            else:
                setattr(persistent, self.name, True)
                renpy.save_persistent()
                renpy.restart_interaction()

        def get_selected(self):
            return getattr(persistent, self.name)

###Some transforms
transform popup_custom:
    xalign 0.5 yalign 0.5 alpha 0.0 yzoom 0.0
    easein 0.3 alpha 1.0 yzoom 1.0
    on hide:
        easeout 0.3 alpha 0.0 yzoom 0.0
