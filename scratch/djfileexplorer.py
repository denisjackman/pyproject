'''
 file explorer
'''
import os
import sys

def main():
    '''
        main routine
    '''
    filelist = []
    if len(sys.argv) == 2:
        rootdir = sys.argv[1]
        if not os.path.isdir(rootdir):
            print(f"Directory path {rootdir} does not exist. Exiting...")
            sys.exit()
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filelist.append(os.path.join(subdir, file))
        for file in filelist:
            name = os.path.basename(file)
            details = name.split('.')
            extension = details[-1]
            print(f" name: {name} extension: {extension} file: {file}")
    else:
        print("Usage: python3 djfileexplorer.py <directory path>")
if __name__ == '__main__':
    main()
