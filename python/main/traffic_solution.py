__author__ = 'karnikamit'
import logging
from vehicles import Bike, Car, Tuktuk
from weather_conditions import Sunny, Rainy, Windy
from orbits import Orbit1, Orbit2

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Traffic(object):
    def __init__(self, weather, traffic_speeds):
        weather_objects = {"sunny": Sunny, "rainy": Rainy, "windy": Windy}
        self.vehicles_object = {"bike": Bike, "tuktuk": Tuktuk, "car": Car}
        try:
            self.weather_instance = weather_objects[weather.lower()]()
            self.orbit1_speed = traffic_speeds['Orbit1']
            self.orbit2_speed = traffic_speeds['Orbit2']
        except Exception, e:
            raise Exception("Wrong input - %s" % e)

    def eta_orbit(self, orbit_object, orbit_speed):
        orbit = orbit_object()
        vehicles = self.weather_instance.vehicles
        eta = []
        for vehicle in vehicles:
            vi = self.vehicles_object[vehicle]()
            speed = vi.speed if orbit_speed > vi.speed else orbit_speed
            time = orbit.length/speed
            craters_time = vi.crater_cross_time * orbit.craters
            eta.append({"vehicle": vehicle, "eta": time + craters_time, "orbit": str(orbit)})
        sorted_eta = sorted(eta, key=lambda k: k['eta'])
        logger.info("sorted etas: {}".format(sorted_eta))
        return [sorted_eta[0]]

    def solution(self):
        eta_orbit1 = self.eta_orbit(Orbit1, self.orbit1_speed)
        eta_orbit2 = self.eta_orbit(Orbit2, self.orbit2_speed)
        eta_orbit1.extend(eta_orbit2)
        sorted_eta = sorted(eta_orbit1, key=lambda k: k['eta'])
        return "Vehicle {0} on {1}".format(sorted_eta[0]['vehicle'], sorted_eta[0]['orbit'])


if __name__ == "__main__":
    t = Traffic("sunny", {"Orbit1": 12, "Orbit2": 10})
    print t.solution()
