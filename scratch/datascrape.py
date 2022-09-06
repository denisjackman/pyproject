#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
datascrape.py

This is a os utility tool

'''

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/05 09:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

import os
from urllib.request import urlopen
from bs4 import BeautifulSoup

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
    print("Starting a data scrape")

    # set up the variables
    listfiles = list()
    checkfilepath = "Y:/Data/comment_votes.csv"
    #checkfilepath = "/home/share/disk1/workspace/Data/comment_votes.csv"

    with open(checkfilepath, encoding="utf8") as input_file:
        for item in input_file.readlines():
            listitems = item.split(',')
            listfiles.append(listitems[1])

    # step through the list of files
    for item in listfiles:
        if item != 'permalink':
            #print(f"file: {item}")
            page = urlopen(item)
            soup = BeautifulSoup(page, features="lxml")
            stuff = soup.find("meta", property="og:title")
            if stuff is not None:
                print(f"file: {item} title: {stuff['content']}")
    print("Finished a data scrape")

if __name__ == '__main__':
    datascrapemain()
