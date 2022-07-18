#!/usr/bin/python
'''
    NAME: snake game

    SETUP:
    27 rows of 20 squares (540 in total)
    each square is 16 pixels by 16 pixels

    CONCEPT:
    The snake starts with 5 squares
    when it eat a food it adds a square
    if it does not eat in a number of cycles it shrinks
    after it has eaten new food appears
    if the snake goes out of bounds it dies
    if it touches itself it dies
    if all the squares are snake then it resets to 5.
    Each piece of food eaten adds one to the score

    CONTROLS:
    arrow keys changes the direction of travel.
    each cycle moves the snake in the direction of travel

    TECHNICAL:
    Using python (latest) and pygame (latest).

    REFERENCES:
    [Original Instagram Idea](https://www.instagram.com/p/Cf3iNhOjeOx/)
    [Mechanics](https://www.kosbie.net/cmu/fall-10/15-110/handouts/snake/snake.html)
    [mechanics](https://technologies4.me/articles/snake-game-a32/snake-game-concept-mechanics-77/)
    [Mechanics](https://microsoft.github.io/tilecode/doc/mechanics.html)
    [how to](https://www.instagram.com/p/CHXliT1gTfq/?igshid=YmMyMTA2M2Y=)
    [How to](https://www.instagram.com/p/CUHbqHDjKYQ/?igshid=YmMyMTA2M2Y=)

'''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/07/17 09:27:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
# colours
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)


def snake_main():
    '''
        main routine for the snake game
    '''
    numberofsquares = 540
    numberinrow = 20
    squaresize = 16
    score = 0
    squarecolour = GRAY
    snakecolour = WHITE
    foodcolour = GREEN


if __name__ == '__main__':
    snake_main()
