import pygame,model,random,schet
from pygame import display

def skrin_3(screen):
    schet.schet_mones()
    screen.fill([45,134,252])
    screen.blit(schet.schet_mone_left_kartinka,[30,0])
    screen.blit(schet.schet_mone_right_kartinka,[1090,0])
    display.flip()