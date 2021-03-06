Installation
============

Download the mod tools here_.
Extract the zip and copy-paste bootstrap.rpy, mods, and modloader folders to the game directory in your AWSW installation.

The DRM-free installation directory is wherever you extracted the game. The Steam installation directory can be found by right-clicking the entry in your Steam library, hitting 'Properties', clicking the 'Local Files' tab, and then clicking 'Browse Local Files'.

The only mod required is the core mod. The core mod loads some crucial components of the mod framework.

.. _here: https://github.com/AWSWCommunity/AWSW-Modtools/archive/develop.zip

The resulting directory structure should look like the following:

::

    Installation Directory
    |-- game
        |-- mods
            |-- core
            |-- ...
        |-- modloader
            |-- ...
        |-- bootstrap.rpy
        |-- archive.rpa
    |-- lib
        |-- ...
    |-- renpy
        |-- ...
    |-- Angels with Scaly Wings.exe
    |-- Angels with Scaly Wings.py
    |-- Angels with Scaly Wings.sh

## Contributing

You can contribute! Writers and drawers are needed to produce high-quality mods. Programmers are needed to ensure a stable and easy-to-use modding framework.

If you need assistance, please make a Github account and [create an issue](https://help.github.com/articles/creating-an-issue/).

## Roadmap

[*] Complete

[!] Important!

[.] In progress

#### Level 1 (usability: barely*)
*You are here. Good luck.*

[\*] \# Modify Renpy screens

[\*] \# Hook interpretted opcodes

[\*] \# Virtual file system for resources

#### Level 2 (usability: better)
[.] \# Hook Menus

[.] \# Better menu finding algorithm

\# Easy hooking for any instruction type

\# Docs and easy hooking for screen lang objects
#### Level 3 (usability: easy)

[.] # Complete abstraction of apartment menu

[!] # Debug overlay(menu option jump viewing, code peaking, on the fly decompilation)

[*] \# Post true ending hook

\# Post chracter ending hooks

\# Pre ending hooks

\# Ending determination point hook

\# Fine grain character patching

\# Postponing chapters and key game events without manual label lookup

\* results may vary
