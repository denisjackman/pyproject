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

def check_file(filename, checkitem):
    ''' This checks the file name and returns true or false '''
    result = False
    lowerfilename = filename.lower()
    lowercheckitem = checkitem.lower()
    if lowercheckitem in lowerfilename:
        result = True
    return result

def rename_file(filename, newname, count):
    ''' This renames the file '''
    head,tail = os.path.split(filename)
    _, ext = os.path.splitext(tail)
    newfilename = os.path.join(head, f"{newname}-{count:03}{ext}")
    print (f"Renaming {filename} to {newfilename}")
    os.rename(filename, newfilename)

def main():
    ''' This is the main function. '''
    print("Start")
    allfiles = walk_through("Y:\\Resources\\denis")
    check = "Sucess"
    count = 1
    for item in allfiles:
        if check_file(item, check):
            rename_file(item, check, count)
            count += 1
    print(f"Total files: {len(allfiles)}")
    print(f"Total files renamed: {count-1}")
    print("Done")

if __name__ == "__main__":
    main()
