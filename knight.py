import pygame

class Knight:

    def __init__(self, ai_game):
        """Knights starting position"""
        self.screen = ai_game.screen
        self.speed = 3
        self.cooldown = 0
        self.face_right = True

        # Loading the knight image
        self.image = pygame.image.load('assets/Knight.png')
        self.rect = self.image.get_rect()

        # knight's starting position is at the middle bottom of the screen
        self.rect.midbottom = self.screen.get_rect().midbottom

        # store a decimal value for the knights horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the knights position based on movement flag"""
        # Update the knight's x value, not the rect
        # determines which way the knight will face given certain criteria
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.face_right = True
            self.x += self.speed
            self.image = pygame.image.load('assets/Knight.png')
        if self.moving_left and self.rect.left > 0:
            self.face_right = False
            self.x -= self.speed
            self.image = pygame.image.load('assets/Knight1.png')
        # establishes which slashing pic to use when facing a certain direction
        if self.cooldown > 0:
            if self.face_right:
                self.image = pygame.image.load('assets/knight_slashing.png')
            else:
                self.image = pygame.image.load('assets/knight_slashing1.png')
        else:
            if self.face_right:
                self.image = pygame.image.load('assets/Knight.png')
            else:
                self.image = pygame.image.load('assets/Knight1.png')

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the knight at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_knight(self):
        """center the knight on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
