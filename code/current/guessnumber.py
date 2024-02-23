'''
# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
'''
# imports here
import random
import math
import simpleguitk as simplegui

# initialize global variables used in your code
SECRETNUMBER = 0
GAMEGUESSES = 0
LOW = 0
HIGH = 100
NUMBERGUESSES = int(round(math.log(HIGH, 2)))


def new_game():
    ''' helper function to start and restart the game'''
    # pylint: disable=global-statement
    global SECRETNUMBER, GAMEGUESSES
    SECRETNUMBER = random.randrange(LOW, HIGH)
    GAMEGUESSES = NUMBERGUESSES
    print("")
    print(f"New Game! You have {str(GAMEGUESSES)} guesses left to go ")


def range100():
    ''' button that changes range to range [0,100) and restarts'''
    # define event handlers for control panel
    # button that changes range to range [0,100) and restarts
    # pylint: disable=global-statement
    global HIGH, NUMBERGUESSES
    HIGH = 100
    NUMBERGUESSES = int(round(math.log(HIGH, 2)))
    new_game()


def range1000():
    ''' button that changes range to range [0,1000) and restarts '''
    # pylint: disable=global-statement
    global HIGH, NUMBERGUESSES
    HIGH = 1000
    NUMBERGUESSES = int(round(math.log(HIGH, 2)))
    new_game()


def check_game():
    ''' helper function to check the game'''
    # pylint: disable=global-statement
    global GAMEGUESSES
    GAMEGUESSES = GAMEGUESSES - 1
    if GAMEGUESSES == 0:
        print("Game over! you lose")
        print(f"The number was {str(SECRETNUMBER)}")
        print("")
        new_game()
    else:
        print(f"you have {str(GAMEGUESSES)} guesses left")


def input_guess(guess):
    ''' main game logic goes here'''
    guess_number = int(guess)
    if SECRETNUMBER == guess_number:
        print("Correct!")
        new_game()
    elif SECRETNUMBER > guess_number:
        print("Higher!")
        check_game()
    else:
        print("Lower!")
        check_game()


def main():
    ''' main function'''
    # create frame
    frame = simplegui.create_frame("Guess the Number", 200, 200)

    # register event handlers for control elements
    frame.add_button("Range (0, 100)", range100, 200)
    frame.add_button("Range (0, 1000)", range1000, 200)
    frame.add_input("Enter a Guess", input_guess, 200)

    # call new_game and start frame
    new_game()
    frame.start()
    # always remember to check your completed
    # program against the grading rubric


if __name__ == '__main__':
    main()
