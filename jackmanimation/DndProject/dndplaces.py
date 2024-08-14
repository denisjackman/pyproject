''' dnd places module '''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/25 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"
import platform
import json
from random import choice
from djgamemodule import dice as Dice
if platform.system() == "Windows":
    DNDP_FILEPATH = "Z:/Resources/development"
else:
    DNDP_FILEPATH = "/mnt/y/Resources/development"
# pylint: disable=too-many-locals


def town_name_generator():
    '''Generates a town name'''
    with open(f"{DNDP_FILEPATH}/referencedata/TownNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)

    result = ''
    roll = Dice.dice(4)
    affix = choice(data['town_name_affix'])
    prefix = choice(data['town_name_prefix'])
    suffix = choice(data['town_name_suffix'])

    if roll == 1:
        result = f"{affix} {prefix}{suffix}"
    elif roll == 2:
        result = f"{prefix} {suffix}"
    else:
        result = f"{prefix}{suffix}"
    return result.title()


def woodname_generator():
    '''Generates a wood name'''
    result = ''
    with open(f"{DNDP_FILEPATH}/referencedata/WoodNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    prefix = choice(data['wood_name_prefix'])
    suffix = choice(data['wood_name_suffix'])
    result = f"{prefix}{suffix}"
    return result.title()


def streetname_generator():
    '''Generates a street name'''
    result = ''
    with open(f"{DNDP_FILEPATH}/referencedata/StreetNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    prefix = choice(data['street_name_prefix'])
    suffix = choice(data['street_name_suffix'])
    result = f"{prefix}{suffix}"
    return result.title()


def dwarven_settlement_name_generator():
    '''Generates a dwarven settlement name'''
    result = ''
    with open(f"{DNDP_FILEPATH}/referencedata/DwarvenSettlementNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(10)
    community = choice(data['dwarven_settlement_community'])
    prefix = choice(data['dwarven_settlement_prefix'])
    suffix = choice(data['dwarven_settlement_suffix'])

    if roll <= 4:
        result = f"The {community} of {prefix}{suffix}"
    else:
        result = f"{prefix}{suffix} {community}"
    return result


def place_name_generator():
    '''Generates a place name'''
    result = ''
    with open(f"{DNDP_FILEPATH}/referencedata/PlaceNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(2)
    if roll == 0:
        prefix = choice(data['place_name_prefix_1'])
        suffix = choice(data['place_name_suffix_1'])
    elif roll == 1:
        prefix = choice(data['place_name_prefix_2'])
        suffix = choice(data['place_name_suffix_2'])
    else:
        prefix = choice(data['place_name_prefix_3'])
        suffix = choice(data['place_name_suffix_3'])
    result = f"{prefix}{suffix}"
    return result.title()


def inn_name_generator():
    '''Generates an Inn Name'''
    with open(f"{DNDP_FILEPATH}/referencedata/InnNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(16)
    result = ''
    name = ''
    adj = choice(data["inn_adj"])
    adj2 = choice(data["inn_adj2"])
    adj3 = choice(data["inn_adj3"])
    item = choice(data["inn_item"])
    item2 = choice(data["inn_item2"])
    blding = choice(data["inn_bdlg"])
    person = choice(data["inn_person"])
    creature = choice(data["inn_creature"])
    place = choice(data["inn_place"])

    if roll <= 2:
        name = f'{adj} {creature}'
    elif roll == 3:
        name = f'{adj2} {creature}'
    elif roll == 4:
        name = f'{adj} {item}'
    elif roll == 5:
        name = f'{adj3} {item}'
    elif roll == 6:
        name = f'{adj} {person}'
    elif roll == 7:
        name = f'{adj2} {person}'
    elif roll == 8:
        name = f'{adj} {place}'
    elif roll == 9:
        newcreature = choice(data["inn_creature"])
        name = f'{creature} and {newcreature}'
    elif roll == 10:
        name = f"{creature}'s {item}"
    elif roll == 11:
        name = f"{creature}'s {item2}"
    elif roll == 12:
        name = f"{creature}'s {place}"
    elif roll == 13:
        newitem = choice(data["inn_item"])
        name = f"{item} and {newitem}"
    elif roll == 14:
        newperson = choice(data["inn_person"])
        name = f"{person} and {newperson}"
    elif roll == 15:
        name = f"{person}'s {item}"
    else:
        name = f"{person}'s {place}"

    result = f"The {name}"
    if Dice.dice(2) == 2:
        result = f'{result} {blding}'
    result = result.title().replace("'S", "'s").replace("And", "and")
    return result


def site_name_generator():
    '''Generates a random site name'''
    result = ''
    with open(f"{DNDP_FILEPATH}/referencedata/SiteNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(3)
    if roll == 1:
        result = f"{choice(data['site_place'])} of {choice(data['site_thing'])}"
    elif roll == 2:
        result = f"{choice(data['site_adj'])} {choice(data['site_place'])}"
    else:
        result = f"{choice(data['site_adj'])} {choice(data['site_place'])} of {choice(data['site_thing'])}"
    return result


def main():
    ''' main function '''
    print(f"Town Name               : {town_name_generator()}")
    print(f"Wood Name               : {woodname_generator()}")
    print(f"Street Name             : {streetname_generator()}")
    print(f"Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
    print(f"Place Name              : {place_name_generator()}")
    print(f'Inn Name                : {inn_name_generator()}')
    print(f"Site Name               : {site_name_generator()}")


if __name__ == '__main__':
    main()
