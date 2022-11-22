''' dnd other items mmodule '''
from pathlib import Path
import json
from random import choice
from dnddice import dice

FILEPATH = Path(__file__).parent

def riddle_generator():
    ''' riddle generator '''
    filename = f"{FILEPATH}/referencedata/Riddles.json"
    with open(filename, "r", encoding='utf8') as file:
        data = json.load(file)

    riddle = choice(data['riddle_question'])
    itemcount = data['riddle_question'].index(riddle)
    result = f"question ({itemcount}): {data['riddle_question'][itemcount]}, answer: {data['riddle_answer'][itemcount]}"
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
    oracle_instransient_verb_phrase = ("arrives", "beckons", "takes a rest", "becomes clear",
                                       "learns", "removes a block", "meditates", "remembers the soul",
                                       "jumps without a net", "remembers everything", "cleans the window of awareness",
                                       "feels truth", "returns", "rejoices", "prays", "takes action", "dreams",
                                       "ceases to exist", "hides", "chooses", "laughs with joy", "plays without questioning",
                                       "loves", "wakes up", "hesitates and moves anyway", "trembles with comprehension",
                                       "reflects", "is born", "finds inspiration", "feels completely full", "senses",
                                       "sees", "joins the path", "listens", "reasons", "sits", "flies", "sings",
                                       "knows")
    oracle_conjuction = ("and", "but", "for", "nor",
                         "or", "so", "yet", "becuase")
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

def main():
    ''' main function '''
    print(f"Currency                : {currency_converter(100)}")
    print(f"Currency                : {currency_converter(1, fromcurr='gold', tocurr='copper')}")
    print(f"Currency                : {currency_converter(10, fromcurr='gold', tocurr='gold')}")
    print(f"Currency                : {currency_converter(1, fromcurr='copper', tocurr='gold')}")
    print(f"Currency                : {currency_converter(1, fromcurr='fliiter', tocurr='gold')}")
    print(f"Currency                : {currency_converter(1, fromcurr='gold', tocurr='fliiter')}")
    print(f"Riddle Question         : {riddle_generator()}")
    print(f"Wine Name               : {fantasy_wine_name()}")
    print(f"Hexmap tile             : {hexmap_tile_type()}")

if __name__ == "__main__":
    main()
