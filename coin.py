import pygame as pg
from game_object import GameObject

class Coin(GameObject):
    def init_anim(self):
        self.anim.append(pg.image.load("images/coin_1.png"))
        self.anim.append(pg.image.load("images/coin_2.png"))
        self.anim.append(pg.image.load("images/coin_3.png"))
        self.anim.append(pg.image.load("images/coin_4.png"))
        self.anim.append(pg.image.load("images/coin_5.png"))
        self.anim.append(pg.image.load("images/coin_6.png"))

    def __init__(self, screen, scene, pos, size):
        GameObject.__init__(self, screen, scene)
        self.pos = pos
        self.size = size
        self.rect = pg.Rect((self.pos[0], self.pos[1]), (self.size[0], self.size[1]))
        self.image = pg.image.load("images/coin_1.png")
        self.image = pg.transform.scale(self.image, (self.size[0], self.size[1]))
        self.anim = []
        self.init_anim()
        self.anim_index = 0
        self.remaining_time = 0

    pg.init()

    def start_animating(self):
        self.remaining_time = 30



    def update(self):
        self.remaining_time -= 1
        pg.time.delay(100)
        if self.anim_index >= len(self.anim) - 1:
            self.anim_index = 0
        else:
            self.anim_index += 1

        self.image = self.anim[self.anim_index]
        self.rect = pg.Rect((self.pos[0], self.pos[1]), (self.size[0], self.size[1]))
        self.image = pg.transform.scale(self.image, (self.size[0], self.size[1]))

        if self.remaining_time == 1:
            self.scene.show_results()





    def draw(self):
        if self.remaining_time > 0:
            self.screen.blit(self.image, (self.pos[0], self.pos[1]))
            self.update()

