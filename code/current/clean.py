#!/usr/bin/env python
'''
 Import the os module, for the os.walk function
'''
import os

# set the sprites you want to start from
DELETELIST = [".DS_Store",
              ".AppleDouble",
              "Thumbs.db",
              ".pydevproject"]

ROOTDIR = '/home/share/disk1'
SEARCHTERM = '.lnk'
OTHERSEARCHTERM = '.'
LOGFILE = '/home/share/disk2/logs/findlogs.txt'
COUNT = 0
TOTAL = 0
SIZEFILES = 0

with open(LOGFILE, "w", encoding='utf-8-sig') as logreport:
    for dirName, subdirList, fileList in os.walk(ROOTDIR):
        TOTAL += 1
        for fname in fileList:
            if fname.startswith(OTHERSEARCHTERM) is True:
                logreport.write(f"{os.path.join(dirName, fname)} \n")
                COUNT += 1
                SIZEFILES += os.path.getsize(os.path.join(dirName, fname))
            elif fname.endswith(SEARCHTERM) is True:
                logreport.write(f"{os.path.join(dirName, fname)} \n")
                COUNT += 1
                SIZEFILES += os.path.getsize(os.path.join(dirName, fname))
            elif fname in DELETELIST:
                logreport.write(f"{os.path.join(dirName, fname)} \n")
                COUNT += 1
                SIZEFILES += os.path.getsize(os.path.join(dirName, fname))
print(f" Total files read ({TOTAL}) - Total files to be deleted {COUNT}")
OUTPUTSIZE = SIZEFILES
print(f" Total size to be reclaimed = {OUTPUTSIZE:,.2f} bytes")
OUTPUTSIZE = SIZEFILES/1024
print(f" Total size to be reclaimed = {OUTPUTSIZE:,.2f} KB")
OUTPUTSIZE = (SIZEFILES/1024)/1024
print(f" Total size to be reclaimed = {OUTPUTSIZE:,.2f} MB")
OUTPUTSIZE = ((SIZEFILES/1024)/1024)/1024
print(f" Total size to be reclaimed = {OUTPUTSIZE:,.2f} GB")
