class InputModule:
    """
        Класс для ввода и валидации данных пользователем.

        Ключевые атрибуты:
            error_label (tk.Label): Виджет метки для отображения ошибок пользователю.

        Методы:

            validate_input(self, event):
                Проверяет введенные пользователем данные и отображает сообщения об ошибках.

            get_input_values(self, x1, y1, x2, y2, speed_entry, center_x_entry, center_y_entry):
                Получает и преобразует введенные данные в числовые значения и возвращает их.
    """

    def __init__(self,  error_label):
        self.error_label = error_label

    def validate_input(self, event):
        """
            Валидирует введенные пользователем данные и отображает сообщения об ошибках.

            Ключевые атрибуты:
                event (tk.Event): Объект события ввода, содержащий информацию о виджете и введенных данных.

            Описание:
                Метод валидирует значение, введенное пользователем, и проверяет, является ли оно числовым. В случае,
                если введенное значение не соответствует числу, метод отображает сообщение об ошибке на виджете error_label.
                В противном случае сообщение об ошибке очищается.
        """

        entry = event.widget
        input_text = entry.get()
        if not input_text:
            self.error_label.config(text="")
            return
        if not (input_text.startswith('-') and input_text[1:].isdigit()) and not input_text.isdigit():
            self.error_label.config(text="Введите числовое значение!")
        else:
            self.error_label.config(text="")

    def get_input_values(self, x1,y1,x2,y2,speed_entry,center_x_entry,center_y_entry):
        """
            Получает и преобразует введенные данные в числовые значения и возвращает их.

            Ключевые атрибуты:
                x1, y1, x2, y2: Координаты начала и конца отрезка.
                speed_entry: Угловая скорость вращения, введенная пользователем.
                center_x_entry: Координата X центра вращения, введенная пользователем.
                center_y_entry: Координата Y центра вращения, введенная пользователем.

            Возвращаемое значение:
                tuple: Кортеж с числовыми значениями координат начала и конца отрезка, скоростью и координатами центра вращения.

            Описание:
                Метод получает текстовые значения координат начала и конца отрезка, скорости и координат центра
                вращения в виде аргументов. Затем он преобразует эти значения в числовые форматы (float)
                и возвращает их в виде кортежа.
        """

        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        angular_speed = float(speed_entry)
        center_x = float(center_x_entry)
        center_y = float(center_y_entry)
        return x1, y1, x2, y2, angular_speed, center_x, center_y

