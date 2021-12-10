import model,pygame
from pygame import time


def control():


    e = pygame.event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()

        if r.type == pygame.KEYDOWN and r.key == pygame.K_ESCAPE:
            model.smena_regima_pereriv(False)

