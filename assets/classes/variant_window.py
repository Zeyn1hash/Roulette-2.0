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

        self.min_y=50
        self.max_y=self.size[1]

        self.scroll_speed=25


    def recalculate_vars_poses(self):
        for i in range(len(self.variants)):
            self.variants[i].position=(0, (len(self.variants)-i)*50)


    def update(self, new_variant):
        self.variants.append(new_variant)
        self.recalculate_vars_poses()

    def scroll_down(self):
        if self.variants[0].position[1]+50>self.max_y:
            for var in self.variants:
                var.position=(0, var.position[1]-self.scroll_speed)

    def scroll_up(self):
        if not self.variants[-1].position[1]>=self.min_y:
            for var in self.variants:
                var.position=(0, var.position[1]+self.scroll_speed)



    def draw(self, surface):
        draw.rect(self.surface, "white", self.local_rect)
        draw.rect(self.surface, "black", self.local_rect, width=8)

        for variant in self.variants:
            variant.draw(self.surface)

        surface.blit(self.surface, self.position)