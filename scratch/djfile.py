''' file utilities'''
import sys
import getopt

def getargs():
    '''
        get the argurments from the command line
    '''
    st_commands = 'djfile.py -v <True/False> -d <True/False> DIRECTORY "."'
    argv = sys.argv[1:]
    commands = "hvds:x:"
    long_commands = ["verbose", "delete", "start=", "help", "xmode="]
    verbosemode = False
    deletemode = False
    startdirectory = "."
    xmode = ""
    try:
        clopts, args = getopt.getopt(argv, commands, long_commands)
    except getopt.GetoptError:
        print(st_commands)
        sys.exit(2)
    print(f'clopts is {clopts}')
    print(f'args is {args}')
    for clopt, arg in clopts:
        if clopt in ('-h', "--help"):
            print(st_commands)
            sys.exit()
        elif clopt in ("-v", "--verbose"):
            verbosemode = True
        elif clopt in ("-d", "--delete"):
            deletemode = True
        elif clopt in ("-s", "--start"):
            startdirectory = arg
        elif clopt in ("-x", "--xmode"):
            xmode = arg
    print(f'xmode is {xmode}')
    return {"verbosemode": verbosemode,
            "deletemode": deletemode,
            "startdirectory": startdirectory}

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
