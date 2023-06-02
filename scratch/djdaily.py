''' utility to find zip files '''
import os

#DIRECTORYLIST = ["C:\\","F:\\","G:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
DIRECTORYLIST = ["V:\\","W:\\","X:\\","Y:\\","Z:\\"]

def extract_file_extension(filename):
    ''' This checks the file extension and returns true or false '''
    _, fileext = os.path.splitext(filename)
    result = fileext.lower()
    return result

def walk_through(wt_command_args):
    """
    walk_through function:

        :param : wt_command_args - a list of the command arguments

        :return: a list of files that have been found

    This walks through a directory and returns the name and path of each file.
    It takes one param which is the starting point directory for the search.
    It returns nothing.
    It utilises check_file function to further check the file.
    """
    start_dir = wt_command_args["startdirectory"]
    verbosemode = wt_command_args["verbosemode"]
    if verbosemode:
        print(f"[o] Starting walk through {start_dir}")
    count = 0
    result = []
    if verbosemode:
        print(f"[o] Searching for files in {start_dir}")
    for root, _, files in os.walk(start_dir, topdown=False):
        for name in files:
            result.append(os.path.join(root, name))
            count += 1
    if verbosemode:
        print(f"[o] Finished walk through {start_dir}")
        print(f"[o] Found {count} files")
    return result

def main():
    ''' main function '''
    print("[+] Starting")

    totallist = []
    for directory in DIRECTORYLIST:
        print (f"[-] Searching {directory}")
        commands = {"verbosemode":False, "deletemode":False, "startdirectory":directory}
        totallist.extend(walk_through(commands))
        print (f"[-] Searching {directory} - records found {len(totallist)}:,")

    extensiondict = {}

    for item in totallist:
        extension = extract_file_extension(item)
        if extension not in extensiondict:
            extensiondict[extension] = [item]
        else:
            extensiondict[extension].append(item)

    print("[-] File Inventory ")
    print("-------------------------------")
    for key, value in extensiondict.items():
        print(f"[*] {key} Found {len(value):,} files")
    print(f"[*] Total Found {len(totallist):,} files")
    print("-------------------------------")

if __name__ == '__main__':
    main()
