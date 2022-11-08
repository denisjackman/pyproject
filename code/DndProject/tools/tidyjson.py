'''
    json tidy tool
'''
import os
from pathlib import Path
import json


FILEPATH = Path(__file__).parent
ROOTDIR = f"{FILEPATH}/../referencedata/"

def main():
    ''' main '''
    for dirName, subdirList, fileList in os.walk(ROOTDIR):
        for fname in fileList:
            filename = f"{ROOTDIR}/{fname}"
            with open(filename, "r", encoding='utf8') as file:
                data = json.load(file)
            with open(filename, "w", encoding='utf8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
