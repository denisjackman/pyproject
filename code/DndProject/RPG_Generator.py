'''
    Name : RPG_Generator.py

    Function :
    This is a RPG Games master tool.
    It is a swiss army knife of random generators, and other tools.

    It has in it currently:
        a Dice function
        a number generator
        a riddle generator
        a Shakepspearean Insult generator
        a Dwarven insult generator
        various naming generators
        a currency converter

    Working on:
        Oracle Generator

    References:
        https://www.dndspeak.com/
        https://www.reddit.com/r/d100/new/
        https://stephthedev.com/dnd-exchange-rate
        https://stephthedev.com/dnd-travel-calculator

    Notes:
        This is a work in progress.
'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from pathlib import Path
import json
from random import choice
from dnddice import dice
from dndinsult import shakespearean_insult_generator
from dndinsult import dwarven_insult_generator
from dndother import currency_converter
from dndother import riddle_generator
from dndother import fantasy_wine_name
from dndother import hexmap_tile_type

FILEPATH = Path(__file__).parent
# pylint: disable=too-many-locals
# pylint: disable=too-many-lines

def angelic_name():
    ''' angelic names '''
    with open(f"{FILEPATH}/referencedata/AngelNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data['angel_prefix'])
    suffix = choice(data['angel_suffix'])
    result = f'{prefix}{suffix}'
    return result.capitalize()

def barbarian_name():
    ''' barbarian names '''
    with open(f"{FILEPATH}/referencedata/BarbarianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    roll = dice(2)
    if roll == 1:
        part1 = choice(data["barbarian_names"]).capitalize()
        part2 = part1
        while part1 == part2:
            part2 = choice(data["barbarian_names"])
        result = f'{part1}{part2}'
    else:
        prefix = choice(data["barbarian_prefix"]).capitalize()
        suffix = choice(data["barbarian_suffix"])
        result = f"{prefix} {suffix}"
    return result

def build_demon_name():
    ''' build a name '''
    with open(f"{FILEPATH}/referencedata/DemonNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    syllable = choice(data["demon_syllable"])
    roll = dice(7)
    if roll <= 2:
        result = f"'{syllable}"
    elif roll <= 3:
        result = f"-{syllable}"
    else:
        result = syllable
    return result

def demon_name_one():
    ''' demon name generator '''
    with open(f"{FILEPATH}/referencedata/DemonNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    syllable = choice(data["demon_syllable"])
    roll = dice(7)
    result = ''
    if roll <=4:
        result = build_demon_name() + build_demon_name()
    elif roll <=6:
        result = build_demon_name() + build_demon_name() + build_demon_name()
    else:
        result = build_demon_name() + build_demon_name() + build_demon_name() + build_demon_name()

    return f"{syllable.capitalize()}{result}"

def demon_name_two():
    ''' demon name generator'''
    with open(f"{FILEPATH}/referencedata/DemonNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    result = ''
    truename = ''
    usename = ''
    roll = dice(100)
    number = 0

    if roll <= 8:
        number = 1
    elif roll <= 18:
        number = 2
    elif roll <= 29:
        number = 3
    elif roll <= 42:
        number = 4
    elif roll <= 56:
        number = 5
    elif roll <= 71:
        number = 6
    elif roll <= 79:
        number = 7
    elif roll <= 86:
        number = 8
    elif roll <= 92:
        number = 9
    elif roll <= 96:
        number = 10
    elif roll <= 99:
        number = 11
    else:
        number = 12
    for _ in range(number):
        item = choice(data["demon_truename_elements"])
        truename = f'{truename}{item}'
    usename = f'{choice(data["demon_usename_elements"])}{choice(data["demon_usename_elements"])} {choice(data["demon_usename_elements"]).title()}{choice(data["demon_usename_elements"])}'
    result = f'{truename.capitalize()}({usename})'
    return result

def demon_name():
    ''' demon name generator '''
    if dice(2) == 1:
        return demon_name_one()
    return demon_name_two()

def dwarven_name(gender = None):
    ''' dwarven name generator '''
    firstname = ''
    lastname = ''

    with open(f"{FILEPATH}/referencedata/DwarvenNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    prefix = choice(data["dwarven_name_prefix"])
    suffixmale = choice(data["dwarven_name_suffixmale"])
    suffix = choice(data["dwarven_name_suffix"])
    clanprefix = choice(data["dwarven_clan_prefix"])
    clansuffix = choice(data["dwarven_clan_suffix"])

    if gender is None:
        if dice(2) == 1:
            female = False
            firstname = f'{prefix}{suffixmale}'
        else:
            female = True
            firstname = f'{prefix}{suffix}'
    elif gender.lower() == 'female':
        female = True
        firstname = f'{prefix}{suffixmale}'
    else:
        female = False
        firstname = f'{prefix}{suffixmale}'

    if dice(3) == 1:
        father = f'{prefix}{suffixmale}'
        if female:
            lastname = f"{father}ssdottir"
        else:
            lastname = f"{father}son"
    else:
        lastname = f'{clanprefix}{clansuffix}'

    result = f'{firstname.capitalize()} {lastname.capitalize()}'
    if female:
        result = f"{result} (f.)"
    return result

def town_name_generator():
    '''Generates a town name'''
    with open(f"{FILEPATH}/referencedata/TownNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    result = ''
    roll = dice(4)
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
    with open(f"{FILEPATH}/referencedata/WoodNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data['wood_name_prefix'])
    suffix = choice(data['wood_name_suffix'])
    result = f"{prefix}{suffix}"
    return result.title()

def streetname_generator():
    '''Generates a street name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/StreetNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data['street_name_prefix'])
    suffix = choice(data['street_name_suffix'])
    result = f"{prefix}{suffix}"
    return result.title()

