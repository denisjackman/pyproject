'''
random element generator
'''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from random import randint


def dice(sides=6, rolls=1):
    '''
        Rolls a dice which has 'sides' sides (default is six (6))
        for 'rolls' number of times (default is one (1))
    '''
    result = 0
    item = 0
    while item in range(rolls):
        result = result + randint(1, sides)
        item += 1
    return result


def number_generator(number=100):
    '''
        Generates a random number between 1 and number
    '''
    return randint(1, number)


def main():
    ''' main function'''
    print(f"Dice                    : {dice()}")
    print(f'Number Generator        : {number_generator()}')


if __name__ == '__main__':
    main()
