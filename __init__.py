from __future__ import print_function

import re
import time
import os
import json
import struct
import sys

import renpy

from modloader.modclass import Mod, loadable_mod
from modloader.modast import hook_opcode, find_label

image_table = {
    "adine1": "adine",
    "adine2": "adine",
    "adine3": "adine",
    "adine4": "adine",
    "adine5": "adine",
    "anna1": "anna",
    "anna2": "anna",
    "anna3": "anna",
    "anna4": "anna",
    "anna5": "anna",
    "bryce1": "bryce",
    "bryce2": "bryce",
    "bryce3": "bryce",
    "bryce4": "bryce",
    "bryce5": "bryce",
    "lorem1": "lorem",
    "lorem2": "lorem",
    "lorem3": "lorem",
    "lorem4": "lorem",
    "lorem5": "lorem",
    "remy1": "remy",
    "remy2": "remy",
    "remy3": "remy",
    "remy4": "remy",
    "remy5": "remy"
}

label_table = {
    "chapter5evilending": "evil",
    "chapter5trueendings": "true",
    "dv": "sec",
    "endings": "main",
    "images": "main",
    "script": "main",
    "xemera": "emera",
    "xkatsu": "katsu",
    "xkevin": "kevin",
    "xsebastian": "sebastian",
    "xzhong": "zhong"
}

ignore_labels = {
    '_call_syscheck_100',
    'skipcheck',
    'syscheck',
    '_call_syscheck_97',
    '_call_syscheck_101',
    'optimistcheck',
    'izumimask',
    'popularcheck',
    'skiptut',
    'lazycheck',
    'mainmenu2',
    'no',
    'resetall',
    'resetlevels',
}

name_table = {
    "adine1": "Adine 1",
    "adine2": "Adine 2",
    "adine3": "Adine 3",
    "adine4": "Adine 4",
    "adine5": "Adine 5",
    "anna1": "Anna 1",
    "anna2": "Anna 2",
    "anna3": "Anna 3",
    "anna4": "Anna 4",
    "anna5": "Anna 5",
    "bryce1": "Bryce 1",
    "bryce2": "Bryce 2",
    "bryce3": "Bryce 3",
    "bryce4": "Bryce 4",
    "bryce5": "Bryce 5",
    "chapter1": "Chapter 1",
    "chapter2": "Chapter 2",
    "chapter3": "Chapter 3",
    "chapter4": "Chapter 4",
    "chapter5": "Chapter 5",
    "emera": "Emera",
    "evil": "Evil Ending",
    "katsu": "Katsu",
    "kevin": "Kevin",
    "lorem1": "Lorem 1",
    "lorem2": "Lorem 2",
    "lorem3": "Lorem 3",
    "lorem4": "Lorem 4",
    "lorem5": "Lorem 5",
    "main": "Main Menu",
    "remy1": "Remy 1",
    "remy2": "Remy 2",
    "remy3": "Remy 3",
    "remy4": "Remy 4",
    "remy5": "Remy 5",
    "sebastian": "Sebastian",
    "sec": "sec",
    "true": "True Ending",
    "zhong": "Zhong"
}

client_id = "364534617300140043"

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("Rich Presence", "v1.0", "Blue")

    def mod_load(self):
        renpy.config.after_load_callbacks.append(self.on_load)

    def mod_complete(self):
        self.rich_present_provider = RichPresence()
        for label, node in renpy.game.script.namemap.items():
            if isinstance(label, basestring) and label not in ignore_labels:
                match = re.search(r".*game/(tl/.*/)?(\w+).rpy", node.filename)
                if match:
                    match = match.group(2)
                    hook_opcode(node, lambda _, location=label_table.get(match, match): self.rich_present_provider.set_location(location))

    def on_load(self):
        label = renpy.game.context().return_stack[-1]
        if isinstance(label, basestring):
            label = [find_label(label).filename]
        location = re.search(r".*game/(tl/.*/)?(\w+).rpy", label[0]).group(2)
        self.rich_present_provider.set_location(label_table.get(location, location))


class WinPipe:
    def __init__(self):
        ipc_path = r"\\?\pipe\discord-ipc-{}"
        self.initialised = False
        for i in range(10):
            path = ipc_path.format(i)
            try:
                self._f = open(path, "w+b")
            except OSError:
                pass
            except IOError:
                pass
            else:
                self.initialised = True
                return

    def write(self, data):
        self._f.seek(0, 2)
        self._f.write(data)
        self._f.flush()

    def read(self, amount):
        return self._f.read(amount)

    def close(self):
        self._f.close()


class UnixPipe:
    def __init__(self):
        env_keys = ('XDG_RUNTIME_DIR', 'TMPDIR', 'TMP', 'TEMP')
        for env_key in env_keys:
            dir_path = os.environ.get(env_key)
            if dir_path:
                break
        else:
            dir_path = '/tmp'
        ipc_path = os.path.join(dir_path, 'discord-ipc-{}')
        self.initialised = False
        for i in range(10):
            path = ipc_path.format(i)
            if not os.path.exists(path):
                continue
            try:
                self._f = open(path, "w+b")
            except OSError:
                pass
            except IOError:
                pass
            else:
                self.initialised = True
                return

    def write(self, data):
        self._f.write(data)
        self._f.flush()

    def read(self, amount):
        return self._f.read(amount)

    def close(self):
        self._f.close()


class RichPresence:
    def __init__(self):
        self.location = None
        if sys.platform == 'linux' or sys.platform == 'darwin':
            self.pipe = UnixPipe()
        elif sys.platform == 'win32':
            self.pipe = WinPipe()
        if self.pipe.initialised:
            self.send_data(0, {'v': 1, 'client_id': client_id})
            opcode, data = self.read()
            if opcode == 2:
                print("Unable to connect to Discord ({})".format(data["message"]))
                self.pipe.initialised = False
            self.user_info = None
            if data["evt"] == "READY" and data["cmd"] == "DISPATCH":
                self.user_info = data["data"]["user"]
            print(self.user_info)

    def set_location(self, location):
        if location != self.location:
            self.location = location
            self.on_location_update()

    def on_location_update(self):
        if self.pipe.initialised:
            self.set_activity(self.name, self.image)

    def set_activity(self, details=None, large_image=None):
        payload = {
            "cmd": "SET_ACTIVITY",
            "args": {
                "pid": os.getpid(),
                "activity": {
                    "details": details,
                    "assets": {
                        "large_image": large_image
                    }
                }
            },
            "nonce": '{:.20f}'.format(time.time())
        }
        self.send_data(1, payload)

    def send_data(self, opcode, payload):
        payload = json.dumps(payload)
        self.pipe.write(
            struct.pack(
                '<II',
                opcode,
                len(payload)) +
            payload.encode('utf-8'))

    def read(self):
        opcode, length = struct.unpack("<II", self._read_exact(8))
        payload = self._read_exact(length)
        data = json.loads(payload.decode("utf-8"))
        return opcode, data

    def _read_exact(self, amount):
        buf = b""
        amount_remaining = amount
        while amount_remaining:
            chunk = self.pipe.read(amount_remaining)
            buf += chunk
            amount_remaining -= len(chunk)
        return buf

    @property
    def image(self):
        return image_table.get(self.location, self.location)

    @property
    def name(self):
        return name_table.get(self.location, self.location)
