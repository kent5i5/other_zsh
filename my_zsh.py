import sys,tty
import signal
import subprocess
import os
from contextlib import contextmanager
# import curses
#from pynput import keyboard
from pynput.keyboard import Key, Controller, Listener
from xml.sax.xmlreader import InputSource
from test.test_decimal import directory
from lib2to3.fixer_util import Comma

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
   

def on_release(key):
    print('{0} release'.format( key))
    if key == Key.esc:
        # Stop listener
        return False

def loadingScreen():
    print(" In this shell. Thing works differently")
   
def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")


def haoyifunction():
        
    tty.setraw(sys.stdin)
    while True: # loop for each line
        input = ""
        index = 0
        while True: # loop for each character
            char = ord(sys.stdin.read(1)) # read one char and get char code
            if char == 3: # CTRL-C
                return
            elif 32 <= char <= 126:
                input = input[:index] + chr(char) + input[index:]
                index += 1
            elif char in {10, 13}:
                sys.stdout.write(u"\u001b[1000D")
                print ("\nechoing... ", input)
                input = ""
                index = 0
            elif char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    if next2 == 68: # Left
                        index = max(0, index - 1)
                    elif next2 == 67: # Right
                        index = min(len(input), index + 1)
    sys.stdout.write(u"\u001b[1000D") # Move all the way left
    sys.stdout.write(input)
    sys.stdout.write(u"\u001b[1000D") # Move all the way left again
    if index > 0:
        sys.stdout.write(u"\u001b[" + str(index) + "C") # Move cursor too index
    sys.stdout.flush()
    
def working_directory(directory):
    owd = os.getcwd()
    print(cwd)
    try: 
        cwd = os.getcwd() + "/" + command[1]
        print(cwd)
        os.chdir(cwd)
        yield directory
    finally:
        os.chdir(owd)

if __name__ == "__main__":
    loadingScreen()
    command = sys.argv
    command.remove("my_zsh.py")
    keyboard = Controller()
    
    if keyboard.press('a'):
         print("a")
         
         
    try:
        signal.signal(signal.SIGALRM, handler)
        
    except:
        print("it is ok")
    
#     with Listener( on_press=on_press, on_release=on_release) as listener:
#                
#         listener.join()
        
    if len(sys.argv) == 0:
        g = ''
        while g != signal.SIGQUIT:
            #Collect events until released
            
                
#             listener = keyboard.Listener(on_press=on_press,on_release=on_release)
#             listener.start()
            g = input("give me your wish :<<< ") 
            command = g.split()
            try:
                returncode = 0
                if len(command) == 1:
                    if command[0] ==  "cd":
                        cwd = "/Home"
                        owd = os.getcwd()
                        os.chdir(cwd)
                        os.chdir("../")
                        print("current working directory is "+ owd)
                    else:
                        returncode = subprocess.call([command[0]])
                if len(command) == 2:
                    returncode = subprocess.call([command[0], command[1]])
                    if command[0] ==  "cd":
                        working_directory(command[1])
                      
                        if command[1][:2]== "..":
                            
                            cd = os.getcwd()
                            print(cd.split("/").count())
                            owd = os.getcwd()
                            working_directory(directory)
                    
                if len(command) == 3:
                    subprocess.call([command[0], command[1]], command[2])
                if len(command) == 4:
                    subprocess.call([command[0], command[1]], command[2])
                if len(command) == 5:
                    subprocess.call([command[0], command[1]], command[2], command[3], command[4])
            except:
                print("Try other command")
        
    
        
            
   # text = "ls -l"
    #command = sys.argv # sys.argv is a list of command. argv[0], argv[1], argv[2]
    
    
    
    
