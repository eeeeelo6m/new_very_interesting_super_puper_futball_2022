import pygame
from pygame import draw


class Ball():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.object_rect = pygame.Rect(x-30, y-30, 60, 60)

    def draw(self, screen):
        draw.rect(screen,[0,0,0],self.object_rect)
        draw.circle(screen, [134, 255, 0], [self.x, self.y], 30)



    def dvigenie(self):

        self.object_rect.y-=3
        self.object_rect.x-=3
