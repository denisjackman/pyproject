''' cleaner script '''
import os
import shutil
from datetime import datetime
from tqdm import tqdm

MOVE_FILES = True
RENAME_FILES = False


def sort_files(start_directory, target_directory):
    """
    Sort files from the start_directory into the target_directory.
    Files will be moved into folders by file type and renamed as
    FILETYPE-YYYYMMDD-NNNNN. The program will move recursively from
    the top of the start directory to the bottom.

    Args:
        start_directory (str): The directory to start searching for files.
        target_directory (str): The directory to move sorted files to.
    """
    # Initialize a dictionary to track the sequence number for each file type
    file_counters = {}

    # Walk through the directory tree recursively
    for root, _, files in os.walk(start_directory):
        for file_name in tqdm(files, total=len(files), unit=' file'):
            # Get the file extension and check if it's already tracked
            file_type = file_name.split('.')[-1].lower()

            if file_type not in file_counters:
                # Initialize the counter for new file types
                file_counters[file_type] = 0
            # Increment the counter for the current file type
            file_counters[file_type] += 1

            # Generate the new filename using the provided format
            date_str = datetime.now().strftime('%Y%m%d')
            # Format the new file name with the file type, date, and counter

            new_file_name = f"{file_type.upper()}"
            new_file_name += f"-{date_str}"
            new_file_name += f"-{file_counters[file_type]:05d}"
            new_file_name += f".{file_type}"

            # Create the target folder based on the file type
            target_folder = os.path.join(target_directory, file_type.upper())

            if not os.path.exists(target_folder):
                # Create the folder if it doesn't exist
                os.makedirs(target_folder)

            # Define the full source and destination file paths
            source_file = os.path.join(root, file_name)

            if RENAME_FILES:
                target_file_name = new_file_name
            else:
                target_file_name = file_name

            destination_file = os.path.join(target_folder, target_file_name)

            # Move and rename the file
            if MOVE_FILES:
                shutil.move(source_file, destination_file)


if __name__ == "__main__":
    # Example usage
    START_DIR = 'T:/current'  # Replace with the actual start directory
    TARGET_DIR = 'T:/store'  # Replace with the actual target directory
    sort_files(START_DIR, TARGET_DIR)
