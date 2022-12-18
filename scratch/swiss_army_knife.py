''' file utilities'''
import os
import sys
import getopt
from pathlib import Path
import mimetypes
import json

COMMANDS = "hvds:x:"
LONG_COMMANDS = ["verbose", "debug", "start=", "help", "xmode="]
PROGRAM_NAME = sys.argv[0][2:].replace(".py", "")
STANDARD_COMMANDS = f'{PROGRAM_NAME} -v <True/False> -d <True/False> -s DIRECTORY -x XMODE "."'
FILEPATH = Path(__file__).parent

def loadjsonfile(jf_filename, jf_debug = False, jf_verbose = False):
    ''' load a json file '''
    result = None
    if jf_debug:
        print(f'DEBUG: loadjsonfile - {jf_filename}')
    if jf_verbose:
        print(f'Verbose: loadjsonfile - {jf_filename}')
    filename = f"{FILEPATH}/allMimeTypes.json"
    with open(filename, "r", encoding='utf8') as file:
        result = json.load(file)
    return result

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

def check_file_type(cf_filename, cf_debug = False, cf_verbose = False):
    ''' check the file type '''
    result = None
    if cf_debug:
        print(f'DEBUG: check_file_type - {cf_filename}')
    if cf_verbose:
        print(f'Verbose: check_file_type - {cf_filename}')
    result =  mimetypes.guess_type(cf_filename)
    return result

def check_file_extension(cfe_filename, cfe_debug = False, cfe_verbose = False):
    ''' check the file extension '''
    result = None
    if cfe_debug:
        print(f'DEBUG: check_file_extension - {cfe_filename}')
    if cfe_verbose:
        print(f'Verbose: check_file_extension - {cfe_filename}')
    result = Path(cfe_filename).suffix.replace(".", "")
    return result

def main():
    ''' main function'''
    mainargs = getargs()
    items  = dir_example(mainargs)
    mimetype_list = loadjsonfile('allMimeTypes.json', mainargs["debugmode"], mainargs["verbosemode"])

    print(f'List : {len(items)} items')
    print(f'MimeTypes : {len(mimetype_list)} mime types loaded')
    print(f'{type(mimetype_list)}')

    #for mime_item in mimetype_list:
    #    print(f'{mime_item}')
    #for item in items:
    #    itemtype = check_file_type(item, mainargs["debugmode"], mainargs["verbosemode"])
    #    exttype = check_file_extension(item, mainargs["debugmode"], mainargs["verbosemode"])
    #    answer = mimetype_list.get(itemtype[0])
    #    print(f'{item} - {itemtype} - {exttype} -{itemtype[0]} - {answer} ')
        #print(f'{mimetype_list.index(itemtype[0])}')
        #if exttype in mimetype_list[itemtype[0]]:
        #    print(f'{item} - {itemtype[0]} - {exttype} - {mimetype_list[exttype]} - checked  ')
        #else:
        #    print(f'{item} - {itemtype[0]} - {exttype} - {mimetype_list[exttype]} - not checked  ')


if __name__ == '__main__':
    main()
