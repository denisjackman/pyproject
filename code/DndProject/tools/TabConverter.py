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
# pylint: disable=too-many-locals

def main():
    '''
        main function
    '''
    adj = ["Bright","Burning","Dead","Eternal","Forgotten","Golden","Living","Lost","Shining","Silver","Sunken","Undying"]
    place = ["Castle","Cave","Chasm","City","Coast","Desert","Field","Forest","Fortress","Fountain","Garden","Grove"]
    thing = ["the Abyss","Blood","Bronze","Dawn","the Dead","Doom","Dragons","Dread","Dust","Eternal Peril","Fire"]

    with open(f"{FILEPATH}/../referencedata/SiteNames.json", "w", encoding='utf8') as file:
        json.dump({"site_adj": adj,
                   "site_place": place,
                   "site_thing": thing},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
