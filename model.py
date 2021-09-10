import vorota, ball as modul_ball, igroc, random, controller, schet

vorota_right = vorota.Vorota(1120, 0)
vorota_left = vorota.Vorota(0, 0)
ball = modul_ball.Ball(575, 300, 15, 7, -7)
# ball2=modul_ball.Ball(575,300,30,10,10)
igroc_left = igroc.Igroc(200, 233)
igroc_right = igroc.Igroc(920, 233)
wiiiiiin=0

def make_ball():
    global ball
    ball = modul_ball.Ball(575, 300, 30, random.choice([5, -5]), -5)


def step():
    global ball,wiiiiiin

    if ball != None:
        a = ball.goal(vorota_left, vorota_right)
        ball.dvigenie(igroc_left, igroc_right)
        if a == 1 or a == 2:
            ball = None

            controller.start_timers()
        if a == 1:
            schet.goal1 += 1
            schet.make_schet()
        if a == 2:
            schet.goal2 += 1
            schet.make_schet()
        if schet.goal1==1:
            wiiiiiin=1

            print('LEFT iгрок WIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNN')

        if schet.goal2==2:
            wiiiiiin=2

            print('iгрок RIGHT WIIIIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNN')

    # ball2.dvigenie(igroc_left, igroc_right)
