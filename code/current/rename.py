#!/usr/bin/env python
'''
    RENAME utility for renaming files
'''
# Import the os module, for the os.walk function
import os
import sys
import getopt

# set the directory you want to start from
# DrWho.S0
# Doctor.Who.2005.S0
ROOTDIR = '.'
RENAME = False
OLDNAME = ""
NEWNAME = ""

try:
    opts, args = getopt.getopt(sys.argv[1:],
                               "hrn:f:",
                               ["NEWNAME=",
                                "filename="])
except getopt.GetoptError:
    print('RENAME.py -f <FileName> -n <NewName> -r')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('RENAME.py -f <FileName> -n <NewName> -r')
        sys.exit()
    elif opt in ("-f", "--filename"):
        OLDNAME = arg
    elif opt in ("-n", "--NEWNAME"):
        NEWNAME = arg
    elif opt in ("-r", "--RENAME"):
        RENAME = True
    else:
        print('RENAME.py -f <FileName> -n <NewName> -r')
        sys.exit()


for dirName, subdirList, fileList in os.walk(ROOTDIR):
    for fname in fileList:
        if fname.find(OLDNAME) >= 0:
            name = fname[len(OLDNAME):]
            if RENAME:
                print(f"{NEWNAME} {name} RENAMEd")
                os.RENAME(fname, NEWNAME)
            else:
                print(f"{NEWNAME}  {name} Tested ")

STR1 = "please help me out so that I could solve this"
STR2 = "please help me out"

if STR1.find(STR2) >= 0:
    print("True")
else:
    print("False")
