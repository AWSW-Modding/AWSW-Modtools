Decompiling the game
====================

Fortunately, this game can easily be extracted and decompiled. This makes modding much easier--if it was hard, there probably would be no modding framework.

Easy way
--------

A tool_ for this has already been written for you that can do it for you automatically with little to no input.
Just double click the program and it should automatically find the rpa file for the Steam installation.
If you want to decompile the default Steam installation, the place it gives you by default should work fine but you can choose a different install if you want to.


Hard way
--------

Prerequisites
~~~~~~~~~~~~~

You will need a working Python 2 installation. To check, open up a Powershell, command prompt, terminal, or equivalent and execute ``python --version``.

If you get an error such as

    'python' is not recognized as an internal or external command, operable program or batch file

then you have improperly installed Python.

If you get an output that starts with ``Python 3``, you have installed the incorrect version of Python.

If you get an output that starts with ``Python 2``, you have installed the correct version of Python.

Getting media and compiled source code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



*This assumes you know the basics of command line, such as changing directories.*

* Open up a Powershell, command prompt, terminal, or equivalent
* Make a new folder anywhere and change directories to the new folder
* Copy the archive.rpa from the game directory in the installation folder into the new folder
* Download rpatool_ and extract the file ``rpatool`` into the new folder
* Run ``python rpatool -x archive.rpa``. It might take a while

After the command is executed, a whole plethora of files and folders are made in the new folder. For now, ignore all files with the .rpyc file extension.

Getting the source code (Only required for hard way)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Source code is the human-readable version of the game. All dialog options, games, and spoilers are in these files.
However, the code is compiled into Ren'Py compiled files. They have an extension of .rpyc.
To get the source code, we need to decompile the game. The source code has an extension of .rpy

* Download _unrpyc and extract the zip file into the new folder
* Run ``python unrpyc.py .``
* *Optional:* Remove the .rpyc files


Some notable folders include:

+-----------------+-----------------------------------------------------------------+
|     Location    |                             Purpose                             |
+=================+=================================================================+
| achievements    | Contains all the achievement icons                              |
+-----------------+-----------------------------------------------------------------+
| bg              | Contains all the backgrounds                                    |
+-----------------+-----------------------------------------------------------------+
| bg/in           | Contains backgrounds that take place inside                     |
+-----------------+-----------------------------------------------------------------+
| bg/in/apts      | Contains apartment backgrounds                                  |
+-----------------+-----------------------------------------------------------------+
| bg/in/facility  | Contains backgrounds that take place in the production facility |
+-----------------+-----------------------------------------------------------------+
| bg/out          | Contains backgrounds that take place outside                    |
+-----------------+-----------------------------------------------------------------+
| bg/out/facility | Contains backgrounds that is right outside the facility         |
+-----------------+-----------------------------------------------------------------+
| bg/out/np       | Contains backgrounds that take at night time                    |
+-----------------+-----------------------------------------------------------------+
| bg/out/town     | Contains backgrounds of various places in the town              |
+-----------------+-----------------------------------------------------------------+
| cg              | Contains all the characters' CGs among other stuff              |
+-----------------+-----------------------------------------------------------------+
| cg/extra        | Contains all the cards and image gallery photos                 |
+-----------------+-----------------------------------------------------------------+
| cg/lorem        | Contains extra pictures of Lorem and Ispum                      |
+-----------------+-----------------------------------------------------------------+
| cr              | Contains all the characters expressions                         |
+-----------------+-----------------------------------------------------------------+
| fx              | Contains the sound effects                                      |
+-----------------+-----------------------------------------------------------------+
| mx              | Contains all the music the game has to offer                    |
+-----------------+-----------------------------------------------------------------+
| se/sounds       | Contains more sound effects                                     |
+-----------------+-----------------------------------------------------------------+
| sy              | Never before seen photos!                                       |
+-----------------+-----------------------------------------------------------------+


.. _rpatool: https://github.com/Shizmob/rpatool/archive/master.zip
.. _unrpyc: https://github.com/CensoredUsername/unrpyc/archive/master.zip
.. _tool: https://cdn.discordapp.com/attachments/283326469717884928/391692687063121930/AWSW_Extractor.exe

.. _QuickBMS: http://aluigi.altervista.org/quickbms.htm
.. _Python Pickle Parser: http://aluigi.altervista.org/bms/pickle.bms
.. _RPA Renpy No Python: http://aluigi.altervista.org/bms/rpa_renpy_nopython.bms
