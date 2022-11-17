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
    vcvc = ["agam","agar","akan","akar","alan","alim","amar","asar","azag","ebir","eden","edim","edin","egir","elam","enar","enir","epir","eren","erib","erim","erin","esan","esig","esir","ezem","ezen","idig","idim","imin","inar","inim","isim","itid","itim","itud","ubil","ubur","udug","udun","ugar","ugun","ukum","ukur","ulul","umab","umum","umun","unug","unum","urim","urin","urum","usan","usar","usug","utab","utug","utul","uzug"]
    mix = ["lu-e","ku-a","sha","she"]
    ccvc = ["shab","shag","shak","shal","sham","shap","shar","shed","sheg","shem","shen","sher","shes","shib","shid","shig","shim","ship","shir","shit","shub","shud","shug","shul","shum","shun","shur","skim"]
    cv = ["ba","da","ga","ha","ia","ka","la","ma","na","pa","ra","sa","ta","za","be","de","ge","he","ke","le","me","ne","pe","re","se","te","ze","bi","di","ei","gi","ki","li","mi","ni","pi","ri","si","ti","zi","bu","du","du'","gu","hu","ku","lu","mu","nu","pu","ru","su","tu","zu"]
    cvc = ["bab","bad","bag","bak","bal","ban","bap","bar","baz","ben","bid","bil","bin","bir","biz","bol","bub","bud","bul","bum","bun","bup","bur","buz","dab","dag","dak","dal","dam","dan","dar","del","dib","did","dig","dil","dim","din","dir","dub","dug","duh","duk","dul","dum","dun","dur","egi","esh","esi","ezi","gab","gag","gak","gal","gam","gan","gar","gaz","gen","gib","gid","gig","gik","gil","gim","gin","gir","git","giz","gub","gud","gug","guk","gul","gum","gun","gur","guz","har","hin","hub","hul","hun","hur","kab","kad","kak","kal","kam","kan","kar","kas","kid","kik","kil","kim","kin","kir","kis","kud","kug","kuk","kul","kum","kun","kur","kus","lab","lad","lag","lak","lal","lal'","lam","lan","lib","lid","lil","lim","lub","lud","lug","lul","lum","lun","lus","mab","mad","man","mar","mel","men","mer","mes","mid","min","mir","mud","mug","muk","mul","mun","mur","nad","nag","nal","nam","nan","nar","nen","ner","nib","nid","nig","nim","nin","nir","nis","niz","nud","nug","nun","nus","nuz","pab","pad","pag","pan","pap","par","pil","pin","pir","pun","rab","ran","rap","rib","rig","rim","rin","rub","rud","rug","rum","run","sad","sag","sal","sam","san","sar","sed","seg","ses","shi","sid","sig","sik","sil","sim","sin","sir","sis","sub","sud","sug","suh","suk","sul","sum","sun","sur","sus","tab","tag","tak","tal","tam","tan","tar","ten","tib","til","tim","tin","tir","tub","tud","tug","tuk","tul","tum","tun","tur","ush","zab","zag","zal","zan","zar","zeb","zer","zib","zid","zig","zil","ziz","zub","zud","zum","zur"]
    cvcc = ["bash","gash","kash","mash","rash","desh","kesh","mesh","nesh","pesh","tesh","dish","kish","mish","nish","pish","bush","kush","lush","mush","push","rush","sush","tush"]
    cvcv = ["bada","bala","bala'","bara","bira","buru","dala","dara","deri","dida","didi","dili","diri","dumu","duru","dutu","gaba","gada","gaga","gage","gala","gana","gara","gazi","geme","gidi","gili","giri","gisu","guda","gula","gunu","guru","inda","kala","kara","kili","kiri","kisi","kuba","kuru","lama","lima","limi","liri","liru","luki","luma","lusu","mabi","mana","medu","meli","meze","mina","munu","muru","nala","nana","naza","nele","neme","niga","nigu","nili","ninu","niri","nisi","nita","pala","pana","para","rutu","sagi","sesi","sila","sipa","suku","suru","taka","tena","tuku","tuma","tumu","zubu"]
    vc = ["ab","ad","ag","ak","al","am","an","ar","as","az","eb","ed","eg","el","em","en","er","ib","id","ig","ik","il","im","in","ir","is","it","iz","or","uh","ub","ud","ug","uk","ul","um","un","ur","us","ut","uz"]
    vccv = ["ebla","emma","esha","imma","ugra","asha","iani","ishi","ashe","eshe","ensi","illu","ummu","urdu","urgu","ushu","ussu"]
    vcv = ["aba","ada","aga","aka","ala","ama","ana","ara","asa","dra","eda","era","ida","ila","ima","ira","uga","una","die","due","eme","azu","eru","iku","itu","mau","pau","riu","shu","udu","ugu","uku","ulu","umu","unu","uru","usu","utu","uzu","uri","abi","ali","ash","asi","ibi","idi","igi","ili","imi","isi","iti","izi"]


    with open(f"{FILEPATH}/../referencedata/SumerianNames.json", "w", encoding='utf8') as file:
        json.dump({"sumerian_vcvc": vcvc,
                   "sumerian_mix": mix,
                   "sumerian_ccvc": ccvc,
                   "sumerian_cv": cv,
                   "sumerian_cvc": cvc,
                   "sumerian_cvcv": cvcv,
                   "sumerian_vc": vc,
                   "sumerian_vccv": vccv,
                   "sumerian_vcv": vcv},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
