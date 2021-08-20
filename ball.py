import pygame, igroc
from pygame import draw


class Ball():
    def __init__(self, x, y, radius, speedx, speedy, ):
        self.x = x
        # self.y = y
        self.radius = radius

        self.object_rect = pygame.Rect(x - 30, y - 30, self.radius * 2, self.radius * 2)
        self.speedy = speedy
        self.speedx = speedx

    def draw(self, screen):
        # draw.rect(screen, [0, 0, 0], self.object_rect)
        draw.circle(screen, [134, 255, 0], self.object_rect.center, self.radius)

    def dvigenie(self, igroc_left, igroc_right):
        self.object_rect.y += self.speedy
        self.object_rect.x += self.speedx
        if self.object_rect.y <= 0:
            self.speedy = -self.speedy

        if self.object_rect.bottom >= 600:
            self.speedy = -self.speedy

        if self.object_rect.x <= 0:
            self.speedx = -self.speedx

        if self.object_rect.right >= 1150:
            self.speedx = -self.speedx

        if igroc_left.obect_igroc.colliderect(self.object_rect) == 1:
            self.speedx = -self.speedx
            self.object_rect.x = igroc_left.obect_igroc.right
        if igroc_right.obect_igroc.colliderect(self.object_rect) == 1:
            self.speedx = -self.speedx
            self.object_rect.right = igroc_right.obect_igroc.x

    def goal(self, vorota_left, vorota_right):
        if vorota_right.obect_vorota.colliderect(self.object_rect):
            return True
