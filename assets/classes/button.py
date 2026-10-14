from pygame import *
from pygame.font import Font


class Button:
    def __init__(self, position: tuple, size: tuple, text: str, color: tuple, text_color="black"):
        self.position=position
        self.size=size
        self.surface=Surface(self.size)
        self.rect=Rect(self.position, self.size)
        self.local_rect=Rect((0, 0), self.size)
        self.color=color
        self.function=None

        font = Font(None, self.size[1])
        self.text_color=text_color
        self.text=font.render(text, True, self.text_color)


    def bind(self, function):
        self.function=function

    def click(self):
        if self.function:
            self.function()

    def draw(self, surface):
        draw.rect(self.surface, self.color, self.local_rect)
        draw.rect(self.surface, "black", self.local_rect, width=8)

        text_pos=(self.size[0]/2-self.text.get_size()[0]/2, self.size[1]/2-self.text.get_size()[1]/2)
        self.surface.blit(self.text, text_pos)
        surface.blit(self.surface, self.position)
