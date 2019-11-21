# other_zsh
we are doing our own zsh


Currently, we write the other_zsh in python.

we use sys, os python modules to executes our commands.


sys.argv gives us the command line arguments.

Example, len(sys.argv) == 0:

argv[0] is the command example: "cd /directory/"

argv[1] is the extra options or argument. "-l" or ".."


-------------------------------
we use os.getcwd() to get the current directory and 

use os.chdir() to change directory. 
