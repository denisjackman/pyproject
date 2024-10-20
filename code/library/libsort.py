'''
This script is used to move PDF and ebook files
from a source directory to a target directory,
and generate a CSV file with details of the files moved.
'''

import os
import shutil
import csv
from datetime import datetime
from pypdf import PdfReader
from mobi import extract
# from pathlib import Path


def extract_text_from_pdf(pdf_path):
    """Extracts text from the first page of a PDF file."""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            if len(reader.pages) > 0:
                page = reader.pages[0]
                text = page.extract_text()
    except Exception:
        text = "Error reading PDF"
    return text


def extract_text_from_mobi(mobi_path):
    """Extracts text from a MOBI file."""
    text = ""
    try:
        extract(mobi_path)
        base_path = mobi_path.rsplit('.', 1)[0]
        mobi_content_path = os.path.join(base_path, 'mobi7', 'mobi7.html')
        if os.path.exists(mobi_content_path):
            with open(mobi_content_path, 'r', encoding='utf-8') as file:
                text = file.read(1000)  # Extracting a sample of the content
    except Exception:
        text = "Error reading MOBI"
    return text


def get_file_info(file_path):
    """Returns file info: name, size, type, and sample content."""
    file_info = {}
    file_info['name'] = os.path.basename(file_path)
    file_info['size'] = os.path.getsize(file_path)
    choice = os.path.splitext(file_path)[1]
    match choice:
        case '.pdf':
            file_info['type'] = 'PDF'
            file_info['content_sample'] = "PDF file"
        case '.epub':
            file_info['type'] = 'ebook'
            file_info['content_sample'] = 'epub content'
        case '.mobi':
            file_info['type'] = 'MOBI'
            file_info['content_sample'] = 'MOBI File'
        case '.azw3':
            file_info['type'] = 'AZW3'
            file_info['content_sample'] = 'azw3 content'
        case _:
            file_info['type'] = f'Unknown - {choice}'
            file_info['content_sample'] = 'Not a PDF or ebook'
    return file_info


def move_files_and_generate_csv(source_dir, target_dir, csv_path):
    """
    Searches for PDF/ebook files,
    moves them, and writes details to a CSV file."""
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with open(csv_path, 'w', newline='',  encoding='utf-8-sig') as csvfile:
        fieldnames = ['name', 'size', 'type', 'content_sample']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.lower().endswith(('.pdf', '.epub', '.mobi', '.azw3')):
                    file_path = os.path.join(root, file)
                    target_path = os.path.join(target_dir, file)
                    shutil.move(file_path, target_path)
                    file_info = get_file_info(target_path)
                    writer.writerow(file_info)


if __name__ == "__main__":
    time_now = datetime.now().strftime('%Y%m%d')
    SOURCE_DIRECTORY = 'Z:/Nulibrary/Done'
    TARGET_DIRECTORY = 'Z:/Library'
    CSV_FILE_PATH = f'Z:/Logs/libsort-{time_now}.csv'

    move_files_and_generate_csv(SOURCE_DIRECTORY,
                                TARGET_DIRECTORY,
                                CSV_FILE_PATH)
