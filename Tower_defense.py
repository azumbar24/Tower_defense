import pygame
import sys
import time
from knight import Knight

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

tower = pygame.image.load("assets/towerAlt.png")
tower_rect = tower.get_rect()
background = pygame.image.load("assets/backgroundColorGrass.png")
background_rect = background.get_rect()
knight = pygame.image.load("assets/Knight.png")
knight_rect = knight.get_rect()
knight1 = pygame.image.load("assets/Knight1.png")
knight1_rect = knight1.get_rect()

screen_rect = screen.get_rect()

num_tiles = screen_rect.width // tower_rect.width
screen.blit(background, (0, 50))
screen.blit(tower, (400, 475))
screen.blit(knight, (500, 600))
screen.blit(knight1, (300, 600))


class TowerDefense:
    def _check_events(self):
        """Respond to keypresses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.knight.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
            """Respond to releases."""
            if event.key == pygame.K_RIGHT:
                self.knight.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.knight.moving_left = False






#clock = pygame.tick.Clock()

pygame.init()
pygame.display.set_caption('Tower_Defense')

pygame.display.flip()
#clock.tick(60)
time.sleep(7)

