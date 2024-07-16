'''
    utils
'''
__author__ = 'Denis Jackman'

import sys
import os

DEBUGMODE = False
STARTDIR = "/Users/username/Documents/workspace/tools/"

DRYRUN = True
FILEEXT = False
ZEROFILE = False
REMOVEFILE = False
FINDDUP = False

TOTAL = len(sys.argv)
CMDARGS = str(sys.argv)


def is_file(fpath):
    '''	is file '''
    return bool(os.path.isfile(fpath))


def is_non_zero_file(fpath):
    '''	is non zero file '''
    return bool(os.path.isfile(fpath) and os.path.getsize(fpath) > 0)


def is_zero_file(fpath):
    '''	is zero file '''
    return bool(os.path.isfile(fpath) and os.path.getsize(fpath) == 0)


def zerofilecheck(fpath):
    ''' zero file check '''
    if is_file(fpath):
        if is_zero_file(fpath):
            return True
        return False
    return None


def remove_File(fpath, dryrun=DRYRUN):
    ''' remove file '''
    if dryrun:
        print(f"[-] I would have removed {fpath}")
        return
    os.remove(fpath)


def zero_file():
    ''' zero file '''
    fileList = os.listdir(STARTDIR)
    for file in fileList:
        fileName = STARTDIR+"/"+file
        if zerofilecheck(fileName):
            if REMOVEFILE:
                remove_File(fileName)
            else:
                print(file)


def find_dup():
    ''' find duplicate files '''
    fileList = os.listdir(STARTDIR)
    for file in fileList:
        fileName = STARTDIR+"/"+file
        if file.find("(") != -1:
            if REMOVEFILE:
                remove_File(fileName)
            else:
                print(file)


def file_ext():
    ''' file extension '''
    extList = []
    fileListExt = os.listdir(STARTDIR)
    for file in fileListExt:
        fileName = STARTDIR+"/"+file
        if is_file(fileName):
            extName = os.path.splitext(fileName)[-1].lower()
            extList.append(extName)
    extset = set(extList)
    NewExtList = list(extset)
    print(NewExtList)


def main():
    ''' main '''
    print("main")
    if DEBUGMODE:
        print(f"The TOTAL numbers of args passed to the script: {TOTAL}")
        print(f"Args list: {CMDARGS}")
        print(f"Script name: {str(sys.argv[0])}")


if __name__ == '__main__':
    main()
