#!/usr/bin/env python
'''
    Boid implementation in Python using PyGame
    Ben Dowling - www.coderholic.com
'''

import pygame
import moviepy.editor

pygame.init()
img = pygame.image.load("jackmanimation.png")
white = (255, 255, 255)
WIDTH = 1920
HEIGHT = 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT))

video = moviepy.editor.VideoFileClip("Countdown.mov")
video.preview()
screen.fill((white))
screen.blit(img, (0, 0))

pygame.display.flip()
RUNGAME = True
while RUNGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME = False

pygame.quit()
