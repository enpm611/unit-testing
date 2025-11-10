import unittest
from speed_controller import SpeedController

class TestSpeedControllerWhiteBox(unittest.TestCase):
    def setUp(self):
        self.controller = SpeedController(speed_limit=60)

    def test_example(self):
        self.assertEqual(self.controller.update_speed('clear', 20), 50)

if __name__ == "__main__":
    unittest.main()