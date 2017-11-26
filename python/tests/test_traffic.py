import unittest
from ..main.traffic_solution import Traffic


class TestTraffic(unittest.TestCase):
    def test_instance(self):
        ts = Traffic("Sunny", {"Orbit1": 12, "Orbit2": 10})
        self.assertIsInstance(ts, Traffic)


suite = unittest.TestLoader().loadTestsFromTestCase(TestTraffic)
unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__'and __package__ is None:
#     from os import sys, path
#     sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#     unittest.main()
