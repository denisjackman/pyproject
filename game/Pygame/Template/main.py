#!/usr/bin/env python
'''
    template for a py game
'''
import pygame
from settings import *

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/09/20 00:00:00 $"
__copyright__ = "Copyright (c) 2018 Denis J Jackman"
__license__ = "Python"

class Game():
    '''
        game class
    '''
    def __init__(self):
        # game initiailise
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
        # game loop
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
            handle events
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        '''
            render method
        '''
        # render
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

        # flip the display always do this last
        pygame.display.flip()

    def show_start_screen(self):
        '''
            start screen
        '''
        pass

    def show_go_screen(self):
        '''
            go screen
        '''
        pass

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
