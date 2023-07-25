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

import advclasses.weapons as Weapons
#from advclasses.weapons import Bludgeon
from advclasses.equipment import Clothes
from advclasses.race import Human
from advclasses.creature import Bat, Bees, GiantAnt, Rat, Scorpion

# variable defaults
player_class = ["Warrior", "Mage"]
PLAYER_STATS = ''
weapons_list = []
creatures_list = []

def main():
    '''
        Main Function
    '''
    print('[ ] MAIN ')
    game_start()
    PLAYER_NAME = input("[-] Please Enter your name: ")
    generate_player(PLAYER_NAME)
    # print the introduction
    game_intro(PLAYER_NAME)
    game_main()
    # exit the game
    game_end(PLAYER_NAME)
    print('[ ] END')

def load_weapons():
    '''
        load weapons function
    '''
    # weapons are listed as name, dice, adds, wpnstr, dex, cost, weight, range, handed
    print("[-] loading weapons start")
    result = []
    result.append(Weapons.Bludgeon())
    result.append(Weapons.Broadsword())
    result.append(Weapons.CommonSpear())
    result.append(Weapons.Crossbow())
    result.append(Weapons.Dirk())
    print("[-] loading weapons done")
    return result

def load_creatures():
    '''
        load creatures function
    '''
    print("[-] loading creatures start")
    result = []
    result.append(Bat())
    result.append(Bees())
    result.append(GiantAnt())
    result.append(Rat())
    result.append(Scorpion())
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
    global weapons_list
    global creatures_list
    
    print('[ ] GAME INTRO')
    print(input_name, "here we go!")

    print('[ ] loading weapons  ')
    weapons_list = load_weapons()

    print('[ ] loading equipment ')
    # equipment is listed as name, weight (in wu), cost (in gp)
    equipment = Clothes()
    equipment_list = []
    equipment_list.append(equipment)

    print('[ ] loading races')
    race = Human()
    race_list = []
    race_list.append(race)

    print('[ ] loading creature')
    creatures_list = load_creatures()



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
if __name__ == '__main__':
    main()
