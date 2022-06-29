#!/usr/bin/env python
import pygame
from pygame.locals import *
import random


def grid_build(width, height, tile):
    # Builds a list which is a grid width in width and height in height
    # The tile is a number representig the the tiles
    #
    # Inputs:
    #           width = int
    #           height = int
    #           tile = int
    #
    # Outputs:
    #           map_list = list of lists which represents the grid
    #

    map_list = []
    for row_count in range(width):
        grid_list = []
        for column_count in range(height):
            grid_list.append(random.randint(0, tile))
        map_list.append(grid_list)
    return map_list


pygame.init()
running = True

black = (0, 0, 0)
white = (255, 255, 255)
grid = grid_build(18, 13, 7)
img = pygame.image.load('match3_tiles_px.png').convert()


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


print "width  : ", img.get_rect().size[0]
print "height : ", img.get_rect().size[1]

x = 50
y = 50
pygame.mouse.set_visible(False)
while running:
    game_window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Utility Tool")
    game_window.fill(white)
    b = 0
    i = 0
    for line in grid:
        for col in line:
            game_window.blit(map_tile[col], (x+b*40, y+i*40))
            i += 1
        b += 1
        i = 0

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mouse.set_visible(True)
            running = False
            pygame.quit()
