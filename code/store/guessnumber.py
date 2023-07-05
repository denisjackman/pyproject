# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# imports here 
import random 
import math 
import simplegui 

# initialize global variables used in your code
secret_number=0 
low=0
high=100
number_guesses = int(round(math.log(high,2))) 

# helper function to start and restart the game
def new_game():
    global secret_number, game_guesses, number_guesses
    secret_number = random.randrange(low,high)
    game_guesses = number_guesses
    print ""
    print "New Game! You have " + str(game_guesses) + " guesses left to go "
    return
 
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global high, number_guesses 
    high = 100
    number_guesses = int(round(math.log(high,2)))  
    new_game()
    return 

def range1000():
    # button that changes range to range [0,1000) and restarts
    global high, number_guesses 
    high=1000
    number_guesses = int(round(math.log(high,2))) 
    new_game()
    return

def check_game():
    global game_guesses
    game_guesses = game_guesses - 1 
    if game_guesses == 0:
        print "Game over! you lose"
        print "The number was " + str(secret_number)
        print ""
        new_game()
    else:
        print "you have " + str(game_guesses) + " guesses left"
    return 

def input_guess(guess):
    # main game logic goes here
    global secret_number, game_guesses  
    guess_number = int(guess) 
    if secret_number == guess_number:
        print "Correct!"
        new_game()
    elif secret_number > guess_number:
        print "Higher!" 
        check_game()
    else:
        print "Lower!"
        check_game()
    return
    
# create frame
frame = simplegui.create_frame("Guess the Number",200,200)

# register event handlers for control elements
frame.add_button("Range (0, 100)",range100,200)
frame.add_button("Range (0, 1000)",range1000,200)
frame.add_input("Enter a Guess",input_guess,200)

# call new_game and start frame
new_game()

# always remember to check your completed program against the grading rubric
