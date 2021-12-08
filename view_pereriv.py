import pygame,model,random
from pygame import display

def skrin_2(screen):

    timer = shrift_pereriva.render(str(model.improvizirovanny_timer), True, [0, 0, 0])
    screen.fill([random.randint(0, 255), random.randint(0, 255), random.randint(255, 255)])
    screen.blit(timer, [500, 300])
    display.flip()





shrift_pereriva = pygame.font.SysFont('comicsansms', 200)
