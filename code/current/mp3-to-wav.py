#!/usr/bin/python
"""Simple MP3 to WAV converter

This program takes all the MP3 files in a directory and converts them to WAV
format files.

"""
import os

if __name__ == "__main__":
    print("Starting")
    tempstr = []
    SYSCMD = ""
    os.chdir("Y:/Resources/sounds")
    for files in os.listdir("."):
        if files.endswith(".mp3"):
            tempstr = files.split(".")
            SYSCMD = "ffmpeg -loglevel quiet -i " + tempstr[0] + ".mp3 -ar 8000 -ac 1 -acodec pcm_u8 " + tempstr[0] +".wav"
            os.system(SYSCMD)
    print("Finished")
