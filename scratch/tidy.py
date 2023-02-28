''' This is a folder tidy up script that will rename files. '''
import os

def walk_through(start_dir):
    """
    walk_through function:

        :param : wt_command_args - a list of the command arguments

        :return: a list of files that have been found

    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    """


    listfiles = []

    try:
        listfiles = os.listdir(start_dir)
    except OSError as err:
        print(f"OS error: {err} skipping {start_dir}")
    result = []
    for entry in listfiles:
        fullpath = os.path.join(start_dir, entry)
        if os.path.isdir(fullpath):
            result = result + walk_through(fullpath)
        else:
            result.append(fullpath)
    return result

def main():
    ''' This is the main function. '''
    print("Start")
    allfiles = walk_through("Y:\\Resources\\denis")
    for item in allfiles:
        print(item)
    print(f"Total files: {len(allfiles)}")
    print("Done")

if __name__ == "__main__":
    main()