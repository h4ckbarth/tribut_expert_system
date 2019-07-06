from game_object import GameObject
from label import Label
import pygame as pg

class OutputLabel(GameObject):
    def __init__(self, screen, scene, ncm, cst, aliquota, aliquota_cofins, cst_cofins, aliquota_pis, nat_pis_cofins, icms_reducao):
        GameObject.__init__(self, screen, scene)
        self.ncm = ncm
        self.cst = cst
        self.aliquota = aliquota
        self.icms_reducao = icms_reducao
        self.aliquota_cofins = aliquota_cofins
        self.cst_cofins = cst_cofins
        self.aliquota_pis = aliquota_pis
        self.nat_pis_cofins = nat_pis_cofins
        self.is_showing = False

    pg.init()

    def update(self):
        pass


    def draw(self):
        if self.is_showing:
            self.update()
            font = pg.font.SysFont("chalkduster", 25)
            ncm = font.render("NCM: Sem NCM " if self.ncm == None else "NCM: " + self.ncm, 1, (255, 255, 255))
            self.screen.blit(ncm, (180 - 100, 600))

            cst = font.render("CST ICMS: Sem CST " if self.cst == None else "CST: " + self.cst, 1, (255, 255, 255))
            self.screen.blit(cst, (180 - 100, 620))

            aliquota = font.render("Sem aliquota " if self.aliquota == None else "Aliquota: " + str(self.aliquota), 1, (255, 255, 255))
            self.screen.blit(aliquota, (180 - 100, 640))

            icms_reducao = font.render("Sem Red. " if self.icms_reducao == None else "Red.: " + str(self.icms_reducao), 1, (255, 255, 255))
            self.screen.blit(icms_reducao, (180 - 100, 660))

            cst_cofins = font.render("CST P/C: Sem CST " if self.cst_cofins == None else "CST P/C: " + self.cst_cofins, 1, (255, 255, 255))
            self.screen.blit(cst_cofins, (400 - 100, 600))

            aliquota_pis = font.render("Sem aliquota " if self.aliquota_pis == None else "PIS: " + str(self.aliquota_pis), 1, (255, 255, 255))
            self.screen.blit(aliquota_pis, (400 - 100, 620))

            aliquota_cofins = font.render("Sem aliquota " if self.aliquota_cofins == None else "COFINS: " + str(self.aliquota_cofins), 1, (255, 255, 255))
            self.screen.blit(aliquota_cofins, (400 - 100, 640))

            nat_pis_cofins = font.render("Nat. P/C: " if self.nat_pis_cofins == None else "Nat. P/C: " + self.nat_pis_cofins, 1, (255, 255, 255))
            self.screen.blit(nat_pis_cofins, (400 - 100, 660))


