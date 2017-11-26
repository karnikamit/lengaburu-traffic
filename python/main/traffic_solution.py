__author__ = 'karnikamit'
from vehicles import Bike, Car, Tuktuk
from weather_conditions import Sunny, Rainy, Windy
from orbits import Orbit1, Orbit2


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

    def eta_orbit(self, orbit_object, orbit_speed, orbit_name):
        orbit = orbit_object()
        vehicles = self.weather_instance.vehicles
        eta = []
        for vehicle in vehicles:
            vi = self.vehicles_object[vehicle]()
            speed = vi.speed if orbit_speed > vi.speed else orbit_speed
            time = orbit.length/speed
            craters_time = vi.crater_cross_time * orbit.craters
            eta.append({"vehicle": vehicle, "speed": time + craters_time, "orbit": orbit_name})
        sorted_eta = sorted(eta, key=lambda k: k['speed'])

        return [sorted_eta[0]]

    def solution(self):
        eta_orbit1 = self.eta_orbit(Orbit1, self.orbit1_speed, "Orbit1")
        eta_orbit2 = self.eta_orbit(Orbit2, self.orbit2_speed, "Orbit2")
        eta_orbit1.extend(eta_orbit2)
        sorted_eta = sorted(eta_orbit1, key=lambda k: k['speed'])
        return "Vehicle {} on {}".format(sorted_eta[0]['vehicle'], sorted_eta[0]['orbit'])


if __name__ == "__main__":
    t = Traffic("windy", {"Orbit1": 14, "Orbit2": 20})
    print t.solution()
