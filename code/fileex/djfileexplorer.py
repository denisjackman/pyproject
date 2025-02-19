'''
 file explorer
'''
import os
import csv
import sys


def main():
    '''
        main routine
    '''
    filelist = []
    if len(sys.argv) == 2:
        rootdir = sys.argv[1]
        if not os.path.isdir(rootdir):
            print(f"Directory path {rootdir} does not exist. Exiting...")
            sys.exit()
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filelist.append(os.path.join(subdir, file))

    else:
        print("Usage: python3 djfileexplorer.py <directory path>")
        sys.exit()

    for file in filelist:
        name = os.path.basename(file)
        details = name.split('.')
        extension = details[-1]
        print(f" name: {name} extension: {extension} file: {file}")

    with open("Z:/Resources/development/example.csv",
              'w',
              encoding='utf-8-sig',
              newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["name", "extension", "file"])
        for file in filelist:
            name = os.path.basename(file)
            details = name.split('.')
            extension = details[-1]
            data = [name, extension, file.strip()]
            writer.writerow(data)


if __name__ == '__main__':
    main()
