'''
 file explorer
'''
import os
import sys

def main():
    '''
        main routine
    '''
    rootdir = sys.argv[1]
    if not os.path.isdir(rootdir):
        print("Directory path {} does not exist. Exiting...".format(rootdir))
        sys.exit()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            print(os.path.join(subdir, file))

if __name__ == '__main__':
    main()
