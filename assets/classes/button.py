from pygame import *

class Button:
    def __init__(self, position: tuple, size: tuple, text: str, color: tuple):
        self.rect=Rect(position, size)
        self.color=color
        self.function=None

    def bind(self, function):
        self.function=function

    def click(self):
        if self.function:
            self.function()

    def draw(self, surface):
        draw.rect(surface, self.color, self.rect)