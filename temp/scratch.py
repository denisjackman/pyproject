#!/usr/bin/env python
"""
scratch.py
    this is a scratch utility for trying stuff out prior to folding it
    in elsewhere.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.0 $"
__date__ = "$Date: 2022/06/14 16:38:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
from random import randint
import os
import sys
#pylint: disable=wrong-import-position
MODULE_PATH = "../module/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import number_generator
#pylint: enable=wrong-import-position

# Measure of Memory
KiloByte = 1024
MegaByte = 1024 * KiloByte
GigaByte = 1024 * MegaByte
TeraByte = 1024 * GigaByte
PetaByte = 1024 * TeraByte
ExaByte = 1024 * PetaByte
ZettaByte = 1024 * ExaByte
YottaByte = 1024 * ZettaByte

# Time Items
MonthsInYear = 12
WeeksInYear = 52
DaysInWeek = 7
HoursInDay = 24
MinutesInHour = 60
SecondsInMinutes = 60
MillsecondsInSeconds = 1000

# Tuples
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", " Saturday",
        "Sunday")
MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December")
SEASONS = ("Spring", "Summer", "Autumn", "Winter")
ZODIACS = ("Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra",
           "Scorpio", "Sagittarius", "Capricornus", "Aquarius", "Pisces")
CHINESEYEARS = ("Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse",
                "Goat", "Monkey", "Rooster", "Dog", "Pig")
THREESTOOGES = ("Larry", "Moe", "Curly")
# Dictionaries
WereEaglesDare = {"Traitor:Renegade", "Punk:SecondRate"}
PHONETIC_ALPHABET = {"a": "Alpha", "b": "Bravo", "c": "Charlie", "d": "Delta",
                     "e": "Echo", "f": "Foxtrot", "g": "Golf", "h": "Hotel",
                     "i": "India", "j": "Juliet", "k": "Kilo", "l": "Lima",
                     "m": "Mike", "n": "November", "o": "Oscar", "p": "Papa",
                     "q": "Quebec", "r": "Romeo", "s": "Sierra", "t": "Tango",
                     "u": "Uniform", "v": "Victor", "w": "Whiskey",
                     "x": "X-ray", "y": "Yankee", "z": "Zulu"}
NUMBERS = {0: "ZERO", 1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE",
           6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE"}

# Cards
SUITS = ("Club", "Spades", "Hearts", "Diamonds")
RANKS = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen", "King")
SHORTSUITS = ('C', 'S', 'H', 'D')
SHORTRANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
CARDVALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

# Compass points
COMPASSPOINTS = ["North", "East", "South", "West"]
DIRECTIONS = ["Left", "Right", "Up", "Down"]


def new_rating(player_rating, opponent_rating, game_result):
    '''
        ELO rating scoring system
        The function takes the current player rating.
        The opponets rating along with the game result
        and calculates the new rating based on the ELO formula.
    '''
    game_result = game_result.lower()
    chance_of_winning = int((1 / (1 + (pow(10,
                            ((opponent_rating - player_rating)/400))))) * 100)
    chance_of_losing = 100 - chance_of_winning
    k_factor = 32
    win_points = int(round(k_factor * (chance_of_losing / 100.0)))
    lose_points = int(round(k_factor * (chance_of_winning / 100.0)))
    if game_result == "win":
        result = player_rating + win_points
    else:
        result = player_rating - lose_points
    return result


def generate_name(number=100):
    ''' generates a random name '''
    number = min(number, 255)
    result = ""
    for _ in range(number):
        random_number = randint(97, 122)
        result += chr(random_number)
    return result


def insult_generator():
    '''
    Author : Denis Jackman
    Date : 31-July-2013
    Version : 1.0
    Function :
    This is a random insult generator based on Shakespearean lines.
    There are three (3) columns of Insult terms.
    Which are built then into an insult.
    This is pre-fixed with 'Thou'

    There are no inputs. The output is the insult as a string (result)
    '''
    result = "Thou"
    # Each Column is used to build the insult
    column_one = ("artless", "bawdy", "beslubbering", "bootless", "churlish",
                  "cockered", "clouted", "craven", "currish", "dankish",
                  "dissembling", "droning", "errant", "fawning", "fobbing",
                  "froward", "frothy", "gleeking", "goatish", "gorbellied",
                  "impertinent", "jarring", "loggerheaded", "lumpish")
    column_two = ("base-court", "bat-fowling", "beef-witted", "beetle-headed",
                  "boil-brained", "clapper-clawed", "clay-brained",
                  "common-kissing", "crook-pated", "dismal-dreaming",
                  "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing",
                  "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed",
                  "fly-bitten", "folly-fallen", "fool-born", "full-gorged",
                  "guts-griping", "half-faced", "hasty-witted")
    column_three = ("apple-john", "baggage", "barnacle", "bladder", "boar-pig",
                    "bugbear", "bum-bailey", "canker-blossom", "clack-dish",
                    "clotpole", "coxcomb", "codpiece", "death-token",
                    "dewberry", "flap-dragon", "flax-wench", "flirt-gill",
                    "foot-licker", "fustilarian", "giglet", "gudgeon",
                    "haggard", "harpy", "hedge-pig", "horn-beast")
    # generate the random numbers based on the len of the lists
    xero = number_generator(len(column_one)-1)
    yero = number_generator(len(column_two)-1)
    zero = number_generator(len(column_three)-1)
    # build the results
    result = result + " " + column_one[xero]
    result = result + " " + column_two[yero] + " " + column_three[zero] + "."
    # return it
    return result


def main():
    '''
        this is the main module
    '''
    print("starting")
    playera = 500
    playerb = 1000
    print(" A (" + str(playera) + ") vs B (" + str(playerb) + ")")
    oplayera = new_rating(playera,  playerb, "Win")
    oplayerb = new_rating(playera, playerb, "Lose")
    playera = oplayera
    playerb = oplayerb
    print(" A ("+str(playera)+") vs B (" + str(playerb) + ")")
    oplayera = new_rating(playera, playerb, "Win")
    oplayerb = new_rating(playera, playerb, "lose")
    playera = oplayera
    playerb = oplayerb
    print(" A (" + str(playera)+") vs B (" + str(playerb) + ")")
    kernu = generate_name(20)
    mernu = generate_name(20)
    print("Greetings Earthfolk, I am", kernu, " of the planet", mernu)
    loop = 0
    while loop < 101:
        print(str(loop) + ": " + insult_generator())
        loop = loop + 1

    print("finishing")


if __name__ == '__main__':
    main()
