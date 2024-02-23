''' dnd other items mmodule '''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/25 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import platform
import json
from random import choice
#from dnddice import dice

if platform.system() == "Windows":
    FILEPATH = "Z:/Resources/development"
else:
    FILEPATH = "/mnt/y/Resources/development"


def oracle_generator():
    '''Generates an oracle'''

    with open(f"{FILEPATH}/referencedata/Oracles.json", "r", encoding='utf-8-sig') as file:
        data = json.load(file)

    oracle_noun = choice(data["oracle_noun"])
    oracle_prepostion = choice(data["oracle_prepostion"])
    oracle_adverb = choice(data["oracle_adverb"])
    oracle_adjective = choice(data["oracle_adjective"])
    oracle_instransient_verb_phrase = choice(data["oracle_instransient_verb_phrase"])
    oracle_conjuction = choice(data["oracle_conjuction"])
    oracle_complete_visions = choice(data["oracle_complete_visions"])

    result = f'{oracle_noun} {oracle_prepostion} {oracle_adverb}'
    return result

def main():
    '''Main function'''
    print(f"Welcome to the {oracle_generator()}!")

if __name__ == '__main__':
    main()
