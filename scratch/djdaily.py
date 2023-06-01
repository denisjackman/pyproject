''' utility to find zip files '''
import os

DIRECTORY = "X:\\Pictures"

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
    commands = {"verbosemode":False, "deletemode":False, "startdirectory":DIRECTORY}
    result = walk_through(commands)
    pdffound = 0
    txtfound = 0
    jpgfound = 0
    pngfound = 0
    movfound = 0
    aaefound = 0

    pdflist = []
    txtlist = []
    jpglist = []
    pnglist = []
    movlist = []
    aaelist = [] 

    for item in result:
        if item.endswith(".txt"):
            txtlist.append(item)
            txtfound += 1

        if item.endswith(".pdf"):
            pdflist.append(item)
            pdffound += 1

        if item.endswith(".jpg"):
            jpglist.append(item)
            jpgfound += 1

        if item.endswith(".png"):
            pnglist.append(item)
            pngfound += 1

        if item.endswith(".jpeg"):
            jpglist.append(item)
            jpgfound += 1

        if item.endswith(".mov"):
            movlist.append(item)
            movfound += 1

        if item.endswith(".aae"):
            aaelist.append(item)
            aaefound += 1

    print("[-] File Inventory ")
    print("-------------------------------")
    print(f"[*] JPG Found {jpgfound} files")
    print(f"[*] PDF Found {pdffound} files")
    print(f"[*] TXT Found {txtfound} files")
    print(f"[*] PNG Found {pngfound} files")
    print(f"[*] MOV Found {movfound} files")
    print(f"[*] AAE Found {aaefound} files")
    print("-------------------------------")
    print("[+] Finished")

if __name__ == '__main__':
    main()
