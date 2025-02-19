'''
    This is a sample title credits screen
'''
import pygame
from pygame.locals import (QUIT, KEYDOWN, K_ESCAPE)
WHITE = (255, 255, 255)
NEAR_BLACK = (10, 10, 10)

pygame.init()
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode((800, 600))
screen_r = screen.get_rect()
font = pygame.font.SysFont("Courier", 40)
clock = pygame.time.Clock()


def end_titles():
    '''
        end-titles function
    '''
    end_titles_running = True
    credit_list = ["CREDITS",
                   " ",
                   "Jackmanimation Design Studio",
                   " ",
                   "Denis Jackman - Project Lead",
                   "Marian Jackman - Project Lead",
                   "Liam Jackman - Designer",
                   "Aidan Jackman - Designer",
                   "Xavier Jackman - Designer",
                   " ",
                   "(C) Jackmanimation 2022"]

    texts = []
    # we render the text once, since it's easier to work with surfaces
    # also, font rendering is a performance killer
    for item, line in enumerate(credit_list):
        screen_credit = font.render(line, 1, WHITE)
        # we also create a Rect for each Surface.
        # whenever you use rects with surfaces,
        # it may be a good idea to use sprites instead
        # we give each rect the correct starting position
        render = screen_credit.get_rect(centerx=screen_r.centerx,
                                        y=screen_r.bottom + item * 45)
        texts.append((render, screen_credit))

    while end_titles_running:
        for title_event in pygame.event.get():
            if title_event.type == QUIT or \
               title_event.type == KEYDOWN and \
               title_event.key == K_ESCAPE:
                return

        screen.fill(NEAR_BLACK)

        for render, screen_credit in texts:
            # now we just move each rect by one pixel each frame
            render.move_ip(0, -1)
            # and drawing is as simple as this
            screen.blit(screen_credit, render)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([render for (render, _) in texts]):
            return

        # only call this once so the screen does not flicker
        pygame.display.flip()

        # cap framerate at 60 FPS
        clock.tick(60)


if __name__ == '__main__':
    end_titles()
