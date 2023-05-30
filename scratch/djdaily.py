''' utility to find zip files '''
import os 

DIRECTORY = "Y:\\Resources"

def check_file_for_name(cff_root, cff_name, cff_command_args):
    '''
    check_file_for_name

        :param : cff_root - the root directory for the file
                 cff_name - the name of the file in question
                 cff_command_args - a list of the command arguments

        :return: boolean - True if the file exists
                           False if it does not

        check for the existence of a file in a list.
        If it does return True.
        If not return False.

    '''
    result = False
    delete_list = [".DS_Store",
                   ".AppleDouble",
                   "Thumbs.db",
                   ".pydevproject"]
    startswith = ["."]
    endswith = [".lnk"]
    for name in delete_list:
        if cff_name == name:
            if cff_command_args["deletemode"]:
                if cff_command_args["verbosemode"]:
                    print(f'[FOUND] {os.path.join(cff_root, cff_name)} is to be deleted')
                result = True


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
    verb = wt_command_args["verbosemode"]
    delete_mode = wt_command_args["deletemode"]
    count = 0
    found = 0
    result = []
    for root, dirs, files in os.walk(start_dir, topdown=False):
        for name in files:
            if check_file_for_name(root, name, wt_command_args):
                result.append(os.path.join(root, name))
                found += 1
            else:
                result.append(os.path.join(root, name))               
            count += 1
        for name in dirs:
            if check_file_for_name(root, name, wt_command_args):
                result.append(os.path.join(root, name))
                found += 1
            count += 1
    return result

def main():
    ''' main function '''
    print("[+] Starting")
    commands = {"verbosemode":False, "deletemode":False, "startdirectory":DIRECTORY}
    result = walk_through(commands)
    for item in result:
        if item.endswith(".txt"):
            print(f"[+] {item}")
    print("[+] Finished")

if __name__ == '__main__':
    main()
