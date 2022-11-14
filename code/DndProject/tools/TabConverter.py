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
    adj = ["abhorrent","abominable","ancient","black","blasphemous","crawling","creeping","crypt","damned","dark","dead","deep","dimensional","dread","elder","eldritch","esoteric","evil","faceless","flying","formless","gaunt","hideous","horrific","living","loathsome","lurking","mad","mist","night","red","shadow","shambling","shunned","sightless","slithering","star","tomb","white","winged"]
    noun = ["beasts","burrowers","children","crawlers","creatures","creepers","dead","devourers","dwellers","followers","hounds","horrors","hunters","ones","ooze","outsiders","polyps","prowlers","servants","shamblers","spawn","stalkers","things","walkers","worms","young"]
    prefv = ["aza","bya","ctha","gha","ghata","golo","itha","kha","kla","nya","nyag","nyarla","tsa"]
    prefc = ["ab","ash","ashtor","azar","azaz","byak","byal","chaug","cthon","cthug","cthul","dag","faug","ghatan","hal","hast","ith","ithaq","kyn","len","leng","nyar","nyog","r'y","shog","shub","soth","tsag","tsath","y'g","yith","yog"]
    suff = ["ash","aten","azar","azash","ekesh","eth","gash","gha","gon","goth","gua","hotep","hoth","hu","ikesh","kesh","khee","lash","loth","lyeh","nac","nar","nash","oggua","on","onac","oth","othoa","rath","tha","thal","thoa","thotep","thoth","ugha","ulhu","urath","ze"]

    with open(f"{FILEPATH}/../referencedata/LovecraftCreatures.json", "w", encoding='utf8') as file:
        json.dump({"lovecraft_adjective": adj,
                   "lovecraft_noun": noun,
                   "lovecraft_prefixv": prefv,
                   "lovecraft_prefixc": prefc,
                   "lovecraft_suffix": suff},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
