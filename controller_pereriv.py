import pygame, model
from pygame import time

timer_pereriv = None


def control():
    global timer_pereriv
    if timer_pereriv == None:
        timer_pereriv = pygame.event.custom_type()
        pygame.time.set_timer(timer_pereriv, 1000, 1)
    e = pygame.event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_ESCAPE:
            model.gamemod = 'standard'
            model.make_ball()

        if timer_pereriv == r.type:
            model.improvizirovanny_timer -= 1
            pygame.time.set_timer(timer_pereriv, 1000, 1)
