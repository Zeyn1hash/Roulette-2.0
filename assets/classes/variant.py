from pygame import *
from pygame.font import Font

from assets.classes.button import Button


class Variant:
    def __init__(self, name: str, position: tuple, size: tuple, color: tuple):
        self.name=name
        self.position=position
        self.size=size
        self.color=color
        self.surface=Surface(self.size)
        self.rect=Rect(self.position, self.size)
        self.local_rect = Rect((0, 0), self.size)

        color_r_size=(self.size[0]/5, 50)

        text_r_pos=(self.size[0]*0.2, 0)
        text_r_size=(self.size[0]*0.6, self.size[1])

        del_r_pos=(self.size[0]*0.8, 0)
        del_r_size=(self.size[0]/5, 50)

        self.local_color_rect=Rect((0, 0), color_r_size)
        self.local_text_rect=Rect(text_r_pos, text_r_size)
        self.local_del_rect=Button(del_r_pos, del_r_size, "×", (255, 255, 255), text_color=(255, 0, 0))

        self.color_rect=Rect(self.position, color_r_size)
        self.text_rect=Rect((self.position[0]+text_r_pos[0], self.position[1]), text_r_size)
        self.del_rect=Button((self.position[0]+del_r_pos[0], self.position[1]), del_r_size, "×", (255, 255, 255))

        font = Font(None, self.size[1])
        self.text=font.render(self.name, True, "black")



    def draw(self, surface):
        draw.rect(self.surface, self.color, self.local_color_rect)
        draw.rect(self.surface, "black", self.local_color_rect, width=8)

        draw.rect(self.surface, "white", self.local_text_rect)
        draw.rect(self.surface, "black", self.local_text_rect, width=8)

        self.surface.blit(self.text, (self.local_text_rect.x+8, self.local_text_rect.y+self.local_text_rect.size[1]/2-self.text.get_size()[1]/2))

        self.local_del_rect.draw(self.surface)

        surface.blit(self.surface, self.position)
