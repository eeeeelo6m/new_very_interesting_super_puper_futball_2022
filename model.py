import vorota, ball as modul_ball, igroc, random, controller, schet
pri_smene_raunda=None
vorota_right = vorota.Vorota(1120, 0)
vorota_left = vorota.Vorota(0, 0)
ball = modul_ball.Ball(575, 300, 15, 7, -7)
# ball2=modul_ball.Ball(575,300,30,10,10)
igroc_left = igroc.Igroc(200, 233)
igroc_right = igroc.Igroc(920, 233)

IGROC_LEFT=1
IGROC_RIGHT=2
def make_ball():
    global ball
    ball = modul_ball.Ball(575, 300, 15, random.choice([7, -7]), -7)

def smena_raunda(win):

    if win==IGROC_RIGHT:
        schet.schet_raund_right += 1
    if win==IGROC_LEFT:
        schet.schet_raund_left += 1
    schet.goal_igroc_right = 0
    schet.goal_igroc_left = 0







def step():
    global ball

    if ball != None:
        a = ball.goal(vorota_left, vorota_right)
        ball.dvigenie(igroc_left, igroc_right)
        if a == 1 or a == 2:
            ball = None

            controller.start_timer_ball()
        if a == 1:
            schet.goal_igroc_right += 1
        if a == 2:
            schet.goal_igroc_left += 1

        if schet.goal_igroc_right==3:
            if pri_smene_raunda is not None:
                pri_smene_raunda()
            smena_raunda(IGROC_LEFT)


        if schet.goal_igroc_left==3:
            if pri_smene_raunda is not None:
                pri_smene_raunda()
            smena_raunda(IGROC_RIGHT)




    # ball2.dvigenie(igroc_left, igroc_right)
