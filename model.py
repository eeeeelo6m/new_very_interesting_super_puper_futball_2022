import vorota, ball as modul_ball, igroc, random, controller, schet, MONEEEEEEEEEEEESSSSSSS, bigberrys
BIGBERRY_START=40
pri_smene_raunda = None
pri_pobede = None
vorota_right = vorota.Vorota(1120, 0)
vorota_left = vorota.Vorota(0, 0)
ball = None
# ball2=modul_ball.Ball(575,300,30,10,10)
igroc_left = igroc.Igroc(200, 233)
igroc_right = igroc.Igroc(920, 233)
bigberrys_left = []
bigberrys_right = []
RAUND = 2
GOAL = 3
IGROC_LEFT = 1
IGROC_RIGHT = 2
gamemod = 'standard'

improvizirovanny_timer = 10


def make_mones():
    MONEEEEEEEEEEEESSSSSSS.make_mones(igroc_left, igroc_right)


def make_ball():
    global ball
    ball = modul_ball.Ball(575, 300, 15, 0, 0)


def zapusc_ball():
    global ball
    ball = modul_ball.Ball(575, 300, 15, random.choice([-9, 9]), -9)


def dobavlenie_bigberry(igroc):
    global bigberrys_right, bigberrys_left
    left = len(bigberrys_left)
    right = len(bigberrys_right)

    if igroc == 'left':
        bigberry_left = bigberrys.Bigberry(left * 40 + 150, 16)
        bigberrys_left.append(bigberry_left)

    if igroc == 'right':
        bigberry_right = bigberrys.Bigberry(960 - right * 40, 16)
        bigberrys_right.append(bigberry_right)


def del_bigberry(igroc):
    left = len(bigberrys_left)
    right = len(bigberrys_right)
    if igroc == 'left' and left > 0:
        bigberrys_left.pop()
    if igroc == 'right' and right > 0:
        bigberrys_right.pop()


def umenshit_timer_pereriv():
    global improvizirovanny_timer
    improvizirovanny_timer -= 1
    if improvizirovanny_timer == 0:
        smena_regima_standard()


def smena_raunda(win):
    if win == IGROC_RIGHT:
        schet.schet_raund_right += 1
    if win == IGROC_LEFT:
        schet.schet_raund_left += 1
    schet.goal_igroc_right = 0
    schet.goal_igroc_left = 0


def sobiranie_mones():
    for mone in MONEEEEEEEEEEEESSSSSSS.mones:
        if mone['RECT'].colliderect(igroc_left.obect_igroc) == True:
            MONEEEEEEEEEEEESSSSSSS.mones.remove(mone)
            schet.schet_mone_left += 1
        if mone['RECT'].colliderect(igroc_right.obect_igroc) == True:
            MONEEEEEEEEEEEESSSSSSS.mones.remove(mone)
            schet.schet_mone_right += 1


def step():
    global ball

    if ball == None:
        return
    who_do_goal = ball.goal(vorota_left, vorota_right)
    ball.dvigenie(igroc_left, igroc_right)
    if who_do_goal == "left" or who_do_goal == 'right':
        ball = None

        controller.start_timer_ball()
    if who_do_goal == 'right':
        schet.goal_igroc_left += 1
    if who_do_goal == "left":
        schet.goal_igroc_right += 1

    if schet.goal_igroc_right == GOAL:
        smena_raunda(IGROC_RIGHT)
        if schet.schet_raund_right != RAUND:
            smena_regima_pereriv()

    if schet.goal_igroc_left == GOAL:
        smena_raunda(IGROC_LEFT)
        if schet.schet_raund_left != RAUND:
            smena_regima_pereriv()

    if schet.schet_raund_left == RAUND:
        if callable(pri_pobede):
            pri_pobede()

    if schet.schet_raund_right == RAUND:
        if callable(pri_pobede):
            pri_pobede()
    if ball is not None:
        print(ball.object_rect.x)
        if schet.goal_igroc_right == 0 and schet.schet_raund_right == 0 \
                 and ball.object_rect.x <= BIGBERRY_START and ball.object_rect.x>=BIGBERRY_START+ball.speedx:
            bigberry_left = len(bigberrys_left)
            if bigberry_left >= 1:
                ball.speedx=9
                del_bigberry('left')


def smena_regima_pereriv(sbros_timer=True):
    global gamemod, improvizirovanny_timer
    gamemod = 'pereriv'
    if sbros_timer:
        improvizirovanny_timer = 10
    import controller_pereriv
    controller_pereriv.start_regima()


def smena_regima_standard():
    global gamemod
    gamemod = 'standard'
    controller.start_timer_ball()

# ball2.dvigenie(igroc_left, igroc_right)