def dwarven_settlement_name_generator():
    '''Generates a dwarven settlement name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/DwarvenSettlementNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(10)
    community = choice(data['dwarven_settlement_community'])
    prefix = choice(data['dwarven_settlement_prefix'])
    suffix = choice(data['dwarven_settlement_suffix'])

    if roll <= 4:
        result = f"The {community} of {prefix}{suffix}"
    else:
        result = f"{prefix}{suffix} {community}"
    return result

def book_title_generator(catalogue = False):
    '''Generates a book title'''
    result = ''
    with open(f"{FILEPATH}/referencedata/BookTitles.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(10)
    if roll == 1:
        #religious book
        newroll = dice(4)
        if newroll ==1:
            names = choice(data['names'])
            result = f"Life of Saint {names}"
        elif newroll == 2:
            relthings = choice(data['relthings']).capitalize()
            domain = choice(data['domain']).capitalize()
            rel = choice(data['rel']).capitalize()
            result = f"{relthings} to the {domain} {rel}"
        elif newroll == 3:
            adj = choice(data['adj']).capitalize()
            things = choice(data['things']).capitalize()
            domain = choice(data['domain']).capitalize()
            rel = choice(data['rel']).capitalize()
            result = f"{adj} {things} of the {domain} {rel}"
        else:
            things = choice(data['things']).capitalize()
            domain = choice(data['domain']).capitalize()
            rel = choice(data['rel']).capitalize()
            result = f"{things} of the {domain} {rel}"
        if catalogue:
            result = f"{result} (Religious)"
    elif roll == 2:
        # travel book
        travel = choice(data['travel']).capitalize()
        names = choice(data['names'])
        result = f"{travel} of {names}"
        if catalogue:
            result = f"{result} (Travel)"
    elif roll == 3:
        #biology book
        bioroll = dice(2)
        creature = choice(data['creature']).capitalize()
        if bioroll == 1:
            bio = choice(data['bio']).capitalize()
            result = f"{bio} of {creature}"
        else:
            things = choice(data['things']).capitalize()
            result = f"{creature} {things}"
        if catalogue:
            result = f"{result} (Biology)"
    elif roll == 4:
        #magick book
        magicroll = dice(4)
        adj = choice(data['adj'])
        arcana = choice(data['arcana'])
        things = choice(data['things'])
        regarding = choice(data['regarding'])
        if magicroll == 1:
            result = f"{adj} {arcana} {things}"
        elif magicroll == 2:
            result = f"{arcana} {things}"
        elif magicroll == 3:
            result = f"{adj} {things} {regarding} {arcana}"
        else:
            result = f"{things} {regarding} {arcana}"
        result = result.title()
        if catalogue:
            result = f"{result} (Magick)"
    elif roll == 5:
        #craftwork book
        guide = choice(data['guide']).capitalize()
        crafts = choice(data['crafts']).capitalize()
        result = f'{guide} {crafts}'
        if catalogue:
            result = f"{result} (Craftwork)"
    elif roll == 6:
        #tales book
        talesroll = dice(3)
        story = choice(data['story']).capitalize()
        adj2 = choice(data['adj2'])
        adj3 = choice(data['adj3'])
        place = choice(data['place']).capitalize()
        person = choice(data['person']).capitalize()
        if talesroll == 1:
            result = f"{story} of the {adj2} {place}"
        elif talesroll == 2:
            result = f"{story} of the {adj2} {person}"
        else:
            result = f"{story} of the {adj3} {person}"
        if catalogue:
            result = f"{result} (Tales)"
    elif roll == 7:
        #art book
        poettype = choice(data['poettype']).capitalize()
        poetry = choice(data['poetry']).capitalize()
        result = f'{poettype} {poetry}'
        if catalogue:
            result = f"{result} (Art)"
    elif roll == 8:
        #history  book
        historyroll = dice(4)
        history = choice(data['history']).capitalize()
        histtype = choice(data['histtype']).capitalize()
        things = choice(data['things']).capitalize()
        if historyroll == 1:
            result = f"{history} of the {histtype}"
        elif historyroll == 2:
            adj = choice(data['adj']).capitalize()
            result = f"{adj} {things} of the {histtype}"
        elif historyroll == 3:
            result = f"{things} of the {histtype}"
        else:
            fame = choice(data['fame']).capitalize()
            people = choice(data['people']).capitalize()
            result = f"{fame} {people} of the {histtype}"
        if catalogue:
            result = f"{result} (History)"
    elif roll == 9:
        #geography book
        georoll = dice(3)
        adj2 = choice(data['adj2']).capitalize()
        geo = choice(data['geo']).capitalize()

        if georoll == 1:
            result = f"{adj2} {geo} Atlas"
        elif georoll == 2:
            geothings = choice(data['geothings']).capitalize()
            result = f"{geothings} of the {adj2} {geo}"
        else:
            activity = choice(data['activity']).capitalize()
            result = f"{activity} in the {geo}"
        if catalogue:
            result = f"{result} (Geography)"
    else:
        #linguitics book
        lingroll = dice(2)
        language = choice(data['language']).capitalize()
        if lingroll == 1:
            lang = choice(data['language']).capitalize()
            result = f"{language} {lang}"
        else:
            dictionary = choice(data['dictionary']).capitalize()
            words = choice(data['words']).capitalize()
            result = f"{dictionary} of {language} {words}"
        if catalogue:
            result = f"{result} (Linguistics)"
    return result

def place_name_generator():
    '''Generates a place name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/PlaceNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(2)
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

