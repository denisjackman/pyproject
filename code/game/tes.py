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

#return_code = subprocess.call(["afplay", byc_audio_file])
#return_code = subprocess.call(["afplay", klaxon_audio_file])
#return_code = subprocess.call(["afplay", attention_audio_file])
#return_code = subprocess.call(["afplay", tos_audio_file])

os.system("say this is the voice of the mysterons calling")
os.system('say By your command, centurion')

pygame.mixer.music.load('sfsweep.ogg')
print("Loading Music...")
pygame.mixer.music.play(0)
print("Playing Background Music...")
