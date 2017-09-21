import renpy.ast as ast
import renpy
from modloader import modast
from modloader.modclass import loadable_mod, Mod


@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return "remy_hatchery", "v0.1", ""

    def mod_load(self):
        for node in renpy.game.script.all_stmts:
            if isinstance(node, ast.Say) and node.what == "Well, see you some other time, [player_name].":
                modast.call_hook(node, modast.find_label("hatchery_scene"))
        node = modast.find_say("To some people, it may not matter much if they have one friend more or less. But you know what makes the biggest difference? Having one when you didn't used to.")
        rtn_no_hatchery = node.next

        hatchery_none = modast.find_label("hatchery_none")
        hatchery_none.next = rtn_no_hatchery
        node.next = modast.find_label("hatchery_extension")

        end_hatchery = modast.find_label("hatchery_extension_end")
        end_hatchery.next = modast.find_label("remy4skip2")

        hatchery_denied = modast.find_label("hatchery_denied")
        rtn_hatchery_denied = modast.find_say("But enough about me.")
        hatchery_denied.next = rtn_hatchery_denied

        modast.call_hook(modast.find_say("Don't worry about it. I'm just not sure if I can do this."),
                         modast.find_label("hatchery_nokiss"))

        modast.call_hook(modast.find_say("Yeah. It looks good on you.").next,
                         modast.find_label("hatchery_tie"))

        good_ending_start_hook = modast.find_say("I went as fast as I could, but with my injuries I had no chance to stop him as he aimed at Vara.")
        modast.find_label("hatchery_remy_good_ending_mod_no_requirements").next = good_ending_start_hook.next
        good_ending_start_hook.next = modast.find_label("hatchery_remy_good_ending_mod")

        good_ending_end_hook = modast.find_say("He enveloped her as his tears started raining down on the small body.").next
        modast.find_label("hatchery_remy_good_ending_mod_end").next = good_ending_end_hook

        good_ending_start_hook = modast.find_say("Are you sure about that?")
        modast.find_label("hatchery_remy_good_ending_mod2_no_requirements").next = good_ending_start_hook.next
        good_ending_start_hook.next = modast.find_label("hatchery_remy_good_ending_mod2")

        good_ending_end_hook = modast.find_say("Besides, if you really end up going back in time, I'll see you again.")
        modast.find_label("hatchery_remy_good_ending_mod_end2").next = good_ending_end_hook

        true_ending_start_hook = modast.find_say("Well, if you really want to know, it was Amely.").next
        modast.find_label("hatchery_remy_true_ending_mod_no_requirements").next = true_ending_start_hook.next
        true_ending_start_hook.next = modast.find_label("hatchery_remy_true_ending_mod")

        true_ending_end_hook = modast.find_say("I think it's time to go, anyway.")
        modast.find_label("hatchery_remy_true_ending_mod_end").next = true_ending_end_hook


    def mod_complete(self):
        pass
