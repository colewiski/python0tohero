
# Create "complex code" easy to read
# Now that we can ask for user input, let's check to see if it's right
'''
Let's write a function that takes our previous threecups
'''


# Gotta import shuffle from the library
from random import shuffle

# Function for shuffling the cups
def shuffle_ball(threecups):
    shuffle(threecups)
    return threecups

# Function for users guess
def player_guess():

    guess = ''

    while guess not in ['0','1','2']: # User input always returns as a string
        guess = input("Pick a number: 0, 1, or 2 ")

    return int(guess)

# Function for checking the guess
def check_guess(threecups,myguess):
    if threecups[myguess] == 'O':
        print("Correct!")
    else:
        print("Wrong guess!")
        print(threecups)

# Initial list
threecups = [' ','O',' ']

# Shuffle list
shuffledcups = shuffle_ball(threecups)

# User guess
myguess = player_guess()

# Check guess
check_guess(shuffledcups,myguess) # this is when the functions start playing with each other.

# This allows functions to talk to each other and become much more complex.
