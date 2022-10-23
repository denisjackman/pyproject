#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Data recovery script
    https://codeonby.com/2022/05/07/python-for-data-recovery/
    https://www.garykessler.net/library/file_sigs.html
    https://www.usna.edu/Users/cs/wcbrown/courses/si110AY13S/lec/l31/lec.html
'''

import psutil

__version__ = "$Revision: 0.01 $"
__date__ = "$Date: 2022/08/19 00:00:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"



def main():  #pylint: disable=R0914
    '''
        main function
    '''

    PATH = "Y:"
    DRIVE = f"\\\\.\\{PATH}"     # Open DRIVE as raw bytes
    SIZE = 512              # SIZE of bytes to read
    OFFSET = 0              # Offset location
    REC = False            # Recovery mode

    RECOVERED = 0           # Recovered file ID

    print(f'Path Name ({PATH}):')

    JPEGHEADER = b'\xff\xd8\xff\xe0\x00\x10\x4a\x46' # JPEG header
    JPEGFINISH = b'\xff\xd9'                         # JPEG finish
    PNGHEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'  # PNG header
    PNGFINISH = b'\x49\x45\x4e\x44\xae\x42\x60\x82'  # PNG finish
    READSIZE = 0
    TOTALSIZE = psutil.disk_usage(PATH).total / 2**30 # Total size of drive in GB


    with open(DRIVE, 'rb') as fileD:
        byte = fileD.read(SIZE) # Read 'SIZE' bytes
        print("==== Starting the scan ====")
        while byte:
            jfound = byte.find(JPEGHEADER)
            found = byte.find(PNGHEADER)
            if found >= 0:
                REC = True
                print('==== Found PNG at location: ' + str(hex(found+(SIZE*OFFSET))) + ' ====')
                # Now lets create recovered file and search for ending signature
                RFILENAME = f"recovered/recover-{RECOVERED}.png"
                with open(RFILENAME, "wb") as fileN:
                    fileN.write(byte[found:])
                    while REC:
                        byte = fileD.read(SIZE)
                        bfind = byte.find(PNGFINISH)
                        if bfind >= 0:
                            fileN.write(byte[:bfind+2])
                            fileD.seek((OFFSET+1)*SIZE)

                            print(f"==== Wrote File to location:  {RFILENAME} ====\n")
                            REC = False
                            RECOVERED += 1
                        else:
                            fileN.write(byte)

            if jfound >= 0:
                REC = True
                print('==== Found JPG at location: ' + str(hex(jfound+(SIZE*OFFSET))) + ' ====')
                # Now lets create recovered file and search for ending signature
                FILENAME = f"recovered/recover-{RECOVERED}.png"
                with open(FILENAME, "wb") as fileN:
                    fileN.write(byte[jfound:])
                    while REC:
                        byte = fileD.read(SIZE)
                        find = byte.find(JPEGFINISH)
                        if find >= 0:
                            fileN.write(byte[:find+2])
                            fileD.seek((OFFSET+1)*SIZE)

                            print(f"==== Wrote File to location:  {FILENAME} ====\n")
                            REC = False
                            RECOVERED += 1
                        else:
                            fileN.write(byte)


            byte = fileD.read(SIZE)
            OFFSET += 1
            READSIZE += SIZE
    print(f"==== Read {str(READSIZE / 2 ** 30 )} / {TOTALSIZE} gigabytes ====\n")
    print(f"==== Recovered {RECOVERED} files ====\n")
    print("==== Scan Complete ====")
    print("==== Exiting ====\n")

if __name__ == "__main__":
    main()
