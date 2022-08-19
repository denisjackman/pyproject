'''
    Data recovery script
    https://codeonby.com/2022/05/07/python-for-data-recovery/
    https://www.garykessler.net/library/file_sigs.html
'''
DRIVE = "\\\\.\\H:"     # Open DRIVE as raw bytes
fileD = open(DRIVE, "rb")
SIZE = 512              # SIZE of bytes to read
byte = fileD.read(SIZE) # Read 'SIZE' bytes
OFFSET = 0              # Offset location
DREC = False            # Recovery mode
RECOVERED = 0           # Recovered file ID

JPEGHEADER = b'\xff\xd8\xff\xe0\x00\x10\x4a\x46' # JPEG header
PNGHEADER = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'  # PNG header
PDFHEADER = b'%PDF-'                             # PDF header

while byte:
    found = byte.find(b'\xff\xd8\xff\xe0\x00\x10\x4a\x46')
    if found >= 0:
        DREC = True
        print('==== Found JPG at location: ' + str(hex(found+(SIZE*OFFSET))) + ' ====')
        # Now lets create recovered file and search for ending signature
        RFILENAME = f"recovered/recover-{RECOVERED}.jpg"
        fileN = open(RFILENAME, "wb")
        fileN.write(byte[found:])
        while DREC:
            byte = fileD.read(SIZE)
            bfind = byte.find(b'\xff\xd9')
            if bfind >= 0:
                fileN.write(byte[:bfind+2])
                fileD.seek((OFFSET+1)*SIZE)
                print(f"==== Wrote JPG to location:  {RFILENAME} ====\n")
                DREC = False
                RECOVERED += 1
                fileN.close()
            else: fileN.write(byte)
    byte = fileD.read(SIZE)
    OFFSET += 1
fileD.close()
