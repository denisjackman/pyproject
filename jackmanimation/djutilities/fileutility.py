#!/usr/bin/python
# -*- coding: utf-8 -*-
''' utility to find zip files '''
import os
import sys
import getopt
import math
import csv

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2023/07/02 00:00:00 $"
__copyright__ = "Copyright (c) 2023 Denis J Jackman"
__license__ = "Python"

DIRECTORYLIST = ["C:\\","F:\\","G:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
DIRECTORYLISTFILE = "Y:/Resources/development/directorylist.txt"
DIRECTORYSUMMARY = "Y:/Resources/development/directorysummary.txt"

def check_file_for_name(cff_root, cff_name, cff_command_args):
    '''
    check_file_for_name

        :param : cff_root - the root directory for the file
                 cff_name - the name of the file in question
                 cff_command_args - a list of the command arguments

        :return: boolean - True if the file exists
                           False if it does not

        check for the existence of a file in a list.
        If it does return True.
        If not return False.

    '''
    result = False
    delete_list = [".DS_Store",
                   ".AppleDouble",
                   "Thumbs.db",
                   ".pydevproject"]

    for name in delete_list:
        if cff_name == name:
            if cff_command_args["deletemode"]:
                if cff_command_args["verbosemode"]:
                    print(f'[FOUND] {os.path.join(cff_root, cff_name)} is to be deleted')
                result = True
    return result


def getargs():
    '''
        get the argurments from the command line
    '''
    st_commands = f'{os.path.basename(__file__)} -v <True/False> -d <True/False> DIRECTORY "."'
    argv = sys.argv[1:]
    commands = "hvds:"
    long_commands = ["verbose", "delete", "start=", "help"]
    verbosemode = False
    deletemode = False
    startdirectory = "."
    try:
        clopts, args = getopt.getopt(argv, commands, long_commands)
    except getopt.GetoptError:
        print(st_commands)
        sys.exit(2)
    for clopt, arg in clopts:
        if clopt in ('-h', "--help"):
            print(st_commands)
            sys.exit()
        elif clopt in ("-v", "--verbose"):
            verbosemode = True
        elif clopt in ("-d", "--delete"):
            deletemode = True
        elif clopt in ("-s", "--start"):
            startdirectory = arg
    return {"verbosemode": verbosemode,
            "deletemode": deletemode,
            "startdirectory": startdirectory}


def extract_file_extension(filename):
    ''' This checks the file extension and returns true or false '''
    _, fileext = os.path.splitext(filename)
    result = fileext.lower()
    return result

def walk_through(wt_command_args):
    """
    walk_through function:

        :param : wt_command_args - a list of the command arguments

        :return: a list of files that have been found

    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    It utilises check_file function to further check the file.
    """
    start_dir = wt_command_args["startdirectory"]
    verbosemode = wt_command_args["verbosemode"]
    if verbosemode:
        print(f"[o] Starting walk through {start_dir}")
    result = []
    if verbosemode:
        print(f"[o] Searching for files in {start_dir}")
    for root, _, files in os.walk(start_dir, topdown=False):
        for name in files:
            result.append(os.path.join(root, name))
    if verbosemode:
        print(f"[o] Finished walk through {start_dir}")
    return result

def convert_size(size_bytes):
    '''
        size formating for bytes
    '''
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


def main():
    ''' main function '''
    print("[+] Starting")

    totallist = []
    for directory in DIRECTORYLIST:
        print(f"[-] Searching {directory}")
        commands = {"verbosemode":False, "deletemode":False, "startdirectory":directory}
        totallist.extend(walk_through(commands))
        print(f"[-] Records found {len(totallist):,}")

    extensiondict = {}

    for item in totallist:
        extension = extract_file_extension(item)
        if extension not in extensiondict:
            extensiondict[extension] = [item]
        else:
            extensiondict[extension].append(item)

    print("[-] File Inventory ")
    print("-------------------------------")
    for key, value in extensiondict.items():
        print(f"[*] {key:.<25} Found {len(value):.>10,} files")
    print(f"[*] Total Found {len(totallist):,} files")
    print("-------------------------------")

    with open(DIRECTORYSUMMARY, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for key, value in extensiondict.items():
            csvwriter.writerow([key, len(value)])

    with open(DIRECTORYLISTFILE, 'w', newline='', encoding='utf-8-sig') as filelistfile:
        for item in totallist:
            filelistfile.write(f"{item}\n")

if __name__ == '__main__':
    main()