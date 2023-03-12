''' This is a folder tidy up script that will rename files. '''
import os
from PyPDF2 import PdfReader
import zipfile

TARGET_DIRECTORY = "Y:\\Store\\Zips"
NEW_DIRECTORY = "Y:\\Store\\Zip"
TARGET_CHECK = '.zip'

def extract_pdf_information(pdf_path):
    ''' This extracts the information from a pdf file. '''
    pdf = PdfReader(pdf_path)
    information = pdf.metadata
    result = None
    if information.title is None:
        result = None
    else:
        result = f"{information.title}"
    return result

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
    if count == 0:
        newfilename = os.path.join(head, f"{newname}{ext}")
    else:
        newfilename = os.path.join(head, f"{newname}-{count:04}{ext}")
    os.rename(filename, newfilename)

def check_file_extension(filename, ext):
    ''' This checks the file extension and returns true or false '''
    result = False
    _, fileext = os.path.splitext(filename)
    if fileext.lower() == ext.lower():
        result = True
    return result

def move_file(filename, newdir):
    ''' This moves the file '''
    head,tail = os.path.split(filename)
    newfilename = os.path.join(newdir, tail)
    os.rename(filename, newfilename)

def main():
    ''' This is the main function. '''
    print("Start")
    allfiles = walk_through(TARGET_DIRECTORY)
    check = TARGET_CHECK
    count = 1
    for item in allfiles:
        if check_file(item, check):
            try:
                with zipfile.ZipFile(item, 'r') as archive:
                    print(f"Processing {item} - {len(archive.namelist())}")
            except zipfile.BadZipFile as error:
                print(f"Bad zip file {item} - {error}")

    print(f"Total files: {len(allfiles)}")
    print("Done")

if __name__ == "__main__":
    main()
