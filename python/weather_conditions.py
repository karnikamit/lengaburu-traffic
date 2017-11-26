__author__ = 'karnikamit'


class Sunny(object):
    def __init__(self):
        self.crater_reduced = 0.1
        self.vehicles = ["Bike", "Tuktuk", "car"]


class Rainy(object):
    def __init__(self):
        self.crater_reduced = 0.2
        self.vehicles = ["Car", "Tuktuk"]


class Windy(object):
    def __init__(self):
        self.crater_reduced = 0
        self.vehicles = ["Bike", "Tuktuk", "car"]
