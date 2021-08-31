import pygame, controller, model, time,schet
from pygame import display, event, draw

pygame.init()
screen = display.set_mode([1150, 600])

while True:
    time.sleep(1 / 60)
    controller.control()
    model.step()

    screen.fill([0, 0, 0])
    if model.ball!=None:
        model.ball.draw(screen)
    if model.wiiiiiin==1:
        screen.blit(schet.wiiiiiiiiin,[1150/2,300])
        display.flip()
        time.sleep(3)
        exit()
    # model.ball2.draw(screen)
    model.vorota_left.draw(screen)
    model.vorota_right.draw(screen)
    model.igroc_left.draw(screen)
    model.igroc_right.draw(screen)

    screen.blit(schet.schet,[30,0])
    screen.blit(schet.schet2,[1090,0])

    draw.circle(screen,[255,0,0],[1150/2,600/2],1)
    display.flip()