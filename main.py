"""

    action game program

"""

# import pygame
import pygame as pg
from pygame.locals import *

# import random
import random

# import sys
import sys

# import sleep
from time import sleep


WIDTH = 800
HEIGHT = 600
_surface = pg.Rect(0, 0, 800, 600)

# block color
my_block = "white"
enemy_Block = "magenta"

# player information
player_speed = 5
block_width = 50
block_height = 50

# number of enemy
num_enemies = 4

# count down of time
Time = 3
message = "Start"


# def start_timer(secs : any) -> None:
#
#     """
#         three seconds countdown to game start
#     """
#
#     for i in range(secs, -1, -1):
#         print(i)
#         sleep(1)
#     print(message)
#     return
# start_timer(Time)


# player
class Player(pg.sprite.Sprite):

    """
        Player block generation
    """

    def __init__(self, width, height) -> None:
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(my_block)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - height - 10))

    def update(self, keys) -> None:
        self.rect.clamp_ip(_surface)

        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed

        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += player_speed

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)


class Enemy(pg.sprite.Sprite):

    """
        Enemy block generation
    """

    def __init__(self, width, height) -> None:
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(enemy_Block)
        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.enemy_speed = random.randint(5, 23)

    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.enemy_speed

        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-HEIGHT, 0)
            self.rect.x = random.randint(0, WIDTH)
            self.enemy_speed = random.randint(5, 23)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)


# timer
class Timer(pg.sprite.Sprite):

    """
        Setting a time limit
    """

    def __init__(self) -> None:
        super().__init__()
        self.font = pg.font.Font(None, 36)
        self.start_time = pg.time.get_ticks()
        self.time_limit = 60

    def update(self, *args, **kwargs) -> None:
        pass

    def draw(self, screen) -> None:
        elapsed_time = (pg.time.get_ticks() - self.start_time) // 1000
        remaining_time = max(self.time_limit - elapsed_time, 0)
        timer_text = self.font.render("Time: " + str(remaining_time), True, my_block)
        screen.blit(timer_text, (10, 10))


class act_game:
    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("action game")
        self.clock = pg.time.Clock()
        self.player = Player(block_width, block_height)
        self.enemies = pg.sprite.Group()
        for _ in range(num_enemies):
            enemy = Enemy(block_width, block_height)
            self.enemies.add(enemy)
        self.timer = Timer()

    def running(self) -> None:
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True

            keys = pg.key.get_pressed()
            self.player.update(keys)

            self.enemies.update()

            self.screen.fill("black")
            self.player.draw(self.screen)
            self.enemies.draw(self.screen)
            self.timer.draw(self.screen)

            pg.display.update()
            self.clock.tick(60)

        pg.quit()
        sys.exit()


def main():
    game = act_game()
    game.running()


if __name__ == "__main__":
    main()