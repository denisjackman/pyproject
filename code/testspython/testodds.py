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
from djgamemodule import oddsnsods as odd

def main():
    '''
        this is the main module
    '''
    print("starting")

    print("ELO Rating test")
    playera = 1000
    playerb = 1000
    print(" A (" + str(playera) + ") vs B (" + str(playerb) + ")")
    oplayera = odd.new_rating(playera,  playerb, "Win")
    oplayerb = odd.new_rating(playera, playerb, "Lose")
    playera = oplayera
    playerb = oplayerb
    print(" A ("+str(playera)+") vs B (" + str(playerb) + ")")
    oplayera = odd.new_rating(playera, playerb, "Win")
    oplayerb = odd.new_rating(playera, playerb, "lose")
    playera = oplayera
    playerb = oplayerb
    print(" A (" + str(playera)+") vs B (" + str(playerb) + ")")
    print("Random Name Generator")
    kernu = odd.generate_name(20)
    mernu = odd.generate_name(20)
    print("Greetings Earthfolk, I am", kernu, " of the planet", mernu)
    print("Object Distance test")
    check1 = odd.dist([10, 0], [0, 0])
    check2 = odd.dist([0, 0], [100, 100])
    print("dist([10,0],[0,0]),10", check1, 10, check1 == 10)
    print("dist([0,0],[100,100]),141.421356237", check2,
          141.4213562373095, check2 == 141.4213562373095)
    print("Rating test check")
    print("Win  (1000) :  1400 " + str(odd.rating(1000, 1, 0, 1)))
    print("Draw (1000) : 1000 " + str(odd.rating(1000, 0, 0, 1)))
    print("Win 2 * 1000 : 1400 " + str(odd.rating(2000, 2, 0, 2)))
    print("----")
    print("player 1 (1000 wins) " + str(odd.rating(1000, 1, 0, 1)))
    print("player 2 (1000 loses) " + str(odd.rating(1000, 0, 1, 1)))
    print("player 1 (600 wins again) " + str(odd.rating(600, 1, 0, 1)))
    print("finishing")


if __name__ == '__main__':
    main()
