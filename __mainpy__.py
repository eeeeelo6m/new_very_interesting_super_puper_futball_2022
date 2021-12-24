import pygame, controller, time,view,model,view_pereriv,controller_pereriv,controller_shop,view_shop


pygame.init()


while True:

    time.sleep(1 / 60)
    if model.gamemod=='standard':
        controller.control()
        view.view()
    elif model.gamemod=='pereriv':
        controller_pereriv.control()
        view_pereriv.skrin_2(view.screen)
    elif model.gamemod=='shop':
        controller_shop.control()
        view_shop.skrin_3(view.screen)
    model.step()






