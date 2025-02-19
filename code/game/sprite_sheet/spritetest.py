'''
    this is a test program for sprite sheet
    https://www.youtube.com/watch?v=ePiMYe7JpJo
'''
import pygame
from spritesheet import Spritesheet

pygame.init()
DISPLAY_W = 480
DISPLAY_H = 270
canvas = pygame.Surface((DISPLAY_W, DISPLAY_H))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
RUNNING = True
WHITE = (255, 255, 255)

my_spritesheet = Spritesheet(r'Z:\Resources\development\sprite_sheet\trainer_sheet_two.png')
trainer = [my_spritesheet.parse_sprite('trainer1.png'),
           my_spritesheet.parse_sprite('trainer2.png'),
           my_spritesheet.parse_sprite('trainer3.png'),
           my_spritesheet.parse_sprite('trainer4.png'),
           my_spritesheet.parse_sprite('trainer5.png')]

female_trainer = [my_spritesheet.parse_sprite('f_trainer1.png'),
                  my_spritesheet.parse_sprite('f_trainer2.png'),
                  my_spritesheet.parse_sprite('f_trainer3.png'),
                  my_spritesheet.parse_sprite('f_trainer4.png'),
                  my_spritesheet.parse_sprite('f_trainer5.png')]

INDEX_COUNTER = 0

while RUNNING:
    # CHECK PLAYER INPUT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            # UPDATE SPRITE IF SPACE IS PRESSED
            if event.key == pygame.K_SPACE:
                INDEX_COUNTER = (INDEX_COUNTER + 1) % len(trainer)

    # UPDATE WINDOW AND DISPLAY
    canvas.fill(WHITE)
    canvas.blit(trainer[INDEX_COUNTER], (0, DISPLAY_H - 128))
    canvas.blit(female_trainer[INDEX_COUNTER], (128, DISPLAY_H - 128))
    window.blit(canvas, (0, 0))
    pygame.display.update()
