import pygame

pygame.init()

print(pygame.font.get_fonts())
shrift_goal = pygame.font.SysFont('comicsansms', 50)

goal_igroc_right = 0
goal_igroc_left = 0
cartinca_goal_right=None
cartinca_goals_left=None
schet_raun_left_kartinka=None
schet_raund_right_kartinka=None
schet_raund_left=0
schet_raund_right=0
def make_schet():
    global cartinca_goal_right, cartinca_goals_left,schet_raun_left_kartinka,schet_raund_right_kartinka

    cartinca_goals_left = shrift_goal.render(str(goal_igroc_left), True, [123, 1, 255])
    cartinca_goal_right = shrift_goal.render(str(goal_igroc_right), True, [123, 1, 255])
    schet_raun_left_kartinka=shrift_goal.render(str(schet_raund_left), True, [198, 79, 90])
    schet_raund_right_kartinka=shrift_goal.render(str(schet_raund_right), True, [198, 79, 90])



make_schet()
