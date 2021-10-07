#
# File        : GuessingGame.py
# Created     : 01/10/2021
# Author      : James Bowman
# Version     : v1.0.0
# Licensing   : (C) James Bowman
#               Available under GNU Public License (GPL)
# Description : Simple Guessing Game
#

from random import randrange

if __name__ == '__main__':
    # Store a random number for the user to guess
    secret_number = randrange(10)

    # Create a variable to keep the loop running until we get a correct guess
    guessed = False

    # Enter in to a loop of guesses
    while not guessed:
        # Prompt for guess
        guess = input("Guess a number between 1 and 10: ")
        if int(guess) == secret_number:
            # When true, update our loop variable to finish
            guessed = True

    # Print a nice exit message on success
    if guessed:
        print("Congratulations, you guess the correct number " +str(secret_number))




