'''
    This is a RPG generator tool

    it has in it currently:
        A Dice function
        a number generator
        a riddle generator
        a Shakepspearean Insult generator
        a Dwarven insult generator

    Working on:
        Oracle Generator

    References:
        https://www.dndspeak.com/
        https://www.reddit.com/r/d100/new/

'''
from pathlib import Path
import json
import random
from random import choice
from random import randint

FILEPATH = Path(__file__).parent

def dice(sides=6, rolls=1):
    '''
        Rolls a dice which has 'sides' sides (default is six (6))
        for 'rolls' number of times (default is one (1))
    '''
    result = 0
    loop = 0
    while loop < rolls:
        result = result + random.randrange(1, sides+1)
        loop = loop + 1
    return result

def number_generator(number=100):
    '''
        Generates a random number between 1 and number
    '''
    return random.randint(1, number)

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

    roll = randint(1, 2)
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
    roll = randint(1, 7)
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
    roll = randint(1, 7)
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
    roll = randint(1, 100)
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
    if randint(1, 2) == 1:
        return demon_name_one()
    return demon_name_two()

def dwarven_name():
    ''' dwarven name generator '''
    female = False
    firstname = ''
    lastname = ''

    prefix = ["Ag","Al","Ald","Alf","Ar","Arn","Art","As","Ath","Athran","Aud","Bal","Bala","Bar","Bara","Bel",
              "Bela","Belf","Ber","Bif","Bof","Bok","Bol","Bom","Bor","Bra","Brott","Brun","Bryn","Bur","D",
              "Da","Dag","Dam","Dar","Dor","Dora","Drok","Drong","Dur","Dwal","Eb","Ein","El","Ela","Elan",
              "Elda","Fa","Faf","Far","Fara","Fil","Fim","Fima","Firen","Fo","For","Fros","Fur","Fura","Ga",
              "Gar","Gil","Gim","Gir","Glam","Gol","Gollen","Gor","Got","Gota","Grim","Gro","Grun","Gunn",
              "Gus","Gut","Ha","Had","Hak","Haka","Hal","Han","Har","Has","Hega","Hel","Hun","Hur","Ing",
              "Jar","Kad","Kar","Kata","Kaz","Kaza","Kha","Khar","Kol","Krag","Kur","Lar","Logaz","Lok",
              "Lun","Mag","Mel","Mo","Mola","Mor","Mora","Na","Nar","No","Nola","Nor","Noran","Nord","Nun",
              "Nyr","Oda","Oka","Ol","Olf","Olla","Osk","Oth","Othra","Rag","Rak","Ro","Rog","Ror","Roran",
              "Run","Rur","Sa","Sig","Ska","Skaf","Skalf","Skalla","Skar","Skeg","Skor","Skora","Snor","Snora",
              "Sven","Tak","Thar","Tho","Thor","Thora","Thra","Thro","Thron","Thrun","Thura","Ulf","Ulla","Un",
              "Utha","Val","Vala","Var","Vara","Ver","Ves","Yng","Zak","Zaka","Zakan","Zam","Zar","Zara","Zarna"]
    suffixmale = ["ain","ald","ar","ard","arr","bin","bon","bor","born","brun","bur","dalf","dan","dar","den",
                  "di","dil","din","dir","dok","dor","dran","drin","ed","end","endd","fin","finn","fur","gan",
                  "gar","gard","gi","gil","gin","gir","gni","gon","gor","grim","grin","grir","grom","grond",
                  "groth","grum","grund","grunt","gui","gun","gund","hall","hel","hild","hor","ic","ik","in",
                  "ir","is","jald","ki","kil","kin","krag","kri","krin","li","lik","lin","ling","linn","lir",
                  "lok","lum","lun","mad","min","mir","mund","nar","ni","nin","nir","nus","odd","oin","olf",
                  "or","rag","ran","rand","rek","ri","rig","rik","rin","rir","run","sil","sin","skin","sur",
                  "tan","thor","ti","tin","tok","trek","trok","ur","urd","vald","vard","vir","zin","zor"]
    suffix = ["a","asi","bera","bina","bora","cla","dda","dila","dina","dis","dokina","dora","drid","drinella",
              "era","fina","fya","ga","gana","gara","gella","gerd","gina","gona","gora","grid","grimella",
              "grina","groma","gromina","grondella","grotha","gruma","grunda","gruntina","gula","gundina",
              "gunella","hild","i","ia","il","ilda","ima","ja","kina","kragella","krina","kya","la","likina",
              "lina","loda","loka","luna","mina","mira","na","nala","nina","nira","nya","ona","ra","ragina",
              "rasa","rid","riga","rika","rina","runa","runella","sa","sif","skina","skinella","tina","toka",
              "trekella","trekina","troka","vild","yra","zina","zora"]
    clanprefix = ["ale","anvil","armor","axe","beard","black","cavern","earth","flame","foe","forge","goblin",
                  "gold","granite","grudge","hammer","iron","oath","orc","ore","red","ring","rock","shield",
                  "silver","steel","stone","tunnel","troll"]
    clansuffix = ["arm","axe","back","bane","beard","bearer","beater","bender","binder","breaker","crusher",
                  "cutter","delver","fist","forge","hammer","head","hearth","keg","killer","maker","master",
                  "render","shaker","slayer","smith","splitter","worker"]

    if randint(1, 2) == 1:
        firstname = f'{choice(prefix)}{choice(suffixmale)}'
    else:
        female = True
        firstname = f'{choice(prefix)}{choice(suffix)}'

    if randint(1, 3) == 1:
        father = f'{choice(prefix)}{choice(suffixmale)}'
        if female:
            lastname = f"{father}ssdottir"
        else:
            lastname = f"{father}son"
    else:
        lastname = f'{choice(clanprefix)}{choice(clansuffix)}'
    result = f'{firstname.capitalize()} {lastname.capitalize()}'
    if female:
        result = f"{result} (f.)"
    return result

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

def town_name_generator():
    '''Generates a town name'''
    with open(f"{FILEPATH}/referencedata/TownNames.json", "r", encoding='utf8') as file:
        data = json.load(file)

    result = ''
    roll = randint(1, 4)
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
    roll = randint(1, 10)
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
    roll = randint(1, 10)
    if roll == 1:
        #religious book
        newroll = randint(1, 4)
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
        bioroll = randint(1, 2)
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
        magicroll = randint(1, 4)
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
        talesroll = randint(1, 3)
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
        historyroll = randint(1, 4)
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
        georoll = randint(1, 3)
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
        lingroll = randint(1, 2)
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
    roll = randint(0, 2)
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
    print(f"Demon Name              : {demon_name()}")
    print(f"Town Name               : {town_name_generator()}")
    print(f"Wood Name               : {woodname_generator()}")
    print(f"Street Name             : {streetname_generator()}")
    print(f"Dwarven Settlement Name : {dwarven_settlement_name_generator()}")
    print(f"Place Name              : {place_name_generator()}")
    print(f"Book Title              : {book_title_generator()}")
    print(f"Book Title              : {book_title_generator(catalogue=True)}")

if __name__ == "__main__":
    main()
