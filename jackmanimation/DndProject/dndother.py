''' dnd other items mmodule '''
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
    DNDO_FILEPATH = "Z:/Resources/development"
else:
    DNDO_FILEPATH = "/mnt/y/Resources/development"


def riddle_generator():
    ''' riddle generator '''
    filename = f"{DNDO_FILEPATH}/referencedata/Riddles.json"
    with open(filename, "r", encoding='utf-8-sig') as file:
        data = json.load(file)

    riddle = choice(data['riddle_question'])
    itemcount = data['riddle_question'].index(riddle)
    result = f"question ({itemcount}): {data['riddle_question'][itemcount]},"\
             f" answer: {data['riddle_answer'][itemcount]}"
    return result


def fantasy_wine_name():
    '''
        fantasy wine name generator
    '''
    with open(f"{DNDO_FILEPATH}/referencedata/FantasyWines.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    wine_name = choice(data['wine_name'])
    result = f"{wine_name}"
    return result


def currency_converter(amount, fromcurr="copper", tocurr="gold"):
    '''Converts an amount of one currency to another currency'''
    result = ''
    if amount == 0:
        result = f"{0}"
    if fromcurr == "copper":
        if tocurr == "copper":
            result = f"{amount}"
        elif tocurr == "silver":
            result = f"{amount / 10}"
        elif tocurr == "electrum":
            result = f"{amount / 50}"
        elif tocurr == "gold":
            result = f"{amount / 100}"
        elif tocurr == "platinum":
            result = f"{amount / 1000}"
        else:
            result = f"Invalid to currency type :{tocurr}"
    elif fromcurr == "silver":
        if tocurr == "copper":
            result = f"{amount * 10}"
        elif tocurr == "silver":
            result = f"{amount}"
        elif tocurr == "electrum":
            result = f"{amount / 5}"
        elif tocurr == "gold":
            result = f"{amount / 10}"
        elif tocurr == "platinum":
            result = f"{amount / 100}"
        else:
            result = f"Invalid to currency type :{tocurr}"
    elif fromcurr == "electrum":
        if tocurr == "copper":
            result = f"{amount * 50}"
        elif tocurr == "silver":
            result = f"{amount * 5}"
        elif tocurr == "electrum":
            result = f"{amount}"
        elif tocurr == "gold":
            result = f"{amount / 2}"
        elif tocurr == "platinum":
            result = f"{amount / 20}"
        else:
            result = f"Invalid to currency type :{tocurr}"
    elif fromcurr == "gold":
        if tocurr == "copper":
            result = f"{amount * 100}"
        elif tocurr == "silver":
            result = f"{amount * 10}"
        elif tocurr == "electrum":
            result = f"{amount * 2}"
        elif tocurr == "gold":
            result = f"{amount}"
        elif tocurr == "platinum":
            result = f"{amount / 10}"
        else:
            result = f"Invalid to currency type :{tocurr}"
    elif fromcurr == "platinum":
        if tocurr == "copper":
            result = f"{amount * 1000}"
        elif tocurr == "silver":
            result = f"{amount * 100}"
        elif tocurr == "electrum":
            result = f"{amount * 20}"
        elif tocurr == "gold":
            result = f"{amount * 10}"
        elif tocurr == "platinum":
            result = f"{amount}"
        else:
            result = f"Invalid to currency type :{tocurr}"
    else:
        result = f"Invalid from currency type :{fromcurr}"
    return result


def hexmap_tile_type():
    '''Returns a random hexmap tile type'''
    result = ''
    roll = Dice.dice(20)
    typeroll = Dice.dice()
    if roll == 1:
        result = "City"
        if typeroll == 1:
            result = f"{result} : Capital City"
        elif typeroll == 2:
            result = f"{result} : Free City"
        elif typeroll == 3:
            result = f"{result} : Ruined City"
        elif typeroll == 4:
            result = f"{result} : Towering City"
        elif typeroll == 5:
            result = f"{result} : Magical City"
        else:
            result = f"{result} : Besiged City"
    elif roll == 2:
        result = "Castle/Fort"
        if typeroll == 1:
            result = f"{result} : Guarded Fort"
        elif typeroll == 2:
            result = f"{result} : Deserted Fort"
        elif typeroll == 3:
            result = f"{result} : Lord's Castle"
        elif typeroll == 4:
            result = f"{result} : Royal Keep"
        elif typeroll == 5:
            result = f"{result} : Military Keep"
        else:
            result = f"{result} : Ruined Fort"
    elif roll == 3:
        result = "Town"
        if typeroll == 1:
            result = f"{result} : Bustling Town"
        elif typeroll == 2:
            result = f"{result} : Shanty Town"
        elif typeroll == 3:
            result = f"{result} : Plagued Town"
        elif typeroll == 4:
            result = f"{result} : Stone Town"
        elif typeroll == 5:
            result = f"{result} : Wooden Town"
        else:
            result = f"{result} : Store Fronts"
    elif roll == 4:
        result = "Village"
        if typeroll == 1:
            result = f"{result} : Farm Village"
        elif typeroll == 2:
            result = f"{result} : Tribal Village"
        elif typeroll == 3:
            result = f"{result} : Bandit Camp"
        elif typeroll == 4:
            result = f"{result} : Hunter's Camp"
        elif typeroll == 5:
            result = f"{result} : Empty Village"
        else:
            result = f"{result} : Apothecary"
    elif roll == 5:
        result = "Forest / Woodland"
        if typeroll == 1:
            result = f"{result} : Dense Forest"
        elif typeroll == 2:
            result = f"{result} : Dying Forest"
        elif typeroll == 3:
            result = f"{result} : Sparse Forest"
        elif typeroll == 4:
            result = f"{result} : Cursed Forest"
        elif typeroll == 5:
            result = f"{result} : Woodland"
        else:
            result = f"{result} : Magical Woods"
    elif roll == 6:
        result = "Mountains"
        if typeroll == 1:
            result = f"{result} : Jagged Peaks"
        elif typeroll == 2:
            result = f"{result} : Cold Mountains"
        elif typeroll == 3:
            result = f"{result} : Shadowy Range"
        elif typeroll == 4:
            result = f"{result} : Magical Peak"
        elif typeroll == 5:
            result = f"{result} : Snowy Bluffs"
        else:
            result = f"{result} : Mountains"
    elif roll == 7:
        result = "Grassland"
        if typeroll == 1:
            result = f"{result} : Grassland"
        elif typeroll == 2:
            result = f"{result} : Meadows"
        elif typeroll == 3:
            result = f"{result} : Fields"
        elif typeroll == 4:
            result = f"{result} : Flooded Plains"
        elif typeroll == 5:
            result = f"{result} : Flatland"
        else:
            result = f"{result} : Savannah"
    elif roll == 8:
        result = "Hills / Heath"
        if typeroll == 1:
            result = f"{result} : Hills"
        elif typeroll == 2:
            result = f"{result} : Heath"
        elif typeroll == 3:
            result = f"{result} : Outcropping"
        elif typeroll == 4:
            result = f"{result} : Burial Mounds"
        elif typeroll == 5:
            result = f"{result} : Wet Moors"
        else:
            result = f"{result} : Highland"
    elif roll == 9:
        result = "River"
        if typeroll == 1:
            result = f"{result} : Rushing River"
        elif typeroll == 2:
            result = f"{result} : Canal"
        elif typeroll == 3:
            result = f"{result} : Streams"
        elif typeroll == 4:
            result = f"{result} : Magical River"
        elif typeroll == 5:
            result = f"{result} : Slow River"
        else:
            result = f"{result} : Posioned River"
    elif roll == 10:
        result = "Desert"
        if typeroll == 1:
            result = f"{result} : Hot Desert"
        elif typeroll == 2:
            result = f"{result} : Dry Steppe"
        elif typeroll == 3:
            result = f"{result} : Wasteland"
        elif typeroll == 4:
            result = f"{result} : Cacti Forest"
        elif typeroll == 5:
            result = f"{result} : Cold Desert"
        else:
            result = f"{result} : Deadlands"
    elif roll == 11:
        result = "Water / Lake / Sea"
        if typeroll == 1:
            result = f"{result} : Sea"
        elif typeroll == 2:
            result = f"{result} : Ocean"
        elif typeroll == 3:
            result = f"{result} : Lake"
        elif typeroll == 4:
            result = f"{result} : Reservoir"
        elif typeroll == 5:
            result = f"{result} : Magical Pools"
        else:
            result = f"{result} : Flooded Land"
    elif roll == 12:
        result = "Swamp / Marshland"
        if typeroll == 1:
            result = f"{result} : Swampland"
        elif typeroll == 2:
            result = f"{result} : Putrid Fen"
        elif typeroll == 3:
            result = f"{result} : Sinking Bog"
        elif typeroll == 4:
            result = f"{result} : Cursed Mire"
        elif typeroll == 5:
            result = f"{result} : Muddy Land"
        else:
            result = f"{result} : Marshland"
    elif roll == 13:
        result = "Tundra / Frozen Waste"
        if typeroll == 1:
            result = f"{result} : Snowy Flats"
        elif typeroll == 2:
            result = f"{result} : Blizzards"
        elif typeroll == 3:
            result = f"{result} : Tundra"
        elif typeroll == 4:
            result = f"{result} : Frozen Waste"
        elif typeroll == 5:
            result = f"{result} : Ice"
        else:
            result = f"{result} : Artic Expanse"
    elif roll == 14:
        result = "Jungle"
        if typeroll == 1:
            result = f"{result} : Jungle"
        elif typeroll == 2:
            result = f"{result} : Rainforest"
        elif typeroll == 3:
            result = f"{result} : Tropical Land"
        elif typeroll == 4:
            result = f"{result} : Cursed Jungle"
        elif typeroll == 5:
            result = f"{result} : Bushland"
        else:
            result = f"{result} : Tangled Jungle"
    elif roll == 15:
        result = "Volcano"
        if typeroll == 1:
            result = f"{result} : Volcano"
        elif typeroll == 2:
            result = f"{result} : Planar Break"
        elif typeroll == 3:
            result = f"{result} : Mage's Peak"
        elif typeroll == 4:
            result = f"{result} : Magical Source"
        elif typeroll == 5:
            result = f"{result} : Volcanic Land"
        else:
            result = f"{result} : Gas Clouds"
    elif roll == 16:
        result = "Cave / Dungeon"
        if typeroll == 1:
            result = f"{result} : Cave"
        elif typeroll == 2:
            result = f"{result} : Grotto"
        elif typeroll == 3:
            result = f"{result} : Hill Home"
        elif typeroll == 4:
            result = f"{result} : Dugout Camp"
        elif typeroll == 5:
            result = f"{result} : Tomb"
        else:
            result = f"{result} : Passageway"
    elif roll == 17:
        result = "Fissure / Canyon"
        if typeroll == 1:
            result = f"{result} : Fissure"
        elif typeroll == 2:
            result = f"{result} : Dry Canyon"
        elif typeroll == 3:
            result = f"{result} : River Gorge"
        elif typeroll == 4:
            result = f"{result} : Icy Crevasse"
        elif typeroll == 5:
            result = f"{result} : World Rift"
        else:
            result = f"{result} : Valley"
    elif roll == 18:
        result = "Fungal Forest"
        if typeroll == 1:
            result = f"{result} : Fungal Forest"
        elif typeroll == 2:
            result = f"{result} : Faeland"
        elif typeroll == 3:
            result = f"{result} : Rotten Place"
        elif typeroll == 4:
            result = f"{result} : Fungal Fields"
        elif typeroll == 5:
            result = f"{result} : Sporeland"
        else:
            result = f"{result} : Toadstool Town"
    elif roll == 19:
        result = "Crystal Plains"
        if typeroll == 1:
            result = f"{result} : Crystal Plains"
        elif typeroll == 2:
            result = f"{result} : Crystal Forest"
        elif typeroll == 3:
            result = f"{result} : Shard Tower"
        elif typeroll == 4:
            result = f"{result} : Magical Plane"
        elif typeroll == 5:
            result = f"{result} : Gemstone Mine"
        else:
            result = f"{result} : Crystal Gate"
    else:
        result = "Map Marker / Unknown Location"
        if typeroll == 1:
            result = f"{result} : Dungeon"
        elif typeroll == 2:
            result = f"{result} : Treasure"
        elif typeroll == 3:
            result = f"{result} : Artefact"
        elif typeroll == 4:
            result = f"{result} : MPC Location"
        elif typeroll == 5:
            result = f"{result} : Guild Base"
        else:
            result = f"{result} : Hidden Temple"
    return result


def book_title_generator(catalogue=False):
    '''Generates a book title'''
    # pylint: disable=R0914
    result = ''
    with open(f"{DNDO_FILEPATH}/referencedata/BookTitles.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(10)
    if roll == 1:
        # religious book
        newroll = Dice.dice(4)
        if newroll == 1:
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
        # biology book
        bioroll = Dice.dice(2)
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
        # magick book
        magicroll = Dice.dice(4)
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
        # craftwork book
        guide = choice(data['guide']).capitalize()
        crafts = choice(data['crafts']).capitalize()
        result = f'{guide} {crafts}'
        if catalogue:
            result = f"{result} (Craftwork)"
    elif roll == 6:
        # tales book
        talesroll = Dice.dice(3)
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
        # art book
        poettype = choice(data['poettype']).capitalize()
        poetry = choice(data['poetry']).capitalize()
        result = f'{poettype} {poetry}'
        if catalogue:
            result = f"{result} (Art)"
    elif roll == 8:
        # history  book
        historyroll = Dice.dice(4)
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
        # geography book
        georoll = Dice.dice(3)
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
        # linguitics book
        lingroll = Dice.dice(2)
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
        result = f"an {input_text_string}"
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
    if input_text_string[-2].lower() in ('ch', 'sh'):
        suffix = 'es'
    if input_text_string[-1].lower() == 'y':
        input_text_string = input_text_string[:-1]
        suffix = 'ies'
    result = f"{input_text_string}{suffix}"
    return result


def coatofarms_generator():
    '''Generates a Coat of Arms'''
    # pylint: disable=R0914
    with open(f"{DNDO_FILEPATH}/referencedata/CoatArms.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    result = ''
    roll = Dice.dice()

    metal = choice(data["metal"])
    blazon1 = choice(data["blazon1"])

    if blazon1 == "Creature":
        blazon1 = choice(data["creatures"])
    blaz2roll = Dice.dice(3)
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

    blaz3roll = Dice.dice(3)
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
    with open(f"{DNDO_FILEPATH}/referencedata/HerbNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    result = ''
    roll = Dice.dice(14)
    approll = Dice.dice()
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
    # pylint: disable=R0914
    with open(f"{DNDO_FILEPATH}/referencedata/AdventureNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    result = ''
    roll = Dice.dice(40)
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
        result = f"{geography.capitalize()} of the {monster.capitalize()} "\
                 f"{ruler.title()}"
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
        result = f"{quest.replace('the', '')} {name}'s  {item.capitalize()}"
    elif roll == 37:
        result = f"{ruler.capitalize()} of the {monster} {place.title()}"
    elif roll == 38:
        result = f"{secret.capitalize()} of the {people} {building.title()}"
    elif roll == 39:
        result = f"{secret.capitalize()} of the {adjective.capitalize()} "\
                 f"{item.capitalize()}"
    else:
        result = f"{secret.capitalize()} of {item} {geography.title()}"

    return result


def lovecraft_creature_generator():
    '''Generates a random Lovecraftian creature'''
    with open(f"{DNDO_FILEPATH}/referencedata/LovecraftCreatures.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    adjective = choice(data["lovecraft_adjective"])
    noun = choice(data["lovecraft_noun"])
    prefixv = choice(data["lovecraft_prefixv"])
    prefixc = choice(data["lovecraft_prefixc"])
    suffix = choice(data["lovecraft_suffix"])
    result = ''
    roll = Dice.dice(11)
    if roll <= 2:
        result = f"{adjective.capitalize()} {noun.capitalize()} of "\
                 f"{prefixv.capitalize()} {suffix}"
    elif roll <= 5:
        result = f"{adjective.capitalize()} {noun.capitalize()} of "\
                 f"{prefixc.capitalize()} {suffix}"
    elif roll <= 7:
        result = f"{prefixv.capitalize()}ian {noun.capitalize()}"
    elif roll <= 8:
        result = f"{prefixv.capitalize()}ian {adjective.capitalize()} "\
                 f"{noun.capitalize()}"
    elif roll <= 10:
        result = f"{prefixc.capitalize()} {suffix}"
    else:
        result = f"{prefixv.capitalize()} {suffix}"

    return result


def orc_tribe_generator():
    '''Generates a random orc tribe name'''
    result = ''
    with open(f"{DNDO_FILEPATH}/referencedata/OrcTribes.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(7)
    if roll <= 4:
        result = f"{choice(data['orc_adj'])} {choice(data['orc_thing'])}"
    elif roll <= 6:
        result = f"{choice(data['orc_adj'])} {choice(data['orc_group'])}"
    else:
        result = f"{choice(data['orc_thing'])} {choice(data['orc_group'])}"

    return result.title()


def organization_name_generator():
    '''Generates a random organization name'''
    result = ''
    with open(f"{DNDO_FILEPATH}/referencedata/OrganizationNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    roll = Dice.dice(7)
    plurals = {"city": "cities",
               "cross": "crosses",
               "fox": "foxes",
               "knife": "knives",
               "lotus": "lotuses",
               "staff": "staves",
               "wolf": "wolves"}
    item = choice(data['org_obj'])
    temp = f"{plurals.get(item)}"

    if item is None:
        temp = f"{temp}s"

    if roll == 1:
        result = f"{choice(data['org_group']).capitalize()} of the "\
                 f"{choice(data['org_adj']).capitalize()}"
        if Dice.dice(2) == 1:
            result = f"{result}{choice(data['org_obj']).capitalize()}"
        else:
            result = f"{result}{temp.capitalize()}"
    elif roll == 2:
        result = f"{choice(data['org_adj']).capitalize()} "\
                 f"{temp.capitalize()}"
    elif roll == 3:
        result = f"{choice(data['org_adj']).capitalize()} "\
                 f"{choice(data['org_obj']).capitalize()} "\
                 f"{choice(data['org_group']).capitalize()}"
    elif roll == 4:
        result = f"{choice(data['org_group']).capitalize()} "\
                 f"of the {choice(data['org_obj']).capitalize()}"
    elif roll == 5:
        result = f"{choice(data['org_obj']).capitalize()} "\
                 f"{choice(data['org_group']).capitalize()}"
    elif roll == 6:
        result = f"{choice(data['org_adj']).capitalize()} "\
                 f"{choice(data['org_group']).capitalize()}"
    else:
        result = f"{choice(data['org_adj']).capitalize()} "\
                 f"{choice(data['org_group']).capitalize()} "\
                 f"of the {temp.capitalize()}"
    return result


def ship_name_generator():
    '''Generates a random ship name'''
    result = ''
    with open(f"{DNDO_FILEPATH}/referencedata/ShipNames.json",
              "r",
              encoding='utf-8-sig') as file:
        data = json.load(file)
    temp = choice(data['ship_person'])
    person = temp[:-2]
    gender = temp[-1]

    roll = Dice.dice(6)
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


def main():
    ''' main function '''
    print("Currency                : "
          f"{currency_converter(100)}")
    print("Currency                : "
          f"{currency_converter(1, fromcurr='gold', tocurr='copper')}")
    print("Currency                : "
          f"{currency_converter(10, fromcurr='gold', tocurr='gold')}")
    print("Currency                : "
          f"{currency_converter(1, fromcurr='copper', tocurr='gold')}")
    print("Currency                : "
          f"{currency_converter(1, fromcurr='fliiter', tocurr='gold')}")
    print("Currency                : "
          f"{currency_converter(1, fromcurr='gold', tocurr='fliiter')}")
    print("Riddle Question         : "
          f"{riddle_generator()}")
    print("Wine Name               : "
          f"{fantasy_wine_name()}")
    print("Hexmap tile             : "
          f"{hexmap_tile_type()}")
    print("Book Title              : "
          f"{book_title_generator()}")
    print("Book Title              : "
          f"{book_title_generator(catalogue=True)}")
    print("A or An                 : "
          f"{aoran('apple')}")
    print("Plural                  : "
          f"{plural('apple')}")
    print("Coat of Arms            : "
          f"{coatofarms_generator()}")
    print("Herb Name               : "
          f"{herb_name_generator()}")
    print("Adventure Name          : "
          f"{adventure_name_generator()}")
    print("Lovecraftian Creature   : "
          f"{lovecraft_creature_generator()}")
    print("Orc Tribe Name          : "
          f"{orc_tribe_generator()}")
    print("Organization Name       : "
          f"{organization_name_generator()}")
    print("Ship Name               : "
          f"{ship_name_generator()}")


if __name__ == "__main__":
    main()
