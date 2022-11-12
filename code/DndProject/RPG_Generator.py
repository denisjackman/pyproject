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
from random import randint

FILEPATH = Path(__file__).parent
# pylint: disable=too-many-locals
# pylint: disable=too-many-lines

def dice(sides=6, rolls=1):
    '''
        Rolls a dice which has 'sides' sides (default is six (6))
        for 'rolls' number of times (default is one (1))
    '''
    result = 0
    item = 0
    while item in range(rolls):
        result = result + randint(1, sides)
        item += 1
    return result

def number_generator(number=100):
    '''
        Generates a random number between 1 and number
    '''
    return randint(1, number)

def riddle_generator():
    ''' riddle generator '''
    filename = f"{FILEPATH}/referencedata/Riddles.json"
    with open(filename, "r", encoding='utf8') as file:
        data = json.load(file)

    riddle = choice(data['riddle_question'])
    itemcount = data['riddle_question'].index(riddle)
    result = f"question ({itemcount}): {data['riddle_question'][itemcount]}, answer: {data['riddle_answer'][itemcount]}"
    return result

def shakespearean_insult_generator():
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
    filename = f"{FILEPATH}/referencedata/ShakespeareInsult.json"
    with open(filename, "r", encoding='utf8') as file:
        data = json.load(file)
    column_one = choice(data["insult_column_one"])
    column_two = choice(data["insult_column_two"])
    column_three = choice(data["insult_column_three"])
    result = f"Thou {column_one} {column_two} {column_three}."
    # return it
    return result

def dwarven_insult_generator():
    '''
        dwarven insult generator
    '''
    with open(f"{FILEPATH}/referencedata/DwarvenInsult.json", "r", encoding='utf8') as file:
        data = json.load(file)
    dwarven_insult_one = choice(data["insult_column_one"]).capitalize()
    dwarven_insult_two = choice(data["insult_column_two"])
    dwarven_insult_three = choice(data["insult_column_three"])
    result = f"{dwarven_insult_one} {dwarven_insult_two} {dwarven_insult_three}."
    return result

def fantasy_wine_name():
    '''
        fantasy wine name generator
    '''
    with open(f"{FILEPATH}/referencedata/FantasyWines.json", "r", encoding='utf8') as file:
        data = json.load(file)
    wine_name = choice(data['wine_name'])
    result = f"{wine_name}"
    return result

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

