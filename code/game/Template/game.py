'''
    placeholder for game class
'''
import pygame
from settings import (WIDTH, HEIGHT, CAPTION, FPS, BLACK)

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
        self.all_sprites = pygame.sprite.Group()
        self.playing = False

    def new(self):
        '''
            new method
        '''
        self.playing = True
        self.run()

    def run(self):
        '''
            run method
        '''
        # game loop
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
            show start screen
        '''

    def show_go_screen(self):
        '''
            show go screen
        '''
