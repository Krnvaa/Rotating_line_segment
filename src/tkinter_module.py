import tkinter as tk
from utils import open_about_window, get_version

class TkinterModule:
    """
        Класс для управления пользовательским интерфейсом с использованием библиотеки tkinter.

        Ключевые атрибуты:
            root (tk.Tk): Основное окно приложения.
            window_width (int): Ширина окна.
            window_height (int): Высота окна.
            canvas (tk.Canvas): Холст для рисования и вращения отрезка.
            input_frame (tk.Frame): Виджет для ввода данных пользователем.
            error_label (tk.Label): Виджет метки для отображения ошибок пользователю.
            x1_entry (tk.Entry): Поле ввода для координаты x1.
            y1_entry (tk.Entry): Поле ввода для координаты y1.
            x2_entry (tk.Entry): Поле ввода для координаты x2.
            y2_entry (tk.Entry): Поле ввода для координаты y2.
            speed_entry (tk.Entry): Поле ввода для угловой скорости вращения отрезка.
            center_x_entry (tk.Entry): Поле ввода для координаты x центра вращения.
            center_y_entry (tk.Entry): Поле ввода для координаты y центра вращения.

        Методы:
            create_input_field(self, label_text):
                Создает виджет ввода данных с меткой.

            bind_entry(self, validate_input):
                Привязывает обработчик событий ввода данных к полям ввода.

            get_entry(self):
                Получает текущие значения полей ввода и возвращает их в виде кортежа.

            close_window(self, event):
                Закрывает окно приложения при нажатии клавиши Escape.

            create_button(self, text, command):
                Создает кнопку с указанным текстом и функцией-обработчиком команды.

            create_error_label(self):
                Создает виджет метки для отображения ошибок.

            run(self):
                Запускает цикл обработки событий tkinter и отображает окно.
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Вращение отрезка вокруг заданной точки с угловой скоростью")
        self.window_width = 1000
        self.window_height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - self.window_width) // 2
        y_position = (screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{x_position}+{y_position}")
        self.canvas = tk.Canvas(self.root, width=self.window_width - 250, height=self.window_height,bg="white")
        self.canvas.pack(side="left")
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side="right", padx=10)
        self.error_label = tk.Label(self.input_frame, fg="red")
        self.error_label.grid(row=8, column=0, columnspan=2, pady=5)
        self.x1_entry = self.create_input_field("x1:")
        self.y1_entry = self.create_input_field("y1:")
        self.x2_entry = self.create_input_field("x2:")
        self.y2_entry = self.create_input_field("y2:")
        self.speed_entry = self.create_input_field("Угловая скорость:")
        self.center_x_entry = self.create_input_field("Точка вращения x:")
        self.center_y_entry = self.create_input_field("Точка вращения y:")
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="О программе", command=open_about_window)
        self.file_menu.add_command(label="Версия", command=get_version)
        self.menu_bar.add_cascade(label="Справка", menu=self.file_menu)
        self.root.config(menu=self.menu_bar)
        self.root.bind('<Escape>', self.close_window)

    def create_input_field(self, label_text):
        """
            Создает метку и поле для ввода данных.

            Ключевые атрибуты:
                label_text (str): Текст для метки поля ввода.

            Возвращаемое значение:
                tk.Entry: Созданный виджет поля ввода.

            Описание:
                Метод создает виджет метки с текстом `label_text` и связанное с ней поле для ввода данных.
                Метка и поле размещаются в окне панели ввода. Метод возвращает созданный виджет поля ввода.
        """

        label = tk.Label(self.input_frame, text=label_text)
        label.grid(row=len(self.input_frame.grid_slaves()) // 2, column=0)
        entry = tk.Entry(self.input_frame)
        entry.grid(row=label.grid_info()['row'], column=1, padx=10, pady=5)
        return entry

    def bind_entry(self,validate_input):
        """
            Привязывает функцию обработки ввода к полям ввода.

            Ключевые атрибуты:
                validate_input (function): Функция для обработки ввода.

            Описание:
                Метод связывает функцию `validate_input` с каждым полем ввода для обработки события
                "KeyRelease" (отпускания клавиши). Каждый раз, когда пользователь вводит текст,
                функция `validate_input` будет вызвана для соответствующего поля ввода.
        """

        self.x1_entry.bind('<KeyRelease>', validate_input)
        self.y1_entry.bind('<KeyRelease>',validate_input)
        self.x2_entry.bind('<KeyRelease>', validate_input)
        self.y2_entry.bind('<KeyRelease>', validate_input)
        self.speed_entry.bind('<KeyRelease>', validate_input)
        self.center_x_entry.bind('<KeyRelease>', validate_input)
        self.center_y_entry.bind('<KeyRelease>', validate_input)

    def get_entry(self):
        """
            Получает значения из полей ввода.

            Возвращаемое значение:
                tuple: Кортеж значений из полей ввода (x1, y1, x2, y2, speed, center_x, center_y).

            Описание:
                Метод извлекает значения, введенные пользователем, из каждого поля ввода на панели ввода.
                Затем он возвращает эти значения в виде кортежа, который содержит координаты начала и конца отрезка
                (x1, y1, x2, y2), угловую скорость (speed), а также координаты центра вращения (center_x, center_y).
        """

        return self.x1_entry.get(),self.y1_entry.get(), self.x2_entry.get(),self.y2_entry.get(),self.speed_entry.get(),self.center_x_entry.get(),self.center_y_entry.get()

    def close_window(self,event):
        """
            Закрывает главное окно приложения.

            Ключевые атрибуты:
                event: Событие, которое вызвало закрытие окна.

            Описание:
                Этот метод вызывается, когда пользователь нажимает клавишу "Escape".
                Он закрывает главное окно приложения, завершая выполнение программы.
        """

        self.root.destroy()

    def create_button(self, text, command):
        """
            Создает кнопку на панели ввода.

            Ключевые атрибуты:
                text (str): Текст, отображаемый на кнопке.
                command (function): Функция, которая будет выполнена при нажатии кнопки.

            Описание:
                Этот метод создает кнопку с текстом `text` и связывает ее с функцией `command`,
                которая будет выполнена при нажатии кнопки. Кнопка размещается на панели ввода.
        """

        button = tk.Button(self.input_frame, text=text, command=command)
        button.grid(row=10, column=0, columnspan=2, pady=5)

    def create_error_label(self):
        """
            Создает метку для отображения ошибок.

            Возвращаемое значение:
                tk.Label: Созданный виджет метки.

            Описание:
                Этот метод создает виджет метки для отображения текстовых сообщений об ошибках на панели ввода.
                Метка размещается на панели ввода и возвращается как результат выполнения метода.
        """

        error_label = tk.Label(self.input_frame, fg="red", wraplength=200)
        error_label.grid(row=len(self.input_frame.grid_slaves()) // 2, column=0, columnspan=2, pady=5)
        return error_label

    def run(self):
        """
            Запускает главное окно приложения.

            Описание:
                Этот метод запускает главное окно приложения и начинает его выполнение. После вызова этого метода
                программа остается активной, ожидая действий пользователя и обрабатывая события.
        """

        self.root.mainloop()
