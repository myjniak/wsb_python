import math
import random
from time import time

import pygame

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("eh")

clock = pygame.time.Clock()
pygame.init()


def reevaluate_pos_and_speed(x, y, vx, vy):
    vx += random.uniform(-4, 4)
    vy += random.uniform(-4, 4)

    if x > 600-25 or x < 0+25:
        vx = -vx
    if y > 600-25 or y < 0+25:
        vy = -vy
    vx *= 0.9
    vy *= 0.9
    return vx, vy


class Progress:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

    def get_color(self, x, y):
        if x >= 575 and 0 <= y <= 600:
            self.right = True
        if x <= 25 and 0 <= y <= 600:
            self.left = True
        if 0 <= x <= 600 and y <= 25:
            self.up = True
        if 0 <= x <= 600 and y >= 575:
            self.down = True
        return 255 * [self.up, self.right, self.down, self.left].count(True) // 4


def main():
    vx = 0
    vy = 0
    x = 300
    y = 300
    start = time()
    time_passed = 0
    progress = Progress()
    font = pygame.font.SysFont('Consolas', 30)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        vx, vy = reevaluate_pos_and_speed(x, y, vx, vy)
        x += vx
        y += vy
        pygame.display.update()
        screen.fill((255, 255, 255))
        color = progress.get_color(x, y)

        pygame.draw.rect(screen, (0, color, 0), (x - 25, y - 25, 50, 50))

        clock.tick(50)
        if color != 255:
            time_passed = time() - start
            screen.blit(font.render("{:.2f}".format(time_passed) + "s", True, (0, 0, 0)), (50, 50))
        else:
            screen.blit(font.render("{:.2f}".format(time_passed) + "s" + " You win!!!", True, (0, 0, 0)), (50, 50))


main()

