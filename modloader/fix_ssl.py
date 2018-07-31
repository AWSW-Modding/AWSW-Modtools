import os
import renpy
from steam_workshop.dir_util import copy_tree as copy_files


def fix_ssl():
    modloader_path = os.path.join(renpy.config.gamedir, "modloader")
    orig = os.path.join(modloader_path, "dll")
    backup = os.path.join(modloader_path, "dll_backup")
    copy_files(backup, orig)
