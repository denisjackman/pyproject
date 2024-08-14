'''
    This is a Sprite checking utility
'''
import os
import sys
from pathlib import Path
import pygame
# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.classes.sprite import GameSprite

WIDTH = 800
HEIGHT = 800
CAPTION = "Jackmanimation [SpriteChecker]"
ICON_FILE = 'Z:/Resources/jackmanimation.png'
WHITE = (255, 255, 255)
FILEPATH = Path(__file__).parent


def main():
    ''' main routine '''
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(CAPTION)
    pygame_icon = pygame.image.load(ICON_FILE)
    pygame.display.set_icon(pygame_icon)
    done = False
    clock = pygame.time.Clock()
    playsprite = GameSprite(WIDTH, HEIGHT)
    while not done:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.fill((WHITE))
        playsprite.draw(window)
        pygame.display.update()


if __name__ == '__main__':
    main()
