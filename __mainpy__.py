import pygame, controller, model, time
from pygame import display, event, draw

pygame.init()
screen = display.set_mode([1150, 600])

while True:
    time.sleep(1 / 60)
    controller.control()
    model.step()

    screen.fill([100, 100, 100])
    if model.ball!=None:
        model.ball.draw(screen)
    # model.ball2.draw(screen)
    model.vorota_left.draw(screen)
    model.vorota_right.draw(screen)
    model.igroc_left.draw(screen)
    model.igroc_right.draw(screen)



    draw.circle(screen,[255,0,0],[1150/2,600/2],1)
    display.flip()