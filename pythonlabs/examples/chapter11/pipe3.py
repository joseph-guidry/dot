#!/usr/bin/env python3
from subprocess import Popen, PIPE
def main():
    data = ["Joe", "Jane", "Alice", "Ruth"]
    p = Popen(["sort"], stdin=PIPE, universal_newlines=True)
    for name in data:
        p.stdin.write(name + "\n")
    p.stdin.close()
    return_code = p.wait()
    print("Process terminated with return code: ",
          return_code)

if __name__ == "__main__": main()