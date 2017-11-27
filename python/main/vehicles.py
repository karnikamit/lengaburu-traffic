__author__ = 'karnikamit'


class Bike(object):
    def __init__(self):
        self.speed = 10
        self.crater_cross_time = 2

    def __str__(self):
        return "Bike"


class Tuktuk(object):
    def __init__(self):
        self.speed = 12
        self.crater_cross_time = 1

    def __str__(self):
        return "Tuktuk"


class Car(object):
    def __init__(self):
        self.speed = 20
        self.crater_cross_time = 3

    def __str__(self):
        return "Car"
