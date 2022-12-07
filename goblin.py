import pygame
from random import randint

class Goblin:

    def __init__(self, ai_game):
        # inits the sprite settings, collisions do not work without this
        self.screen = ai_game.screen
        # set screen settings
        self.screen_rect = self.screen.get_rect()
        # set the speed, speed is negative for goblins on the right and vice versa
        self.image = pygame.image.load("assets/goblin.png")
        self.rect = self.image.get_rect()
        # Store a decimal value for the goblins horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # set where the goblins start on the screen, these start at the bottom, but randomly spawn on right or left
        self.y = 620
        # speed rate increases by a factor over 3000 score point
        self.speed = -(1.2 + ai_game.score / 3000)
        self.x = 1100
        # health increase for a factor over 3000 score points, had to draw from the score in the main
        self.health = 1 + ai_game.score // 3000
        # random spawning, had to watch a tutorial to fully understand
        if randint(0, 1) == 0:
            self.speed = 1.2 + ai_game.score / 3000
            self.x = 100
            self.image = pygame.image.load("assets/goblin1.png")

    def update(self):
        """Update the location of the goblins based on their x and y speeds"""
        self.x += self.speed
        # Update rect object from self.x and y
        self.rect.x = self.x
        self.rect.y = self.y
    def blitme(self):
        """Draw the goblin at its current location."""
        self.screen.blit(self.image, self.rect)