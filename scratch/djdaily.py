''' utility to find zip files '''
import os

DIRECTORY = "Y:\\Resources"

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
        print(f"[+] Starting walk through {start_dir}")
    count = 0
    result = []
    if verbosemode:
        print(f"[+] Searching for files in {start_dir}")
    for root, _, files in os.walk(start_dir, topdown=False):
        for name in files:
            result.append(os.path.join(root, name))
            count += 1
    if verbosemode:
        print(f"[+] Finished walk through {start_dir}")
        print(f"[+] Found {count} files")
    return result

def main():
    ''' main function '''
    print("[+] Starting")
    commands = {"verbosemode":True, "deletemode":False, "startdirectory":DIRECTORY}
    result = walk_through(commands)
    pdffound = 0
    txtfound = 0
    pdflist = []
    txtlist = []

    for item in result:
        if item.endswith(".txt"):
            txtlist.append(item)
            txtfound += 1

        if item.endswith(".pdf"):
            pdflist.append(item)
            pdffound += 1

    print(f"[+] PDF Found {pdffound} files")
    print(f"[+] TXT Found {txtfound} files")
    print("[+] Finished")

if __name__ == '__main__':
    main()
