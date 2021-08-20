import pygame
from pygame import draw


class Igroc():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obect_igroc = pygame.Rect(self.x, self.y, 30, 150)

    def draw(self, screen):
        draw.rect(screen, [0, 136, 255], self.obect_igroc)

    def go_up(self):
        self.obect_igroc.y-=7
        if self.obect_igroc.y <= 0:
            self.obect_igroc.y = 7

    def go_down(self):
        self.obect_igroc.bottom += 7
        if self.obect_igroc.bottom>=600:
            self.obect_igroc.bottom=600


