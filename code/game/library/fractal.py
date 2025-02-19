"""
 Sample fractal using recursion.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""

import pygame


def recursive_draw(x,
                   y,
                   width,
                   height,
                   count,
                   screen,
                   color):
    '''
        raw the rectangle
    '''
    # pygame.draw.rect(screen,black,[x,y,width,height],1)
    pygame.draw.line(screen,
                     color,
                     [x + width * .25, height // 2 + y],
                     [x + width * .75, height // 2 + y],
                     3)
    pygame.draw.line(screen,
                     color,
                     [x + width * .25, (height * .5) // 2 + y],
                     [x + width * .25,  (height * 1.5) // 2 + y],
                     3)
    pygame.draw.line(screen,
                     color,
                     [x + width * .75, (height * .5) // 2 + y],
                     [x + width * .75, (height * 1.5) // 2 + y],
                     3)

    if count > 0:
        count -= 1
        # Top left
        recursive_draw(x,
                       y,
                       width // 2,
                       height // 2,
                       count,
                       screen,
                       color)
        # Top right
        recursive_draw(x + width // 2,
                       y,
                       width // 2,
                       height // 2,
                       count,
                       screen,
                       color)
        # Bottom left
        recursive_draw(x,
                       y + width // 2,
                       width // 2,
                       height // 2,
                       count,
                       screen,
                       color)
        # Bottom right
        recursive_draw(x + width // 2,
                       y + width // 2,
                       width // 2,
                       height // 2,
                       count,
                       screen,
                       color)


def main():
    ''' main function'''
    pygame.init()
    # Define some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    # green = (0, 255, 0)
    # red = (255, 0, 0)
    # set the height and width of the screen
    size = [700, 700]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Fractals")

    # Loop until the user clicks the close button.
    DONE = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                DONE = True
        # set the screen background
        screen.fill(white)
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        FRACTAL_LEVEL = 3
        recursive_draw(0, 0, 700, 700, FRACTAL_LEVEL, screen, black)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 20 frames per second
        clock.tick(20)
        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
    pygame.quit()


if __name__ == '__main__':
    main()
