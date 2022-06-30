#!/usr/bin/env python
'''
    Boid implementation in Python using PyGame
    Ben Dowling - www.coderholic.com
'''

import sys
import random
import math
import pygame

pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

MAXVELOCITY = 10
NUMBOIDS = 50
boids = []

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

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Boids")

ball = pygame.image.load("ball.png")
pygame.display.set_icon(ball)
ballrect = ball.get_rect()

# create boids at random positions
for i in range(NUMBOIDS):
    boids.append(Boid(random.randint(0, width), random.randint(0, height)))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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
        # if we roubound we can lose some of our velocity
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

    screen.fill(black)
    for boid in boids:
        boidRect = pygame.Rect(ballrect)
        boidRect.x = boid.x
        boidRect.y = boid.y
        screen.blit(ball, boidRect)
    pygame.display.flip()
    pygame.time.delay(10)
