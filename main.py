"""

    action game program

"""

# import pygame
import pygame as pg
from pygame import *

# import random
import random

# import sys
import sys

# import sleep
from time import sleep


WIDTH = 800
HEIGHT = 600
_surface = Rect(0, 0, 800, 600)

# block color
my_block = "white"
enemy_Block = "red"

# Number of collisions
coll_count = 0

# count down of time
Time = 3
message = "Start"


def start_timer(secs : any) -> None:

    """
        three seconds countdown to game start
    """

    for i in range(secs, -1, -1):
        print(i)
        sleep(1)
    print(message)
    return
start_timer(Time)


class act_game:

    """
        generate act_game class
    """

    # player
    class player(pg.sprite.Sprite):
        def __init__(self, player_width, player_height):
            super().__init__()
            self.player_width = 50
            self.player_height = 50
            self.player_x = WIDTH // 2 - player_width // 2
            self.player_y = HEIGHT - player_height - 10
            self.player_speed = 5

        def update(self, *args, **kwargs):
            self.rect.clamp_ip(_surface)

            if keys[pg.K_LEFT]:
                self.player_x -= self.player_speed

            elif keys[pg.K_RIGHT]:
                self.player_x += self.player_speed

            elif keys[pg.K_UP]:
                self.player_y -= self.player_speed

            elif keys[pg.K_DOWN]:
                self.player_y += self.player_speed

            else:
                pass

        def draw(self):
            pg.draw.rect(screen, enemy_Block,
                         (player_x, player_y, player_width, player_height))

    # enemy
    class enemy(pg.sprite.Sprite):
        def __init__(self):
            super().__init__()
            num_enemy = 5
            _enemy = []
            for _ in range(num_enemy):
                enemy_x = random.randint(0, WIDTH - player_width)
                enemy_y = random.randint(-HEIGHT, 0)
                enemy_speed = random.randint(1, 5)
                _enemy.append([enemy_x, enemy_y, enemy_speed])

        def update(self, *args, **kwargs):
            self.rect.clamp_ip(_surface)
            self.enemy_y += self.enemy_speed

        def draw(self):
            for _enemy in enemies:
                pg.draw.rect(screen, my_block,
                             (_enemy[0], _enemy[1], player_width, player_height))

    # timer
    class timer(pg.sprite.Sprite):
        def __init__(self, font, start_time, time_limit):
            super().__init__()
            self.font = pg.font.Font(None, 36)
            self.start_time = pg.time.get_ticks()
            self.time_limit = 120

        def update(self, *args, **kwargs):
            pass

        def draw(self):
            rem_time = max(time_limit - elapsed_time, 0)
            timer_text = font.render("Time: " + str(rem_time), True, my_block)
            screen.blit(timer_text, (10, 10))


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("action game")
    screen.fill((0, 0, 0))

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

        pg.display.update()

        clock = pg.time.Clock()
        clock.tick(60)

if __name__ == "__main__":
    main()
