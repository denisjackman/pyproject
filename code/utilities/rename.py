#!/usr/bin/env python
# Import the os module, for the os.walk function
import os
import sys
import getopt

# Set the directory you want to start from
# DrWho.S0
# Doctor.Who.2005.S0
rootDir = '.'
rename = False

try:
    opts, args = getopt.getopt(sys.argv[1:], "hrn:f:", ["newname=", "filename="])
except getopt.GetoptError:
    print 'rename.py -f <FileName> -n <NewName> -r'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'rename.py -f <FileName> -n <NewName> -r'
        sys.exit()
    elif opt in ("-f", "--filename"):
        oldname = arg
    elif opt in ("-n", "--newname"):
        newname = arg
    elif opt in ("-r", "--rename"):
        rename = True
    else:
        print 'rename.py -f <FileName> -n <NewName> -r'
        sys.exit()


for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if (fname.find(oldname) >=0):
            name = fname[len(oldname):]
            if rename:
                print newname + name + " Renamed"
                os.rename(fname, newfile)
            else:
                print newname + name + " Tested "

str1 = "please help me out so that I could solve this"
str2 = "please help me out"

if (str1.find(str2)>=0):
  print("True")
else:
  print ("False")