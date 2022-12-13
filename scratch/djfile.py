''' file utilities'''
import os
import sys
import getopt

COMMANDS = "hvds:x:"
LONG_COMMANDS = ["verbose", "delete", "start=", "help", "xmode="]
STANDARD_COMMANDS = 'djfile.py -v <True/False> -d <True/False> -s DIRECTORY -x XMODE "."'

def getargs():
    '''
        get the argurments from the command line
    '''
    argv = sys.argv[1:]
    #runname = sys.argv[0][2:].replace(".py", "")
    verbosemode = False
    deletemode = False
    startdirectory = "."
    xmode = ""
    try:
        command_line_optionss, args = getopt.getopt(argv, COMMANDS, LONG_COMMANDS)
    except getopt.GetoptError:
        print(f'The commands are : {STANDARD_COMMANDS}')
        sys.exit(2)
    for command_line_options, arg in command_line_optionss:
        if command_line_options in ('-h', "--help"):
            print(f'The commands are : {STANDARD_COMMANDS}')
            sys.exit()
        elif command_line_options in ("-v", "--verbose"):
            verbosemode = True
        elif command_line_options in ("-d", "--delete"):
            deletemode = True
        elif command_line_options in ("-s", "--start"):
            startdirectory = arg
        elif command_line_options in ("-x", "--xmode"):
            xmode = arg
    return {"verbosemode": verbosemode,
            "deletemode": deletemode,
            "startdirectory": startdirectory,
            "xmode": xmode}

def walk_through(wt_command_args):
    """
    walk_through function:
    """

    start_dir = wt_command_args["startdirectory"]
    verb = wt_command_args["verbosemode"]
    delete = wt_command_args["deletemode"]
    listoffiles = []
    try:
        listoffiles = os.listdir(start_dir)
    except OSError as err:
        print(f"OS error: {err} skipping {start_dir}")
    result = []
    for entry in listoffiles:
        fullpath = os.path.join(start_dir, entry)

def main():
    ''' main function'''
    mainargs = getargs()


if __name__ == '__main__':
    main()
