from random import randint

from assets.classes.roulette import Roulette
from assets.classes.sector import Sector
from assets.classes.variant import Variant
from assets.classes.variant_window import VariantWindow


wheel_data={"center": (350, 350),
            "radius": 200}

variants_dict={"Base": [Variant("Base", (0, 255, 0)),
                         Sector("Base", (0, 255, 0), wheel_data["center"], wheel_data["radius"])]}

variant_window=VariantWindow((750, 0), (250, 450))
roulette=Roulette(wheel_data["center"], wheel_data["radius"])


def update():
    variant_window.variants.clear()
    roulette.variants.clear()

    for name, l in variants_dict.items():
        l[0].rect.x=variant_window.size[0]-variant_window.size[0]*0.2
        variant_window.variants.append(l[0])
        l[0].del_rect.rect.x = variant_window.position[0] + variant_window.size[0] - l[0].del_rect.size[0]

    for name, l in variants_dict.items():
        roulette.variants.append(l[1])

    variant_window.update()
    roulette.update()


def add_variant(name):
    random_color=(randint(0, 255), randint(0, 255), randint(0, 255))

    variant=Variant(name, random_color)
    sector=Sector(name, random_color, wheel_data["center"], wheel_data["radius"])

    variants_dict[name]=[variant, sector]

    update()

def del_variant(name):
    if len(variants_dict)>1:
        del variants_dict[name]
        update()

update()