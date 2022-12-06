import pygame

class Warrior:

    def __init__(self, ai_game):
        """Warrior's starting position"""
        self.screen = ai_game.screen
        self.speed = 2
        self.cooldown = 0
        self.face_right = True

        # Loading the warrior image
        self.image = pygame.image.load('assets/Warrior.png')
        self.rect = self.image.get_rect()

        # Warrior's starting position is at the middle bottom of the screen
        self.rect.midbottom = self.screen.get_rect().midbottom

        # store a decimal value for the warriors horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the warriors position based on movement flag"""
        # Update the warrior's x value, not the rect
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.face_right = True
            self.x += self.speed
            self.image = pygame.image.load('assets/Warrior.png')
        if self.moving_left and self.rect.left > 0:
            self.face_right = False
            self.x -= self.speed
            self.image = pygame.image.load('assets/Warrior1.png')
        if self.cooldown > 0:
            if self.face_right:
                self.image = pygame.image.load('assets/warrior_slashing.png')
            else:
                self.image = pygame.image.load('assets/warrior_slashing1.png')
        else:
            if self.face_right:
                self.image = pygame.image.load('assets/Warrior.png')
            else:
                self.image = pygame.image.load('assets/Warrior1.png')

        # Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw the warrior at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_warrior(self):
        """center the warrior on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
