#!/usr/bin/env python
# Import the os module, for the os.walk function
import os
import magic


rootDir = '.'
# Set the sprites you want to start from

extTypes = {
    "RIFF (little-":"avi",
    "ISO Media, MP":"mp4",
    "Ogg data, OGM":"ogg",
    "Matroska data":"mkv:",
    "Apple QuickTi":"mov",
    "MPEG sequence":"mpg",
    "Microsoft ASF":"asf"}

14

for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.find('.') == -1:
            print(dirName+"/"+fname+extTypes[fname,magic.from_file(dirName+"/"+fname)[:14]])

