from pygame import *
from math import radians, sin, cos
from pygame.font import Font

init()

class Sector:
    def __init__(self, name: str, color: tuple, center: tuple, radius: int, start_angle: int=0, stop_angle: int=360):
        self.name=name
        self.color=color
        self.center=center
        self.radius=radius
        self.start_angle=start_angle
        self.stop_angle=stop_angle

        # s_font = Font(None, (self.stop_angle-self.start_angle)//4)
        # self.text_color=(0, 0, 0)
        # self.text=s_font.render(self.name, True, self.text_color)
        #
        # offset = math.Vector2(self.radius/2, 0)
        # angle=(stop_angle-start_angle)/2
        # rotated_offset = offset.rotate(-angle)
        #
        # self.rotated_text=transform.rotate(self.text, angle)
        #
        # self.r_text_rect = self.rotated_text.get_rect(center=math.Vector2(self.center) + rotated_offset)

    def update_angle(self, start_angle, stop_angle):
        self.start_angle=start_angle
        self.stop_angle=stop_angle

        # offset = math.Vector2(self.radius/2, 0)
        # angle=(self.stop_angle-self.start_angle)/2+self.start_angle
        # rotated_offset = offset.rotate(-angle)
        #
        # self.rotated_text=transform.rotate(self.text, angle)
        # self.r_text_rect = self.rotated_text.get_rect(center=math.Vector2(self.center) + rotated_offset)

    def draw_filled_sector(self, surface):
        """
        Малює заповнений сектор кола.
        Кути start_angle та stop_angle задаються в градусах.
        """
        points = [self.center]  # Починаємо з центру кола

        # Крок обчислення точок (чим менший, тим плавніша дуга)
        step = 1

        # Якщо початковий кут більший за кінцевий (наприклад, від 300 до 45 градусів)
        if self.start_angle > self.stop_angle:
            self.stop_angle += 360

        # Розраховуємо кожну точку на дузі
        for angle in range(int(self.start_angle), int(self.stop_angle) + 1, step):
            # Переводимо в радіани.
            # У Pygame вісь Y направлена вниз, тому міняємо знак перед кутом,
            # щоб відлік йшов проти годинникової стрілки, як у математиці.
            rad = radians(angle)

            x = self.center[0] + self.radius * cos(rad)
            y = self.center[1] - self.radius * sin(rad)  # Мінус для правильного напрямку Y

            points.append((x, y))

        # Якщо сектора не вийшло (замало точок), не малюємо
        if len(points) > 2:
            draw.polygon(surface, self.color, points)

    def draw(self, surface):
        self.draw_filled_sector(surface)
        # surface.blit(self.rotated_text, self.r_text_rect)