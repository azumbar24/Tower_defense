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
crusader = pygame.image.load("assets/Crusader.png")
crusader_rect = crusader.get_rect()
crusader1 = pygame.image.load("assets/Crusader1.png")
crusader1_rect = crusader1.get_rect()

screen_rect = screen.get_rect()

num_tiles = screen_rect.width // tower_rect.width
screen.blit(background, (0, 50))
screen.blit(tower, (400, 475))
screen.blit(crusader, (500, 600))
screen.blit(crusader1, (300, 600))


while True:
        # checking for user inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print('left')
            if event.key == pygame.K_RIGHT:
                print('right')
            if event.key == pygame.K_UP:
                print('jump')

        if event.type == pygame.QUIT:
            sys.exit()



#clock = pygame.tick.Clock()

pygame.init()
pygame.display.set_caption('Tower_Defense')

pygame.display.flip()
#clock.tick(60)
time.sleep(5)
