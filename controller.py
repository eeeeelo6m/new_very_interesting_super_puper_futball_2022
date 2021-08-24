import pygame, model, random, ball as modul_ball
from pygame import key

pygame.init()
TIMER_POYVLENIY_BALL = pygame.event.custom_type()
def start_timers():
    pygame.time.set_timer(TIMER_POYVLENIY_BALL, 10000, 1)


def control():
    e = pygame.event.get()
    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type == TIMER_POYVLENIY_BALL:
            model.make_ball()

    keys = key.get_pressed()
    if keys[pygame.K_w]:
        model.igroc_left.go_up()
    if keys[pygame.K_s]:
        model.igroc_left.go_down()
    if keys[pygame.K_UP]:
        model.igroc_right.go_up()
    if keys[pygame.K_DOWN]:
        model.igroc_right.go_down()
