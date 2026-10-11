from pygame import *
from math import radians, sin, cos

class Sector:
    def __init__(self, color: tuple, center: tuple, radius: int, start_angle: int, stop_angle: int):
        self.color=color
        self.center=center
        self.radius=radius
        self.start_angle=start_angle
        self.stop_angle=stop_angle

    def draw_filled_sector(self, surface):
        """
        Малює заповнений сектор кола.
        Кути start_angle та stop_angle задаються в градусах.
        """
        points = [self.center]  # Починаємо з центру кола

        # Крок обчислення точок (чим менший, тим плавніша дуга)
        step = 20

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
