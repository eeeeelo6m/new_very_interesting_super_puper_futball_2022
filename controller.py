import pygame, model, random, ball as modul_ball, MONEEEEEEEEEEEESSSSSSS
from pygame import key

pygame.init()
TIMER_POYVLENIY_BALL = pygame.event.custom_type()
TIMER_POYVLENIY_MONES = pygame.event.custom_type()



def start_timer_ball():
    pygame.time.set_timer(TIMER_POYVLENIY_BALL, 10000, 1)


pygame.time.set_timer(TIMER_POYVLENIY_MONES, random.randint(3000,5000), 1)


def control():
    e = pygame.event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type == TIMER_POYVLENIY_BALL:
            model.make_ball()

        if MONEEEEEEEEEEEESSSSSSS.TIMER_DELETE_MONES==r.type:
            MONEEEEEEEEEEEESSSSSSS.delete_mones()
            MONEEEEEEEEEEEESSSSSSS.delete_mones()
            MONEEEEEEEEEEEESSSSSSS.delete_mones()
        if r.type == TIMER_POYVLENIY_MONES and MONEEEEEEEEEEEESSSSSSS.mone != 10:
            MONEEEEEEEEEEEESSSSSSS.make_moneeesss()
            pygame.time.set_timer(TIMER_POYVLENIY_MONES, random.randint( 3000,5000), 1)

    keys = key.get_pressed()
    if keys[pygame.K_w]:
        model.igroc_left.go_up()
    if keys[pygame.K_s]:
        model.igroc_left.go_down()
    if keys[pygame.K_UP]:
        model.igroc_right.go_up()
    if keys[pygame.K_DOWN]:
        model.igroc_right.go_down()
