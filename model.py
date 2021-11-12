import vorota, ball as modul_ball, igroc, random, controller, schet,MONEEEEEEEEEEEESSSSSSS
pri_smene_raunda=None
pri_pobede=None
vorota_right = vorota.Vorota(1120, 0)
vorota_left = vorota.Vorota(0, 0)
ball = modul_ball.Ball(1150/2, 600/2, 15, 9, -9)
# ball2=modul_ball.Ball(575,300,30,10,10)
igroc_left = igroc.Igroc(200, 233)
igroc_right = igroc.Igroc(920, 233)
RAUND=2
GOAL=9
IGROC_LEFT=1
IGROC_RIGHT=2
def make_ball():
    global ball
    ball = modul_ball.Ball(575, 300, 15, random.choice([-9, 9]), -9)

def smena_raunda(win):

    if win==IGROC_RIGHT:
        schet.schet_raund_right += 1
    if win==IGROC_LEFT:
        schet.schet_raund_left += 1
    schet.goal_igroc_right = 0
    schet.goal_igroc_left = 0


def sobiranie_mones():
    for mone in MONEEEEEEEEEEEESSSSSSS.mones:
        if mone['RECT'].colliderect(igroc_left.obect_igroc)==True:
            MONEEEEEEEEEEEESSSSSSS.mones.remove(mone)



def step():
    global ball

    if ball == None:
        return
    who_do_goal = ball.goal(vorota_left, vorota_right)
    ball.dvigenie(igroc_left, igroc_right)
    if who_do_goal == "left" or who_do_goal == 'right':
        ball = None

        controller.start_timer_ball()
    if who_do_goal ==  'right':
        schet.goal_igroc_left += 1
    if who_do_goal =="left":
        schet.goal_igroc_right += 1

    if schet.goal_igroc_right==GOAL:
        smena_raunda(IGROC_RIGHT)
        if callable(pri_smene_raunda) and schet.schet_raund_right!=RAUND:
            pri_smene_raunda()



    if schet.goal_igroc_left==GOAL:
        smena_raunda(IGROC_LEFT)
        if callable(pri_smene_raunda) and schet.schet_raund_left != RAUND:
            pri_smene_raunda()



    if schet.schet_raund_left==RAUND:
        if callable(pri_pobede):
            pri_pobede()

    if schet.schet_raund_right==RAUND:
        if callable(pri_pobede):
            pri_pobede()

    # ball2.dvigenie(igroc_left, igroc_right)
