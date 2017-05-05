#!/usr/bin/env python3

"""
This module plays the guessing game.
Author: Joseph Guidry
Date  : 05 May 2017
"""

import random
import os


def guess_game():
    """This is the main function to start the guessing game"""
    banner_fmt = "{:^78}"
    statement1 = "number between 1 and 100"
    line_break = ("-" * 79)
    while True:
        os.system('clear')
        print(line_break + banner_fmt .format("The Guessing Game\n"))
        print(banner_fmt.format("Guess the " + statement1 + "\n"))
        print(line_break)
        rand_num = game_numbers(100)
        lie_num = game_numbers(10)
        end_turn = play_game(rand_num, lie_num)  # Start guessing game
        print("Finishing on turn: " + str(end_turn))
        if lie_num < end_turn:                   # If answer after lie
            print("I lied about the results on turn " + str(lie_num))
        cont = input("Enter 'y' to play again:  ")
        if cont != 'y':
            break


def play_game(rand_num, lie_num):
    """Takes in random number and lie number. Starts guessing game."""
    turn = 0
    while True:
        try:
            response_fmt = "Your guess is too {}. Pick a {} number"
            guess = get_guess()          # Get integer guess value
            turn += 1                    # Add turn iteration
            if guess is rand_num:        # First guess evaluation
                print("\nCorrect\n")
                return turn
            if guess < rand_num:         # Guess is lower evaluation
                if turn is lie_num:      # Check if turn to lie
                    lower(response_fmt)  # Print lie
                else:
                    higher(response_fmt)
            else:                         # Higher guess response
                if turn is lie_num:       # Check if turn to lie
                    higher(response_fmt)
                else:
                    lower(response_fmt)
        except (ValueError, UnboundLocalError):
            print("Enter a number between 1 and 100")


def higher(response_fmt):
    """Outputs a formated response to guess higher"""
    print(response_fmt.format("low", "bigger"))


def lower(response_fmt):
    """Returns a formated response to guess lower"""
    print(response_fmt.format("high", "smaller"))


def game_numbers(upper_limit):
    """Takes upper limit. Returns a random number in the range"""
    return random.randrange(1, upper_limit)


def get_guess():
    """Return a integer value of valid guess"""
    guess = input("Enter your guess> ")
    if not guess.isnumeric():           # Check if uess is number
        raise UnboundLocalError
    guess = int(guess)                  # Convert to integer
    if guess > 100 | guess < 0:         # Check if out of range
        raise ValueError

    return guess


def main():
    """The main function. Starts the guess_game()"""
    guess_game()
    os.system('clear')   # Clear screen after the game is over.

if __name__ == "__main__": main()
