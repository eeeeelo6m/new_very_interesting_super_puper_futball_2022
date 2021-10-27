import pygame, controller, model, time,view
from pygame import display, draw


pygame.init()





while True:

    time.sleep(1 / 60)
    controller.control()
    view.view()
    model.step()






