from __future__ import division
import logging
from vehicle import Vehicle
from weather_condition import Weather
from orbit import Orbit
import config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FastestRoute(object):
    def __init__(self, weather, orbit_details):
        self.orbit1 = Orbit(config.ORBIT1_LENGTH, config.ORBIT1_CRATERS, "Orbit1", orbit_details["Orbit1"])
        self.orbit2 = Orbit(config.ORBIT2_LENGTH, config.ORBIT2_CRATERS, "Orbit2", orbit_details["Orbit2"])
        try:
            self.weather = config.WEATHER_CONDITIONS[weather.lower()]
            self.vehicles = self.weather["VEHICLES"]
            self.craters_reduced = self.weather["CATERS_REDUCED"]
        except (KeyError, AttributeError), e:
            raise Exception(e)
