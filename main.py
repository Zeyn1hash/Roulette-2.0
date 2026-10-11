from pygame import *
import math
import sys
from assets.classes.roulette import Roulette
from assets.classes.sector import Sector

# Ініціалізація Pygame
init()
screen = display.set_mode((1000, 700))
display.set_caption("Заповнений сектор кола")

# Кольори
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
GREEN = (0, 200, 100)
YELLOW = (250, 200, 0)

roulette=Roulette((500, 350), 200, 3)
roulette.variants={"1": Sector("green", roulette.center, roulette.radius, 0, 360),
                   "2": Sector("blue", roulette.center, roulette.radius, 0, 360),
                   "3": Sector("red", roulette.center, roulette.radius, 0, 360),
                   "4": Sector("yellow", roulette.center, roulette.radius, 0, 360),
                   }
roulette.recalculate_angles()
# Головний цикл програми
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()

    screen.fill(WHITE)

    roulette.draw(screen)

    display.update()
