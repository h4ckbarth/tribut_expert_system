import pygame as pg
import main_scene as scene
from background import Background
from label import Label
from button import Button
from product import Product
from button_group import ButtonGroup
from icms_engine import IcmsEngine
from tribut_base_fact import TributBaseFact
from product import Product
from pyknow import *
from coin import Coin

def add_node(game_object):
    game_objects.append(game_object)


def draw():
    win.fill((0, 0, 0))

    for i in game_objects:
        i.draw()

    pg.display.flip()

def populate_products():

    product_1_button = Button(win, scene, [50, 50], [100, 100], 'product_1.png', button_group)
    product_1_button.is_pressed = True
    product_1_button.product = Product('normal', 1)

    product_2_button = Button(win, scene, [150, 50], [100, 100], 'product_2.png', button_group)
    product_2_button.product = Product('normal', 2)

    product_3_button = Button(win, scene, [250, 50], [100, 100], 'product_3.gif', button_group)
    product_3_button.product = Product('normal', 3)

    product_4_button = Button(win, scene, [350, 50], [100, 100], 'product_4.png', button_group)
    product_4_button.product = Product('normal', 4)

    product_5_button = Button(win, scene, [50, 150], [100, 100], 'product_5.png', button_group)
    product_5_button.product = Product('exempt', None)

    product_6_button = Button(win, scene, [150, 150], [100, 100], 'product_6.png', button_group)
    product_6_button.product = Product('exempt', None)

    product_7_button = Button(win, scene, [250, 150], [100, 100], 'product_7.png', button_group)
    product_7_button.product = Product('icms_st', None)

    product_8_button = Button(win, scene, [350, 150], [100, 100], 'product_8.png', button_group)
    product_8_button.product = Product('icms_st', None)

    add_node(product_1_button)
    add_node(product_2_button)
    add_node(product_3_button)
    add_node(product_4_button)
    add_node(product_5_button)
    add_node(product_6_button)
    add_node(product_7_button)
    add_node(product_8_button)


def populate_other_buttons():
    buy_button = Button(win, scene, [50, 300], [150, 70], 'compra.png', button_group1)
    buy_button.is_pressed = True
    sale_button = Button(win, scene, [260, 300], [150, 70], 'venda.png', button_group1)

    consumer_button = Button(win, scene, [30, 420], [100, 70], 'consumidor.png', button_group2)
    consumer_button.is_pressed = True
    distributor_button = Button(win, scene, [140, 420], [100, 70], 'distribuidor.png', button_group2)
    varejo_button = Button(win, scene, [250, 420], [100, 60], 'varejo.png', button_group2)
    simple_button = Button(win, scene, [360, 420], [100, 60], 'simples.png', button_group2)

    add_node(sale_button)
    add_node(buy_button)
    add_node(consumer_button)
    add_node(distributor_button)
    add_node(varejo_button)
    add_node(simple_button)


def setup_ui():
    bg = Background(win, scene)
    choose_your_product_label = Label(win, scene, "Escolha seu produto", [100, 0])
    calculate_button = Button(win, scene, [240 - 75, 510], [150, 70], 'calculate.png', ButtonGroup(scene, win))
    add_node(bg)
    add_node(choose_your_product_label)
    add_node(calculate_button)


def run_engine():
    coin.start_animating()
    product = button_group.product
    engine = IcmsEngine(product)

    tp_mvto = "compra" if button_group1.buttons[0].is_pressed else "venda"
    car_trib = ""

    if button_group2.buttons[0]:
        car_trib = 'consumidor'
    elif button_group2.buttons[1]:
        car_trib = 'distribuidor'
    elif button_group2.buttons[2]:
        car_trib = 'varejo'
    elif button_group2.buttons[3]:
        car_trib = 'simples'

    engine.reset()

    engine.declare(TributBaseFact(tp_mvto=tp_mvto))
    engine.declare(TributBaseFact(car_trib=car_trib))

    engine.run()

    global facts
    facts = engine.facts



def show_results():
    print(facts)

pg.init()
#screen
win = pg.display.set_mode((480, 720))  ##100 pixels = 1 meter

# crucial variables for the scene
is_running = True

game_objects = []
facts = []
button_group = ButtonGroup(win, scene)
button_group1 = ButtonGroup(win, scene)
button_group2 = ButtonGroup(win, scene)

setup_ui()
populate_products()
populate_other_buttons()

coin = Coin(win, scene, [240 - 40, 600], [80, 80])
coin.is_showing = True
add_node(coin)



while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False

    draw()























