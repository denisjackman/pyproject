'''
    Name : TabConverter.py

    Function :
    This is a converter for the Data items from TAB files to JSON files
    The TAB files are from the DnD 5e SRD
'''
__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from pathlib import Path
import json

FILEPATH = Path(__file__).parent

def main():
    '''
        main function
    '''
    prefix = ["Ag","Al","Ald","Alf","Ar","Arn"]
    suffixmale = ["ain","ald","ar","ard","arr"]
    suffix = ["a","asi","bera","bina","bora"]
    clanprefix = ["ale","anvil","armor","axe"]
    clansuffix = ["arm","axe","back","bane","beard"]
    with open(f"{FILEPATH}/../referencedata/DwarvenNames.json", "w", encoding='utf8') as file:
        json.dump({"dwarven_name_prefix": prefix,
                   "dwarven_name_suffixmale": suffixmale,
                   "dwarven_name_suffix": suffix,
                   "dwarven_clan_prefix": clanprefix,
                   "dwarven_clan_suffix": clansuffix},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
