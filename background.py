import pygame as pg
from game_object import GameObject

class Background(GameObject):
    image = pg.image.load("images/background.jpg")
    pg.init()

    def update(self):
        pass


    def draw(self):
        self.update()
        self.screen.blit(self.image, (0, 0))