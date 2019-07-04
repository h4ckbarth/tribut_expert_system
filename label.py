import pygame as pg
from GameObject import GameObject

class Label(GameObject):
    degrees_text = ""
    v0_text = ""
    x_maximum_text = ""
    y_maximum_text = ""
    time_text = ""

    pg.init()

    def update(self):
        pass


    def draw(self):
        self.update()
        myfont = pg.font.SysFont("monospace", 25)

        degrees = myfont.render("Degrees: " + self.degrees_text, 1, (255, 255, 0))
        self.screen.blit(degrees, (50, 50))

        v0 = myfont.render("Applied Force: " + self.v0_text, 1, (255, 255, 0))
        self.screen.blit(v0, (50, 80))

        y = myfont.render("Maximum at Y: " + self.y_maximum_text + " meters", 1, (255, 255, 0))
        self.screen.blit(y, (50, 110))

        x = myfont.render("Maximum at X: " + self.x_maximum_text + " meters", 1, (255, 255, 0))
        self.screen.blit(x, (50, 140))

        time = myfont.render("Passed time: " + self.time_text + " seconds", 1, (255, 255, 0))
        self.screen.blit(time, (50, 170))





