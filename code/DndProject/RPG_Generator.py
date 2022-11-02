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
import json
import random
from random import choice
from random import randint

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
    with open("Y:/Resources/dnd/Riddles.json", "r", encoding='utf8') as file:
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
    with open("Y:/Resources/dnd/ShakespeareInsult.json", "r", encoding='utf8') as file:
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
    with open("Y:/Resources/dnd/DwarvenInsult.json", "r", encoding='utf8') as file:
        data = json.load(file)
    dwarven_insult_one = choice(data["insult_column_one"]).capitalize()
    dwarven_insult_two = choice(data["insult_column_two"])
    dwarven_insult_three = choice(data["insult_column_three"])
    result = f"{dwarven_insult_one} {dwarven_insult_two} {dwarven_insult_three}."
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

def fantasy_wine_name():
    '''
        fantasy wine name generator
    '''
    with open("Y:/Resources/dnd/FantasyWines.json", "r", encoding='utf8') as file:
        data = json.load(file)
    wine_name = choice(data['wine_name'])
    result = f"{wine_name}"
    return result

def angelic_name():
    ''' angelic names '''
    with open("Y:/Resources/dnd/AngelNames.json", "r", encoding='utf8') as file:
        data = json.load(file)
    prefix = choice(data['angel_prefix'])
    suffix = choice(data['angel_suffix'])
    result = f'{prefix}{suffix}'
    return result.capitalize()

def barbarian_name():
    ''' barbarian names '''
    with open("Y:/Resources/dnd/BarbarianNames.json", "r", encoding='utf8') as file:
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
    syllable= ["slag","el","nagir","girruk","zug","tha","meg","skal","deth","esh","uth","sshul","zan","zhel",
               "khs","chal","vush","chlu","varn","elts","ch","aa","ugg","ksin","ven","phod","sagy","aak",
               "qek","zohr","kkis","eg","zan","gkil","aezg","gluU"]

    roll = randint(1, 7)
    if roll <= 2:
        result = "'" + choice(syllable)
    elif roll <= 3:
        result = "-" +choice(syllable)
    else:
        result = choice(syllable)
    return result

def demon_name_one():
    ''' demon name generator '''
    syllable= ["slag","el","nagir","girruk","zug","tha","meg","skal","deth","esh","uth","sshul","zan","zhel",
               "khs","chal","vush","chlu","varn","elts","ch","aa","ugg","ksin","ven","phod","sagy","aak",
               "qek","zohr","kkis","eg","zan","gkil","aezg","gluU"]
    roll = randint(1, 7)
    result = ''
    if roll <=4:
        result = build_demon_name() + build_demon_name()
    elif roll <=6:
        result = build_demon_name() + build_demon_name() + build_demon_name()
    else:
        result = build_demon_name() + build_demon_name() + build_demon_name() + build_demon_name()

    return f"{choice(syllable).capitalize()}{result}"

def demon_name_two():
    ''' demon name generator'''

    truename_elements = ["a","er","fol","n'n","thl","an","e","il","rh","yy",
                         "cog","kw","mm","th","ak","du","i","ow","y","ch",
                         "fl","pp","sh","ae","dh","hl","oo","uu","io","ff",
                         "ll","z","abl","dh","hh","oe","ul","bh","eu","ks",
                         "ss","aa","de","gz","oa","u","ar","eo","ir","q'",
                         "cc","da","g'g","o","tl","ao","ee","il","ph","zh"]
    usename_elements = ["blue","suck","chew","sword","canker","rut","mark","grab","vile","worm","maim",
                        "doom","break","rheum","lewd","fiend","spurt","spot","howl","bite","dangle","thigh",
                        "dog","wrack","eat","skull","red","gristle","whip","blech","moulder","foul","dread",
                        "scum","plague","gnash","throb","warp","lust","claw","dreg","bane","gibber","cackle",
                        "fester","spike","spider","helm","blunt","bog","pinch","grin","eye","smut","slake",
                        "grasp","war","bend","man","filth","fondle","carnal","gnaw","fang","flux","tremble",
                        "thrash","loon","drink","buttock","scratch","loose","thrust","tear","squeeze","hack",
                        "beetle","blight","ooze","glutton","grind","fiddle","grope","hammer","glut","vomit",
                        "bag","pest","gall","crush","slobber","putrid","fury","twist","whine","lick","craze",
                        "bowel","rotten","kill","grunt","hot","maul","mildew","hate","wind","blade","puke",
                        "gross","fire","spew","slob","grue","water","ash","nibble","flesh","clap","sinew",
                        "pain","mad","mucus","offal","rot","ichor","brute","cold","rip","maggot","froth",
                        "stare","sting","heart","blast","beast","pierce","gore","fat","slug","scrape","pox",
                        "sate","pus","toad","leper","dung","death","sharp","rabid","gobble","wart","wither",
                        "loath","cut","chaos","reap","lip","flush","spoor","spine","quiver","vex","spasm",
                        "bile","mire","glop","face","spume","sore","grim","wobble","axe","mange","foam",
                        "crab","scab","pile","fume","venom","wail","slash","bubo","spittle","blister","rend",
                        "gut","fist","sweat","taint","liver","blood","black","quake","green","drool","spite",
                        "sin","gob","wight","burble"]
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
        truename = f'{truename}{choice(truename_elements)}'
    usename = f'{choice(usename_elements)}{choice(usename_elements)} {choice(usename_elements).title()}{choice(usename_elements)}'
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

def main():
    '''
        Main function
    '''
    print(f"Shakey  insult  : {shakespearean_insult_generator()}")
    print(f"Dwarven insult  : {dwarven_insult_generator()}")
    print(f"Riddle Question : {riddle_generator()}")
    print(f"Wine Name       : {fantasy_wine_name()}")
    print(f"Angelic Name    : {angelic_name()}")
    print(f"Barbarian Name  : {barbarian_name()}")
    print(f"Dwarven Name    : {dwarven_name()}")
    print(f"Demon Name      : {demon_name()}")

if __name__ == "__main__":
    main()
