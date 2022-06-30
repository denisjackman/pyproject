'''
    A test for a pygame
'''
import pygame
from pygame.locals import QUIT

pygame.init()
RUNNING = True
black = (0, 0, 0)
white = (255, 255, 255)
img = []

game_window = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Sample Game")

imgload = pygame.image.load('test/sprites/e_000.png').convert()

img.append(pygame.image.load('test/sprites/e_000.png').convert())
img.append(pygame.image.load('test/sprites/e_001.png').convert())
img.append(pygame.image.load('test/sprites/e_002.png').convert())
img.append(pygame.image.load('test/sprites/e_003.png').convert())
img.append(pygame.image.load('test/sprites/e_004.png').convert())
img.append(pygame.image.load('test/sprites/e_005.png').convert())
img.append(pygame.image.load('test/sprites/e_006.png').convert())
img.append(pygame.image.load('test/sprites/e_007.png').convert())
img.append(pygame.image.load('test/sprites/e_008.png').convert())
img.append(pygame.image.load('test/sprites/e_009.png').convert())
img.append(pygame.image.load('test/sprites/e_010.png').convert())
img.append(pygame.image.load('test/sprites/e_011.png').convert())
img.append(pygame.image.load('test/sprites/e_012.png').convert())
img.append(pygame.image.load('test/sprites/e_013.png').convert())
img.append(pygame.image.load('test/sprites/e_014.png').convert())
img.append(pygame.image.load('test/sprites/e_015.png').convert())
img.append(pygame.image.load('test/sprites/e_016.png').convert())
img.append(pygame.image.load('test/sprites/e_017.png').convert())
img.append(pygame.image.load('test/sprites/e_018.png').convert())
img.append(pygame.image.load('test/sprites/e_019.png').convert())
img.append(pygame.image.load('test/sprites/e_020.png').convert())
img.append(pygame.image.load('test/sprites/e_021.png').convert())
img.append(pygame.image.load('test/sprites/e_022.png').convert())
img.append(pygame.image.load('test/sprites/e_023.png').convert())
img.append(pygame.image.load('test/sprites/e_024.png').convert())
img.append(pygame.image.load('test/sprites/e_025.png').convert())
img.append(pygame.image.load('test/sprites/e_026.png').convert())
img.append(pygame.image.load('test/sprites/e_027.png').convert())
img.append(pygame.image.load('test/sprites/e_028.png').convert())
img.append(pygame.image.load('test/sprites/e_029.png').convert())
img.append(pygame.image.load('test/sprites/e_030.png').convert())
img.append(pygame.image.load('test/sprites/e_031.png').convert())
img.append(pygame.image.load('test/sprites/e_032.png').convert())
img.append(pygame.image.load('test/sprites/e_033.png').convert())
img.append(pygame.image.load('test/sprites/e_034.png').convert())
img.append(pygame.image.load('test/sprites/e_035.png').convert())
img.append(pygame.image.load('test/sprites/e_036.png').convert())

def sprite(sx, sy):
    '''
        sprite function
    '''
    game_window.blit(imgload, (sx, sy))

COUNTER = 0
LOOPER = 0
LIMIT = len(img)
clock = pygame.time.Clock()
while RUNNING:
    SPRITE_X = 82
    SPRITE_Y = 64
    imgload = img[COUNTER]
    COUNTER += 1
    if COUNTER == LIMIT:
        COUNTER = 0
    imgload.set_colorkey(black)
    game_window.fill(white)

    sprite(SPRITE_X, SPRITE_Y)

    pygame.display.flip()
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False
            pygame.quit()
