#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
datascrape.py

This is a os utility tool

'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/04 22:43:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from asyncio import format_helpers
import os

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
    listoffiles = list()
    try:
        listoffiles = os.listdir(start_dir)
    except OSError as err:
        print(f"OS error: {err} skipping {start_dir}")
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

def datascrapemain():
    '''
        this is the main function
    '''
    listfiles = list()
    checkfilepath = "Y:/Data"
    print("Starting a data scrape")
    listfiles = walk_through({"verbosemode": True,
                              "deletemode": False,
                              "startdirectory": checkfilepath})
    # open the file
    for item in listfiles:
        print(f"file: {item}")    
    print("Finished a data scrape")

if __name__ == '__main__':
    datascrapemain()