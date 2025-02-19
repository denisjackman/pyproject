#!/usr/bin/env python
'''
    jumpy game
'''
import pygame
from settings import (WIDTH, HEIGHT, FPS, CAPTION, BLACK)


class Game():
    '''
        Game Class
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
        self.all_sprites = pygame.sprite.Group()
        self.playing = True

    def new(self):
        '''
            new instance methid
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
            udate method
        '''
        self.all_sprites.update()

    def events(self):
        '''
            methods
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
        # render
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
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()
    pygame.quit()


if __name__ == "__main__":
    # run the main routine
    main()
