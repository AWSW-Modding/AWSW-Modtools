import os
import json
import shutil
import renpy
import zipfile

with open(os.path.join(renpy.config.gamedir, "modloader", "modtools_files.json")) as json_f:
    modtools_files = json.load(json_f)
for rel_path in modtools_files[1]:
    fullpath = os.path.join(renpy.config.gamedir, rel_path)
    if os.path.exists(fullpath):
        if os.path.isdir(fullpath):
            shutil.rmtree(fullpath)
        else:
            os.remove(fullpath)

zip_path = os.path.join(renpy.config.gamedir, "modtools-update.zip")
zip_f = zipfile.ZipFile(zip_path, 'r', zipfile.ZIP_DEFLATED)

print("Saving new version...")
norm_renpy = os.path.normpath(renpy.config.gamedir)
root = zip_f.namelist()[0]
replace = root if root.endswith("/") else ""
for path in zip_f.namelist():
    true_path = os.path.normpath(os.path.join(norm_renpy, path.replace(replace, "", 1)))
    if not true_path.startswith(norm_renpy):
        print("Bad path:", true_path, "not saving")
        continue
    if true_path == norm_renpy:
        continue
    if not path.endswith('/'):
        print("Extract", path, true_path)
        if not os.path.isdir(os.path.dirname(true_path)):
            os.makedirs(os.path.dirname(true_path))
        with zip_f.open(path) as source, open(true_path, "wb") as target:
            shutil.copyfileobj(source, target)

zip_f.close()
os.remove(os.path.join(norm_renpy, "modtools-update.zip"))