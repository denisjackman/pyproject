#!/usr/bin/env python
'''
    find files
'''
import os
ROOTDIR = '.'

for dirName, subdirList, fileList in os.walk(ROOTDIR):
    for filename in fileList:
        if filename.find('.') == -1:
            # os.rename(filename, filename+".dcim")
            print(filename)