def dwarven_name(setfemale = False):
    ''' dwarven name generator '''
    female = False
    firstname = ''
    lastname = ''

    with open(f"{FILEPATH}/referencedata/DwarvenNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    prefix = choice(data["dwarven_name_prefix"])
    suffixmale = choice(data["dwarven_name_suffixmale"])
    suffix = choice(data["dwarven_name_suffix"])
    clanprefix = choice(data["dwarven_clan_prefix"])
    clansuffix = choice(data["dwarven_clan_suffix"])
    if setfemale:
        female = True
        firstname = f'{prefix}{suffix}'
    else:
        if dice(2) == 1:
            firstname = f'{prefix}{suffixmale}'
        else:
            female = True
            firstname = f'{prefix}{suffix}'

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

def oracle_generator():
    '''
        oracle generator
    '''
    oracle_noun = ("endless capacity", "life", "wondering person", "intention", "core", "fluid", "delicious fruit",
                   "fruition", "wheel", "dream", "purpose", "desire", "reason", "world", "light", "power", "work",
                   "change", "energy", "job", "choice", "Spirit", "nature", "connection", "fire", "dancer", "offering",
                   "peace", "simple unity", "forgiving act", "center", "source", "glowing ember", "spiritual food",
                   "practical purpose", "ocean", "doubt", "faith", "ritual", "practice", "student", "teacher",
                   "sacred time", "soul", "winding path", "challenge", "transformation", "transience", "burden",
                   "release", "support", "oracle", "direction", "wondering", "God", "local community", "world community",
                   "creation", "relaxation", "moving planet", "gift", "present", "never-failing Source", "body",
                   "part", "mind", "river", "waterfall", "leader", "community", "soul", "lesson", "destination",
                   "journey", "confusion", "striking clarity", "lover", "home", "serendipitous design", "similar dream",
                   "hope", "loving action", "joy", "path", "gateway", "transcendent experience", "angel", "soul guide",
                   "curious spirit", "song", "method", "map", "blueprint", "received wisdom", "block", "true wonder",
                   "star", "entire universe", "immense sky", "whole", "tree", "branch", "power", "peace maker",
                   "genius", "seed", "marvelous ruby", "wondrous alchemy", "turning", "hidden science", "jewel",
                   "forest", "exchange", "remembered passion", "fiery stillness", "elder", "communication", "root",
                   "crossroads", "nexus", "way", "integrated reality", "integral notion", "catharsis", "distinction",
                   "compassionate action", "forgiving word", "action", "cycle", "feeling", "season", "harvest",
                   "dawn", "birth", "notion", "circle", "ring", "myth", "radical truth", "essence", "infinite and gentle force",
                   "spiritual cycle", "reason", "graceful act", "discovery", "need", "forgotton mystery", "wing",
                   "motivation", "structure")
    oracle_preposition = ("of", "from", "near", "about", "around", "for", "toward", "over", "behind",
                          "beyond", "related to", "defined by", "within", "living with")
    oracle_adverb = ("knowingly", "consciously", "gently", "emphatically", "enthusiastically", "strangely",
                     "surprisingly", "nearly", "yearningly", "non-chalantly", "hardly", "eagerly", "purposefully",
                     "actively", "inexorably", "accurately", "accidentally", "completely", "differently",
                     "single-handledly", "consciously", "almost", "wisely", "creatively", "somewhat",
                     "overwhelmingly", "seldom", "often")
    oracle_adjective = ("quick", "kind", "gentle", "optimal", "challenging", "loyal", "sweet", "ravishing",
                        "stimulating", "strong", "activating", "graceful", "devoted", "global", "genuine",
                        "magnificent", "masked", "separated", "gratifying", "elusive", "revered", "rigorous",
                        "righteous", "mysterious", "infinite", "salient", "magnificent", "activated", "sharing",
                        "feeling", "powerful", "clear", "energized", "rainbow", "perfect", "truly united", "world",
                        "local", "ripe", "loving", "anticipating", "pleasant", "personalized", "transient", "individualized",
                        "truly-unique", "ancient", "loving", "experienced", "creative", "foreign", "familiar",
                        "worthy", "precise", "intelligent", "gifted", "strained", "free-spirited", "true",
                        "clear", "caring", "dreamlike", "imaginative", "collaborative", "service-oriented", "straightforward",
                        "strong", "orbiting", "glowing", "stable", "outer", "nearest", "most-difficult", "transient",
                        "full", "round", "fluid", "opaque", "known", "highly-valued", "smooth", "warm", "loose",
                        "ready", "burning", "effervescent", "impactful", "parental", "childlike", "soft",
                        "simple", "subtle", "new", "abundant", "intergalactic", "questioning", "resplendent",
                        "terrific", "energetic", "powerful", "discriminating", "self-actualized",
                        "ecological", "planetary")
    oracle_instransient_verb_phrase = ( "arrives", "beckons", "takes a rest", "becomes clear",
                                       "learns", "removes a block", "meditates", "remembers the soul",
                                       "jumps without a net", "remembers everything", "cleans the window of awareness",
                                       "feels truth", "returns", "rejoices", "prays", "takes action", "dreams",
                                       "ceases to exist", "hides", "chooses", "laughs with joy", "plays without questioning",
                                       "loves", "wakes up", "hesitates and moves anyway", "trembles with comprehension",
                                       "reflects", "is born", "finds inspiration", "feels completely full", "senses",
                                       "sees", "joins the path", "listens", "reasons", "sits", "flies", "sings",
                                       "knows")
    oracle_conjuction = ("and", "but", "for", "nor", "or", "so", "yet", "becuase")
    oracle_complete_visions = ("There is a storm in your past and yet another in your future, but persistence and clear thinking will show you the road once more",
                               "The answers you seek will be found within. Seek the obvious to address the unknown",
                               "What one man has wrought, another can undo. Although they differ, they are one and the same",
                               "The path you walk is built on faith. Fear not your choices, as they are the stepping stones that bridge the chasm",
                               "One cannot be truly wrong if he is really right. Believe in yourself, and you will find the answers you seek",
                               "What you possess is all you need. Don’t be swayed by the illusion of what’s needed",
                               "Although you fear your choices, they are all you have. Fear the Choice you‘ve lost more than the choices that you still possess",
                               "Don’t be blinded by the tree that blocks your sight, skirt its trunk to see the forest",
                               "The one you seek will need you more. He is hanging from the precipice of shattered dreams, and has lost what cannot be found",
                               "Trust what you know, since it is also the answer to what you do not")
    result = ''
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
            result = f"{amount /50}"
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
    roll = dice(20)
    typeroll = dice()
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

def main():
    '''
        Main function
    '''
    print(f"Shakey  insult          : {shakespearean_insult_generator()}")
    print(f"Dwarven insult          : {dwarven_insult_generator()}")
    print(f"Riddle Question         : {riddle_generator()}")
    print(f"Wine Name               : {fantasy_wine_name()}")
    print(f"Angelic Name            : {angelic_name()}")
    print(f"Barbarian Name          : {barbarian_name()}")
    print(f"Dwarven Name            : {dwarven_name()}")
    print(f"Dwarven Name            : {dwarven_name(setfemale=True)}")
    print(f"Demon Name              : {demon_name()}")
    print(f"Town Name               : {town_name_generator()}")
    print(f"Wood Name               : {woodname_generator()}")
    print(f"Street Name             : {streetname_generator()}")
    print(f"Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
    print(f"Place Name              : {place_name_generator()}")
    print(f"Book Title              : {book_title_generator()}")
    print(f"Book Title              : {book_title_generator(catalogue=True)}")
    print(f"Currency                : {currency_converter(100)}")
    print(f"Currency                : {currency_converter(1, fromcurr='gold', tocurr='copper')}")
    print(f"Currency                : {currency_converter(10, fromcurr='gold', tocurr='gold')}")
    print(f"Currency                : {currency_converter(1, fromcurr='copper', tocurr='gold')}")
    print(f"Currency                : {currency_converter(1, fromcurr='fliiter', tocurr='gold')}")
    print(f"Currency                : {currency_converter(1, fromcurr='gold', tocurr='fliiter')}")
    print(f"Hexmap tile             : {hexmap_tile_type()}")
    print(f"A or An                 : {aoran('apple')}")
    print(f"Plural                  : {plural('apple')}")
    print(f"Dice                    : {dice()}")
    print(f'Number Generator        : {number_generator()}')
    print(f'Coat of Arms            : {coatofarms_generator()}')
    print(f'Elf Name                : {elfname_generator()}')
    print(f'Herb Name               : {herb_name_generator()}')
    print(f'Hyborian Name           : {hyborian_name_generator()}')
    print(f'Inn Name                : {inn_name_generator()}')
    print(f'Adventure Name          : {adventure_name_generator()}')

if __name__ == "__main__":
    main()
