#!/usr/bin/env python
'''
    pygame-test
'''
# https://stackoverflow.com/questions/18067219/pygame-image-screen-fill
import pygame
pygame.init()
img = pygame.image.load("oreg.PNG")
white = (255, 255, 255)
WIDTH = 843
HEIGHT = 798

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((white))

screen.fill((white))
screen.blit(img, (0, 0))
pygame.display.flip()
RUNGAME = True
while RUNGAME:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNGAME = False
