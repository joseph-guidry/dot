#!/usr/bin/env python3
import os, sys
from _ast import arguments
def parent_process():
    print("Parent Proces will wait until")
    print("Child Process has completed\n")
    os.wait()
    
def use_execv():
    pid_from_fork = os.fork()
    if pid_from_fork > 0:
        parent_process()
    elif pid_from_fork == 0:
        os.execv("/bin/echo", arguments)
    else:
        print("error in forking!")

def use_execvp():
    pid_from_fork = os.fork()
    if pid_from_fork > 0:
        parent_process()
    elif pid_from_fork == 0:
        os.execvp("echo", arguments)
    else:
        print("error in forking!")
def main():
    global arguments
    arguments = ["echo", "this", "will", "be", "echoed"]
    use_execv()
    print("*" * 60)
    use_execvp()
    
if __name__ == "__main__": main()