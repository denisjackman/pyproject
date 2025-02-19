'''
    pygame main
'''
import os
import pygame
from pygame.locals import RLEACCEL

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')

# Global Variables
WIDTH = 640
HEIGHT = 480
TITLE = "My_Project"
Speed = [2, 2]

# Colours Add them as needed
white_color = pygame.Color(255, 255, 255)
gold_color = pygame.Color(255, 215, 0)
red_color = pygame.Color(255, 0, 0)
green_color = pygame.Color(0, 255, 0)
blue_color = pygame.Color(0, 0, 255)

pygame.init()
# Fonts
# need to create fonts and colour objects in PyGame
# fontObj = pygame.font.Font('ARBERKLEY.ttf', 32)
# fontObj2 = pygame.font.Font('ARBERKLEY.ttf', 24)
fontObj4 = pygame.font.Font('Z:/Resources/Fonts/halfelven.ttf', 32)
fontObj3 = pygame.font.Font(pygame.font.match_font('timenewroman'), 32)

# Initialise Game

canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

draw_colour = gold_color

# Helper Functions


def load_image(name, colorkey=None):
    '''
        load image
    '''
    fullname = os.path.join('Z:/Resources/images', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print(f'Cannot load image: {name} : {message}')
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    else:
        image = image.convert_alpha()
    return image, image.get_rect()


def load_sound(name):
    '''
        load sound
    '''
    class NoneSound:
        '''
            none sound object
        '''
        def name(self):
            '''
                naming method
            '''

        def play(self):
            '''
                Play
            '''

    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('Z:/Resources/sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as message:
        print(f'Cannot load sound: {name} : {message}')
    return sound


def draw_handler(dhcanvas, dhcount):
    '''
        draw handler function
    '''
    dhcanvas.fill((0, 0, 0))
    dhcount += 1
    text_draw = fontObj4.render("CodeSkulptor Port", True, draw_colour)
    text_draw2 = fontObj4.render("Tutorial", True, draw_colour)
    if dhcount % 90 < 45:
        dhcanvas.blit(text_draw, (190, 220))
    else:
        dhcanvas.blit(text_draw2, (250, 220))
    pygame.display.update()
    return dhcount


def main():
    '''
        main function
    '''
    count = 0
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.KEYDOWN:
                pass
        count = draw_handler(canvas, count)
        clock.tick(60)
    pygame.quit()


# Main loop for the game
if __name__ == '__main__':
    main()
