import pygame as pg
from game_object import GameObject

class Label(GameObject):
    def __init__(self, screen, scene, text, pos):
        GameObject.__init__(self, screen, scene)
        self.text = text
        self.pos = pos

    pg.init()

    def update(self):
        pass


    def draw(self):
        self.update()
        myfont = pg.font.SysFont("chalkduster", 25)

        degrees = myfont.render(self.text, 1, (255, 255, 255))
        self.screen.blit(degrees, (self.pos[0], self.pos[1]))






