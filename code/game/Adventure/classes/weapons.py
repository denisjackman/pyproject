"""
    Use tunnels and trolls as the basis of the game engine
    Update the system to use metric system (metres and kilos)
    tabulate the creature, races and equipment
"""


class Equipment:
    name = ""


class Weapon:
    # taken from here
    # http://5edndwiki.wikidot.com/equipment-weapons
    # modified as noted
    name = ""
    # price should be in GP
    # 1gp = 1
    # 1sp = .1
    # 1cp = .01
    price = 0

    damage = 0
    damage_type = ""
    # weight should be kg
    weight = 0
    properties = ""
    group = ""
    weapon_type = ""


class Race:
    # taken from http://www.onrpg.com/boards/threads/14942-Basic-Races-and-Classes
    """
    Human
    Dwarf
    Elf
    Halfling
    Gnome
    Orc
    Goblin
    Drow (or Dark Elf)
    Troll
    """
    name = ""


class Creature:
    # taken from
    """
    Rat
    Snake
    Wolf
    Slug
    Bat
    Giant Ant
    Scorpion
    Spider
    Wasps
    Bees
    """
    name = ""
