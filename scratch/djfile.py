''' file utilities'''
import sys
import getopt

COMMANDS = "hvds:x:"
LONG_COMMANDS = ["verbose", "delete", "start=", "help", "xmode="]

def getargs():
    '''
        get the argurments from the command line
    '''
    standard_commands = 'djfile.py -v <True/False> -d <True/False> DIRECTORY "."'
    argv = sys.argv[1:]
    runname = sys.argv[0][2:].replace(".py", "")
    verbosemode = False
    deletemode = False
    startdirectory = "."
    xmode = ""
    print(f'runname is {runname}')
    try:
        command_line_optionss, args = getopt.getopt(argv, COMMANDS, LONG_COMMANDS)
    except getopt.GetoptError:
        print(f'The commands are : {standard_commands}')
        sys.exit(2)
    for command_line_options, arg in command_line_optionss:
        if command_line_options in ('-h', "--help"):
            print(f'The commands are : {standard_commands}')
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

def main():
    ''' main function'''
    mainargs = getargs()
    print(f'the list of args is {mainargs}')
    if mainargs["verbosemode"]:
        print("verbose mode is on")
    if mainargs["deletemode"]:
        print("delete mode is on")

if __name__ == '__main__':
    main()
