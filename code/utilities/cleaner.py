#!/usr/bin/python

"""
cleaner.py clean up script

Walk through a chosen directory. from the designated top to the bottom
looking for files to clean up.
The list of files to be removed is listed at the top.
There will be a read mode and a delete mode.

Read mode will read through and inform which files will be deleted.
Delete mode will delete all the offending files.
"""
import os
import sys
import getopt
import shutil

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/04/23 00:00:00 $"
__copyright__ = "Copyright (c) 2019 Denis J Jackman"
__license__ = "Python"

delete_list = [".DS_Store", ".AppleDouble", "Thumbs.db", ".pydevproject"]
DELETE_MODE = True
VERBOSE_MODE = False
start_directory = "y:/"


def walk_through(params):
    """
        :param params:
        :return:

    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    It utilises check_file function to further check the file.
    """
    print(f"Starting with [{params}]")
    count = 0
    found = 0
    for root, dirs, files in os.walk(params, topdown=False):
        for name in files:
            if check_file_for_name(root, name):
                found += 1
            count += 1
        for name in dirs:
            if check_file_for_name(root, name):
                found += 1
            count += 1
    print(f"Count : {count}")
    print(f"Found : {found}")
    return "Done!"


def check_file_for_name(file_path, file_name):
    """

    :param file_path:
    :param file_name:
    :return:

    This looks at each file and will decide what to do based in the modes.
    if DELETE_MODE is set to TRUE then it will delete [DELETE] the file.
    Otherwise it will report the file as [FOUND]
    if VERBOSE_MODE is set to TRUE the it will only report files of interest.
    Otherwise it will report the file as [IGNORED]
    """
    result = False
    for name in delete_list:
        if file_name == name:
            if DELETE_MODE:
                if os.path.exists(os.path.join(file_path, file_name)):
                    if os.path.isfile(os.path.join(file_path, file_name)):
                        os.remove(os.path.join(file_path, file_name))
                    if os.path.isdir(os.path.join(file_path, file_name)):
                        shutil.rmtree(os.path.join(file_path, file_name))
                else:
                    print('[File does not exists]' + os.path.join(file_path, file_name))
                print("[DELETED] : " + os.path.join(file_path, file_name))
            else:
                print("[FOUND] : " + os.path.join(file_path, file_name))
                result = True
        else:
            if VERBOSE_MODE:
                print("[IGNORED] : " + os.path.join(file_path, file_name))
    return result


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv:d:s", ["verbose=", "delete=", "start=", "help"])
    except getopt.GetoptError:
        print('cleaner.py -v <True/False> -d <True/False> DIRECTORY ')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print('cleaner.py -v <True/>False -d <True/>False -s <DIRECTORY/>"." ')
            sys.exit()
        elif opt in ("-v", "--verbose"):
            VERBOSE_MODE = arg
        elif opt in ("-d", "--delete"):
            DELETE_MODE = arg
        elif opt in ("-s", "--start"):
            start_directory = arg

    print(walk_through(start_directory))
