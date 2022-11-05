'''
    this converts a tab file into a json file
'''
from pathlib import Path
import json
    # generate the random numbers based on the len of the lists
    # build the results

FILEPATH = Path(__file__).parent

def main():
    '''
        main function
    '''

    affix = ["east","fort","high","lake","low","mount","new","north","old","port","south","west"]
    prefix = ["abbey","abbots","aber","ad","amber","ard","arrow","ash","ashen","autumn","ballin","bards"]
    suffix = [ "abbey","ant","arbor","bank","bluff","bourne","bridge","brook","burg","bury","by","caster"]

    with open(f"{FILEPATH}/../referencedata/ExampleNames.json", "w", encoding='utf8') as file:
        json.dump({"town_name_affix":affix, "town_name_prefix": prefix, "town_name_suffix": suffix}, file)
    print(f"Affix : {len(affix)} Prefix: {len(prefix)} Suffix: {len(suffix)} ")

if __name__ == "__main__":
    main()
