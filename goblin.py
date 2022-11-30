import pygame

class Goblin:

    def __init__(self, ai_game):
        """Goblins starting position"""
        self.screen = ai_game.screen
        self.speed = 2

        # Loading the goblin image
        self.image = pygame.image.load('assets/goblin.png')
        self.rect = self.image.get_rect()

        # Goblin's starting position is at the middle bottom of the screen
        self.rect.midbottom = self.screen.get_rect().midbottom

        # store a decimal value for the knights horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on movement flag"""
        # Update the goblin's x value, not the rect
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the goblin at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_goblin(self):
        """center the goblin on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
