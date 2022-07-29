#!/usr/bin/env python
'''
 Import the os module, for the os.walk function
'''
import os

# Set the sprites you want to start from
DELETELIST = [".DS_Store",
              ".AppleDouble",
              "Thumbs.db",
              ".pydevproject"]

ROOTDIR = '/home/share/disk1/family'
SEARCHTERM = '.lnk'
OTHERSEARCHTERM ='.'
for dirName, subdirList, fileList in os.walk(ROOTDIR):
    for fname in fileList:
        if fname.startswith(OTHERSEARCHTERM) is True:
            print(os.path.join(dirName, fname))
        if fname.endswith(SEARCHTERM) is True:
            print(os.path.join(dirName, fname))
        if fname in DELETELIST:
            print(os.path.join(dirName, fname))
