#!/usr/bin/python
"""
    audioplayer.py
    This is the main source.
    This is a tool for viewer images.
"""

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/09/24 00:00:00 $"
__copyright__ = "Copyright (c) 2018 Denis J Jackman"
__license__ = "Python"

import os
import pygame
from settings import (WIDTH, HEIGHT, FPS, BLACK)

CAPTION = "audioplayer"

class Game():
    '''
        game class
    '''
    def __init__(self):
        # game initialise
        self.running = True
        # initialise pygame and set up the screen
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

    def new(self):
        '''
            new method
        '''
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        '''
            game loop
        '''
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        '''
            update method
        '''
        self.all_sprites.update()

    def events(self):
        '''
            events method
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        '''
            render
        '''
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # flip the display always do this last
        pygame.display.flip()

    def show_start_screen(self):
        '''
            start screen
        '''

    def show_go_screen(self):
        '''
            go screen
        '''


def main():
    '''
        main routine
    '''
    target = ".wav"
    directory = '/Users/username/Documents/workspace/Resources/audio'
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith(target):
            file_list.append(os.path.join(directory, filename))
            # print os.path.join(directory, filename)

    for _ in file_list:
        print(_)

    # g = Game()
    # g.show_start_screen()
    # while g.running:
    #     g.new()
    #     g.show_go_screen()
    # pygame.quit()


if __name__ == '__main__':
    main()
