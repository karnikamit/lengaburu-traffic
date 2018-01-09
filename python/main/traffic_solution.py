from __future__ import division
# -*- coding: utf-8 -*-
__author__ = 'karnikamit'
from orbit import Orbit
import logging
import config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

    def _get_orbit_min_time(self, orbit):
        """

        :param (Orbit) orbit:
        :return (int): minimum time(hrs) to cover this orbit
        """
        speeds = {}
        vehicles = self.weather["VEHICLES"]
        for vehicle in vehicles:
            time_taken = self._get_time(orbit, vehicle)
            speeds[vehicle] = time_taken
        return speeds

    def main(self):
        ob1_time = self._get_orbit_min_time(self.orbit1)
        ob2_time = self._get_orbit_min_time(self.orbit2)
        min_time = min(min(ob1_time.values()), min(ob2_time.values()))
        vehicle, orbit = "", 0
        if min_time in ob1_time.values():
            ob = ob1_time
            orbit = 1
        else:
            ob = ob2_time
            orbit = 2
        for v in ob:
            if ob[v] == min_time:
                vehicle = v
        return "Vehicle {} on Orbit{}".format(vehicle, orbit)


if __name__ == "__main__":
    fs = FastestRoute("sunny", {"Orbit1": 12, "Orbit2": 10})
    print fs.main()
