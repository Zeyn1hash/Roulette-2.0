from pygame import *
from math import radians, sin, cos
from assets.classes.sector import Sector


class Roulette:
    def __init__(self, center: tuple, radius: int):
        self.center=center
        self.radius=radius
        self.variants=[]

        self.length=len(self.variants)

    def update(self, new_sector):
        self.variants.append(new_sector)
        self.recalculate_angles()

    def recalculate_angles(self):
        self.length = len(self.variants)
        angle=360/self.length
        start_angle=0
        for sector in self.variants:
            sector.update_angle(start_angle, start_angle+angle)
            # sector.start_angle=start_angle
            # sector.stop_angle=start_angle+angle
            start_angle+=angle

    def draw(self, surface):
        for sector in self.variants:
            sector.draw(surface)

    def add(self, sector: Sector, name: str):
        self.variants[name]=sector
        self.recalculate_angles()