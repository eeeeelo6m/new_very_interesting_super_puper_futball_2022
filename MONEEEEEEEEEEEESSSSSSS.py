import pygame,random,time,igroc
mones=[]
mone_count=0

TIMER_DELETE_MONES = pygame.event.custom_type()


def make_mones(igroc_left,igroc_right):
    global mone_count
    mone_dict={'RECT':pygame.Rect(random.choice([200,920]),random.randint(237,237),30,30),'time':time.time()}
    while igroc_left.obect_igroc.colliderect(mone_dict['RECT']) or igroc_right.obect_igroc.colliderect(mone_dict['RECT']):
        mone_dict['RECT'].y=random.randint(0,590)
    mones.append(mone_dict)
    pygame.time.set_timer(TIMER_DELETE_MONES,3000,1)

    mone_count+=1


def delete_mones():
    for mane in mones:
        a=time.time()-mane['time']
        if a>=3:
            mones.remove(mane)




