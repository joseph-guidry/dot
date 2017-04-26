#!/usr/bin/env python3
import os
def main():
    original_pid = os.getpid()
    print("Application PID is :", original_pid)
    print("Forking will create a second process...\n")
    pid_from_fork = os.fork()
    
    # The following code will now be executed by both
    # the parent & child process - in no particular order
    if pid_from_fork > 0:
        print("Parent Proces is running",original_pid,
              pid_from_fork, os.getpid())
        os.wait()
        print("Parent Process returned from wait()")
    elif pid_from_fork == 0:
        print("Child Proces is running",original_pid,
              pid_from_fork, os.getpid())
    else:
        print("error in forking!")
    
    print("Current process id:", os.getpid())
    
if __name__ == "__main__": main()