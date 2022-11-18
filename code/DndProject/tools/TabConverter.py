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
    adj = ["accursed","arcane","astral","azure","benevolent","black","blessed","blue","brass","brave","bronze","burning","celestial","cerulean","chromatic","copper","courageous","crimson","crystal","cursed","dark","diamond","divine","emerald","eternal","ethereal","fallen","glass","glorious","gold","golden","green","grey","hidden","holy","imperial","infernal","invincible","iron","jade","just","legendary","lost","magic","magical","malevolent","merciful","mighty","mystic","mystical","oak","obsidian","opal","orange","pure","purple","red","royal","ruby","sacred","sapphire","scarlet","secret","silver","steel","stone","unholy","veiled","white","yellow"]
    obj = ["arrow","axe","bat","bear","blade","bull","castle","chalice","city","cloud","crescent","cross","crow","crown","cup","dagger","dark","dawn","dragon","drake","dusk","eagle","eye","falcon","fist","flame","forest","forge","fox","gate","gauntlet","gem","griffin","hand","hart","hawk","heart","helm","hill","horn","hound","king","knife","knight","light","lion","lotus","moon","mountain","night","ocean","queen","raven","ring","river","rose","rune","scorpion","scroll","sea","serpent","shadow","shard","shield","skull","spider","staff","stag","star","storm","sun","sword","tome","tower","town","truth","village","wall","wind","wizard","wolf","word","wyrm","wyvern"]
    group = ["alliance","band","brotherhood","brothers","cabal","circle","clan","compact","company","coven","covenant","cult","defenders","fellowship","fighters","guardians","guards","guild","heroes","horde","house","hunters","keepers","knights","masters","order","protectors","raiders","regulars","ring","seekers","servants","sisterhood","sisters","society","tribunal","trinity","wanderers","warriors","watchers","way"]
    pluralform = {"city": "cities","cross": "crosses","fox": "foxes","knife": "knives","lotus": "lotuses","staff": "staves","wolf": "wolves"}

    with open(f"{FILEPATH}/../referencedata/OrganizationNames.json", "w", encoding='utf8') as file:
        json.dump({"org_adj": adj,
                   "org_obj": obj,
                   "org_group": group,
                   "org_pluralform": pluralform},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
