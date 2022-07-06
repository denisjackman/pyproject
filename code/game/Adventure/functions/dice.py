#!/usr/bin/python
"""
dice.py
    This rolls a dice
"""
import random

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2016/03/05 00:00:00 $"
__copyright__ = "Copyright (c) 2016 Denis J Jackman"
__license__ = "Python"


def dice(sides=6, rolls=1):
    """
    Rolls a dice
    :param sides: the number of sides for a dice (default is six (6) )
    :param rolls: the number of rolls to be made for a dice (default is one (1))
    """
    result = 0
    for roll in range(0, rolls):
        result = result + random.randrange(1, sides+1)
    return result


def numgen(number=100):
    '''
        number generator
    '''
    return random.randint(1, number)


if __name__ == '__main__':
    print(" Dice roll one six sided     : " + str(dice()))
    print(" Dice roll one hundred sided : " + str(dice(100)))
    print(" Dice roll five six sided    : " + str(dice(rolls=5)))
    print(" Dice roll ten four sided    : " + str(dice(4, 10)))
    for _ in range(1, 1000):
        jolder = dice()
        if jolder > 6:
            print(" oops")
        if jolder < 1:
            print(" whhooops")
