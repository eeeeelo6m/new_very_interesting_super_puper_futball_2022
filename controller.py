import pygame, model, random, ball as modul_ball, MONEEEEEEEEEEEESSSSSSS
from pygame import key

pygame.init()
TIMER_POYVLENIY_BALL = pygame.event.custom_type()
TIMER_POYVLENIY_MONES = pygame.event.custom_type()
TIMER_ZAPUSKA_BALL=pygame.event.custom_type()


def start_timer_ball():
    pygame.time.set_timer(TIMER_POYVLENIY_BALL, 3000, 1)



def start_timer_zapuska_ball():
    pygame.time.set_timer(TIMER_ZAPUSKA_BALL,2000,1)




pygame.time.set_timer(TIMER_POYVLENIY_MONES, random.randint(3000,5000), 1)
start_timer_ball()

def control():
    e = pygame.event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()


        if r.type == TIMER_POYVLENIY_BALL:
            model.make_ball()
            start_timer_zapuska_ball()

        if TIMER_ZAPUSKA_BALL==r.type:
            model.zapusc_ball()

        if MONEEEEEEEEEEEESSSSSSS.TIMER_DELETE_MONES==r.type:
            MONEEEEEEEEEEEESSSSSSS.delete_mones()

        if r.type == TIMER_POYVLENIY_MONES and MONEEEEEEEEEEEESSSSSSS.mone_count != 10:
            model.make_mones()
            pygame.time.set_timer(TIMER_POYVLENIY_MONES, random.randint( 3000,5000), 1)


    keys = key.get_pressed()
    if keys[pygame.K_w]:
        model.igroc_left.go_up()
        model.sobiranie_mones()
    if keys[pygame.K_s]:
        model.sobiranie_mones()
        model.igroc_left.go_down()
    if keys[pygame.K_UP]:
        model.igroc_right.go_up()
        model.sobiranie_mones()
    if keys[pygame.K_DOWN]:
        model.igroc_right.go_down()
        model.sobiranie_mones()
