import pygame

class Knight:

    def __init__(self, ai_game):
        """Knights starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading the knight image
        self.image = pygame.image.load('assets/Knight.bmp')
        self.rect = self.image.get_rect()

        # knight's starting position is at the middle bottom of the screen
        self.rect.midbottom = self.screen.get_rect().midbottom

        # store a decimal value for the knights horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on movement flag"""
        # Update the knight's x value, not the rect
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the knight at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_knight(self):
        """center the knight on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
