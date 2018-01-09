__author__ = 'karnikamit'
from main.traffic_solution import FastestRoute


cases = input("No of tests: ")

for case in xrange(cases):
    weather = raw_input("Weather is ").lower()
    orbit1_speed = int(raw_input("Orbit1 traffic speed is "))
    orbit2_speed = int(raw_input("Orbit2 traffic speed is "))
    orbit_details = {"Orbit1": orbit1_speed, "Orbit2": orbit2_speed}
    traffic = FastestRoute(weather, orbit_details)
    print traffic.main()

