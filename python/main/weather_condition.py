__author__ = 'karnikamit'


class Weather(object):
    def __init__(self, craters_reduced, vehicles, weather):
        """

        :param (int) craters_reduced: craters reduced percent
        :param (list) vehicles: List of vehicles that can be used
        :param (str) weather: Type of weather name
        """
        self.craters_reduced = craters_reduced
        self.vechiles = vehicles
        self.weather = weather

    def __str__(self):
        return self.weather


# class Sunny(object):
#     def __init__(self):
#         self.crater_reduced = 0.1
#         self.vehicles = ["bike", "tuktuk", "car"]
#
#
# class Rainy(object):
#     def __init__(self):
#         self.crater_reduced = 0.2
#         self.vehicles = ["car", "tuktuk"]
#
#
# class Windy(object):
#     def __init__(self):
#         self.crater_reduced = 0     # No change
#         self.vehicles = ["bike", "tuktuk", "car"]
