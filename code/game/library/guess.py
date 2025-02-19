'''
    guessing game
'''
# This is a guess the number game.
import random


def main():
    ''' main function'''
    GUESSESTAKEN = 0
    print('Hello! What is your name?')
    myName = input()
    TOPRANGE = 30
    NUMBER = random.randint(1, TOPRANGE)
    print(f'Well, {myName}, I am thinking of a'
          f' number between 1 and {str(TOPRANGE)}.')

    while GUESSESTAKEN < 6:
        print('Take a guess.')
        # There are four spaces in front of print.
        guess = input()
        guess = int(guess)
        GUESSESTAKEN = GUESSESTAKEN + 1
        if guess < NUMBER:
            print('Your guess is too low.')
            # There are eight spaces in front of print.
        if guess > NUMBER:
            print('Your guess is too high.')
        if guess == NUMBER:
            break

    if guess == NUMBER:
        GUESSESTAKEN = str(GUESSESTAKEN)
        print(f'Good job, {myName}! You guessed my'
              f' number in {GUESSESTAKEN} guesses!')

    if guess != NUMBER:
        NUMBER = str(NUMBER)
        print(f'Nope. The number I was thinking of was {NUMBER}')


if __name__ == '__main__':
    main()
