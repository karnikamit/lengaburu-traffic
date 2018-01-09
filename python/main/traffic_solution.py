from __future__ import division
# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from orbit import Orbit
import logging
import config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Distance = Speed x Time


class FastestRoute(object):
    def __init__(self, weather, orbit_details):
        self.orbit1 = Orbit(config.ORBIT1_LENGTH, config.ORBIT1_CRATERS, "Orbit1", orbit_details["Orbit1"])
        self.orbit2 = Orbit(config.ORBIT2_LENGTH, config.ORBIT2_CRATERS, "Orbit2", orbit_details["Orbit2"])
        try:
            self.weather = config.WEATHER_CONDITIONS[weather.lower()]
        except KeyError:
            raise KeyError

    @staticmethod
    def _get_speed(orbit_object, vehicle):
        return orbit_object.speed if orbit_object.speed < vehicle["SPEED"] else vehicle["SPEED"]

    def _get_craters(self, orbit_object):
        """
        Get total no of craters after calculating with weather conditions
        :param (Orbit) orbit_object:
        :return (int): total number of craters after calculating with weather conditions
        """
        craters_reduced_percent = self.weather["CATERS_REDUCED"]
        craters_increased_percent = self.weather["CATERS_INCREASED"]
        total_craters = orbit_object.craters
        if craters_reduced_percent:
            less_craters = total_craters * craters_reduced_percent
            total_craters = total_craters - less_craters
        elif craters_increased_percent:
            more_craters = total_craters * craters_increased_percent
            total_craters = total_craters + more_craters
        return total_craters

    def _get_time(self, orbit, vehicle):
        """

        :param (Orbit) orbit:
        :param (str) vehicle: name of the vehicle
        :return (int): time taken by vehicle
        """
        properties = config.VEHICLES[vehicle]
        v_speed = self._get_speed(orbit, properties)
        time = orbit.length/v_speed
        time += self._get_craters(orbit) * properties["CRATER_CROSS_TIME"]
        return time

    def test(self):
        print self._get_time(self.orbit1, "BIKE")


fs = FastestRoute("windy", {"Orbit1": 14, "Orbit2": 20})
fs.test()
