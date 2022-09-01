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
    It utilises check_file function to further check the file.
    """

    start_dir = wt_command_args["startdirectory"]
    verb = wt_command_args["verbosemode"]

    count = 0
    found = 0
    result = []
    for root, dirs, files in os.walk(start_dir, topdown=False):
        for name in files:
            if verb:
                print(f"file found {name}")
            if check_file_for_name(root, name, wt_command_args):
                result.append(os.path.join(root, name))
                found += 1
                if verb:
                    print(f"File found {count} {name}")

            count += 1
        for name in dirs:
            if verb:
                print(f"Directory found {count} {name}")
            if check_file_for_name(root, name, wt_command_args):
                result.append(os.path.join(root, name))
                found += 1
                if verb:
                    print(f"Directory found {count} {name}")
            count += 1
    return result


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
    if cff_command_args["verbosemode"]:
        print(f"Checking {cff_name} in {cff_root}")
    # check the name tio see if has "(1)" in it
    # if it does then record the size and delete the file
    # if not then do nothing
    # 
    #delete_list = [".DS_Store",
    #               ".AppleDouble",
    #               "Thumbs.db",
    #               ".pydevproject"]
    #startswith = ["."]
    #endswith = [".lnk"]
    #for name in delete_list:
    #    if cff_name == name:
    #        if cff_command_args["deletemode"]:
    #            if cff_command_args["verbosemode"]:
    #                print(f'[FOUND] {os.path.join(cff_root, cff_name)} is to be deleted')
    #            result = True


    return result


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    mainargs = getargs()
    print(mainargs)
    filelist = walk_through(mainargs)
    print(filelist)   
    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
