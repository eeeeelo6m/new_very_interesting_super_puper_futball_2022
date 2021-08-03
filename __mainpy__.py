import pygame,ball as modul_ball,vorota,controller
from pygame import display,event,draw
pygame.init()
screen=display.set_mode([1150,600])
ball=modul_ball.Ball(50, 50)
vorota_right=vorota.Vorota(1120,0)
vorota_left=vorota.Vorota(0,0)
while True:
    controller.control()

    display.flip()
    screen.fill([100,100,100])



    ball.draw(screen)
    vorota_left.draw(screen)
    vorota_right.draw(screen)










