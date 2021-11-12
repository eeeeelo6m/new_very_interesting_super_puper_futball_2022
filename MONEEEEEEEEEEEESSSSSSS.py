import pygame,random,time,igroc
mones=[]
mone_count=0

TIMER_DELETE_MONES = pygame.event.custom_type()


def make_mones():
    global mone_count
    mone_dict={'RECT':pygame.Rect(random.choice([200,920]),random.randint(0,590),30,30),'time':time.time()}
    mones.append(mone_dict)
    pygame.time.set_timer(TIMER_DELETE_MONES,3000,1)

    mone_count+=1


def delete_mones():
    for mane in mones:
        a=time.time()-mane['time']
        if a>=3:
            mones.remove(mane)




