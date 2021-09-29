import pygame,random
moneeeeeeessss=[]
mone=0
def make_moneeesss():
    global mone
    moneeeeeeessss.append(pygame.Rect(random.choice([200,920]),random.randint(0,590),20,20))
    mone+=1
