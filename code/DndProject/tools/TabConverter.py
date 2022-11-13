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
    vc = ["aal","al","an","ang","atl","ax","axl","az","il","ill","is","iss","it","ith","itz","iz","otl","ov","oxl","us","uss","uz"]
    vv = ["a","aka","aza","i","ila","illa","iza","o","ova","ovi"]
    cv = ["cha","chka","cho","chta","hexo","hu","ka","kaa","kha","khi","ki","kii","kra","kry","ky","kzo","la","pa","qua","que","ra","rasa"]
    cc = ["ch","cotl","cus","haat","has","hass","haz","hex","his","hiss","huax","kaar","kar","khat","kil","kis","kys","lan","mas","mass","mis","miss","pec","poc","ptar","pter","ras","rep","rept","sal","sith","tak","tan","tax","tec","tek","tep","than","this","tis","tl","tlac","tlan","tlax","trax","tzun","val","var","vas","ven","vil","vis","xh","xlan","yxl","zaal","zah","zak","zal","zla"]

    with open(f"{FILEPATH}/../referencedata/LizardNames.json", "w", encoding='utf8') as file:
        json.dump({"lizard_vc": vc,
                   "lizard_vv": vv,
                   "lizard_cv": cv,
                   "lizard_cc": cc},
                  file,
                  indent=4,
                  ensure_ascii=False)

if __name__ == "__main__":
    main()
