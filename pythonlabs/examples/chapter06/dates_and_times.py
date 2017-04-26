#!/usr/bin/env python3
from datetime import *

def main():
    now = datetime.today()
    print("Today is:", now)
    print(now.month, now.day, now.year, sep="/", end="\n\n")
    
    delta36hours = timedelta(days = 1, hours = 12)
    theFuture = now + delta36hours
    print("36 hours from now:", theFuture, end="\n\n")
    
    thePast = datetime(2000,1, 31, 14, 25, 59)
    print("A date in the past:", thePast, end = "\n\n")

if __name__ == "__main__": main()