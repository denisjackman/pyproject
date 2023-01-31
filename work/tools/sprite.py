''' Sprite class for pygame games'''
import os
import pygame

class GameSprite:
    ''' GameSprite class'''
    def __init__(self, x=0, y=0):
        self.image = None
        self.images = []
        self.animation_count = 0
        for item in range(20):
            add_str = str(item)
            if item < 10:
                add_str = '0' + add_str
            asset = f"{os.path.join('y:/tower-defense/tim-tower/game_assets/2d-monster-sprites/PNG/10')}/10_enemies_1_run_0{add_str}.png"
            asset_store = pygame.image.load(asset)
            self.images.append(asset_store)
        self.x = x/2 - self.images[0].get_width()/2
        self.y = y/2 - self.images[0].get_height()/2

    def draw(self, screen):
        ''' draw the sprite '''
        self.animation_count += 1
        if self.animation_count >= len(self.images):
            self.animation_count = 0
        self.image = self.images[self.animation_count]
        screen.blit(self.image, (self.x, self.y))

    def move(self, x, y):
        ''' move the sprite '''
        self.x += x
        self.y += y
