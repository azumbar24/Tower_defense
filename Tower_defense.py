import pygame
import sys
import time
from knight import Knight
from settings import Settings

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

#screen.blit(knight, (500, 600))
screen.blit(knight1, (300, 600))


class TowerDefense:

    def __init__(self):
        """Initializing the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Tower Defense")

        self.knight = Knight(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            self.knight.update()
            screen.blit(background, (130, 20))
            screen.blit(tower, (600, 430))
            self._update_screen()

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

    def _update_screen(self):
        # Update images on the screen, and flip to the new scren.
        self.knight.blitme()

        # make the most recently drawn screen visisble.
        pygame.display.flip()




    # clock = pygame.tick.Clock()
    # clock.tick(60)

if __name__=='__main__':
    #make a game instance, and run the game.
    ai = TowerDefense()
    ai.run_game()
