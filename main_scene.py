import pygame as pg
import main_scene as scene
from background import Background
from label import Label
from button import Button
from product import Product
from button_group import ButtonGroup

def add_node(game_object):
    game_objects.append(game_object)


def draw():
    win.fill((0, 0, 0))

    for i in game_objects:
        i.draw()

    pg.display.flip()


pg.init()
#screen
win = pg.display.set_mode((480, 720))  ##100 pixels = 1 meter

# crucial variables for the scene
is_running = True

game_objects = []
bg = Background(win, scene)

choose_your_product_label = Label(win, scene, "Escolha seu produto", [100, 0])

button_group = ButtonGroup(win, scene)
product_1_button = Button(win, scene, Product('normal', 1, 'product_1.png'), [50, 50], [100, 100], button_group)
product_2_button = Button(win, scene, Product('normal', 1, 'product_2.png'), [150, 50], [100, 100], button_group)

add_node(bg)
add_node(choose_your_product_label)
add_node(product_1_button)
add_node(product_2_button)

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    draw()























