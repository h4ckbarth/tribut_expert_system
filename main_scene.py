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
product_1_button = Button(win, scene, [50, 50], [100, 100], 'product_1.png', button_group)
product_1_button.is_pressed = True
product_1_button.product = Product('normal', 1)

product_2_button = Button(win, scene, [150, 50], [100, 100], 'product_2.png', button_group)
product_2_button.product = Product('normal', 1)


button_group1 = ButtonGroup(win, scene)
buy_button = Button(win, scene, [50, 300], [150, 70], 'compra.png', button_group1)
buy_button.is_pressed = True
sale_button = Button(win, scene, [260, 300], [150, 70], 'venda.png', button_group1)

button_group2 = ButtonGroup(win, scene)
consumer_button = Button(win, scene, [30, 420], [100, 70], 'consumidor.png', button_group2)
consumer_button.is_pressed = True
distributor_button = Button(win, scene, [140, 420], [100, 70], 'distribuidor.png', button_group2)
varejo_button = Button(win, scene, [250, 420], [100, 60], 'varejo.png', button_group2)
simple_button = Button(win, scene, [360, 420], [100, 60], 'simples.png', button_group2)

calculate_button = Button(win, scene, [240 - 75, 510], [150, 70], 'calculate.png', ButtonGroup(scene, win))

add_node(bg)
add_node(choose_your_product_label)
add_node(product_1_button)
add_node(product_2_button)
add_node(sale_button)
add_node(buy_button)
add_node(consumer_button)
add_node(distributor_button)
add_node(varejo_button)
add_node(simple_button)
add_node(calculate_button)

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    draw()























