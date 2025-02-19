'''
a util to find files with a pattern in the name and delete them
'''
import os
import sys
import getopt

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 0.00 $"
__date__ = "$Date: 2022/09/02 15:50:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"


def getargs():
    '''
        get the argurments from the command line
    '''
    st_commands = 'scratch.py -v <True/False> -d <True/False> DIRECTORY "."'
    argv = sys.argv[1:]
    commands = "hvrs:"
    long_commands = ["verbose", "rename", "start=", "help"]
    verbosemode = False
    renamemode = False
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
        elif opt in ("-r", "--rename"):
            renamemode = True
        elif opt in ("-s", "--start"):
            startdirectory = arg
    return {"verbosemode": verbosemode,
            "renamemode": renamemode,
            "startdirectory": startdirectory}


def rename_run(wt_command_args):
    """
    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    """

    start_dir = wt_command_args["startdirectory"]
    verb = wt_command_args["verbosemode"]
    rename = wt_command_args["renamemode"]
    listoffiles = []
    try:
        listoffiles = os.listdir(start_dir)
    except OSError as err:
        if verb:
            print(f"OS error: {err} skipping {start_dir}")
    count = 0
    for entry in listoffiles:
        fullpath = os.path.join(start_dir, entry)
        if os.path.isdir(fullpath):
            rename_run({"verbosemode": verb,
                        "renamemode": rename,
                        "startdirectory": fullpath})
        else:
            name = start_dir.split("\\")
            nowname = "".join(name[-1].split(" "))
            nowname.replace(' ', '')
            ext = entry.split('.')
            count += 1
            newname = f"{nowname}_{count:05d}.{ext[-1]}"
            newpath = os.path.join(start_dir, newname)
            if verb:
                print(f"rename {entry} to {newname}")
            if rename:
                os.rename(fullpath, newpath)


def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    progargs = getargs()
    print(f"progargs: {progargs}")
    rename_run(progargs)

    print("finishing up and closing down:")


if __name__ == '__main__':
    main()
