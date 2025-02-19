#!/usr/bin/env python
# Import the os module, for the os.walk function
'''
    file RENAMEr
'''
import os
import sys
import getopt
import magic


ext = {"Apple QuickTi": "mov",
       "ISO Media, MP": "mp4",
       "Longer, Uncut": "avi",
       "Matroska data": "mkv",
       "MPEG sequence": "mpeg",
       "Ogg data, OGM": "ogg",
       "RIFF (little-": "avi"}

SERIES = ''
SEASON = ''
RENAME = False

# set the directory you want to start from
ROOTDIR = '.'

try:
    opts, args = getopt.getopt(sys.argv[1:], "hrn:s:", ["name=", "SEASON="])
except getopt.GetoptError:
    print('filenamer.py -n <Name> -s <SEASON> -r ')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('filenamer.py -n <Name> -s <SEASON> -r ')
        sys.exit()
    elif opt in ("-n", "--name"):
        SERIES = arg
    elif opt in ("-s", "--SEASON"):
        SEASON = arg
    elif opt in ("-r", "--RENAME"):
        RENAME = True
    else:
        print('filenamer.py -n <Name> -s <SEASON> -r')
        sys.exit()

if SERIES == "":
    sys.exit()

if SEASON == "":
    sys.exit()

for dirName, subdirList, fileList in os.walk(ROOTDIR):
    for fname in fileList:
        if fname.find('.') == -1:
            name = fname[2:]
            extension = magic.from_file(dirName+"/"+fname)[:13]
            episode = fname[:2]
            newfile = SERIES+"."+SEASON+episode+"."+name+"."+ext[extension]
            if RENAME:
                print(f"+[{fname}][{newfile}] - RENAMEd")
                os.RENAME(fname, newfile)
            else:
                print(f"+[{fname}][{newfile}] - test")
