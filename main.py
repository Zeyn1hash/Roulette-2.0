from pygame import *
import sys

from assets.classes.button import Button

from roulette_manager import add_variant, roulette, variant_window, variants_dict, del_variant

# Ініціалізація Pygame
init()
screen = display.set_mode((1000, 700))
display.set_caption("Заповнений сектор кола")

# Кольори
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
GREEN = (0, 200, 100)
YELLOW = (250, 200, 0)

add_button=Button(variant_window.position, (variant_window.size[0], 50), "+", (255, 255, 255))
sectors_num=1
add_button.bind(lambda: add_variant(f"{sectors_num}"))

# Головний цикл програми
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
            sys.exit()
        if e.type==MOUSEBUTTONDOWN:
            if add_button.rect.collidepoint(e.pos):
                add_button.click()
                sectors_num+=1

            for var in variant_window.variants:
                if var.del_rect.rect.collidepoint(e.pos) and variant_window.rect.collidepoint(e.pos):
                    var.del_rect.click()
                    del_variant(var.name)
                    print(var.name)

        if e.type==MOUSEWHEEL:
            if variant_window.rect.collidepoint(mouse.get_pos()):
                if e.y<=-1:
                    variant_window.scroll_down()
                else:
                    variant_window.scroll_up()

    screen.fill(WHITE)

    roulette.draw(screen)
    variant_window.draw(screen)
    add_button.draw(screen)

    # for var in variant_window.variants:
    #     draw.rect(screen, "red", var.del_rect.rect, width=5)

    display.update()
