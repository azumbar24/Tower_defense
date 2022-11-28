import pygame
from pygame.sprite import Sprite

class Goblin(Sprite):
    "A class to represent a goblin"

    def __init__(self, ai_game):
        "Initializing the goblin and set its starting position"
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the goblin image and set its rect attribute
        self.image = pygame.image.load('assets/goblin.png')
        self.rect = self.image.get_rect()

        #Start each goblin near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the goblin exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the goblin to the right or left"""
        self.x -= 1
        self.rect.x = self.x
    def check_edges(self):
        """return true if goblin is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
