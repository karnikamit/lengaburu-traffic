import unittest
import sys
sys.path.append('../main')
from traffic_solution import FastestRoute


class TestFastestRoute(unittest.TestCase):

    def setUp(self):
        self.traffic = FastestRoute("Sunny", {"Orbit1": 12, "Orbit2": 10})

    def test_instance(self):
        self.assertIsInstance(self.traffic, FastestRoute)
