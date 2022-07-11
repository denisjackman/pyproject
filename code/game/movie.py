#!/usr/bin/env python
'''
    movie example
'''
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import moviepy.editor

pygame.init()
img = pygame.image.load("y:/pyproject/resources/jackmanimation.png")

white = (255, 255, 255)
WIDTH = 1920
HEIGHT = 1080

img_x = (WIDTH / 2 ) - (img.get_rect()[2] / 2)
img_y = (HEIGHT / 2) - (img.get_rect()[3] / 2)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

video = moviepy.editor.VideoFileClip("y:/pyproject/resources/Countdown.mov")
video.preview()
screen.fill((white))
screen.blit(img, (img_x, img_y))

pygame.display.flip()
RUNGAME = True
while RUNGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNGANE = False
pygame.quit()
