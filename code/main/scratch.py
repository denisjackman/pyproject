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
import math

#pylint: disable=wrong-import-position
MODULE_PATH = "../jackmanimation/"
sys.path.append(os.path.abspath(MODULE_PATH))
from jackmanimation import number_generator
#pylint: enable=wrong-import-position

# Measure of Memory
KILOBYTE = 1024
MEGABYTE = 1024 * KILOBYTE
GIGABYTE = 1024 * MEGABYTE
TERABYTE = 1024 * GIGABYTE
PETABYTE = 1024 * TERABYTE
EXABYTE = 1024 * PETABYTE
ZETTABYTE = 1024 * EXABYTE
YOTTABYTE = 1024 * ZETTABYTE

# Time Items
MONTHS_IN_A_YEAR = 12
WEEKS_IN_A_YEAR = 52
DAYS_IN_A_WEEK = 7
HOURS_IN_A_DAY = 24
MINUTES_IN_A_HOUR = 60
SECONDS_IN_A_MINUTE = 60
MILLISECONDS_IN_A_SECOND = 1000

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


def dist(pont1, pont2):
    '''
    Measure the distance between two spots
    '''
    res = 0
    res = math.sqrt((pont1[0] - pont2[0]) ** 2 + (pont1[1] - pont2[1]) ** 2)
    return res


def collide(pos1, pos2, rad1, rad2):
    '''
        check for a collision between two objects
    '''
    result = False
    object1 = dist(pos1, pos2)
    object2 = rad1 + rad2
    result = object1 <= object2
    return result


def rating(total_rating, player_wins, player_losses, player_games):
    '''
    This is a function to return a performance rating for a player
    you pass the total rating for the players played
    the number of wins
    number of losses
    number of games
    and it calculates and return the new rating
    a win  - rating(1000,1,0,1) should return 1400
    a draw - rating(1000,0,0,1)
    a win against 2 players (2 * 1000) rating(2000,2,0,2)) should return 1400
    '''
    rating_new = (total_rating) + 400
    rating_new = rating_new * (player_wins - player_losses)
    rating_new = rating_new / player_games
    return rating_new


def main():
    '''
        this is the main module
    '''
    print("starting")

    print("ELO Rating test")
    playera = 1000
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
    print("Random Name Generator")
    kernu = generate_name(20)
    mernu = generate_name(20)
    print("Greetings Earthfolk, I am", kernu, " of the planet", mernu)
    print("Insult generator test")
    loop = 0
    while loop < 101:
        print(str(loop) + ": " + insult_generator())
        loop = loop + 1
    print("Object Distance test")
    check1 = dist([10, 0], [0, 0])
    check2 = dist([0, 0], [100, 100])
    print("dist([10,0],[0,0]),10", check1, 10, check1 == 10)
    print("dist([0,0],[100,100]),141.421356237", check2,
          141.4213562373095, check2 == 141.4213562373095)
    print("Rating test check")
    print("Win  (1000) :  1400 " + str(rating(1000, 1, 0, 1)))
    print("Draw (1000) : 1000 " + str(rating(1000, 0, 0, 1)))
    print("Win 2 * 1000 : 1400 " + str(rating(2000, 2, 0, 2)))
    print("----")
    print("player 1 (1000 wins) " + str(rating(1000, 1, 0, 1)))
    print("player 2 (1000 loses) " + str(rating(1000, 0, 1, 1)))
    print("player 1 (600 wins again) " + str(rating(600, 1, 0, 1)))
    print("finishing")


if __name__ == '__main__':
    main()