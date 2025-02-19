#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Labtest.py
    this is a test run for screens and stuff
    primer for pygame out prior to using it elsewhere.

References:
 https://realpython.com/pygame-a-primer/
 https://github.com/realpython/pygame-primer
 https://github.com/sagardspeed2/PrimerGame
 https://stackoverflow.com/questions/18067219/pygame-image-screen-fill

"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2022/07/30 11:31:00 $"
__copyright__ = "Copyright (c) 2022 Denis J Jackman"
__license__ = "Python"

from djgamemodule import colours as col
import pygame

WIDTH = 800
HEIGHT = 600


def create_surface(surface_colour, surface_size):
    '''
        surface create function
        take a surface colour (RGB code)
        take a size (width , height)
        create and return a surface
    '''
    result_surface = pygame.Surface(surface_size)
    # Create empty pygame surface
    result_surface.fill(surface_colour)
    # Fill the background white color (red,green,blue)
    result_surface = result_surface.convert()
    # Convert Surface to make blitting faster
    return result_surface


def title_work():
    '''
        do everything needed for the tile
    '''
    font_title = pygame.font.SysFont(None, 48)
    title_work_result = create_surface(col.RED, (800, 50))
    titlefont = font_title.render('Game Title', True, col.BLACK)
    xwidth = (title_work_result.get_width() / 2) - (titlefont.get_width() / 2)
    yheight = (title_work_result.get_height() / 2) - (titlefont.get_height() / 2)

    title_work_result.blit(titlefont, (xwidth, yheight))
    return title_work_result


def log_messages():
    '''
        do everything needed for the tile
    '''
    font_log = pygame.font.SysFont(None, 24)
    log_work_result = create_surface(col.DIM_GRAY, (800, 50))
    logfont = font_log.render('Message status', True, col.BLACK)
    log_work_result.blit(logfont, (0, 0))
    return log_work_result


def labtest_main():
    '''
        labtest main function
    '''
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    runtest = True
    while runtest:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runtest = False
        screen.fill((col.WHITE))

        background = create_surface(col.BLACK, (800, 600))
        gamearea = create_surface(col.DARK_GREEN, (700, 500))
        stats = create_surface(col.BLUE, (100, 500))

        screen.blit(background, (0, 0))
        screen.blit(title_work(), (0, 0))
        screen.blit(gamearea, (0, 50))
        screen.blit(stats, (700, 50))
        screen.blit(log_messages(), (0, 550))

        pygame.display.flip()


# Main loop for the game
if __name__ == '__main__':
    labtest_main()
