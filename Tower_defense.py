import pygame
import sys
import time
from knight import Knight
from warrior import Warrior
from settings import Settings
from goblin import Goblin
from random import *

pygame.init()

clock = pygame.time.Clock()

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

tower = pygame.image.load("assets/towerAlt.png")
tower_rect = tower.get_rect()
background = pygame.image.load("assets/backgroundColorGrass.png")
background_rect = background.get_rect()
font = pygame.font.SysFont("verdana", 48)
goblins = pygame.sprite.Group()
screen_rect = screen.get_rect()

num_tiles = screen_rect.width // tower_rect.width


class TowerDefense:

    def __init__(self):
        """Initializing the game, and create game resources."""
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.current_health = 100
        self.health_bar_length = 400
        self.health_ratio = self.current_health / self.health_bar_length
        self.goblins = []

        pygame.display.set_caption("Tower Defense")

        self.warrior = Warrior(self)
        self.knight = Knight(self)

    def run_game(self):
        """Start the main loop for the game"""
        score = 0
        while True:
            self._check_events()
            self.warrior.update()
            self.knight.update()
            self._create_goblin()
            for i in self.goblins:
                i.update()
            self._update_screen(score//60)
            self.clock.tick(60)
            score += 1


    def _create_goblin(self):
        """Create a goblin, if conditions are right."""
        # Every tick a random numb between 0-1 is generated.
        goblin_frequency = .004
        if random() < goblin_frequency:
            # assign variables for fan functions
            self.goblins.append(Goblin(self))


    def _check_events(self):
        """Respond to key presses"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_d:
            self.warrior.moving_right = True
        elif event.key == pygame.K_a:
            self.warrior.moving_left = True
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.knight.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
            """Respond to releases."""
            if event.key == pygame.K_d:
                self.warrior.moving_right = False
            elif event.key == pygame.K_a:
                self.warrior.moving_left = False
            if event.key == pygame.K_RIGHT:
                self.knight.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.knight.moving_left = False


    def get_damage(self, amount):
      if self.current_health > 0:
        self.current_amount -= amount
      if self.current_health <= 0:
        self.current_health = 0
    def basic_health(self):
        # draw the health bar on the screen
        pygame.draw.rect(screen, (255,0,0), (150,80, self.current_health/self.health_ratio, 42))
        # draw the white border of the health bar
        pygame.draw.rect(screen, (0,0,0), (150,80,self.health_bar_length, 42), 4)
        font = pygame.font.SysFont("verdana", 36)
        health_img = font.render(f'Health', True, (0, 0, 0))
        health_img_rect = health_img.get_rect()
        screen.blit(health_img, (290, 25))

    def draw_time(self, score):
        """Function that starts with a score then subtracts as time goes"""
        # display the score in the top right and change at every refresh. dynamic
        img = font.render(f'Score:{score * 100}', True, (0, 0, 255))
        screen.blit(img, (850, 50))

    def _update_screen(self, score):
        global goblins
        # Update images on the screen, and flip to the new screen.
        self.screen.fill((0, 0, 0))
        screen.blit(background, (130, 20))
        screen.blit(tower, (600, 430))
        self.warrior.blitme()
        for i in self.goblins:
            i.blitme()
        self.knight.blitme()
        self.basic_health()
        self.draw_time(score)
        # make the most recently drawn screen visible.
        pygame.display.update()



if __name__=='__main__':
    # make a game instance, and run the game.
    ai = TowerDefense()
    ai.run_game()
