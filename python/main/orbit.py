__author__ = 'karnikamit'


class Orbit(object):
    def __init__(self, length, craters, orbit):
        """
        Path to destination

        :param (int) length: length of the orbit
        :param (int) craters: no. of craters in the orbit
        :param (str) orbit: orbit name
        """
        self.length = length
        self.craters = craters
        self.orbit = orbit

    def __str__(self):
        return self.orbit
