__author__ = 'karnikamit'
from vehicles import Bike, Car, Tuktuk
from weather_conditions import Sunny, Rainy, Windy
from orbits import Orbit1, Orbit2


class Traffic(object):
    def __init__(self, weather, traffic_speeds):
        self.weather = weather
        self.traffic_speeds = traffic_speeds     #{"Orbit1": 12, "Orbit2": 10}
