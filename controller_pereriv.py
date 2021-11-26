import  pygame,model
from pygame import time
TIMER_PERERIV=pygame.event.custom_type()
def control():
    e = pygame.event.get()

    for r in e:

        if r.type == pygame.QUIT:
            exit()
        if r.type==pygame.KEYDOWN and r.key==pygame.K_ESCAPE:
            model.gamemod='standard'

        if TIMER_PERERIV==r.type:
            model.improvizirovanny_timer-=1


