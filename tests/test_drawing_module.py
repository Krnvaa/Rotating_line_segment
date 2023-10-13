import unittest
from unittest.mock import Mock, patch
from src.drawing_module import DrawingModule

class TestDrawingModule(unittest.TestCase):

    def setUp(self):
        self.canvas = Mock()
        self.drawing_module = DrawingModule(self.canvas)

    def test_rotate_line(self):
        with patch('math.radians') as mock_radians:
            mock_radians.return_value = 45.0
            self.drawing_module.rotate_line((0, 0, 1, 0,), (0.5, 0.5), 45.0)
        self.canvas.create_line.assert_called()

    def test_rotate_line_no_rotation(self):
        original_line = (0, 0, 1, 0)
        center = (0.5, 0.5)
        angular_speed = 0.0
        self.drawing_module.rotate_line(original_line, center, angular_speed)
        rotated_segment = self.canvas.create_line.call_args[0]
        self.assertEqual(rotated_segment, original_line)

if __name__ == '__main__':
    unittest.main()
