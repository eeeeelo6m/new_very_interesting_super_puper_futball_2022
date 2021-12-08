import pygame, model
from pygame import time

timer_pereriv = None



def control():


    e = pygame.event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type == pygame.KEYDOWN and r.key == pygame.K_ESCAPE:

            model.smena_regima_standard()


        if timer_pereriv == r.type:
            model.umenshit_timer_pereriv()
            pygame.time.set_timer(timer_pereriv, 1000, 1)


def start_regima():
    global timer_pereriv
    timer_pereriv = pygame.event.custom_type()
    pygame.time.set_timer(timer_pereriv, 1000, 1)
