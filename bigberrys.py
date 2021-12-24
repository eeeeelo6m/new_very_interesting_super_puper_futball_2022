import pygame,help
from pygame import draw

class Bigberry ():
    def __init__(self,x,y):

        self.obect_bigberry=[x,y,40,40]


    def draw(self, screen:pygame.Surface):
        self.bigberry = pygame.image.load('picture/bigbaeri.png')
        self.bigberry = help.izmeni_kartinku(self.bigberry, 40, 40, [236, 28, 36], 120)


        screen.blit(self.bigberry,self.obect_bigberry)
