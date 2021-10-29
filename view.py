import pygame, schet, random, MONEEEEEEEEEEEESSSSSSS, help, time, model
from pygame import display, draw


def mercanie(text,text2):
    igroc_win_color1 = shrift_win.render(text, True, [255, 237, 44])
    igroc_win_color2 = shrift_win.render(text, True, [255, 110, 22])
    win1 = shrift_win.render(text2, True, [255, 237, 44])
    win2 = shrift_win.render(text2, True, [255, 110, 22])
    for a in range(0, 25):
        screen.blit(win1, [350, 300])
        screen.blit(igroc_win_color1, [125, 0])
        display.flip()
        time.sleep(0.2)
        screen.blit(win2, [350, 300])
        screen.blit(igroc_win_color2, [125, 0])
        display.flip()
        time.sleep(0.2)


def pri_pobede():
    if schet.schet_raund_left>schet.schet_raund_right:
        mercanie('igroc_left', 'WIN')

    if schet.schet_raund_right > schet.schet_raund_left:
        mercanie('igroc_right','WIN')

    exit()

def vesolyu_pereriv():
    screen.fill([19, 179, 81])
    for b in range(10, 0, -1):
        timer = shrift_pereriva.render(str(b), True, [0, 0, 0])
        screen.blit(timer, [500, 300])
        display.flip()
        screen.fill([random.randint(10, 150), random.randint(100, 255), random.randint(75, 175)])

        time.sleep(1)


def view():
    screen.fill([0, 0, 0])
    schet.make_schet()
    if model.ball != None:
        model.ball.draw(screen)





    # model.ball2.draw(screen)
    model.vorota_left.draw(screen)
    model.vorota_right.draw(screen)
    model.igroc_left.draw(screen)
    model.igroc_right.draw(screen)

    for mones in MONEEEEEEEEEEEESSSSSSS.moneeeeeeessss:
        draw.rect(screen, [123, 132, 231], mones['RECT'], 1, 1)
        screen.blit(bitcoin, [mones['RECT'].x, mones['RECT'].y])

    screen.blit(schet.schet_goals, [30, 0])
    screen.blit(schet.schet_goals2, [1090, 0])
    screen.blit(schet.schet1, [70, 0])
    screen.blit(schet.schet2, [1050, 0])

    draw.circle(screen, [255, 0, 0], [1150 / 2, 600 / 2], 1)
    display.flip()


pygame.init()
model.pri_smene_raunda = vesolyu_pereriv
model.pri_pobede=pri_pobede
screen = display.set_mode([1150, 600])

shrift_pereriva = pygame.font.SysFont('comicsansms', 200)
shrift_win = pygame.font.SysFont('comicsansms', 200)

bitcoin = pygame.image.load('picture/биткоин.jpg')
bitcoin = help.izmeni_kartinku(bitcoin, 30, 30, [255, 255, 255], 120)
