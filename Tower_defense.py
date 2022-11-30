import pygame
import sys
import time
from knight import Knight
from goblin import Goblin
from settings import Settings

TILE_SIZE = 64
WINDOW_SIZE = 15 * TILE_SIZE
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
#clock = pygame.tick.Clock()
#clock.tick(60)

tower = pygame.image.load("assets/towerAlt.png")
tower_rect = tower.get_rect()
background = pygame.image.load("assets/backgroundColorGrass.png")
background_rect = background.get_rect()


screen_rect = screen.get_rect()

num_tiles = screen_rect.width // tower_rect.width

# self.current_health = 100
# self.health_bar_length = 200
# self.health_ratio = self.current_health / self.health_bar_length
# def get_damage(self, amount):
    # if self.current_health > 0:
        # self.current_amount -= amount
    # if self.current_health <= 0:
        # self.current_health = 0

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
        self.goblin = Goblin(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

            self.knight.update()
            self.goblin.update()
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

        #collision = pygame.sprite.collide_rect(Goblin, tower)
        #if collision:
            #tower.health = tower.health - 1
            #print(f"Collision: tower health={ship.health}!!")

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.knight.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.knight.moving_left = True
        if event.key == pygame.K_d:
            self.goblin.moving_right = True
        elif event.key == pygame.K_a:
            self.goblin.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
            """Respond to releases."""
            if event.key == pygame.K_RIGHT:
                self.knight.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.knight.moving_left = False
            if event.key == pygame.K_d:
                self.goblin.moving_right = False
            elif event.key == pygame.K_a:
                self.goblin.moving_left = False

    def _update_screen(self):
        # Update images on the screen, and flip to the new screen.
        self.knight.blitme()
        self.goblin.blitme()

        # make the most recently drawn screen visible.
        pygame.display.flip()



if __name__=='__main__':
    #make a game instance, and run the game.
    ai = TowerDefense()
    ai.run_game()
