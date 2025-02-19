#!/usr/bin/env python
'''
    move
'''
# Import the os module, for the os.walk function
import os

# set the sprites you want to start from
ROOTDIR = '.'
NEWNAME = "pic"
NEWNUM = 1
if ROOTDIR == '.':
    print("You are in the wrong directory")
else:
    for dirName, subdirList, fileList in os.walk(ROOTDIR):
        for fname in fileList:
            newfile = NEWNAME+str(NEWNUM).zfill(3)+os.path.splitext(fname)[1]
            os.rename(fname, newfile)
            NEWNUM += 1
