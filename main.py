from pygame import *
from random import randint
import sys

from assets.classes.roulette import Roulette
from assets.classes.sector import Sector
from assets.classes.button import Button

# Ініціалізація Pygame
init()
screen = display.set_mode((1000, 700))
display.set_caption("Заповнений сектор кола")

# Кольори
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
GREEN = (0, 200, 100)
YELLOW = (250, 200, 0)

roulette=Roulette((350, 350), 200, 3)
roulette.variants={"1": Sector("green", roulette.center, roulette.radius, 0, 360),
                   "2": Sector("blue", roulette.center, roulette.radius, 0, 360),
                   "3": Sector("red", roulette.center, roulette.radius, 0, 360),
                   "4": Sector("yellow", roulette.center, roulette.radius, 0, 360),
                   }

def random_sector():
    return Sector((randint(0, 255), randint(0, 255), randint(0, 255)), roulette.center, roulette.radius, 0, 1)
button=Button((650, 300), (300, 100), "ADD", (0, 255, 0))

sectors_num=5
button.bind(lambda: roulette.add(random_sector(), f"{sectors_num}"))
roulette.recalculate_angles()
# Головний цикл програми
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
        if e.type==MOUSEBUTTONDOWN:
            if button.rect.collidepoint(e.pos):
                button.click()
                sectors_num+=1

    screen.fill(WHITE)

    roulette.draw(screen)
    button.draw(screen)

    display.update()
