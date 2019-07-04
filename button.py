import pygame as pg
from game_object import GameObject
from product import Product

class Button(GameObject):
    def __init__(self, screen, scene, product, pos, size, button_group):
        GameObject.__init__(self, screen, scene)
        self.button_group = button_group
        self.button_group.buttons.append(self)
        self.product = product
        self.pos = pos
        self.size = size
        self.rect = pg.Rect((self.pos[0], self.pos[1]), (self.size[0], self.size[1]))
        self.pressed_image = pg.image.load("images/chalk.png")
        self.pressed_image = pg.transform.scale(self.pressed_image, (self.size[0] + 10, self.size[1] + 10))
        self.button_image = pg.image.load("images/" + self.product.image)
        self.button_image = pg.transform.scale(self.button_image, (self.size[0] + 5, self.size[1] + 5))
        self.is_pressed = False



    pg.init()

    def update(self):
            if pg.mouse.get_pressed()[0] and self.rect.collidepoint(pg.mouse.get_pos()):
                self.is_pressed = True
                self.button_group.press_button(self)


    def draw(self):
        if self.is_pressed:
            self.screen.blit(self.pressed_image, (self.pos[0], self.pos[1]))
        self.screen.blit(self.button_image, (self.pos[0], self.pos[1]))

        self.update()
