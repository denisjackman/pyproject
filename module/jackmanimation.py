#!/usr/bin/python
"""
jackmanimation.py

This program is a template for python programs
All this stuff at the top of the script is just optional metadata;

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.1 $"
__date__ = "$Date: 2022/06/14 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import json
import random


def dice(sides=6, rolls=1):
    '''
    Rolls a dice which has 'sides' sides (default is six (6))
    for 'rolls' number of times (default is one (1))
    '''
    result = 0
    loop = 0
    while loop < rolls:
        result = result + random.randrange(1, sides+1)
        loop = loop + 1
    return result


def number_generator(number=100):
    '''
    Generates a random number between 1 and number
    '''
    return random.randint(1, number)


def credscheck(file_details):
    """ This function gathers the credentials needed to open anything """

    credentials = file_details
    try:
        with open(credentials, encoding="utf8") as creds_file:
            creds = json.load(creds_file)
    except OSError as err:
        message = f'Danger! Danger! Will Robinson!: {err}'
        print(message)
    else:
        print("Secrets loaded OK")

    return creds


def fileread(filename):
    """ this is a file read function """
    result = []
    with open(filename, 'r',  encoding="utf8") as inputfile:
        for item in inputfile:
            result.append(item)
    inputfile.close()
    return result


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    testcreds = credscheck("credtest.json")
    if (testcreds["checkTest"] == "test") and (len(fileread("test.txt")) == 5):
        print('All systems nominal')
    loop = 0
    count = 0
    dice_count = 0
    while loop < 101:
        dice_count = dice_count + dice()
        count = count + number_generator()
        loop = loop + 1
    print(" Average Dice roll           : " + str(int(dice_count/101)))
    print(" Average Number generator    : " + str(int(count/101)))
    print(" Dice roll one six sided     : " + str(dice()))
    print(" Dice roll one hundred sided : " + str(dice(100)))
    print(" Dice roll five six sided    : " + str(dice(rolls=5)))
    print(" Dice roll ten four sided    : " + str(dice(4, 10)))
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
