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
from dndnames import angelic_name
from dndnames import barbarian_name
from dndnames import dwarven_name
from dndnames import demon_name
from dndnames import elfname_generator
from dndnames import hyborian_name_generator
from dndnames import lizardman_name_generator
from dndnames import celtic_name_generator
from dndnames import epyptian_name_generator
from dndnames import greek_name_generator
from dndnames import orc_name_generator
from dndnames import oldenglish_name_generator
from dndnames import sumerian_name_generator
from dndplaces import town_name_generator
from dndplaces import woodname_generator
from dndplaces import streetname_generator
from dndplaces import dwarven_settlement_name_generator
from dndplaces import place_name_generator
from dndplaces import inn_name_generator
from dndplaces import site_name_generator

FILEPATH = Path(__file__).parent

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
        print(f"Town Name               : {town_name_generator()}")
        print(f"Wood Name               : {woodname_generator()}")
        print(f"Street Name             : {streetname_generator()}")
        print(f"Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
        print(f"Place Name              : {place_name_generator()}")
        print(f'Inn Name                : {inn_name_generator()}')
        print(f"Site Name               : {site_name_generator()}")

if __name__ == "__main__":
    main(test=False)
