''' zip file cracker '''
import zipfile
from threading import Thread

import os
import sys
import getopt


def get_args():
    '''
        get the argurments from the command line
    '''
    st_commands = f'{os.path.basename(__file__)} -v <True/False> -f <Zipfile> -d <Dictionary> -h <help>'
    argv = sys.argv[1:]
    commands = "hvf:d:"
    long_commands = ["help", "verbose", "file=", "dictionary="]
    verbosemode = False
    dictionary = ''
    zipfilename = ''
    try:
        clopts, args = getopt.getopt(argv, commands, long_commands)
    except getopt.GetoptError:
        print(st_commands)
        sys.exit(2)
    for clopt, arg in clopts:
        if clopt in ('-h', "--help"):
            print(st_commands)
            sys.exit()
        elif clopt in ("-v", "--verbose"):
            verbosemode = True
        elif clopt in ("-d", "--dictionary"):
            dictionary = arg
        elif clopt in ("-f", "--file"):
            zipfilename = arg
    return {"verbosemode": verbosemode,
            "dictionary": dictionary,
            "zipfile": zipfilename}


def extract_file(zFile, password):
    ''' extract file from zip file '''''
    result = False
    try:
        zFile.extractall(pwd=password.encode())
    except Exception as err:
        result = False
    else:
        result = True
    return result


def main():
    ''' main function '''
    main_args = get_args()
    do_threading = False
    with zipfile.ZipFile(main_args["zipfile"]) as zFile:
        with open(main_args["dictionary"],
                  'r',
                  encoding='utf-8-sig') as passFile:
            for line in passFile.readlines():
                password = line.strip('\n')
                if do_threading:
                    t = Thread(target=extract_file, args=(zFile, password))
                    t.start()
                else:
                    answer = extract_file(zFile, password)
                    if answer:
                        print(f'[+] Password = {password}')
                        break


if __name__ == '__main__':
    main()
