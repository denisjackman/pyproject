''' file utilities'''
import os
import sys
import getopt
from pathlib import Path
#import json

COMMANDS = "hvds:x:"
LONG_COMMANDS = ["verbose", "debug", "start=", "help", "xmode="]
PROGRAM_NAME = sys.argv[0][2:].replace(".py", "")
STANDARD_COMMANDS = f'{PROGRAM_NAME} -v <True/False> -d <True/False> -s DIRECTORY -x XMODE "."'
FILEPATH = Path(__file__).parent

def getargs():
    '''
        get the argurments from the command line
    '''
    argv = sys.argv[1:]
    #runname = sys.argv[0][2:].replace(".py", "")
    verbosemode = False
    debugmode = False
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
        elif command_line_options in ("-d", "--debug"):
            debugmode = True
        elif command_line_options in ("-s", "--start"):
            startdirectory = arg
        elif command_line_options in ("-x", "--xmode"):
            xmode = arg
    return {"verbosemode": verbosemode,
            "debugmode": debugmode,
            "startdirectory": startdirectory,
            "xmode": xmode}

def dir_example(ex_command_args):
    ''' example function '''
    verb = ex_command_args["verbosemode"]
    debug = ex_command_args["debugmode"]
    result = []
    rootdir = ex_command_args["startdirectory"]
    if debug:
        print(f'DEBUG: rootdir - {rootdir}')
    for dirName, subdirList, fileList in os.walk(rootdir):
        if debug:
            print(f'DEBUG: Found directory: {dirName} - {subdirList} - {fileList} - {len(fileList)}')
        for fname in fileList:
            temp = f'{FILEPATH}\\{fname}'
            if debug:
                print(f'DEBUG: {temp}')
            if verb:
                print(temp)
            result.append(temp)
    return result

def main():
    ''' main function'''
    mainargs = getargs()
    items  = dir_example(mainargs)
    print(f'List : {len(items)} items')


if __name__ == '__main__':
    main()
