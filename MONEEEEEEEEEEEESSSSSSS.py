import pygame,random,time
moneeeeeeessss=[]
mone=0

TIMER_DELETE_MONES = pygame.event.custom_type()


def make_moneeesss():
    global mone
    moneess={'RECT':pygame.Rect(random.choice([200,920]),random.randint(0,590),30,30),'time':time.time()}
    moneeeeeeessss.append(moneess)
    pygame.time.set_timer(TIMER_DELETE_MONES,3000,1)

    mone+=1


def delete_mones():
    for mane in moneeeeeeessss:
        a=time.time()-mane['time']
        if a>=3:
            moneeeeeeessss.remove(mane)

