import pygame
from pygame.sprite import Sprite

class Crusader(Sprite):
    "A class to represent the crusader"

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings


        self.image = pygame.image.load('assets/Crusader.png')
        self.rect = self.image.get_rect()

        # Starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the crusaders exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the crusader to the right or left"""
        self.x += (self.settings.crusader_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    def check_edges(self):
        """return true if crusader is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

