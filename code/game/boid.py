#!/usr/bin/env python
'''
    Boid implementation in Python using PyGame
    Ben Dowling - www.coderholic.com
'''

# import sys
import random
import math
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import cv2

pygame.init()

size = width, height = 800, 600
BLACK = 0, 0, 0
WHITE = (255, 255, 255)
NEAR_BLACK = (10, 10, 10)

MAXVELOCITY = 10
NUMBOIDS = 100
boids = []

screen = pygame.display.set_mode(size)
screen_r = screen.get_rect()
pygame.display.set_caption("Boids")
font = pygame.font.SysFont("Courier", 40)
clock = pygame.time.Clock()

class Boid:
    '''
        boid class
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = random.randint(1, 10) / 10.0
        self.velocityY = random.randint(1, 10) / 10.0


    def distance(self, distance_boid):
        '''
            Return the distance from another boid
        '''
        distX = self.x - distance_boid.x
        distY = self.y - distance_boid.y
        return math.sqrt(distX * distX + distY * distY)

    def moveCloser(self, mc_boids):
        '''
            Move closer to a set of boids"
        '''
        if len(mc_boids) < 1:
            return
        # calculate the average distances from the other boids
        avgX = 0
        avgY = 0
        for mc_boid in mc_boids:
            if mc_boid.x == self.x and mc_boid.y == self.y:
                continue

            avgX += (self.x - mc_boid.x)
            avgY += (self.y - mc_boid.y)

        avgX /= len(mc_boids)
        avgY /= len(mc_boids)

        # set our velocity towards the others
        mc_distance = math.sqrt((avgX * avgX) + (avgY * avgY)) * -1.0

        self.velocityX -= (avgX / 100)
        self.velocityY -= (avgY / 100)


    def moveWith(self, mw_boids):
        '''
            Move with a set of boids
        '''
        if len(mw_boids) < 1:
            return
        # calculate the average velocities of the other boids
        avgX = 0
        avgY = 0

        for mw_boid in mw_boids:
            avgX += mw_boid.velocityX
            avgY += mw_boid.velocityY

        avgX /= len(mw_boids)
        avgY /= len(mw_boids)

        # set our velocity towards the others
        self.velocityX += (avgX / 40)
        self.velocityY += (avgY / 40)


    def moveAway(self, ma_boids, minDistance):
        '''
            Move away from a set of boids. This avoids crowding
        '''
        if len(ma_boids) < 1:
            return

        distanceX = 0
        distanceY = 0
        numClose = 0

        for ma_boid in ma_boids:
            ma_distance = self.distance(ma_boid)
            if  ma_distance < minDistance:
                numClose += 1
                xdiff = (self.x - ma_boid.x)
                ydiff = (self.y - ma_boid.y)

                if xdiff >= 0:
                    xdiff = math.sqrt(minDistance) - xdiff
                elif xdiff < 0:
                    xdiff = -math.sqrt(minDistance) - xdiff

                if ydiff >= 0:
                    ydiff = math.sqrt(minDistance) - ydiff
                elif ydiff < 0:
                    ydiff = -math.sqrt(minDistance) - ydiff

                distanceX += xdiff
                distanceY += ydiff

        if numClose == 0:
            return

        self.velocityX -= distanceX / 5
        self.velocityY -= distanceY / 5


    def move(self):
        '''
            Perform actual movement based on our velocity
        '''
        if abs(self.velocityX) > MAXVELOCITY or abs(self.velocityY) > MAXVELOCITY:
            scaleFactor = MAXVELOCITY / max(abs(self.velocityX), abs(self.velocityY))
            self.velocityX *= scaleFactor
            self.velocityY *= scaleFactor

        self.x += self.velocityX
        self.y += self.velocityY


def game_keypress():
    '''
        check for key-press
    '''
    result = True
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                result = False
            elif event.type == QUIT:
                result = False
    return result


def boid_title():
    '''
        this is the titles for the boid program
    '''
    video = cv2.VideoCapture("clock.mp4")
    img = pygame.image.load("jackmanimation.png")
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)
    run = True
    while run:
        clock.tick(fps)
        run = game_keypress()
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
            video_surf = pygame.transform.scale(video_surf, size)
        else:
            run = False
        screen.blit(video_surf, (0, 0))
        pygame.display.flip()

    TITLE_RUNNING = True
    while TITLE_RUNNING:
        TITLE_RUNNING = game_keypress()
        screen.fill(WHITE)
        screen.blit(img, (240, 140))
        pygame.display.flip()
        pygame.time.delay(60)

def boid_main():
    '''
        main boid routine
    '''

    ball = pygame.image.load("ball.png")
    leader = pygame.image.load("boid.png")
    boid_image = pygame.image.load("greenboid.png")
    pygame.display.set_icon(ball)
    ballrect = boid_image.get_rect()

    # create boids at random positions
    for i in range(NUMBOIDS):
        boids.append(Boid(random.randint(0, width), random.randint(0, height)))
    BOID_RUNNING = True
    while BOID_RUNNING:
        BOID_RUNNING = game_keypress()
                # sys.exit()

        for boid in boids:
            closeBoids = []
            for otherBoid in boids:
                if otherBoid == boid:
                    continue
                distance = boid.distance(otherBoid)
                if distance < 200:
                    closeBoids.append(otherBoid)


            boid.moveCloser(closeBoids)
            boid.moveWith(closeBoids)
            boid.moveAway(closeBoids, 20)

            # ensure they stay within the screen space
            # if we rebound we can lose some of our velocity
            BORDER = 25
            if boid.x < BORDER and boid.velocityX < 0:
                boid.velocityX = -boid.velocityX * random.random()
            if boid.x > width - BORDER and boid.velocityX > 0:
                boid.velocityX = -boid.velocityX * random.random()
            if boid.y < BORDER and boid.velocityY < 0:
                boid.velocityY = -boid.velocityY * random.random()
            if boid.y > height - BORDER and boid.velocityY > 0:
                boid.velocityY = -boid.velocityY * random.random()

            boid.move()

        screen.fill(BLACK)
        for boid in boids:
            boidRect = pygame.Rect(ballrect)
            boidRect.x = boid.x
            boidRect.y = boid.y
            screen.blit(boid_image, boidRect)
        pygame.display.flip()
        pygame.time.delay(10)


def end_titles():
    '''
        end-titles function
    '''
    end_titles_running = True
    credit_list = ["CREDITS",
                   " ",
                   " ",
                   " ",
                   "Jackmanimation Design Studio",
                   " ",
                   " ",
                   " ",
                   "Denis Jackman - Project Lead",
                   "Marian Jackman - Project Director",
                   "Liam Jackman - Designer",
                   "Aidan Jackman - Designer",
                   "Xavier Jackman - Designer",
                   "Frankie - Moral Support",
                   "Sugar - Encouragement",
                   " ",
                   " ",
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
        end_titles_running = game_keypress()

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


def main():
    '''
        Main Routine
    '''
    boid_title()
    boid_main()
    end_titles()

if __name__ == '__main__':
    main()
