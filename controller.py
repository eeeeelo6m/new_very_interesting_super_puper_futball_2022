import pygame, model, time
from pygame import key

pygame.init()


def control():
    e = pygame.event.get()
    for r in e:

        if r.type == pygame.QUIT:
            exit()

    keys = key.get_pressed()
    if keys[pygame.K_w]:
        model.igroc_left.go_up()
    if keys[pygame.K_s]:
        model.igroc_left.go_down()

    if keys[pygame.K_UP]:
        model.igroc_right.go_up()
