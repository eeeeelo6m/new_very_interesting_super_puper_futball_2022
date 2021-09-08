import pygame, controller, model, time, schet
from pygame import display, event, draw


def mercanie():
    for a in range(0, 25):
        screen.blit(schet.wiiiiiiiiin, [350, 300])
        screen.blit(schet.igroc, [125, 0])
        display.flip()
        time.sleep(0.2)
        screen.blit(schet.wiiiiiiiin, [350, 300])
        screen.blit(schet.igroc2, [125, 0])
        display.flip()
        time.sleep(0.2)


pygame.init()
screen = display.set_mode([1150, 600])

while True:
    time.sleep(1 / 60)
    controller.control()
    model.step()

    screen.fill([0, 0, 0])
    if model.ball != None:
        model.ball.draw(screen)
    if model.wiiiiiin == 1:
        screen.fill([0, 0, 0])
        schet.igroc = schet.b.render('igroc left', True, [255, 237, 44])
        schet.igroc2 = schet.b.render('igroc left', True, [255, 110, 22])
        mercanie()
        exit()

    if model.wiiiiiin == 2:
        schet.igroc = schet.b.render('igroc right', True, [255, 237, 44])
        schet.igroc2 = schet.b.render('igroc right', True, [255, 110, 22])
        mercanie()
        exit()
    # model.ball2.draw(screen)
    model.vorota_left.draw(screen)
    model.vorota_right.draw(screen)
    model.igroc_left.draw(screen)
    model.igroc_right.draw(screen)

    screen.blit(schet.schet_goals, [30, 0])
    screen.blit(schet.schet_goals2, [1090, 0])

    draw.circle(screen, [255, 0, 0], [1150 / 2, 600 / 2], 1)
    display.flip()
