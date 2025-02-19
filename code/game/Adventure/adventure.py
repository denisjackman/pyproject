#!/usr/bin/env python
'''
adventure.py
    This is the main game source.
    It is based on Tunnels and Trolls
    and particularly the Goblin Lake solo scenario.
    This is done as an exercise in python and development.
'''
from __future__ import annotations

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 2.0 $"
__date__ = "$Date: 2019/09/20 00:00:00 $"
__copyright__ = "Copyright (c) 2018 Denis J Jackman"
__license__ = "Python"

import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../../..'))
# Adventure game classes and imports
from jackmanimation.advclasses.equipment import Clothes
from jackmanimation.advclasses.race import Human
from jackmanimation.advclasses.weapons import Broadsword, CommonSpear, Crossbow, Dirk
from jackmanimation.advclasses.creature import Bat, Bee, GiantAnt, Rat, Scorpion
from jackmanimation.advclasses.playerclass import Mage, Warrior
from jackmanimation.advclasses.player import GamePlayer as Player
from jackmanimation.advclasses.magicspells import Bubble, Hail
# custom number generator
from jackmanimation.DndProject.dnddice import number_generator

# variable defaults
PLAYER_STATS = ''
WORLDWIDTH = 10
WORLDHEIGHT = 10

player_class = [Warrior(), Mage()]
weapons_list = [Broadsword(), CommonSpear(), Crossbow(), Dirk()]
creatures_list = [Bat(), Bee(), GiantAnt(), Rat(), Scorpion()]
spell_list = [Bubble(), Hail()]
newplayer = Player()
world_map = [
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None]
            ]


def main():
    '''
        Main Function
    '''
    print('[ ] MAIN ')
    game_start()
    player_name = input("[-] Please Enter your name: ")
    generate_player(player_name)
    # print the introduction
    game_intro(player_name)
    game_main()
    # exit the game
    game_end(player_name)
    print('[ ] END')


def check_tile(x_coord, y_coord):
    '''
        check tile function
    '''
    result = False
    print(f"[-] checking tile {x_coord} {y_coord}")
    if world_map[x_coord][y_coord] == ' ':
        print(f"[-] tile {x_coord} {y_coord} is empty")
        result = True
    return result


def game_start():
    '''
        game start function
    '''
    print('[ ] GAME START')


def game_intro(input_name):
    '''
        game intoduction function
    '''

    print('[ ] GAME INTRO')
    print(input_name, "here we go!")

    print('[ ] loading equipment ')
    # equipment is listed as name, weight (in wu), cost (in gp)
    equipment = Clothes()
    equipment_list = []
    equipment_list.append(equipment)

    print('[ ] loading races')
    race = Human()
    race_list = []
    race_list.append(race)


def game_end(input_name):
    '''
        game end function
    '''
    print(f"[-] {input_name} goodbye and thanks for playing !O")
    print('[ ] GAME OVER')


def generate_player(input_name):
    '''
        generate player function
    '''
    print('[+] GENERATING THE PLAYER')
    print(f"[+] {input_name} here you go.")

    # TODO: generate the player statistics
    # TODO: choose the class and race
    # TODO: Display the Player data to the player


def game_main():
    '''
        main game function
    '''
    for item in weapons_list:
        print(f"[-] I have a {item.name}")
    for item in creatures_list:
        print(f"[-] I see a {item.name}")
    for item in player_class:
        print(f"[-] I am a {item.name}")
    for item in spell_list:
        roll = number_generator()
        if roll > item.castscore:
            print(f"[-] I cannot cast a {item.name} "
                  f"spell ({roll}) vs ({item.castscore})")
        else:
            print(f"[-] I can cast a {item.name} spell "
                  f"({roll}) vs ({item.castscore})")


if __name__ == '__main__':
    main()
