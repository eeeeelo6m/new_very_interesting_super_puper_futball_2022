
from pygame import draw


class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def draw(self, screen):
        draw.circle(screen, [150, 150, 150], [self.x, self.y], 2)

