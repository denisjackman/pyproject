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
    prefix = ["Agh","Alim","Aquil","Ar","Arg","As","Bel","Boss","Bry","Cim","Cor","Dar","Er","Gal","Gun","Hal","Hyp","Hyr","Ian","Ir","Kass","Kesh","Khaur","Khaw","Khem","Khit","Khor","Khor","Khor","Kor","Kord","Koth","Kush","Kuth","Larsh","Lux","Mes","Nem","Num","Oph","Pte","Punt","Sam","Shad","Sham","Shang","Styg","Sul","Sukh","Tan","Taur","Tur","Tyb","Van","Vendh","Vil","Xa","Xuch","Xuth","Zam","Zarkh","Zing"]
    suffix = ["a","ai","aja","al","ali","an","ane","ar","ara","as","ava","borea","boula","chem","der","e","eba","ed","en","eria","er","es","far","gal","gard","heim","i","ia","ia","in","ir","ish","ism","istan","jun","kan","land","mer","met","og","on","onia","or","ora","org","os","ot","otl","par","pur","ra","san","shem","tana","the","thia","thun","tia","uk","ul","un","ur","us","ver","ya","yet","zar"]

    with open(f"{FILEPATH}/../referencedata/HyborianNames.json", "w", encoding='utf8') as file:
        json.dump({"hyborian_prefix": prefix,
                   "hyborian_suffix": suffix},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
