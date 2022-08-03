#!/usr/bin/python
"""Simple MP3 to WAV converter

This program takes all the MP3 files in a directory and converts them to WAV
format files.

"""

__author__ = "Mark Pilgrim (mark@diveintopython.org)"
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2013/08/31 20:31:00 $"
__copyright__ = "Copyright (c) 2013 Denis J Jackman"
__license__ = "Python"
import os

if __name__ == "__main__":
    print("Starting")
    tempstr = []
    syscmd = ""
    os.chdir("/home/username/sounds")
    for files in os.listdir("."):
        if files.endswith(".mp3"):
            tempstr = files.split(".")
            syscmd = "ffmpeg -loglevel quiet -i " + tempstr[0] + ".mp3 -ar 8000 -ac 1 -acodec pcm_u8 " + tempstr[0] +".wav"
            os.system(syscmd)
    print("Finished")
