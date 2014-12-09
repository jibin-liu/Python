# Programmed by Jibin Liu
# "Guess the number" mini-project
# Can be played at http://www.codeskulptor.org/#user29_iXv7W5KlzJA5vMe.py

# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui
import math

# initialize global variables used in your code
secret_num = 0
guest_guess = 0
guess_num = 0
guess_range = 100

# helper function to start and restart the game
def new_game(guess_range):
    print
    global secret_num, guess_num
    secret_num = random.randrange(0, guess_range)
    guess_num = int(math.ceil(math.log(guess_range + 1, 2)))
    print "The game starts in the range of [0, %s). Good luck!" % guess_range
    print "You have %s guesses left." % guess_num
    return secret_num

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global guess_range
    guess_range = 100
    return new_game(guess_range)

def range1000():
    # button that changes range to range [0,1000) and restarts
    global guess_range
    guess_range = 1000
    return new_game(guess_range)
    
def input_guess(guess):
    # main game logic goes here	
    global secret_num, guest_guess, guess_num, guess_range
    guess_num -= 1
    guest_guess = int(guess)
    if guest_guess == secret_num:
        print "You guessed %s, it is correct! Great job!" % guest_guess
        new_game(guess_range)
    elif guest_guess > secret_num:
        print "You guessed %s, it is higher! You have %s guesses left." % (guest_guess, guess_num)
    else:
        print "You guessed %s, it is lower! You have %s guesses left." % (guest_guess, guess_num)
    if (guess_num == 0) and not (guest_guess == secret_num):
        print "Sorry, you have used up your guesses."
        new_game(guess_range)

# create frame
frame = simplegui.create_frame("Guess The Number", 200, 200)


# register event handlers for control elements
frame.add_button("Range: [0, 100)", range100, 200)
frame.add_button("Range: [0, 1000)", range1000, 200)
frame.add_input("Enter your guess below:", input_guess, 200)


# call new_game and start frame
new_game(guess_range)
frame.start()
