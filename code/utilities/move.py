#!/usr/bin/env python
'''
    move
'''
# Import the os module, for the os.walk function
import os
import magic

# Set the sprites you want to start from
rootDir = '.'
newname = "pic"
newnum = 1
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        newfile =  newname+str(newnum).zfill(3)+os.path.splitext(fname)[1]
        os.rename(fname, newfile)
        newnum += 1
