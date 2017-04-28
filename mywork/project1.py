"""Author: Joseph Guidry    """
"""Date  : 27 April 2017    """

#! /usr/bin/env python3

"""This module displays to the screen the song "99 bottles of beer on the wall" """

import sys

def get_bottles(args_list, num):
    """Gets list of command line arguments. Returns number of bottles"""
     
    while len(args_list) > 1:        # If there is a command line arguement
        args_list.pop(0)
        #if int(args_list[0]) is type(1): # Remove non-integers from arguments in the list.
        return int(args_list[0])
    else:                            # Default to 99 if no arguments given.
        return (num)
    
def song(bottles):
    """Takes beer phrase and number of bottles.  Displays the verses of the song, 
    decrementing bottle number"""
    beer = "bottles of beer"      
    wall = "on the wall!"
    take = "Take one down \nAnd pass it around"
    for bottle in range(bottles, 0, -1):
        print()
        print(bottle, beer, wall)              #Prints "# bottles of beer on the wall!
        print(bottle, beer + "!")              #Prints "# bottles of beer!
        print(take)
        bottle -= 1
        if bottle == 1:
            beer = "bottle of beer"            # Change wording for single beer.
        if bottle == 0: 
           beer = "No more bottles of beer"    # Change wording for no beers.
           print(beer, wall)
           return                              #Returns to "No more bottles of beer on the wall"
        print(bottle, beer, wall)              #Prints "(# - 1) bottles of beer on the wall!
        
def main():
    """This is the programs main function"""
    
    bottle = get_bottles(sys.argv, num=99)
    song(bottle)                            # Begin song "99 bottles of beer on the wall". 
    print() 
        
if __name__=="__main__":main()
