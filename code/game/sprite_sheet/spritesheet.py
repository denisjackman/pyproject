'''
    spritesheet module
'''
import json
import pygame


class Spritesheet:
    '''
        spritesheet class
    '''
    def __init__(self, filename):
        '''
            the init method
        '''
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data, encoding="utf8") as sprite_file:
            self.data = json.load(sprite_file)
        sprite_file.close()

    def get_sprite(self, x_pos, y_pos, width, height):
        '''
            get sprite method
        '''
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0, 0, 0))
        sprite.blit(self.sprite_sheet, (0, 0), (x_pos, y_pos, width, height))
        return sprite

    def parse_sprite(self, name):
        '''
            parse the sprite
        '''
        sprite = self.data['frames'][name]['frame']
        x_pos = sprite["x"]
        y_pos = sprite["y"]
        width = sprite["w"]
        height = sprite["h"]
        image = self.get_sprite(x_pos, y_pos, width, height)
        return image
