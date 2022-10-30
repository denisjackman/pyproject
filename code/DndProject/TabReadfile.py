'''
    exmple read json file from tab file
'''
import json
import random

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

    itemcount = number_generator(171-1)
    result = f"question ({itemcount}): {data['question'][itemcount]}, answer: {data['answer'][itemcount]}"
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
    # Each Column is used to build the insult
    column_one = ("artless", "bawdy", "beslubbering", "bootless", "churlish",
                  "cockered", "clouted", "craven", "currish", "dankish",
                  "dissembling", "droning", "errant", "fawning", "fobbing",
                  "froward", "frothy", "gleeking", "goatish", "gorbellied",
                  "impertinent", "jarring", "loggerheaded", "lumpish", "mammering",
                  "mangled", "mewling", "paunchy", "pribbling", "puking", "puny",
                  "qualling", "rank", "reeky", "roguish", "ruttish", "saucy", "spleeny",
                  "spongy", "surly", "tottering", "unmuzzled", "vain", "venomed",
                  "villainous", "warped", "wayward", "weedy", "yeasty")
    column_two = ("base-court", "bat-fowling", "beef-witted", "beetle-headed",
                  "boil-brained", "clapper-clawed", "clay-brained",
                  "common-kissing", "crook-pated", "dismal-dreaming",
                  "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing",
                  "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed",
                  "fly-bitten", "folly-fallen", "fool-born", "full-gorged",
                  "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed",
                  "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", "motley-minded",
                  "onion-eyed", "plume-plucked", "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn",
                  "rude-growing", "rump-fed", "shard-borne", "sheep-biting", "spur-galled", "swag-bellied",
                  "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted", "weather-bitten")
    column_three = ("apple-john", "baggage", "barnacle", "bladder", "boar-pig",
                    "bugbear", "bum-bailey", "canker-blossom", "clack-dish",
                    "clotpole", "coxcomb", "codpiece", "death-token",
                    "dewberry", "flap-dragon", "flax-wench", "flirt-gill",
                    "foot-licker", "fustilarian", "giglet", "gudgeon",
                    "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger",
                    "joithead", "lewdster", "lout", "maggot-pie", "malt-worm",
                    "mammet", "measle", "minnow", "miscreant", "moldwarp",
                    "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock",
                    "pumpion", "ratsbane", "scut", "skainsmate", "strumpet",
                    "varlet", "vassal", "whey-face", "wagtail")
    # generate the random numbers based on the len of the lists
    xero = number_generator(len(column_one)-1)
    yero = number_generator(len(column_two)-1)
    zero = number_generator(len(column_three)-1)
    # build the results
    result = f"Thou {column_one[xero]} {column_two[yero]} {column_three[zero]}."
    # return it
    return result

def dwarven_insult_generator():
    '''
        dwarven insult generator
    '''
    dwarven_insult_one = ("babbling", "barbed", "beardless", "bulbous", "cantankerous",
                          "craftless", "dainty", "dangling", "drooling", "friendless",
                          "fungular", "gemless", "gibbering", "incompetent", "mouldy",
                          "pompous", "reeking", "repugnant", "rickety", "slothful", "tentacled",
                          "unhoned", "unweened", "warty", "witless")
    dwarven_insult_two = ("anvil-dropping", "axe-breaking", "bunyon-brained", "cave-slinking",
                          "chasm-hearted", "crystal-breaking", "donkey-eared", "elf-kissing",
                          "fish-catching", "gnat-ridden", "hearth-hating", "lantern-lugging",
                          "milk-drinking", "moss-bearded", "nib-chewing", "nose-picking",
                          "pech-skulled", "porridge-faced", "rust-minded", "silver-witted",
                          "slate-carving", "toe-biting", "toll-snatching", "tree-climbing", "willow-waisted")
    dwarven_insult_three = ("armpit", "breadcrumb", "carbuncle", "fuzzpot", "gargoyle", "gas spore",
                            "gasbladder", "goblin-spawn", "ledge lizard", "mole", "mushroom", "natterling",
                            "osquip", "pebble", "pestle", "pixie", "rockrunt", "rust monster", "shard", "smudge-rubber",
                            "snake's egg", "stalactite", "stench kow", "thumb-basher", "tunnel worm")

    xero = number_generator(len(dwarven_insult_one)-1)
    yero = number_generator(len(dwarven_insult_two)-1)
    zero = number_generator(len(dwarven_insult_three)-1)

    result = f"{dwarven_insult_one[xero].capitalize()} {dwarven_insult_two[yero]} {dwarven_insult_three[zero]}"
    return result

def main():
    '''
        Main function
    '''
    print(f"Shakey  insult  : {shakespearean_insult_generator()}")
    print(f"Shakey  insult  : {shakespearean_insult_generator()}")
    print(f"Dwraven insult  : {dwarven_insult_generator()}")
    print(f"Dwarven insult  : {dwarven_insult_generator()}")
    print(f"Riddle Question : {riddle_generator()}")
if __name__ == "__main__":
    main()

