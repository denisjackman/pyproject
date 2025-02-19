'''
a util to find files with a pattern in the name and delete them
'''
import os
import sys
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.utilities.fileutility import walk_through
from jackmanimation.utilities.fileutility import getargs
from jackmanimation.utilities.fileutility import convert_size

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/01 12:50:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    search_list = [".DS_Store",
                   ".AppleDouble",
                   "Thumbs.db",
                   ".pydevproject"]

    mainargs = getargs()
    filelist = walk_through(mainargs)
    delete_list = []
    totalsize = 0
    for item in filelist:
        if item in search_list:
            totalsize += os.path.getsize(item)
            delete_list.append(item)
        if item.find("(1)") != -1:
            totalsize += os.path.getsize(item)
            delete_list.append(item)
        if item.endswith(".lnk"):
            totalsize += os.path.getsize(item)
            delete_list.append(item)

    print(mainargs)
    print(f"total count is {len(filelist)} - with {len(delete_list)} to be deleted")
    print(f"total size is {convert_size(totalsize)}")
    if mainargs["deletemode"]:
        for item in delete_list:
            try:
                os.remove(item)
                print(f"deleted {item}")
            except OSError as err:
                print(f"OS error: {err}")
                print(f"failed to delete {item}")

    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
