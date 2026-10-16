from pygame import *

from assets.classes.button import Button
from assets.classes.variant import Variant


class VariantWindow:
    def __init__(self, position: tuple, size: tuple):
        self.position=position
        self.size=size
        self.surface=Surface(self.size)
        self.rect=Rect(self.position, self.size)
        self.local_rect = Rect((0, 0), self.size)

        self.variants=[]


    def recalculate_vars_poses(self):
        for i in range(len(self.variants)):
            self.variants[i].position=(0, (len(self.variants)-i)*50)

    def update(self, new_variant):
        self.variants.append(new_variant)
        self.recalculate_vars_poses()

    def draw(self, surface):
        draw.rect(self.surface, "white", self.local_rect)
        draw.rect(self.surface, "black", self.local_rect, width=8)

        for variant in self.variants:
            variant.draw(self.surface)

        surface.blit(self.surface, self.position)