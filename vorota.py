import pygame
from pygame import draw


class Vorota():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.obect_vorota=pygame.Rect(self.x,self.y,30,1150)

    def draw(self,screen):
        draw.rect(screen,[255,0,120],self.obect_vorota)
