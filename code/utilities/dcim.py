#!/usr/bin/env python
'''
    find files
'''
import os
rootDir = '.'

for dirName, subdirList, fileList in os.walk(rootDir):
    for filename in fileList:
        if filename.find('.') == -1:
            # os.rename(filename, filename+".dcim")
            print(filename)
