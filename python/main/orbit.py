__author__ = 'karnikamit'


class Orbit(object):
    def __init__(self, length, craters, orbit, speed):
        """
        Path to destination

        :param (int) length: length of the orbit
        :param (int) craters: no. of craters in the orbit
        :param (str) orbit: orbit name
        :param (int) speed: Max speed of the orbit
        """
        self.length = length
        self.craters = craters
        self.speed = speed
        self.orbit = orbit

    def __str__(self):
        return self.orbit
