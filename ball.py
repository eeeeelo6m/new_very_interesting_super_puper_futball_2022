
from pygame import draw


class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, screen):
        draw.circle(screen, [134, 255, 0], [self.x, self.y], 30)