def aoran(input_text_string):
    '''Returns a or an depending on the first letter of the string'''
    result = ''
    if input_text_string[0] in "aeiou":
        result =  f"an {input_text_string}"
    else:
        result = f"a {input_text_string}"
    return result

def plural(input_text_string):
    '''Returns a plural version of the string'''
    result = ''
    suffix = 's'
    if input_text_string[-1].lower() in 'sxz':
        suffix = 'es'
    if input_text_string[-2].lower() == 'ff':
        input_text_string = input_text_string[:-2]
        suffix = 'ves'
    if input_text_string[-1].lower() == 'f':
        input_text_string = input_text_string[:-1]
        suffix = 'ves'
    if input_text_string[-1].lower() == 'is':
        input_text_string = input_text_string[:-2]
        suffix = 'es'
    if input_text_string[-2].lower() in ('ch','sh'):
        suffix = 'es'
    if input_text_string[-1].lower() == 'y':
        input_text_string = input_text_string[:-1]
        suffix = 'ies'
    result = f"{input_text_string}{suffix}"
    return result

def coatofarms_generator():
    '''Generates a Coat of Arms'''
    with open(f"{FILEPATH}/referencedata/CoatArms.json", "r", encoding='utf8') as file:
        data = json.load(file)
    result = ''
    roll = dice()

    metal = choice(data["metal"])
    blazon1 = choice(data["blazon1"])

    if blazon1 == "Creature":
        blazon1 = choice(data["creatures"])
    blaz2roll = dice(3)
    if blaz2roll == 1:
        blaz2metal = choice(data["metal"])
        blaz2blaz1 = choice(data["blazon1"])
        if blaz2blaz1 == "Creature":
            blaz2blaz1 = choice(data["creatures"])
        blazon2 = f' and {aoran(blaz2metal)} {blaz2blaz1} '
    elif blaz2roll == 2:
        blaz2numwords = choice(data["numwords"])
        blaz2blaz1 = choice(data["blazon1"])
        if blaz2blaz1 == "Creature":
            blaz2blaz1 = choice(data["creatures"])
        blazon2 = f' and {blaz2numwords} {plural(choice(data["colour"]))} {blaz2blaz1} '
    else:
        blazon2 = ' '

    blaz3roll = dice(3)
    if blaz3roll == 1:
        blaz3colour = choice(data["colour"])
        blaz2blaz1 = choice(data["blazon1"])
        if blaz2blaz1 == "Creature":
            blaz2blaz1 = choice(data["creatures"])
        blazon3 = f' and {aoran(blaz3colour)} {blaz2blaz1} '
    elif blaz3roll == 2:
        blaz2numwords = choice(data["numwords"])
        blaz2blaz1 = choice(data["blazon1"])
        if blaz2blaz1 == "Creature":
            blaz2blaz1 = choice(data["creatures"])
        blazon3 = f' and {blaz2numwords} {choice(data["colour"])} {plural(blaz2blaz1)} '
    else:
        blazon3 = ' '


    colour = choice(data["colour"])
    numwords = choice(data["numwords"])

    if roll <= 2:
        result = f"{aoran(metal)} {blazon1}{blazon2}on a {colour} field"
    elif roll <= 4:
        result = f'{aoran(colour)} {blazon1}{blazon3}on a {metal} field'
    elif roll <= 5:
        result = f'{numwords} {metal} {plural(blazon1)}{blazon2}on a {colour} field'
    else:
        result = f'{numwords} {colour} {plural(blazon1)}{blazon3}on a {metal} field'

    return result

