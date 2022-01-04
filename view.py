import pygame, schet, random, MONEEEEEEEEEEEESSSSSSS, help, time, model
from pygame import display, draw


def mercanie(text, text2):
    igroc_win_color1 = shrift_win.render(text, True, [255, 237, 44])
    igroc_win_color2 = shrift_win.render(text, True, [255, 110, 22])
    hirina = igroc_win_color1.get_width()
    visota = igroc_win_color1.get_height()
    rect = pygame.Rect(125, 0, hirina, visota)
    rect.centerx = 1150 / 2
    win1 = shrift_win.render(text2, True, [255, 237, 44])
    win2 = shrift_win.render(text2, True, [255, 110, 22])

    screen.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
    for a in range(0, 25):
        screen.blit(win1, [350, 300])
        screen.blit(igroc_win_color1, [rect.left, 0])
        display.flip()
        time.sleep(0.2)
        screen.blit(win2, [350, 300])
        screen.blit(igroc_win_color2, [rect.left, 0])

        display.flip()
        time.sleep(0.2)


def pri_pobede():
    if schet.schet_raund_left > schet.schet_raund_right:
        mercanie('igroc_left', 'WIN')

    if schet.schet_raund_right > schet.schet_raund_left:
        mercanie('igroc_right', 'WIN')

    exit()


def view():
    screen.fill([10, 0, 0])

    # if int(time.time())%5>3:
    #     display.flip()
    #     return

    schet.make_schet()
    if model.ball != None:
        model.ball.draw(screen)

    # model.ball2.draw(screen)
    model.vorota_left.draw(screen)
    model.vorota_right.draw(screen)
    model.igroc_left.draw(screen, [0, 136, 255])
    model.igroc_right.draw(screen, [255, 89, 145])

    for bigberrys_left in model.bigberrys_left:
        bigberrys_left.draw(screen)



    for bigberrys_right in model.bigberrys_right:
        bigberrys_right.draw(screen)

    for mones in MONEEEEEEEEEEEESSSSSSS.mones:
        draw.rect(screen, [123, 132, 231], mones['RECT'], 1, 1)
        screen.blit(bitcoin, [mones['RECT'].x, mones['RECT'].y])

    screen.blit(schet.cartinca_goals_left, [30, 0])
    screen.blit(schet.cartinca_goal_right, [1090, 0])

    screen.blit(schet.schet_raun_left_kartinka, [70, 0])
    screen.blit(schet.schet_raund_right_kartinka, [1050, 0])

    screen.blit(schet.schet_mone_left_kartinka, [110, 0])
    screen.blit(schet.schet_mone_right_kartinka, [1010, 0])
    draw.circle(screen, [255, 0, 0], [1150 / 2, 600 / 2], 1)
    display.flip()


pygame.init()

model.pri_pobede = pri_pobede
screen = display.set_mode([1150, 600])

shrift_win = pygame.font.SysFont('comicsansms', 200)

bitcoin = pygame.image.load('picture/биткоин.jpg')
bitcoin = help.izmeni_kartinku(bitcoin, 30, 30, [255, 255, 255], 120)
