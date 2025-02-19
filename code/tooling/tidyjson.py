'''
    Name : tidyjson.py

    Function :
    This takes all the JSON files in the
    referencedata folder and tidies them up.

'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.00 $"
__date__ = "$Date: 2022/11/01 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import os
import json

FILEPATH = "Z:/Resources/development/"
ROOTDIR = f"{FILEPATH}referencedata/"


def main():
    ''' main '''
    for dirName, subdirList, fileList in os.walk(ROOTDIR):
        for fname in fileList:
            filename = f"{ROOTDIR}/{fname}"
            with open(filename, "r", encoding='utf-8-sig') as file:
                data = json.load(file)
            with open(filename, "w", encoding='utf-8-sig') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
