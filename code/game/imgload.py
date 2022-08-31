#!/usr/bin/env python
'''
    imageload python script
'''
import random

import pygame
from pygame.locals import (QUIT, Rect)


def grid_build(width, height, tile):
    '''
    Builds a list which is a grid width in width and height in height
    The tile is a number representig the the tiles

     Inputs:
               width = int
               height = int
               tile = int

     Outputs:
               map_list = list of lists which represents the grid

    '''
    map_list = []
    for row_count in range(width):
        grid_list = []
        for column_count in range(height):
            grid_list.append(random.randint(0, tile))
        map_list.append(grid_list)
    return map_list


pygame.init()
RUNNING = True
game_window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Utility Tool")
black = (0, 0, 0)
white = (255, 255, 255)
grid = grid_build(18, 13, 7)
IMG_FILE = 'Y:/pyproject/resources/images/match3_tiles_px.png'
img = pygame.image.load(IMG_FILE).convert()


map_tile = []
map_tile.append(img.subsurface(Rect(0, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(40, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(80, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(120, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(160, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(200, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(240, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(280, 0, 40, 39)))
map_tile.append(img.subsurface(Rect(0, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(40, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(80, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(120, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(160, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(200, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(240, 40, 40, 39)))
map_tile.append(img.subsurface(Rect(280, 40, 40, 39)))


print("width  : ", img.get_rect().size[0])
print("height : ", img.get_rect().size[1])

X_POS = 50
Y_POS = 50
pygame.mouse.set_visible(False)
while RUNNING:

    game_window.fill(white)
    BUTTON = 0
    ITEM = 0
    for line in grid:
        for col in line:
            game_window.blit(map_tile[col], (X_POS + BUTTON * 40,
                                             Y_POS + ITEM * 40))
            ITEM += 1
        BUTTON += 1
        ITEM = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mouse.set_visible(True)
            RUNNING = False
            pygame.quit()
