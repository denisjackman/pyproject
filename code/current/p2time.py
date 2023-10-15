'''new playtime file for p2'''
def compare_files(cf_file1_path, cf_file2_path):
    """Compares two files and checks if they are identical.

    Args:
        cf_file1_path (str): The path to the first file.
        cf_file2_path (str): The path to the second file.

    Returns:
        bool: True if the two files are identical, False otherwise.
    """

    # Open the two files in read mode.
    with open(cf_file1_path, "r", encoding='utf-8-sig') as file1, open(cf_file2_path, "r", encoding='utf-8-sig') as file2:

        # Read the contents of both files into lists.
        file1_contents = file1.readlines()
        file2_contents = file2.readlines()

    # Compare the two lists of file contents.
    if file1_contents != file2_contents:
        return False
    return True

def main():
    ''' main function'''
    # Example usage:

    file1_path = "playtime.py"
    file2_path = "movie.py"

    # Compare the two files and check if they are identical.
    are_files_identical = compare_files(file1_path, file2_path)

    # If the files are identical, print a message.
    if are_files_identical:
        print("[-] run 1 The two files are identical.")
    else:
        print("[-] run 1 The two files are different.")
    # Compare the two files and check if they are identical.
    are_files_identical = compare_files(file1_path, file1_path)

    # If the files are identical, print a message.
    if are_files_identical:
        print("[-] run 2 The two files are identical.")
    else:
        print("[-] run 2 The two files are different.")

if __name__ == '__main__':
    print('[=] playtime starting up')
    main()
    print('[=] playtime shutting down')
