import pygame

pygame.init()

print(pygame.font.get_fonts())
a = pygame.font.SysFont('comicsansms', 50)
b = pygame.font.SysFont('comicsansms',200)
goal1 = 0
goal2 = 0
schet_goals=None
schet_goals2=None
schet1=None
schet2=None
schet_raund_left=0
schet_raund_right=0
def make_schet():
    global schet_goals, schet_goals2,schet1,schet2

    schet_goals = a.render(str(goal1), True, [123, 1, 255])
    schet_goals2 = a.render(str(goal2), True, [123, 1, 255])
    schet1=a.render(str(schet_raund_left), True, [198, 79, 90])
    schet2=a.render(str(schet_raund_right), True, [198, 79, 90])

wiiiiiiiiin= b.render('WIN',True,[255,237,44])
wiiiiiiiin=b.render('WIN',True,[255,110,22])
igroc=None
igroc2=None
make_schet()
