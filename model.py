import vorota, ball as modul_ball, igroc

vorota_right = vorota.Vorota(1120, 0)
vorota_left = vorota.Vorota(0, 0)
ball = modul_ball.Ball(575, 300,30,10,-0)
ball2=modul_ball.Ball(100,100,10,2,10)
igroc_left = igroc.Igroc(200, 233)
igroc_right = igroc.Igroc(920, 233)
def step():
    ball.dvigenie(igroc_left,igroc_right)
    ball2.dvigenie(igroc_left,igroc_right)








