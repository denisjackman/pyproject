#!/usr/bin/env python
# Import the os module, for the os.walk function
'''
    file renamer
'''
import os
import magic
import sys
import getopt


ext = {   "Apple QuickTi":"mov",
          "ISO Media, MP":"mp4",
          "Longer, Uncut":"avi",
          "Matroska data":"mkv",
          "MPEG sequence":"mpeg",
          "Ogg data, OGM":"ogg",
          "RIFF (little-":"avi"}

series = ''
season = ''
rename = False

# Set the directory you want to start from
rootDir = '.'

try:
    opts, args = getopt.getopt(sys.argv[1:], "hrn:s:", ["name=", "season="])
except getopt.GetoptError:
    print('filenamer.py -n <Name> -s <season> -r ')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('filenamer.py -n <Name> -s <season> -r ')
        sys.exit()
    elif opt in ("-n", "--name"):
        series = arg
    elif opt in ("-s", "--season"):
        season = arg
    elif opt in ("-r", "--rename"):
        rename = True
    else:
        print('filenamer.py -n <Name> -s <season> -r')
        sys.exit()

if series == "":
    sys.exit()

if season == "":
    sys.exit()

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.find('.') == -1:
             name = fname[2:]
             extension = magic.from_file(dirName+"/"+fname)[:13]
             episode = fname[:2]
             newfile = series+"."+season+episode+"."+name+"."+ext[extension]
             if rename:
                print(f"+[{fname}][{newfile}] - renamed")
                os.rename(fname, newfile)
             else:
                print(f"+[{fname}][{newfile}] - test")
