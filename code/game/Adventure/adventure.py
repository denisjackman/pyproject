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

# from djgamemodule import dice
# from djgamemodule import gamemodule
# from currency import *
# from weight import *
from advclasses.weapons import Weapon
from advclasses.equipment import Equipment
from advclasses.race import Race
from advclasses.creature import Creature

# variable defaults
player_class = ["Warrior", "Mage"]

PLAYER_STATS = ''

def main():
    '''
        Main Function
    '''
    print(' --- MAIN --- ')
    game_start()
    PLAYER_NAME = input("Please Enter your name: ")
    generate_player(PLAYER_NAME)
    # print the introduction
    game_intro(PLAYER_NAME)
    game_main()
    # exit the game
    game_end(PLAYER_NAME)
    print('--- END ---')


def game_start():
    '''
        game start function
    '''
    print('--- GAME START ---')


def game_intro(input_name):
    '''
        game intoduction function
    '''
    print('--- GAME INTRO ---')
    print(input_name, "here we go!")

    print('--- loading weapons --- ')
    wpn=[]
    wpn.append(Weapon("Bludgeon",3,0,5,2,15,50))
    wpn.append(Weapon("Broadsword",3,4,15,10,70,120))
    wpn.append(Weapon("Common Spear",3,1,8,8,22,50,40))
    wpn.append(Weapon("Crossbow",5,0,15,10,250,180,100,True))
    wpn.append(Weapon("Dirk",2,1,1,4,18,16,10))
    wpn.append(Weapon("Doublebitted Axe",6,3,21,10,140,220,0,True))
    wpn.append(Weapon("Falchion",4,4,12,13,75,110))
    wpn.append(Weapon("Great Sword",6,0,21,18,120,170,0,True))
    wpn.append(Weapon("Heavy Mace",5,2,17,3,120,200,0,True))
    wpn.append(Weapon("Medium Longbow",4,3,15,15,100,60,140,True))
    wpn.append(Weapon("Quarterstaff",2,0,2,8,10,50,0,True))
    wpn.append(Weapon("Sax (Dagger)",2,5,7,10,30,25))
    wpn.append(Weapon("Scimitar",4,0,10,11,60,100))
    wpn.append(Weapon("Short Sword",3,0,7,3,35,30))
    wpn.append(Weapon("Trident",4,3,10,10,60,75,10))
    wpn.append(Weapon("Very Light Bow",2,0,9,15,50,30,60,True))


    print('--- loading equipment --- ')
    # equipment is listed as name, weight (in wu), cost (in gp)
    equipment_list = []
    equipment_list.append(Equipment("Warm dry clothing and Pack", 10, 5))
    equipment_list.append(Equipment("Provisions", 20, 10))
    equipment_list.append(Equipment("Delver's Package", 20, 20))
    equipment_list.append(Equipment("Torch", 10, .1))
    equipment_list.append(Equipment("Rope, Silk, 1ft", 1, 1))
    equipment_list.append(Equipment("Rope, Hemp, 1ft", 5, .1))
    equipment_list.append(Equipment("Lantern and Oil", .10, .1))
    equipment_list.append(Equipment("Spare Skin of Oil", 15, 10))
    equipment_list.append(Equipment("Magnetic compass", 1, 15))
    equipment_list.append(Equipment("Boots, knee high", 40, 10))
    equipment_list.append(Equipment("Boots, calf high", 20, 5))
    equipment_list.append(Equipment("Sandals", 2, 2))
    equipment_list.append(Equipment("Pitons (10)", 25, 10))
    equipment_list.append(Equipment("Piton Hammer", 25, 4))
    equipment_list.append(Equipment("Ordinary Magic Staff", 30, 100))
    equipment_list.append(Equipment("Deluxe Magic Staff", 30, 5000))


    print('--- loading races --- ')
    races = []
    races.append(Race("Human"))
    races.append(Race("Dwarf"))
    races.append(Race("Elf"))
    races.append(Race("Halfling"))
    races.append(Race("Gnome"))
    races.append(Race("Orc"))
    races.append(Race("Goblin"))
    races.append(Race("Drow"))
    races.append(Race("Dark Elf"))
    races.append(Race("Troll"))

    print('--- loading creature ---')
    creatures = []
    creatures.append(Creature("Rat"))
    creatures.append(Creature("Snake"))
    creatures.append(Creature("Wolf"))
    creatures.append(Creature("Slug"))
    creatures.append(Creature("Bat"))
    creatures.append(Creature("Giant Ant"))
    creatures.append(Creature("Scorpion"))
    creatures.append(Creature("Spider"))
    creatures.append(Creature("Wasps"))
    creatures.append(Creature("Bees"))


def game_end(input_name):
    '''
        game end function
    '''
    print(input_name, " goodbye and thanks for playing !O")
    print('--- GAME OVER ---')


def generate_player(input_name):
    '''
        generate player function
    '''
    print('--- GENERATING THE PLAYER ---')
    print(input_name, " here you go.")
    # TODO: generate the player statistics
    # TODO: choose the class and race
    # TODO: Display the Player data to the player


def game_main():
    '''
        main game function
    '''

if __name__ == '__main__':
    main()
