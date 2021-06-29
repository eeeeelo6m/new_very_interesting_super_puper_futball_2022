import pygame,ball
from pygame import display,event,draw
pygame.init()
screen=display.set_mode([500,500])
a=ball.Ball(50,50)
b=ball.Ball(100,100)
while True:
    event.get()
    display.flip()
    screen.fill([100,100,100])



    a.draw_ball(screen)
    b.draw_ball(screen)