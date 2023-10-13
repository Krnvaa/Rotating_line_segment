class ControllerModule:
    """
        Класс для управления вращением отрезка.

        Ключевые атрибуты:
            root (tk.Tk): Основное окно приложения.
            input_module (InputModule): Модуль для ввода данных.
            drawing_module (DrawingModule): Модуль для рисования и вращения отрезка.
            tkinter_module (TkinterModule): Модуль для создания пользовательского интерфейса.

        Методы:
            point_point_on_line(self, x1, y1, x2, y2, x, y):
                Проверяет, принадлежит ли точка отрезку.

            input_value(self):
                Получает входные значения от пользовательского интерфейса.

            start_rotation(self):
                Начинает вращение отрезка.
    """

    def __init__(self, input_module, drawing_module,tkinter_module):
        self.input_module = input_module
        self.drawing_module = drawing_module
        self.input_module.error_label = self.input_module.error_label
        self.input_module.get_input_values=self.input_module.get_input_values
        self.tkinter_module = tkinter_module
        self.tkinter_module.create_button = tkinter_module.create_button("Начать вращение",self.start_rotation)

    def point_on_line(self, x1, y1, x2, y2, x, y):
        """
            Проверяет, принадлежит ли точка отрезку.

            Ключевые аргументы:
                x1, y1, x2, y2: Координаты начала и конца отрезка.
                x, y: Координаты точки вращения.

            Возвращаемое значение:
                bool: True, если точка принадлежит отрезку, иначе False.

            Описание:
                Эта функция проверяет, принадлежит ли заданная точка отрезку. Если точка лежит на прямой, проходящей через отрезок, то возвращается True.
        """
        if (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1) == 0:
            return True
        return False

    def input_value(self):
        """
            Используется для получения входных данных от пользовательского интерфейса.

            Возвращаемое значение:
                tuple: Кортеж с входными значениями координат начала и конца отрезка, угловой скорости вращения, точки вращения
                (x1, y1, x2, y2, speed_entry, center_x, center_y).

            Описание:
                Этот метод извлекает значения, введенные пользователем, из пользовательского интерфейса
                с помощью объекта tkinter_module. Затем он возвращает эти значения в виде кортежа,
                содержащего координаты начала и конца отрезка (x1, y1, x2, y2), угловой скорости вращения (speed_entry),
                а также координаты центра вращения (center_x, center_y).
        """

        x1, y1,x2, y2, speed_entry, center_x_entry,center_y_entry=self.tkinter_module.get_entry()
        return self.input_module.get_input_values(x1, y1,x2, y2, speed_entry, center_x_entry,center_y_entry)

    def start_rotation(self):
        """
            Начинает вращение отрезка.

            Описание:
                Данный метод вызывается при нажатии кнопки "Начать вращение" и начинает вращение отрезка.
                Сначала метод проверяет, принадлежит ли заданная точка отрезку. Если точка
                не принадлежит отрезку, то устанавливает текст ошибки и завершает выполнение. В противном
                случае сбрасывает текст ошибки. Затем вызывается метод для вращения отрезка с учетом
                введенных данных.
        """

        x1, y1, x2, y2, speed, center_x, center_y = self.input_value()
        if not self.point_on_line(x1, y1, x2, y2, center_x, center_y):
            self.input_module.error_label.config(text="Точка не принадлежит отрезку")
            return
        self.input_module.error_label.config(text="")
        self.drawing_module.rotate_line((x1, y1, x2, y2), (center_x, center_y), speed)

