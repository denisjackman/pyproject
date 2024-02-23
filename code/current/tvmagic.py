#!/usr/bin/env python
'''
TV program to find all the files
in a directory tree with a given extension.
'''
# Import the os module, for the os.walk function
import os
import magic

ROOTDIR = '.'


def main():
    ''' main function'''
    # Set the sprites you want to start from

    extTypes = {
        "RIFF (little-": "avi",
        "ISO Media, MP": "mp4",
        "Ogg data, OGM": "ogg",
        "Matroska data": "mkv:",
        "Apple QuickTi": "mov",
        "MPEG sequence": "mpg",
        "Microsoft ASF": "asf"}
    for dirName, _, fileList in os.walk(ROOTDIR):
        for fname in fileList:
            if fname.find('.') == -1:
                tempstr = dirName+"/"+fname
                tempstr += extTypes[magic.from_file(dirName+"/"+fname)[:14]]
                print(f"{tempstr}")


if __name__ == '__main__':
    main()