def elfname_generator():
    '''Generates an Elf Name'''
    with open(f"{FILEPATH}/referencedata/ElfNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    result = ''
    firstname = ""
    surname = f"{choice(data['elf_surname_prefix'])}{choice(data['elf_surname_suffix'])}"
    roll = dice()
    if roll <= 4:
        firstname = f"{choice(data['elf_prefix'])}{choice(data['elf_mid'])}{choice(data['elf_suffix'])}"
    elif roll <= 5:
        firstname = f"{choice(data['elf_prefix'])}{choice(data['elf_mid'])}{choice(data['elf_mid'])}{choice(data['elf_suffix'])}"
    else:
        firstname = f"{choice(data['elf_prefix'])}{choice(data['elf_suffix'])}"
    result = f"{firstname.capitalize()} {surname.capitalize()}"
    return result

def herb_name_generator():
    '''Generates a Herb Name'''
    with open(f"{FILEPATH}/referencedata/HerbNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    result = ''
    roll = dice(14)
    approll = dice()
    appsuff = ''
    if approll <= 5:
        appsuff = f" {choice(data['herb_suff'])}"
    else:
        appsuff = f"{choice(data['herb_suff'])}{choice(data['herb_suff'])}"

    if roll <= 5:
        result = f"{choice(data['herb_pref'])}{appsuff}"
    elif roll <= 7:
        result = f"{choice(data['herb_color'])}{choice(data['herb_pref'])}{appsuff}"
    elif roll <= 9:
        result = f"{choice(data['herb_color'])}{choice(data['herb_misc'])}"
    elif roll <= 10:
        result = f"{choice(data['herb_color'])}{choice(data['herb_suff'])}"
    elif roll <= 11:
        result = f"St. {choice(data['herb_name'])}'s {choice(data['herb_misc'])}"
    elif roll <= 12:
        result = f"{choice(data['herb_creature'])}'s {choice(data['herb_misc'])}"
    elif roll <= 13:
        result = f"{choice(data['herb_thing'])}'s {choice(data['herb_misc'])}"
    else:
        result = f"{choice(data['herb_adj'])} {choice(data['herb_misc'])}"
    return result.title().replace("'S", "'s")

def hyborian_name_generator():
    '''Generates a Hyborian Name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/HyborianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["hyborian_prefix"])
    suffix = choice(data["hyborian_suffix"])
    result = f"{prefix}{suffix}"
    return result

def inn_name_generator():
    '''Generates an Inn Name'''
    with open(f"{FILEPATH}/referencedata/InnNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(16)
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
    if dice(2) == 2:
        result = f'{result} {blding}'
    result = result.title().replace("'S", "'s").replace("And", "and")
    return result

def adventure_name_generator():
    '''Generates an Adventure Name'''
    with open(f"{FILEPATH}/referencedata/AdventureNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    result = ''
    roll = dice(40)
    action = choice(data["adventure_action"])
    monster = choice(data["adventure_monster"])
    if monster == 'creature':
        monster = choice(data["adventure_creature"])
    ruler = choice(data["adventure_ruler"])
    adjective = choice(data["adventure_adjective"])
    if adjective == 'color':
        adjective = choice(data["adventure_color"])
    building = choice(data["adventure_building"])
    name = choice(data["adventure_name"])
    place = choice(data["adventure_place"])
    colour = choice(data["adventure_color"])
    geography = choice(data["adventure_geography"])
    element = choice(data["adventure_element"])
    diety = choice(data["adventure_deity"])
    journey = choice(data["adventure_journey"])
    region = choice(data["adventure_region"])
    item = choice(data["adventure_item"])
    creature = choice(data["adventure_creature"])
    escape = choice(data["adventure_escape"])
    people = choice(data["adventure_people"])
    person = choice(data["adventure_person"])
    quest = choice(data["adventure_quest"])
    secret = choice(data["adventure_secret"])

    if roll == 1:
        result = f"{action.capitalize()} of the {monster} {ruler.title()}"
    elif roll == 2:
        result = f"{adjective} {building.title()} of {diety}"
    elif roll == 3:
        result = f"{adjective} {building.title()} of {name}"
    elif roll == 4:
        result = f"{adjective} {place.title()} of {name}"
    elif roll == 5:
        result = f"{adjective.capitalize()} {item.capitalize()} of {name}"
    elif roll == 6:
        result = f"{building.capitalize()}  of {adjective.capitalize()} {element.title()}"
    elif roll == 7:
        result = f"{building.capitalize()} of {element.capitalize()}"
    elif roll == 8:
        result = f"{building.capitalize()} of {name}"
    elif roll == 9:
        result = f"{building.capitalize()} of the {creature} {ruler.title()}"
    elif roll == 10:
        result = f"{building.capitalize()} of the {colour} {ruler.title()}"
    elif roll == 11:
        result = f"{building.capitalize()} of the {monster.title()}"
    elif roll == 12:
        result = f"{building.capitalize()} of the {creature} {ruler.title()}"
    elif roll == 13:
        result = f"{building.capitalize()} on {creature} {geography.title()}"
    elif roll == 14:
        result = f"{building.capitalize()} of the {region}"
    elif roll == 15:
        result = f"{building.capitalize()}'s of the {monster.title()} {ruler.capitalize()}"
    elif roll == 16:
        result = f"{colour} {item} {geography.title()}"
    elif roll == 17:
        result = f"{escape.capitalize()} from {name}'s {building.capitalize()}"
    elif roll == 18:
        result = f"{escape.capitalize()} from {name} {building.capitalize()}"
    elif roll == 19:
        result = f"{geography.capitalize()} of {element.capitalize()}"
    elif roll == 20:
        result = f"{geography.capitalize()} of the {monster.capitalize()} {ruler.title()}"
    elif roll == 21:
        result = f"{item.capitalize()} of {diety}"
    elif roll == 22:
        result = f"{item.capitalize()} of {element.capitalize()}"
    elif roll == 23:
        result = f"{journey.capitalize()} the {region}"
    elif roll == 24:
        result = f"{journey.capitalize()} {name} {place.capitalize()}"
    elif roll == 25:
        result = f"{monster} {place.title()} of {name}"
    elif roll == 26:
        result = f"{name} {building.capitalize()}"
    elif roll == 27:
        result = f"{people.capitalize()} of the {adjective} {place.title()}"
    elif roll == 28:
        result = f"{people.capitalize()} of {element.capitalize()}"
    elif roll == 29:
        result = f"{person.capitalize()} of {name} {geography.title()}"
    elif roll == 30:
        result = f"{place.capitalize()} of {name}"
    elif roll == 31:
        result = f"{place.capitalize()} of the {colour} {item.title()}"
    elif roll == 32:
        result = f"{place.capitalize()} of the {monster.title()}"
    elif roll == 33:
        newplace = choice(data["adventure_place"])
        result = f"{person} {place.title()} of the {newplace.capitalize()}"
    elif roll == 34:
        result = f"{quest} {adjective.capitalize()} {item.capitalize()}"
    elif roll == 35:
        result = f"{quest} {adjective.capitalize()} {place.title()}"
    elif roll == 36:
        result = f"{quest.replace('the','')} {name}'s  {item.capitalize()}"
    elif roll == 37:
        result = f"{ruler.capitalize()} of the {monster} {place.title()}"
    elif roll == 38:
        result = f"{secret.capitalize()} of the {people} {building.title()}"
    elif roll == 39:
        result = f"{secret.capitalize()} of the {adjective.capitalize()} {item.capitalize()}"
    else:
        result = f"{secret.capitalize()} of {item} {geography.title()}"

    return result

def lizardman_name_generator():
    '''Generates a random lizardman name'''
    result = ''

    with open(f"{FILEPATH}/referencedata/LizardNames.json", "r", encoding='utf8') as file:
        data = json.load(file)


    if dice(3) == 3:
        apos = "'"
    else:
        apos = ""
    cc = choice(data["lizard_cc"])
    cv = choice(data["lizard_cv"])
    vv = choice(data["lizard_vv"])
    vc = choice(data["lizard_vc"])

    if dice(4)<=3:
        roll = dice(8)
        if roll == 1:
            newcc = choice(data["lizard_cc"])
            result = f"{cc}{apos}{newcc}"
        elif roll == 2:
            result = f"{cv}{cc}"
        elif roll == 3:
            newcv = choice(data["lizard_cv"])
            result = f"{cv}{newcv}"
        elif roll == 4:
            result = f"{vc}{apos}{cc}"
        elif roll == 5:
            result = f"{vc}{apos}{cv}"
        elif roll == 6:
            newvc = choice(data["lizard_vc"])
            result = f"{vc}{apos}{newvc}"
        elif roll == 7:
            result = f"{vv}{cc}"
        else:
            result = f"{vv}{cv}"
        # twosyllable
    else:
        roll = dice(11)
        newcc = choice(data["lizard_cc"])
        newcv = choice(data["lizard_cv"])
        newvc = choice(data["lizard_vc"])
        if roll == 1:
            if dice(3) == 3:
                newapos = "'"
            else:
                newapos = ""
            supcc = choice(data["lizard_cc"])
            result = f"{cc}{apos}{newcc}{newapos}{supcc}"
        elif roll == 2:
            result = f"{cc}{apos}{vv}{newcc}"
        elif roll == 3:
            result = f"{cc}{vv}{cc}"
        elif roll == 4:
            result = f"{vc}{vv}{cv}"
        elif roll == 5:
            result = f"{cv}{vc}{vc}"
        elif roll == 6:
            supcv = choice(data["lizard_cv"])
            result = f"{cv}{newcv}{supcv}"
        elif roll == 7:
            supvc = choice(data["lizard_vc"])
            result = f"{vc}{newvc}{supvc}"
        elif roll == 8:
            result = f"{vv}{cc}{vc}"
        elif roll == 9:
            newvv = choice(data["lizard_vv"])
            result = f"{vv}{cc}{newvv}"
        elif roll == 10:
            result = f"{vv}{cv}{newcv}"
        else:
            result = f"{vc}{cc}{newcc}"
        # threesyllable
    return result.capitalize()

def lovecraft_creature_generator():
    '''Generates a random Lovecraftian creature'''
    with open(f"{FILEPATH}/referencedata/LovecraftCreatures.json", "r", encoding='utf8') as file:
        data = json.load(file)
    adjective = choice(data["lovecraft_adjective"])
    noun = choice(data["lovecraft_noun"])
    prefixv = choice(data["lovecraft_prefixv"])
    prefixc = choice(data["lovecraft_prefixc"])
    suffix = choice(data["lovecraft_suffix"])
    result = ''
    roll = dice(11)
    if roll <= 2:
        result = f"{adjective.capitalize()} {noun.capitalize()} of {prefixv.capitalize()} {suffix}"
    elif roll <= 5:
        result = f"{adjective.capitalize()} {noun.capitalize()} of {prefixc.capitalize()} {suffix}"
    elif roll <= 7:
        result = f"{prefixv.capitalize()}ian {noun.capitalize()}"
    elif roll <= 8:
        result = f"{prefixv.capitalize()}ian {adjective.capitalize()} {noun.capitalize()}"
    elif roll <= 10:
        result = f"{prefixc.capitalize()} {suffix}"
    else:
        result = f"{prefixv.capitalize()} {suffix}"

    return result

def celtic_name_generator(gender = None):
    '''Generates a random Celtic name'''
    with open(f"{FILEPATH}/referencedata/CelticNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    prefix_male = choice(data["celtic_prefix_male"])
    middle_male = choice(data["celtic_middle_male"])
    suffix_male = choice(data["celtic_suffix_male"])
    prefix_female = choice(data["celtic_prefix_female"])
    middle_female = choice(data["celtic_middle_female"])
    suffix_female = choice(data["celtic_suffix_female"])

    if gender is None:
        if dice(2) == 1:
            female = False
        else:
            female = True
    elif gender.lower() == 'female':
        female = True
    else:
        female = False

    if female:
        result = f"{prefix_female}{middle_female}{suffix_female} (.f)"
    else:
        result = f"{prefix_male}{middle_male}{suffix_male}"

    return result

def epyptian_name_generator():
    '''Generates a random Egyptian name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/EgyptianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["egyptian_prefix"])
    middle = choice(data["egyptian_middle"])
    suffix = choice(data["egyptian_suffix"])
    roll = dice(7)
    if roll <= 4:
        result = f"{prefix}{suffix.capitalize()}"
    elif roll <= 6:
        newprefix = choice(data["egyptian_prefix"])
        newsuffix = choice(data["egyptian_suffix"])
        result = f"{prefix}{suffix.capitalize()}-{newprefix}{newsuffix.capitalize()}"
    else:
        roll2 = dice(3)
        temp = ''
        for _ in range(roll2):
            temp += choice(data["egyptian_middle"])
        result += f"{prefix.capitalize()}{temp}{suffix}"

    return result

def greek_name_generator():
    '''Generates a random greek name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/GreekNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["greek_prefix"])
    suffix = choice(data["greek_suffix"])
    begin = choice(data["greek_begin"])
    middle = choice(data["greek_middle"])
    end = choice(data["greek_end"])
    result = f"{prefix}{suffix}{begin}{middle}{end}"
    return result.capitalize()

def oldenglish_name_generator():
    '''Generates a random Old English name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/OldEnglishNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data["oldenglish_prefix"])
    suffix = choice(data["oldenglish_suffix"])
    result = f"{prefix}{suffix}"
    return result.capitalize()

