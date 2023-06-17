import pygame
from pygame.locals import *
import random

class BALL ():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('/Pygame/images/ball.png')

        # A Rect is made up of [x, y, width, height]
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height

        # max dimensions are to make sure that ball image allways stays in window.
        self.maxWidth = self.windowWidth - self.width
        self.maxHeight = self.windowHeight - self.height

        # Pick a random starting position
        self.x = random.randrange(self.maxWidth)
        self.y = random.randrange(self.maxHeight)

        # choose  a random speed -4 & 4, but not zero.
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # check for hitting a wall. If so, change that direction.
        if (self.x < 0) or (self.width >= self.windowWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.windowHeight):
            self.ySpeed = -self.xSpeed
        # Update the Ball's position
            self.x = self.x + self.xSpeed
            self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))

