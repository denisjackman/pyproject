"""Simple MP3 to WAV converter

This program takes all the MP3 files in a directory and converts them to WAV
format files.

"""
import os
import platform

MP3_OS_NAME = platform.system()
MP3_RUN_CHECK = True

if MP3_OS_NAME == 'Windows':
    MP3_RUN_CHECK = False


if __name__ == "__main__":
    print("Starting")
    tempstr = []
    SYSCMD = ""
    if MP3_RUN_CHECK:
        os.chdir("/mnt/z/Resources/sounds")
        for files in os.listdir("."):
            if files.endswith(".mp3"):
                tempstr = files.split(".")
                SYSCMD = f"ffmpeg -loglevel quiet -i {tempstr[0]}.mp3 -ar 8000 -ac 1 -acodec pcm_u8 {tempstr[0]}.wav"
                print(f'executing [{SYSCMD}]')
                os.system(SYSCMD)
    else:
        print(f"{MP3_OS_NAME} not supported")
    print("Finished")
