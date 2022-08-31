<<<<<<< Updated upstream
'''
    tes.py
'''
import os
import pygame

pygame.init()

BYC_AUDIO_FILE = "/Users/denisjackman/Documents/workspace/sounds/byc.wav"
KLAXON_AUDIO_FILE ="/Users/denisjackman/Documents/workspace/sounds/klaxon.wav"
ATTENTION_AUDIO_FILE = "/Users/denisjackman/Documents/workspace/sounds/attention.wav"
TOS_AUDIO_FILE = "/Users/denisjackman/Documents/workspace/sounds/soundtosredalert.wav"

MP3_AUDIO_FILE="/Users/denisjackman/Documents/workspace/sounds/sfsweep.mp3"

os.system("say this is the voice of the mysterons calling")
os.system('say By your command, centurion')

pygame.mixer.music.load('sfsweep.ogg')
print("Loading Music...")
pygame.mixer.music.play(0)
print("Playing Background Music...")
=======
'''
    tes.py
'''
import os
import subprocess
import pygame
from pygame.locals import *

pygame.init()

byc_audio_file = "/Users/denisjackman/Documents/workspace/sounds/byc.wav"
klaxon_audio_file ="/Users/denisjackman/Documents/workspace/sounds/klaxon.wav"
attention_audio_file = "/Users/denisjackman/Documents/workspace/sounds/attention.wav"
tos_audio_file = "/Users/denisjackman/Documents/workspace/sounds/soundtosredalert.wav"

mp3_audio_file="/Users/denisjackman/Documents/workspace/sounds/sfsweep.mp3"

os.system("say this is the voice of the mysterons calling")
os.system('say By your command, centurion')

pygame.mixer.music.load('sfsweep.ogg')
print("Loading Music...")
pygame.mixer.music.play(0)
print("Playing Background Music...")
>>>>>>> Stashed changes
