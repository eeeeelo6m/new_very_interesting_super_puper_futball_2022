import pygame,model,random
from pygame import display

def skrin_2(screen):
    screen.fill([12,31,255])
    display.flip()
    screen.fill([19, 179, 81])
    for b in range(6000, 0, -1):
        timer = shrift_pereriva.render(str(model.improvizirovanny_timer), True, [0, 0, 0])
        screen.blit(timer, [500, 300])
        display.flip()
        screen.fill([random.randint(0, 255), random.randint(0, 255), random.randint(255, 255)])

    model.gamemod='standard'




shrift_pereriva = pygame.font.SysFont('comicsansms', 200)
