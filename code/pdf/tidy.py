''' This is a folder tidy up script that will rename files. '''
import os
import zipfile
from openpyxl import Workbook
from pypdf import PdfReader
from colorama import Fore

TARGET_DIRECTORY = r"Z:/Store/Zips"
NEW_DIRECTORY = r"Z:/Store/Zip"
TARGET_CHECK = '.zip'
PDF_FILENAME = r"Z:/pyproject/code/viscous/chapter3/data/ANONOPS_The_Press_Release.pdf"
WORKBOOK_FILE = r'Z:/Resources/zip.xlsx'


def pdf_reader(pdffile_path):
    ''' This is the PDF reader function'''
    reader = PdfReader(pdffile_path)
    for page in reader.pages:
        print("-------------------------------")
        print(page.extract_text())
        print("-------------------------------")
    print(f"Number of pages: {len(reader.pages)}")


def excel_store(data_list):
    ''' This is the main function '''
    title = TARGET_CHECK.upper().replace('.', '')
    current_workbook = Workbook()
    current_worksheet = current_workbook.create_sheet(title)
    for item in data_list:  # pylint: disable=not-an-iterable
        current_worksheet.append([item])
    current_workbook.save(WORKBOOK_FILE)


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
    head, tail = os.path.split(filename)
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
    head, tail = os.path.split(filename)
    newfilename = os.path.join(newdir, tail)
    os.rename(filename, newfilename)


def main():
    ''' This is the main function. '''
    print("Start")
    allfiles = walk_through(TARGET_DIRECTORY)
    check = TARGET_CHECK
    for item in allfiles:
        if check_file(item, check):
            try:
                with zipfile.ZipFile(item, 'r') as archive:
                    print(Fore.YELLOW + f"Processing {item} - {len(archive.namelist())}")
            except zipfile.BadZipFile as error:
                print(Fore.RED + f"Bad zip file {item} - {error}")
    excel_store(allfiles)
    print(f"Total files: {len(allfiles)}")
    print("Done")


if __name__ == "__main__":
    main()
