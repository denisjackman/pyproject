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
    adjs = ["bitter","burning","dwarf","fire","ice","master","night","old","snow","sweet","wild"]
    thing = ["angel","bishop","corpse","demon","elf","hag","hangman","king","knight","lady","maiden","mountain","oak","queen","shepard","spring","virgin","winter","witch"]
    color = ["black","blue","gold","green","purple","red","silver","white","yellow"]
    creature = ["adder","boar","bull","cock","demon","devil","dragon","drake","eagle","falcon","fox","goat","hare","hawk","hind","hound","lion","owl","ox","ram","rat","raven","serpent","shadow","snake","stag","swine","wolf","wyrm","wyvern"]
    misc = ["bane","beard","blood","bone","clover","crown","eye","feather","foot","fruit","grass","heart","leaf","nut","pepper","root","rose","seal","seed","spike","tail","thorn","tongue","weed","wort"]
    suff = ["aas","aca","acca","acea","ach","age","ali","am","amom","amon","ana","ander","any","ard","bate","bena","berry","cana","cena","cess","cia","der","dock","drake","el","ell","eric","few","frey","gal","gana","gol","gon","gul","ian","iar","ica","icle","il","ilia","in","ind","indes","iper","ite","ley","lic","many","mile","mond","mony","mus","na","nel","net","nis","oe","ome","ony","ory","osa","osia","per","pias","ram","rans","rant","ranth","ray","rel","rind","rome","ron","rosia","row","rue","sali","se","seng","shade","sley","spur","tany","thal","ther","thin","url","us","usar","vil","vir","way","wort"]
    pref = ["ab","aca","acon","ad","ado","ag","agri","al","aleth","alka","ama","amb","ani","ans","ar","aric","asara","ath","ati","bal","bar","bas","bel","bil","bor","bry","bur","caf","caff","cal","cala","cara","card","cel","chamo","cher","cinn","col","com","cori","cum","cur","dil","dit","echin","ed","el","eld","els","fen","fetha","fumi","gar","gin","hol","jan","jin","jinn","jun","kal","kel","kla","lar","lor","lot","lung","man","mari","marjer","mug","mull","nap","night","ore","par","pe","peri","ras","sad","saff","san","sav","sen","sera","sor","stra","tama","tamar","tarra","teph","thu","tum","val","valer","ver","wan","win","yar","zal","zu"]
    name = ["Amanapa","Arannash","Aspin","Astarte","Avilion","Celindaria","Crystanor","Dalis","Denudiel","Derenome","Doniri","Dwinian","Egildas","Elargir","Eldraz","El-Wisbin","Eninope","Findrillian","Foobar","Fordulana","Hirondelle","Ignius","Isrid","Jinarf","Lagwyn","Loriel","Margwas","Melpomene","Meridian","Mitzi","Mortick","Mystrene","Nilf","Ornill","Pildar","Prodge","Quailandir","Ravaniof","Repetitios","Rhyidon","Rhyndis","Sidiar","Spiridon","Splinders","Spork","Syniara","Tiffany","Trisilyan","Valdison","Vermopolis","Vevrissan","Widgil","Wrastforth","Xandiri","Zwind"]

    with open(f"{FILEPATH}/../referencedata/HerbNames.json", "w", encoding='utf8') as file:
        json.dump({"herb_adj": adjs,
                   "herb_thing": thing,
                   "herb_color": color,
                   "herb_creature": creature,
                   "herb_misc": misc,
                   "herb_suff": suff,
                   "herb_pref": pref,
                   "herb_name": name},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
