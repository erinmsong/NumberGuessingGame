"""
The program randomly generates an integer number and prompts the user
to guess the number. It will display "you guessed too high" if you
guessed a number bigger than the correct one the program randomly
generated. It will display "you guessed too small" if you guessed
a number smaller than the correct one.
"""

import random
import sys

# TODO: prompt the user to enter the lower bound.
lowBound = int(input("Enter the lower bound: "))

# TODO: prompt the user to enter the upper bound.
upBound = int(input("Enter the upper bound: "))

# TODO: stop the program if lower bound is higher than upper bound.
# sys.exit() stops the program from running.
if (lowBound > upBound):
    print("Invalid input: your lower bound is higher than the upper bound")
    sys.exit()

# TODO: prompt the user to enter the number of guesses allowed from the user.
guessNum = int(input("Enter the number of guesses allowed: "))

# TODO: stop the program if the total number of guesses that the user entered is smaller or equal to 0.
# sys.exit() stops the program from running.
if (guessNum <= 0):
    print("Invalid input: the number of guesses must be greater than 0")
    sys.exit()

# TODO: generate a random integer between lower and upper bounds (inclusive).
numChoice = random.randint(lowBound, upBound)

# TODO: prompt the user to guess the number and display if the guess is too high or too low.
# Display "congratulations, you have found the correct number" if the user guesses the correct number.
# Repeat as long as the user has not guessed the correct number and the user has not used all their guesses.

guessLim = 0
while(guessLim != guessNum):
    playerGuess= int(input("Guess a number: "))
    if(playerGuess < numChoice):
        print("You guessed too low")
        guessLim = guessLim + 1
    elif(playerGuess > numChoice):
        print("You guessed too high")
        guessLim = guessLim + 1
    elif(playerGuess == numChoice):
        print("Congratulations, you have found the correct answer")
        sys.exit()

# TODO: display the correct number if user used all guesses and still has not found the correct number.
print("You have used all your guesses. The correct answer was: ")
print(numChoice)
