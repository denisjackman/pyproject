#!/usr/bin/python
"""Simple MP3 to WAV converter
This program takes all the MP3 files in a sprites and converts them to WAV
format files.
"""

__author__ = "Denis Jackman"
__version__ = "$Revision: 2.0 $"
__date__ = "$Date: 2013/08/31 20:31:00 $"
__copyright__ = "Copyright (c) 2013 Denis J Jackman"
__license__ = "Python"

import os
if __name__ == "__main__":
    print("Starting")
    tempstr = []
    CMDSYS = ""
    os.chdir("Y:/Resources/sounds")
    for files in os.listdir("."):
        if files.endswith(".mp3"):
            tempstr = files.split(".")
            CMDSYS = "ffmpeg -loglevel quiet -i " + tempstr[0] + ".mp3 -ar 8000 -ac 1 -acodec pcm_u8 " + tempstr[0] +".wav"
            os.system(CMDSYS)
    print("Finished")
