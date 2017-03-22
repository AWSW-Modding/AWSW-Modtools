
## Getting what you want in spite of everyone else. 
Reverse engineering is a fact of life, and while I will do my best to make modding AWSW as painless as possible, it will still need to be done. Luckily, you have all the information you need right here. 

* Extract the archive with Rpatool: [Rpatool](https://github.com/Shizmob/rpatool) 
    Move rpatool into the same folder as archive.rpa (normally located in AWSW's game/ folder) and run with  ```python rpatool.py -x archive.rpa```. It is recommended that you move rpatool and archive.rpa into a subdirectory first, as rpatool extracts the archive into the **current directory**. 
* Decompile rpyc files (the game's code) with unrpyc: [UnRpyc](https://github.com/CensoredUsername/unrpyc)
    Move the contents of the git repository into a folder in the directory where the extracted archive files are. Decompile the rpyc files with ```python unrpyc.py ../*.rpyc```. See how the developers did it. (You'll also need this to figure out the handles for the characters and stock images.)
* Look at the example code!
* Look at the ren'py engine code (just kidding)
* When in doubt, see the the Ren'py docs: [Docs](https://www.renpy.org/doc/html/index.html)
* If none of the above options help: hold tight for the debug overlay, or ask for help!
