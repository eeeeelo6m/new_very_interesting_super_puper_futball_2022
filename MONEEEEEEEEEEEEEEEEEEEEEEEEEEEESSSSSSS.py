import pygame,random
moneeeeeeessss=[]
mone=0
def make_moneeesss():
    global mone
    moneeeeeeessss.append(pygame.Rect(random.choice([200,920]),random.randint(0,590),30,30))
    mone+=1
a={'name':'Andrey', 'age':12}
b={'name':'Vova','age':1}
c=[a,b]
a['age']=13
del b
for b in c:
    b['age']+=1
    b['year']=2021- b['age']


