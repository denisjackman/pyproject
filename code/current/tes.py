'''
    tes.py
'''
import os
import pygame

pygame.init()

BYC_AUDIO_FILE = "Z:/Resources/sounds/byc.wav"
KLAXON_AUDIO_FILE = "Z:/Resources/sounds/klaxon.wav"
ATTENTION_AUDIO_FILE = "Z:/Resources/sounds/attention.wav"
TOS_AUDIO_FILE = "Z:/Resources/sounds/tos-redalert.wav"
TALK = False
MP3_AUDIO_FILE = "Z:/Resources/sounds/sfsweep.mp3"

if TALK:
    os.system("say this is the voice of the mysterons calling")
    os.system('say By your command, centurion')

pygame.mixer.music.load('Z:/Resources/sounds/sfsweep.ogg')
print("Loading Music...")
pygame.mixer.music.play(0)
print("Playing Background Music...")
