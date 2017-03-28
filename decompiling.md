Fortunately, this game can easily be extracted and decompiled. This makes modding much easier--if it was hard, there probably would be no modding framework.

### Prerequisites

You will need a working Python 2 installation. To check, open up a Powershell, command prompt, terminal, or equivalent and execute `python --version`.

If you get an error such as

    'python' is not recognized as an internal or external command, operable program or batch file

then you have improperly installed Python.

If you get an output that starts with `Python 3`, you have installed the incorrect version of Python.

If you get an output that starts with `Python 2`, you have installed the correct version of Python.

## Getting media and compiled source code
*This assumes you know the basics of command line, such as changing directories.*

* Open up a Powershell, command prompt, terminal, or equivalent
* Make a new folder anywhere and change directories to the new folder
* Copy the archive.rpa from the game directory in the installation folder into the new folder
* [Download rpatool](https://github.com/Shizmob/rpatool/archive/master.zip) and extract the file `rpatool` into the new folder.
* Run `python rpatool -x archive.rpa`. It might take a while

After the command is executed, a whole plethora of files and folders are made in the new folder. For now, ignore all files with the .rpyc file extension.

Some notable folders include:
|     Location    |                             Purpose                             |
| --------------- | --------------------------------------------------------------- |
| achievements    | Contains all the achievement icons                              |
| bg              | Contains all the backgrounds                                    |
| bg/in           | Contains backgrounds that take place inside                     |
| bg/in/apts      | Contains apartment backgrounds                                  |
| bg/in/facility  | Contains backgrounds that take place in the production facility |
| bg/out          | Contains backgrounds that take place outside                    |
| bg/out/facility | Contains backgrounds that is right outside the facility         |
| bg/out/np       | Contains backgrounds that take at night time                    |
| bg/out/town     | Contains backgrounds of various places in the town              |
| cg              | Contains all the characters' CGs among other stuff              |
| cg/extra        | Contains all the cards and image gallery photos                 |
| cg/lorem        | Contains extra pictures of Lorem and Ispum                      |
| cr              | Contains all the characters expressions                         |
| fx              | Contains the sound effects                                      |
| mx              | Contains all the music the game has to offer                    |
| se/sounds       | Contains more sound effects                                     |
| sy              | Never before seen photos!                                       |

## Getting the source code

Source code is the human-readable version of the game. All dialog options, games, and spoilers are in these files.
However, the code is compiled into Ren'Py compiled files. They have an extension of .rpyc.
To get the source code, we need to decompile the game. The source code has an extension of .rpy

* [Download unrpyc](https://github.com/CensoredUsername/unrpyc/archive/master.zip) and extract the zip file into the new folder
* Run `python unrpyc.py .`
* *Optional* Remove the .rpyc files
