import pygame
from pygame.sprite import Sprite
from random import randint
import math

"""
TILE_SIZE = 64
WINDOW_WIDTH = 14 * TILE_SIZE
WINDOW_HEIGHT = 8 * TILE_SIZE
goblin_frequency = .005
"""
class Goblin:
    def __init__(self, ai_game):
        # inits the sprite settings, collisions do not work without this
        self.screen = ai_game.screen
        # set screen settings
        self.screen_rect = self.screen.get_rect()
        # load image and get the rect
        self.image = pygame.image.load("assets/goblin.png")
        self.rect = self.image.get_rect()
        #set the speed
        self.speed = .2 if randint(0, 1) == 0 else -0.2

        # Store a decimal value for the goblins horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # set where the goblins start on the screen, these start at the bottom, but randomly spawn on right or left
        self.y = 620
        self.x = 1100 if (self.speed == .2) else 100


    def update(self):
        """Update the location of the goblins based on their x and y speeds"""
        self.x -= self.speed

        # Update rect object from self.x and y
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the goblin at its current location."""
        self.screen.blit(self.image, self.rect)