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
    community = ["City","Town","Village","Mines","Deep","Delving"]
    prefix = ["Stone","Granite","Deep","Iron","Rock","Silver","Crystal"]
    suffix = ["hold","home","delve","deep","mine","fast"]
    with open(f"{FILEPATH}/../referencedata/DwarvenSettlementNames.json", "w", encoding='utf8') as file:
        json.dump({"dwarven_settlement_community": community, "dwarven_settlement_prefix": prefix, "dwarven_settlement_suffix": suffix}, file)
    print(f"Community: {len(community)} Prefix: {len(prefix)} Suffix: {len(suffix)} ")

if __name__ == "__main__":
    main()
