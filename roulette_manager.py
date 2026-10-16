from random import randint

from assets.classes.roulette import Roulette
from assets.classes.sector import Sector
from assets.classes.variant import Variant
from assets.classes.variant_window import VariantWindow


wheel_data={"center": (350, 350),
            "radius": 200}

variants_list=[{"Base": [Variant("Base", (0, 255, 0)),
                         Sector((0, 255, 0), wheel_data["center"], wheel_data["radius"], 0, 360)]}]

variant_window=VariantWindow((750, 0), (250, 450))
roulette=Roulette(wheel_data["center"], wheel_data["radius"])

def setup():
    for variant in variants_list:
        for name, l in variant.items():
            roulette.variants.append(l[1])

    for variant in variants_list:
        for name, l in variant.items():
            variant_window.variants.append(l[0])


def add_variant(name):
    random_color=(randint(0, 255), randint(0, 255), randint(0, 255))

    variant=Variant(name, random_color)
    sector=Sector(random_color, wheel_data["center"], wheel_data["radius"], 0, 360)
    variants_list.append(
        {name: [variant, sector]})

    roulette.update(sector)
    variant_window.update(variant)

setup()