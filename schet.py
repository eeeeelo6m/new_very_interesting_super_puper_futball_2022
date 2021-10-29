import pygame

pygame.init()

print(pygame.font.get_fonts())
shrift_goal = pygame.font.SysFont('comicsansms', 50)

goal_igroc_right = 0
goal_igroc_left = 0
schet_goals=None
schet_goals2=None
schet1=None
schet2=None
schet_raund_left=0
schet_raund_right=0
def make_schet():
    global schet_goals, schet_goals2,schet1,schet2

    schet_goals = shrift_goal.render(str(goal_igroc_right), True, [123, 1, 255])
    schet_goals2 = shrift_goal.render(str(goal_igroc_left), True, [123, 1, 255])
    schet1=shrift_goal.render(str(schet_raund_left), True, [198, 79, 90])
    schet2=shrift_goal.render(str(schet_raund_right), True, [198, 79, 90])



make_schet()
