import pygame
pygame.init()

def control():
    e = pygame.event.get()
    for r in e:
        print(r)
        if r.type==pygame.QUIT:
            exit()



