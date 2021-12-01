import pygame, controller, model, time,view,view_pereriv,controller_pereriv


pygame.init()


while True:

    time.sleep(1 / 60)
    if model.gamemod=='standard':
        controller.control()
        view.view()
    elif model.gamemod=='pereriv':

        controller_pereriv.control()

        view_pereriv.skrin_2(view.screen)
    model.step()






