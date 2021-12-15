import pygame,model,random,schet
from pygame import display,draw
SHIRINA_NIGNEY_PANELI=525
shrift_pomogalca= pygame.font.SysFont('vinerhanditc',50)
pomogalka = shrift_pomogalca.render('press Esc to quite shop', True, [0, 0, 0])

def skrin_3(screen:pygame.Surface):
    schet.schet_mones()
    screen.fill([45,134,252])
    screen.blit(schet.schet_mone_left_kartinka,[30,0])
    screen.blit(schet.schet_mone_right_kartinka,[1090,0])
    screen.blit(pomogalka,[200,525])

    b=screen.get_width()
    draw.line(screen, [0,0,0], [b/2,0], [b / 2, SHIRINA_NIGNEY_PANELI], 8)
    draw.line(screen, [0,0,0], [0, SHIRINA_NIGNEY_PANELI], [b, SHIRINA_NIGNEY_PANELI], 8)
    draw.line(screen,[0,0,0],[0,0],[b,0],16)


    display.flip()