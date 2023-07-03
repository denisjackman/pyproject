'''
    filer.py
'''
import os

PATH = '/Users/username/'
FILETYPE = '.ppt'
fileslist = []

for root, dirname, files in os.walk(PATH):
    for file in files:
        if FILETYPE in file:
            fileslist.append(os.path.join(root, file))

for fileitems in fileslist:
    print(fileitems)
