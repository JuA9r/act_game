"""

    Action game program

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


# window size
WIDTH: int = 800
HEIGHT: int = 600
_surface = pg.Rect(0, 0, 800, 600)

# block color
my_block = "white"
enemy_block = "fuchsia"

# player information
player_speed = 7
block_width = 50
block_height = 50

# number of enemy
num_enemies = 5

# game time
game_time = 30

# count down of time
Time = 3
message = "Start"


def start_timer(secs: any) -> None:

    """
        three seconds countdown to game start
    """

    for i in range(secs, -1, -1):
        print(i)
        sleep(1)
    print(message)
    return
start_timer(Time)


# player
class Player(pg.sprite.Sprite):

    """
        Player block generation
    """

    def __init__(self, width, height) -> None:
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(my_block)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-height-10))

    def update(self, keys, *args, **kwargs) -> None:
        self.rect.clamp_ip(_surface)

        if keys[pg.K_LEFT] and self.rect.left > 0:
            self.rect.x -= player_speed

        if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += player_speed

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)


# enemy
class Enemy(pg.sprite.Sprite):

    """
        Enemy block generation
    """

    def __init__(self, width, height, id) -> None:
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(enemy_block)
        self.id = id
        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), random.randint(0, HEIGHT)))
        self.enemy_speed = random.randint(7, 25)

    def update(self, *args, **kwargs) -> None:
        self.rect.y += self.enemy_speed

        if self.rect.top > HEIGHT:
            self.rect.y = random.randint(-HEIGHT, 0)
            self.rect.x = random.randint(0, WIDTH)
            self.enemy_speed = random.randint(7, 25)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)


# game countdown timer
class Timer(pg.sprite.Sprite):

    """
        Setting a time limit
    """

    def __init__(self) -> None:
        super().__init__()
        self.font = pg.font.Font(None, 36)
        self.start_time = pg.time.get_ticks()

    def update(self, *args, **kwargs) -> None: ...

    def draw(self, screen) -> None:
        elapsed_time = (pg.time.get_ticks() - game_time) // 1000
        remaining_time = max(game_time - elapsed_time, 0)
        timer_text = self.font.render("Time: " + str(remaining_time), True, "lime")
        # print(remaining_time)

        if elapsed_time == game_time + 1:
            print("\nGame clear")
            sys.exit()

        if remaining_time <= 10 and not remaining_time <= 5:
            timer_text = self.font.render("Time: " + str(remaining_time), True, "yellow")

        elif remaining_time <= 5:
            timer_text = self.font.render("Time: " + str(remaining_time), True, "crimson")

        else:
            pass

        screen.blit(timer_text, (10, 10))


# block collision
class block_collision(pg.sprite.Sprite):

    """
        Collision detection
    """

    def __init__(self, my_block, enemy_block) -> None:
        super().__init__()
        self.player = my_block
        self.enemies = enemy_block
        self.coll_count = 0

    def update(self, *args, **kwargs) -> None: ...

    def collision(self) -> None:
        for enemy in self.enemies:
            if pg.sprite.collide_rect(self.player, enemy):
                self.coll_count += 1
                print(f"\n collision: {self.coll_count}")
                enemy.kill()
                return True
        # print(self.coll_count)
        return False


class act_game:

    """
        Basic functions
    """

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Action game")
        self.clock = pg.time.Clock()
        self.player = Player(block_width, block_height)
        self.enemies = pg.sprite.Group()
        for i in range(num_enemies):
            enemy = Enemy(block_width, block_height, i)
            self.enemies.add(enemy)
        self._collision = block_collision(self.player, self.enemies)
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

            if self._collision.coll_count > 0:
                pass
                # print("collision")

            if self._collision.collision():
                if self._collision.coll_count == 3:
                    print("\nGame over")
                    break

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