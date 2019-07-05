from game_object import GameObject
from label import Label
import pygame as pg

class OutputLabel(GameObject):
    def __init__(self, screen, scene, ncm, cst, aliquota):
        GameObject.__init__(self, screen, scene)
        self.ncm = ncm
        self.cst = cst
        self.aliquota = aliquota
        self.is_showing = False

    pg.init()

    def update(self):
        pass


    def draw(self):
        if self.is_showing:
            self.update()
            font = pg.font.SysFont("chalkduster", 25)
            ncm = font.render("NCM: Sem NCM " if self.ncm == None else "NCM: " + self.ncm, 1, (255, 255, 255))
            self.screen.blit(ncm, (240 - 60, 600))

            cst = font.render("CST: Sem CST " if self.cst == None else "CST: " + self.cst, 1, (255, 255, 255))
            self.screen.blit(cst, (240 - 60, 620))

            aliquota = font.render("Sem aliquota " if self.aliquota == None else "Aliquota: " + str(self.aliquota), 1, (255, 255, 255))
            self.screen.blit(aliquota, (240 - 60, 640))


