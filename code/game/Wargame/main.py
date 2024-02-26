#!/usr/bin/env python
'''
    Main game routine
'''
import pygame
from settings import CAPTION, WIDTH, HEIGHT, FPS, BLACK

__author__ = "Denis J Jackman (denis_jackman@hotmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2019/09/20 00:00:00 $"
__copyright__ = "Copyright (c) 2018 Denis J Jackman"
__license__ = "Python"


class Game():
    '''
        game object
    '''
    def __init__(self):
        # game initiailise
        self.running = True
        self.all_sprites = None
        self.playing = None
        # initialise pygame and set up the screen
        pygame.init()
        pygame.mixer.init()
        self.gscreen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()

    def new(self):
        '''
            new instance
        '''
        self.all_sprites = pygame.sprite.Group()
        self.run()

    def run(self):
        '''
            run the game
        '''
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        '''
            events method
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        '''
            update method
        '''
        self.all_sprites.update()

    def draw(self):
        '''
            render
        '''
        self.gscreen.fill(BLACK)
        self.all_sprites.draw(self.gscreen)

        # flip the display always do this last
        pygame.display.flip()

    def show_game_start_screen(self):
        '''
            start screen
        '''

    def show_game_go_screen(self):
        '''
            go screen
        '''


def wargame_main():
    '''
        main routine
    '''
    g = Game()
    g.show_game_start_screen()
    while g.running:
        g.new()
        g.show_game_go_screen()
    pygame.quit()


if __name__ == "__main__":
    # run the main routine
    wargame_main()