def sumerian_name_generator():
    '''Generates a random Sumerian name'''
    result = ''
    roll = dice(37)
    with open(f"{FILEPATH}/referencedata/SumerianNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    if roll == 1:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 2:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_mix'])}"
    elif roll == 3:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 4:
        result = f"{choice(data['sumerian_vcvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 5:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 6:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_mix'])}"
    elif roll == 7:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vc'])}"
    elif roll == 8:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vccv'])}"
    elif roll == 9:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 10:
        result = f"{choice(data['sumerian_cv'])}{choice(data['sumerian_cv'])}"
    elif roll == 11:
        result = f"{choice(data['sumerian_cv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 12:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 13:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_mix'])}"
    elif roll == 14:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 15:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 16:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vc'])}"
    elif roll == 17:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vccv'])}"
    elif roll == 18:
        result = f"{choice(data['sumerian_cvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 19:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 20:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vc'])}"
    elif roll == 21:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 22:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_cv'])}"
    elif roll == 23:
        result = f"{choice(data['sumerian_ccvc'])}{choice(data['sumerian_cvcv'])}"
    elif roll == 24:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vcvc'])}"
    elif roll == 25:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vc'])}"
    elif roll == 26:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vccv'])}"
    elif roll == 27:
        result = f"{choice(data['sumerian_vc'])}{choice(data['sumerian_vcv'])}"
    elif roll == 28:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 29:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_cv'])}"
    elif roll == 30:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 31:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_cvc'])}"
    elif roll == 32:
        result = f"{choice(data['sumerian_vccv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 33:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_ccvc'])}"
    elif roll == 34:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_cv'])}"
    elif roll == 35:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_cvc'])}"
    elif roll == 36:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_ccvc'])}"
    else:
        result = f"{choice(data['sumerian_vcv'])}{choice(data['sumerian_cvcv'])}"

    return result.capitalize()

def orc_name_generator():
    '''Generates a random orc name'''
    result = ""
    roll = dice(4)

    with open(f"{FILEPATH}/referencedata/OrcNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    if dice(4) <= 3:
        if roll == 1:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_seg'])}"
        elif roll == 2:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_seg'])}"
        elif roll == 3:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_suff'])}"
        else:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_suff'])}"
    else:
        if roll == 1:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_seg'])}{choice(data['orc_seg'])}"
        elif roll == 2:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_seg'])}{choice(data['orc_seg'])}"
        elif roll == 3:
            result = f"{choice(data['orc_seg'])}{choice(data['orc_seg'])}{choice(data['orc_suff'])}"
        else:
            result = f"{choice(data['orc_pref'])}{choice(data['orc_seg'])}{choice(data['orc_suff'])}"
    result = result.capitalize()
    if dice(2) == 1:
        result = f"{result} {choice(data['orc_lastpref']).capitalize()}{choice(data['orc_lastsuff'])}"

    return result

def orc_tribe_generator():
    '''Generates a random orc tribe name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/OrcTribes.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(7)
    if roll <= 4:
        result = f"{choice(data['orc_adj'])} {choice(data['orc_thing'])}"
    elif roll <= 6:
        result = f"{choice(data['orc_adj'])} {choice(data['orc_group'])}"
    else:
        result = f"{choice(data['orc_thing'])} {choice(data['orc_group'])}"

    return result.title()

def organization_generator():
    '''Generates a random organization name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/OrganizationNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(7)
    plurals = {"city": "cities", "cross": "crosses", "fox": "foxes", "knife": "knives",
               "lotus": "lotuses", "staff": "staves", "wolf": "wolves"}
    item = choice(data['org_obj'])
    temp = f"{plurals.get(item)}"

    if item is None:
        temp = f"{temp}s"

    if roll == 1:
        result = f"{choice(data['org_group']).capitalize()} of the {choice(data['org_adj']).capitalize()}"
        if dice(2) == 1:
            result = f"{result}{choice(data['org_obj']).capitalize()}"
        else:
            result = f"{result}{temp.capitalize()}"
    elif roll == 2:
        result = f"{choice(data['org_adj']).capitalize()} {temp.capitalize()}"
    elif roll == 3:
        result = f"{choice(data['org_adj']).capitalize()} {choice(data['org_obj']).capitalize()} {choice(data['org_group']).capitalize()}"
    elif roll == 4:
        result = f"{choice(data['org_group']).capitalize()} of the {choice(data['org_obj']).capitalize()}"
    elif roll == 5:
        result = f"{choice(data['org_obj']).capitalize()} {choice(data['org_group']).capitalize()}"
    elif roll == 6:
        result = f"{choice(data['org_adj']).capitalize()} {choice(data['org_group']).capitalize()}"
    else:
        result = f"{choice(data['org_adj']).capitalize()} {choice(data['org_group']).capitalize()} of the {temp.capitalize()}"
    return result

def ship_name_generator():
    '''Generates a random ship name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/ShipNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    temp = choice(data['ship_person'])
    person =temp[:-2]
    gender = temp[-1]

    roll = dice(6)
    if roll == 1:
        result = f"The {choice(data['ship_adj'])} {choice(data['ship_noun'])}"
    elif roll == 2:
        result = f"The {choice(data['ship_adj'])} {person}"
    elif roll == 3:
        result = f"The {person}'s {choice(data['ship_noun'])}"
    elif roll <= 5:
        result = f"The {choice(data['ship_noun'])}"
    else:
        if gender == 'm':
            result = f"{person} {choice(data['ship_nameM'])}"
        else:
            result = f"{person} {choice(data['ship_nameF'])}"
        result = f"{result}'s {choice(data['ship_noun'])}"

def site_name_generator():
    '''Generates a random site name'''
    result = ''
    with open(f"{FILEPATH}/referencedata/SiteNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    roll = dice(3)
    if roll == 1:
        result = f"{choice(data['site_place'])} of {choice(data['site_thing'])}"
    elif roll == 2:
        result = f"{choice(data['site_adj'])} {choice(data['site_place'])}"
    else:
        result = f"{choice(data['site_adj'])} {choice(data['site_place'])} of {choice(data['site_thing'])}"
    return result

def main(test=True):
    '''
        Main function
    '''
    if test:
        print(f"Riddle Question         : {riddle_generator()}")
        print(f"Wine Name               : {fantasy_wine_name()}")
        print(f"Angelic Name            : {angelic_name()}")
        print(f"Barbarian Name          : {barbarian_name()}")
        print(f"Dwarven Name            : {dwarven_name()}")
        print(f"Dwarven Name            : {dwarven_name(gender='Male')}")
        print(f"Dwarven Name            : {dwarven_name(gender='female')}")
        print(f"Demon Name              : {demon_name()}")
        print(f"Town Name               : {town_name_generator()}")
        print(f"Wood Name               : {woodname_generator()}")
        print(f"Street Name             : {streetname_generator()}")
        print(f"Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
        print(f"Place Name              : {place_name_generator()}")
        print(f"Book Title              : {book_title_generator()}")
        print(f"Book Title              : {book_title_generator(catalogue=True)}")
        print(f"Hexmap tile             : {hexmap_tile_type()}")
        print(f"A or An                 : {aoran('apple')}")
        print(f"Plural                  : {plural('apple')}")
        print(f"Shakey  insult          : {shakespearean_insult_generator()}")
        print(f"Dwarven insult          : {dwarven_insult_generator()}")
        print(f'Coat of Arms            : {coatofarms_generator()}')
        print(f'Elf Name                : {elfname_generator()}')
        print(f'Herb Name               : {herb_name_generator()}')
        print(f'Hyborian Name           : {hyborian_name_generator()}')
        print(f'Inn Name                : {inn_name_generator()}')
        print(f'Adventure Name          : {adventure_name_generator()}')
        print(f'Lizardman Name          : {lizardman_name_generator()}')
        print(f'Lovecraftian Creature   : {lovecraft_creature_generator()}')
        print(f'Celtic Name             : {celtic_name_generator()}')
        print(f"Celtic Name             : {celtic_name_generator(gender='male')}")
        print(f"Celtic Name             : {celtic_name_generator(gender='female')}")
        print(f"Egyptian Name           : {epyptian_name_generator()}")
        print(f"Greek Name              : {greek_name_generator()}")
        print(f"Old English Name        : {oldenglish_name_generator()}")
        print(f"Sumerian Name           : {sumerian_name_generator()}")
        print(f"Orc Name                : {orc_name_generator()}")
        print(f"Orc Tribe Name          : {orc_tribe_generator()}")
        print(f"Organization Name       : {organization_generator()}")
        print(f"Ship Name               : {ship_name_generator()}")
        print(f"Site Name               : {site_name_generator()}")
        print(f"Currency                : {currency_converter(100)}")
    else:
        print(f"Riddle Question         : {riddle_generator()}")
        print(f"Wine Name               : {fantasy_wine_name()}")
        print(f"Currency                : {currency_converter(100)}")
        print(f"Currency                : {currency_converter(1, fromcurr='gold', tocurr='copper')}")
        print(f"Currency                : {currency_converter(10, fromcurr='gold', tocurr='gold')}")
        print(f"Currency                : {currency_converter(1, fromcurr='copper', tocurr='gold')}")
        print(f"Currency                : {currency_converter(1, fromcurr='fliiter', tocurr='gold')}")
        print(f"Currency                : {currency_converter(1, fromcurr='gold', tocurr='fliiter')}")
        print(f"Hexmap tile             : {hexmap_tile_type()}")


if __name__ == "__main__":
    main(test=False)
