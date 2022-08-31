<<<<<<< Updated upstream
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

for dirName, subdirList, fileList in os.walk(ROOTDIR):
    for fname in fileList:
        newfile =  NEWNAME+str(NEWNUM).zfill(3)+os.path.splitext(fname)[1]
        os.rename(fname, newfile)
        NEWNUM += 1
=======
#!/usr/bin/env python
'''
    move
'''
# Import the os module, for the os.walk function
import os
import magic

# set the sprites you want to start from
rootDir = '.'
newname = "pic"
newnum = 1
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        newfile =  newname+str(newnum).zfill(3)+os.path.splitext(fname)[1]
        os.rename(fname, newfile)
        newnum += 1
>>>>>>> Stashed changes
