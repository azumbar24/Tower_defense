import pygame
import sys
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

file = "sword_draw.mp3"

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
            # created a range for goblins to spawn
            for i in self.goblins:
                i.update()
            self._update_screen(score//60)
            self.clock.tick(60)
            score += 1


    def _create_goblin(self):
        """Create a goblin, if conditions are right."""
        # Every tick a random numb between 0-1 is generated.
        goblin_frequency = .004
        self.goblin_health = 100
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
        if event.key == pygame.K_SPACE and self.knight.cooldown == 0:
            self.knight.cooldown = 20
            slash = pygame.mixer.Sound(file)
            pygame.mixer.Sound.play(slash)
        if event.key == pygame.K_x and self.warrior.cooldown == 0:
            self.warrior.cooldown = 20
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

    def basic_health(self):
        # draw the health bar on the screen
        pygame.draw.rect(screen, (255,0,0), (150,80, self.current_health/self.health_ratio, 42))
        # draw the white border of the health bar
        pygame.draw.rect(screen, (0,0,0), (150,80,self.health_bar_length, 42), 4)
        font = pygame.font.SysFont("verdana", 36)
        health_img = font.render(f'Tower Health', True, (0, 0, 0))
        health_img_rect = health_img.get_rect()
        screen.blit(health_img, (240, 25))

    def draw_time(self, score):
        """Function that starts with a score then subtracts as time goes"""
        # display the score in the top right and change at every refresh. dynamic
        img = font.render(f'Score:{score * 100}', True, (0, 0, 255))
        screen.blit(img, (850, 50))

    def game_over(self):
        """shows game over screen"""
        global score
        screen.fill((255, 0, 0))
        #img = font.render(f'GAME OVER: Score: {score * 100}', True, (255, 255, 255))
        #img_rect = img.get_rect()
        #img_rect.center = screen.get_rect().center
        #screen.blit(img, img_rect)




    def _update_screen(self, score):
        global goblins
        # Update images on the screen, and flip to the new screen.
        self.screen.fill((0, 0, 0))
        screen.blit(background, (130, 20))
        screen.blit(tower, (600, 430))
        # method for deleting goblins, made an array and delete goblins from the right
        # that way they don't flicker when they reach the tower, removes 5 health points from the tower for every gob
        for j in range(len(self.goblins) - 1, -1, -1):
            i = self.goblins[j]
            i.blitme()
            # established terms for what x destination goblins need to reach to damage tower
            if (i.x > 560 and i.speed == 1.8) or (i.x < 620 and i.speed == -1.8):
                self.goblins.remove(i)
                self.current_health -= 10
            # made a slight pause for in between swings to kill gobs, 20 ticks, range of = or - 20
            # pixels from ech character
            elif(self.warrior.cooldown == 20 and i.x - self.warrior.x >= -50 and i.x - self.warrior.x <= 50):
                self.goblins.remove(i)
            elif(self.knight.cooldown == 20 and i.x - self.knight.x >= -50 and i.x - self.knight.x <= 50):
                self.goblins.remove(i)
        # ticker for how long the cooldown should last
        if(self.knight.cooldown > 0):
            self.knight.cooldown -= 1
        if(self.warrior.cooldown > 0):
            self.warrior.cooldown -= 1
        self.warrior.blitme()
        self.knight.blitme()
        self.basic_health()
        self.draw_time(score)
        if self.current_health == 0:
            self.game_over()

        # make the most recently drawn screen visible.
        pygame.display.update()



if __name__=='__main__':
    # make a game instance, and run the game.
    ai = TowerDefense()
    ai.run_game()
