import math

class DrawingModule:
    """
        Класс для рисования и вращения отрезка на холсте.

        Ключевые атрибуты:
            canvas (tk.Canvas): Виджет холста, на котором будет производиться рисование и вращение отрезка.
            line (tuple): Кортеж, содержащий координаты конца и начала отрезка.

        Методы:
            rotate_line(self, line, center, angular_speed):
                Вращает отрезок вокруг центра вращения с указанной угловой скоростью.

    """

    def __init__(self, canvas):
        self.canvas = canvas
        self.line = None

    def rotate_line(self, line, center, angular_speed):
        """
            Вращает отрезок вокруг центра вращения с указанной угловой скоростью.

            Ключевые атрибуты:
                line (tuple): Кортеж, содержащий координаты начала и конца отрезка (x1, y1, x2, y2).
                center (tuple): Кортеж с координатами центра вращения (center_x, center_y).
                angular_speed (float): Угловая скорость вращения в градусах в секунду.

            Описание:
                Этот метод вращает отрезок, заданный координатами начала и конца, вокруг указанного
                центра вращения с заданной угловой скоростью. При каждой итерации метода, отрезок
                поворачивается на угол, равный `angular_speed`, вокруг точки `center`. Затем новые
                координаты начала и конца отрезка используются для отображения его нового положения на
                холсте. Метод выполняет рекурсивные вызовы с задержкой 20 миллисекунд для плавного
                вращения отрезка.
        """

        x1, y1, x2, y2 = line
        center_x, center_y = center
        angle = angular_speed
        radian_angle = math.radians(angle)
        rotated_x1 = center_x + (x1 - center_x) * math.cos(radian_angle) - (y1 - center_y) * math.sin(radian_angle)
        rotated_y1 = center_y + (x1 - center_x) * math.sin(radian_angle) + (y1 - center_y) * math.cos(radian_angle)
        rotated_x2 = center_x + (x2 - center_x) * math.cos(radian_angle) - (y2 - center_y) * math.sin(radian_angle)
        rotated_y2 = center_y + (x2 - center_x) * math.sin(radian_angle) + (y2 - center_y) * math.cos(radian_angle)
        self.canvas.delete('line')
        self.line = self.canvas.create_line(rotated_x1, rotated_y1, rotated_x2, rotated_y2, tags='line', fill='purple', width=3)
        self.canvas.after(20, self.rotate_line, (rotated_x1, rotated_y1, rotated_x2, rotated_y2), (center_x, center_y), angular_speed)

