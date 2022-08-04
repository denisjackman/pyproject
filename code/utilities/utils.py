#!/usr/bin/python
'''
    utils
'''
__author__ = 'Denis Jackman'

import sys
import os

DebugMode = False
StartDir ="/Users/username/Documents/workspace/tools/"

dryRun = True
fileExt = False
zeroFile = False
removeFile = False
findDup = False

total = len(sys.argv)
cmdargs = str(sys.argv)

def is_file(fpath):
    return True if os.path.isfile(fpath)  else False

def is_non_zero_file(fpath):
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False

def is_zero_file(fpath):
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) == 0 else False

def zeroFilecheck(fpath):
	if is_file(fpath) :
		if is_zero_file(fpath) :
				return True
	return False

def remove_File(fpath):
	if dryRun :
		print(f"I would have removed {fpath}")
	else :
		os.remove(fpath)

def zero_file():
	fileList=os.listdir(StartDir)
	for file in fileList :
		fileName = StartDir+"/"+file
		if zeroFilecheck(fileName):
            if removeFile:
                remove_File(fileName)
            else:
                print(file)

def find_dup():
	fileList=os.listdir(StartDir)
	for file in fileList :
		fileName = StartDir+"/"+file
		if file.find("(") != -1 :
			if removeFile :
				remove_File(fileName)
 			else :
 				print file

def file_ext():
	extList=[]
	fileListExt=os.listdir(StartDir)
	for file in fileListExt :
		fileName = StartDir+"/"+file
		if is_file(fileName) :
			extName = os.path.splitext(fileName)[-1].lower()
			extList.append(extName)
	extset = set(extList)
	NewExtList = list(extset)
	print NewExtList

if DebugMode :
	print ("The total numbers of args passed to the script: %d " % total)
	print ("Args list: %s " % cmdargs)
	print ("Script name: %s" % str(sys.argv[0]))

for i in range(total):
	if DebugMode :
		print ("Argument # %d : %s" % (i, str(sys.argv[i])))
	if str(sys.argv[i]) == "--dryrun" :
		dryRun = True
	if str(sys.argv[i]) == "--fileext" :
		fileExt = True
	if str(sys.argv[i]) == "--zerofile" :
		zeroFile = True
	if str(sys.argv[i]) == "--removefile" :
		removeFile = True
	if str(sys.argv[i]) == "--finddup" :
		findDup = True

if zeroFile :
	zero_file()

if findDup :
	find_dup()

if fileExt :
	file_ext()
