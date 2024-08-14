''' this is a fire script'''
import os
import sys

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through

CONSOLIDATE_DIR = 'This PC/Fire/Storage device/Books'


def main():
    '''Main function'''
    print('[-] Main Function Starting...')
    picture_mainargs = {"verbosemode": False,
                        "deletemode": False,
                        "startdirectory": CONSOLIDATE_DIR,
                        "targetdirectory": CONSOLIDATE_DIR}
    picture_filelist = walk_through(picture_mainargs)
    print(picture_filelist)


if __name__ == '__main__':
    main()
