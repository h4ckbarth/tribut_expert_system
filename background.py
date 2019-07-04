import pygame as pg
from GameObject import GameObject

class Background(GameObject):
    image = pg.image.load("images/background.png")
    pg.init()

    def update(self):
        pass


    def draw(self):
        self.update()
        self.screen.blit(self.image, (0, 0))