#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
a util lto find files with a pattern in the name and delete them
'''
import os
import sys
import getopt

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/01 12:50:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def getargs():
    '''
        get the argurments from the command line
    '''
    st_commands = 'scratch.py -v <True/False> -d <True/False> DIRECTORY "."'
    argv = sys.argv[1:]
    commands = "hvds:"
    long_commands = ["verbose", "delete", "start=", "help"]
    verbosemode = False
    deletemode = False
    startdirectory = "."
    try:
        opts, args = getopt.getopt(argv, commands, long_commands)
    except getopt.GetoptError:
        print(st_commands)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print(st_commands)
            sys.exit()
        elif opt in ("-v", "--verbose"):
            verbosemode = True
        elif opt in ("-d", "--delete"):
            deletemode = True
        elif opt in ("-s", "--start"):
            startdirectory = arg
    return {"verbosemode": verbosemode,
            "deletemode": deletemode,
            "startdirectory": startdirectory}


def walk_through(wt_command_args):
    """
    walk_through function:

        :param : wt_command_args - a list of the command arguments

        :return: a list of files that have been found

    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    """

    start_dir = wt_command_args["startdirectory"]
    verb = wt_command_args["verbosemode"]
    delete = wt_command_args["deletemode"]
    listoffiles = os.listdir(start_dir)
    result = list()
    for entry in listoffiles:
        fullpath = os.path.join(start_dir, entry)
        if os.path.isdir(fullpath):
            result = result + walk_through({"verbosemode": verb,
            "deletemode": delete,
            "startdirectory": fullpath})
        else:
            result.append(fullpath)
    return result





def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    search_list = [".DS_Store",
                   ".AppleDouble",
                   "Thumbs.db",
                   ".pydevproject"]

    mainargs = getargs()
    filelist = walk_through(mainargs)
    delete_list = list()

    for item in filelist:
        if item in search_list:
            delete_list.append(item)
        if item.find("(1)") != -1:
            delete_list.append(item)
        if item.endswith(".lnk"):
            delete_list.append(item)

    print(mainargs)
    print(f"total count is {len(filelist)} - with {len(delete_list)} to be deleted")

    if mainargs["deletemode"]:
        for item in delete_list:
            os.remove(item)
            print(f"deleted {item}")

    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
