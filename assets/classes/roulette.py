from pygame import *
from math import radians, sin, cos
from assets.classes.sector import Sector


class Roulette:
    def __init__(self, center: tuple, radius: int, length: int):
        self.center=center
        self.radius=radius
        self.variants={"Base": Sector("green", self.center, self.radius, 0, 360)}
        self.length=len(self.variants)

    def recalculate_angles(self):
        self.length = len(self.variants)
        angle=360/self.length
        start_angle=0
        for key, sector in self.variants.items():
            sector.start_angle=start_angle
            sector.stop_angle=start_angle+angle
            start_angle+=angle

    def draw(self, surface):
        for key, sector in self.variants.items():
            sector.draw_filled_sector(surface)