import pygame
import sys
import time

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

tower = pygame.image.load("assets/towerAlt.png")
tower_rect = tower.get_rect()
background = pygame.image.load("assets/backgroundColorGrass.png")
background_rect = background.get_rect()
screen_rect = screen.get_rect()

num_tiles = screen_rect.width // tower_rect.width
screen.blit(background, (0, 50))
screen.blit(tower, (400, 475))

#clock = pygame.tick.Clock()

pygame.init()
pygame.display.set_caption('Tower_Defense')

pygame.display.flip()
#clock.tick(60)
time.sleep(2)
