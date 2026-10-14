from pygame import *
from assets.classes.variant import Variant

class VariantWindow:
    def __init__(self, position: tuple, size: tuple):
        self.position=position
        self.size=size
        self.surface=Surface(self.size)
        self.rect=Rect(self.position, self.size)
        self.local_rect = Rect((0, 0), self.size)
        self.variants=[{"Base": Variant("Base", (0, 0), (self.size[0], 50), (0, 255, 0))}]

    def draw(self, surface):
        draw.rect(self.surface, "white", self.local_rect)
        draw.rect(self.surface, "black", self.local_rect, width=8)

        for data in self.variants:
            for name, var in data.items():
                var.draw(self.surface)

        surface.blit(self.surface, self.position)