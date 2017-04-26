#!/usr/bin/env python3
from subprocess import Popen, PIPE
def main():
    p = Popen("ls", stdout=PIPE, universal_newlines=True)
    for line in p.stdout:
        print(line, end="")
    p.stdout.close()
    return_code = p.wait()
    print("Process terminated ~ return code: ", return_code)

if __name__ == "__main__": main()