__author__ = 'karnikamit'


class Sunny(object):
    def __init__(self):
        self.crater_reduced = 0.1
        self.vehicles = ["bike", "tuktuk", "car"]


class Rainy(object):
    def __init__(self):
        self.crater_reduced = 0.2
        self.vehicles = ["car", "tuktuk"]


class Windy(object):
    def __init__(self):
        self.crater_reduced = 1     # No change
        self.vehicles = ["bike", "tuktuk", "car"]
