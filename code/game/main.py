#!/usr/bin/env python
'''
    template for a py game
'''
import pygame
# from settings import (WIDTH, HEIGHT, CAPTION, FPS, BLACK)
from game import Game

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/09/20 00:00:00 $"
__copyright__ = "Copyright (c) 2018 Denis J Jackman"
__license__ = "Python"


def main():
    '''
        main routine
    '''
    game = Game()
    game.show_start_screen()
    while game.running:
        game.new()
        game.show_go_screen()
    pygame.quit()


if __name__ == "__main__":
    # run the main routine
    main()
