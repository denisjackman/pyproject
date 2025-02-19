''' file unpacker '''
import os
import sys
import zipfile36 as zipfile
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through

BASE_DIR = "Y:/Data/Goodreads/"
TARGET_DIR = "Y:/Data/Temp/"


def main():
    ''' main function'''
    main_args = {"verbosemode": False,
                 "debugmode": False,
                 "startdirectory": BASE_DIR,
                 "xmode": False}
    main_list = walk_through(main_args)
    for item in main_list:
        print(f"[-] Processing {item} ")
        if os.path.splitext(item)[1] == ".zip":
            with zipfile.ZipFile(item, "r") as zip_ref:
                zip_ref.extractall(TARGET_DIR)


if __name__ == '__main__':
    main()
