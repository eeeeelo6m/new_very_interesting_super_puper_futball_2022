import pygame, controller, model, time, schet
from pygame import display, event, draw


def mercanie():
    for a in range(0, 1):
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
        screen.fill([19, 179, 81])
        schet.goal1=0
        schet.goal2=0
        schet.schet_raund1+=1
        schet.make_schet()
        model.wiiiiiin=0
        display.flip()
        time.sleep(10)


    if model.wiiiiiin == 2:
        screen.fill([19, 179, 81])
        schet.goal1=0
        schet.goal2=0
        schet.schet_raund2+=1
        model.wiiiiiin=0
        schet.make_schet()
        display.flip()
        time.sleep(10)

    if schet.schet_raund1==2:
        schet.igroc = schet.b.render('igroc left', True, [255, 237, 44])
        schet.igroc2 = schet.b.render('igroc left', True, [255, 110, 22])
        mercanie()
        exit()

    if schet.schet_raund2==2:
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
    screen.blit(schet.schet1,[70,0])
    screen.blit(schet.schet2,[1050,0])

    draw.circle(screen, [255, 0, 0], [1150 / 2, 600 / 2], 1)
    display.flip()
