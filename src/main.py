from tkinter_module import TkinterModule
from input_module import InputModule
from drawing_module import DrawingModule
from controller_module import ControllerModule

"""
    Описание:
        Создаются объекты, которые используются для управления  графическим интерфейсом и взаимодействия с пользователем. 
        В частности, создается TkinterModule для создания окон и элементов интерфейса, InputModule для обработки
        ввода данных, DrawingModule для отрисовки на холсте и ControllerModule для управления всеми этими модулями.

"""

tkinter_module = TkinterModule()
input_module = InputModule(tkinter_module.error_label)
tkinter_module.bind_entry(input_module.validate_input)
drawing_module = DrawingModule(tkinter_module.canvas)
controller = ControllerModule(input_module, drawing_module,tkinter_module)
tkinter_module.run()

