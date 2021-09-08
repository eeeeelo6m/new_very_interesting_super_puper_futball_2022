import pygame

pygame.init()

print(pygame.font.get_fonts())
a = pygame.font.SysFont('comicsansms', 50)
b = pygame.font.SysFont('comicsansms',200)
goal1 = 0
goal2 = 0
schet_goals=None
schet_goals2=None
def make_schet():
    global schet_goals, schet_goals2

    schet_goals = a.render(str(goal1), True, [123, 1, 255])
    schet_goals2 = a.render(str(goal2), True, [123, 1, 255])

wiiiiiiiiin= b.render('WIN',True,[255,237,44])
wiiiiiiiin=b.render('WIN',True,[255,110,22])
igroc=None
igroc2=None
make_schet()
