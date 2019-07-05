import pygame as pg
from game_object import GameObject
from product import Product

class ButtonGroup(GameObject):
    def __init__(self, screen, scene):
        GameObject.__init__(self, screen, scene)
        self.buttons = []
        self.product = Product(None, None)

    def press_button(self, button):
        self.product = button.product
        for but in self.buttons:
            if but is not button:
                but.is_pressed = False

    def update(self):
        pass

    def draw(self):
        self.update()