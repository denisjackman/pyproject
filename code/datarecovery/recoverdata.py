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

def main():
    '''
        main function
    '''
    PATH = "H:"
    DRIVE = f"\\\\.\\{PATH}"     # Open DRIVE as raw bytes
    fileD = open(DRIVE, "rb")
    SIZE = 512              # SIZE of bytes to read
    byte = fileD.read(SIZE) # Read 'SIZE' bytes
    OFFSET = 0              # Offset location
    DREC = False            # Recovery mode
    JDREC = False            # Recovery mode

    RECOVERED = 0           # Recovered file ID

    print(f'Path Name ({PATH}):')

    JPEGHEADER = b'\xff\xd8\xff\xe0\x00\x10\x4a\x46' # JPEG header
    JPEGFINISH = b'\xff\xd9'                         # JPEG finish
    PNGHEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'  # PNG header
    PNGFINISH = b'\x49\x45\x4e\x44\xae\x42\x60\x82'  # PNG finish
    PDFHEADER = b'%PDF-'                             # PDF header
    READSIZE = 0
    TOTALSIZE = psutil.disk_usage(PATH).total / 2**30 # Total size of drive in GB
    print("==== Starting the scan ====")
    while byte:
        jfound = byte.find(JPEGHEADER)
        found = byte.find(PNGHEADER)
        if found >= 0:
            DREC = True
            print('==== Found PNG at location: ' + str(hex(found+(SIZE*OFFSET))) + ' ====')
            # Now lets create recovered file and search for ending signature
            RFILENAME = f"recovered/recover-{RECOVERED}.png"
            fileN = open(RFILENAME, "wb")
            fileN.write(byte[found:])
            while DREC:
                byte = fileD.read(SIZE)
                bfind = byte.find(PNGFINISH)
                if bfind >= 0:
                    fileN.write(byte[:bfind+2])
                    fileD.seek((OFFSET+1)*SIZE)

                    print(f"==== Wrote File to location:  {RFILENAME} ====\n")
                    DREC = False
                    RECOVERED += 1
                    fileN.close()
                else:
                    fileN.write(byte)

        if jfound >= 0:
            JDREC = True
            print('==== Found JPG at location: ' + str(hex(jfound+(SIZE*OFFSET))) + ' ====')
            # Now lets create recovered file and search for ending signature
            JRFILENAME = f"recovered/recover-{RECOVERED}.png"
            jfileN = open(JRFILENAME, "wb")
            jfileN.write(byte[jfound:])
            while JDREC:
                byte = fileD.read(SIZE)
                jbfind = byte.find(JPEGFINISH)
                if jbfind >= 0:
                    jfileN.write(byte[:jbfind+2])
                    fileD.seek((OFFSET+1)*SIZE)

                    print(f"==== Wrote File to location:  {JRFILENAME} ====\n")
                    JDREC = False
                    RECOVERED += 1
                    jfileN.close()
                else:
                    jfileN.write(byte)


        byte = fileD.read(SIZE)
        OFFSET += 1
        READSIZE += SIZE
    fileD.close()
    print(f"==== Read {str(READSIZE / 2 ** 30 )} / {TOTALSIZE} gigabytes ====\n")
    print(f"==== Recovered {RECOVERED} files ====\n")
    print("==== Scan Complete ====")
    print("==== Exiting ====\n")

if __name__ == "__main__":
    main()
