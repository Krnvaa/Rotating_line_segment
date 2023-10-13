import unittest
from unittest.mock import Mock
from src.controller_module import ControllerModule

class TestControllerModule(unittest.TestCase):

    def setUp(self):
        self.input_module = Mock()
        self.drawing_module = Mock()
        self.storage_module = Mock()
        self.tkinter_module = Mock()
        self.controller = ControllerModule( self.input_module, self.drawing_module, self.tkinter_module )

    def test_point_on_line(self):
        result = self.controller.point_on_line(100, 20, 100, 80, 100, 60)
        self.assertTrue(result)

    def test_point_is_not_on_line(self):
        result = self.controller.point_on_line(600, 20, 60, 80, 100, 10)
        self.assertFalse(result)

    def test_start_rotation_valid_input(self):
        self.tkinter_module.get_entry.return_value = (100, 40, 100, 200, 1, 100, 100)
        self.input_module.get_input_values.return_value = (100, 40, 100, 200, 1, 100, 100)
        self.controller.start_rotation()
        self.input_module.error_label.config.assert_called_with(text="")
        self.drawing_module.rotate_line.assert_called_with((100, 40, 100, 200), (100, 100), 1)

    def test_start_rotation_invalid_input(self):
        self.tkinter_module.get_entry.return_value = (100, 40, 100, 200, 1, 90, 30)
        self.input_module.get_input_values.return_value = (100, 40, 100, 200, 1, 90, 30)
        self.controller.start_rotation()
        self.input_module.error_label.config.assert_called_with(text="Точка не принадлежит отрезку")
        self.storage_module.set_input_values.assert_not_called()
        self.drawing_module.rotate_segment.assert_not_called()

if __name__ == '__main__':
    unittest.main()
