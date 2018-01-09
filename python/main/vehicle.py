__author__ = 'karnikamit'


class Vehicle(object):
    def __init__(self, speed, crater_cross_time, vehicle):
        """

        :param (int) speed: Max speed of the vehicle
        :param (int) crater_cross_time: crater cross time of the vehicle
        :param (str) vehicle: Name of the vehicle
        """
        self.speed = speed
        self.crater_cross_time = crater_cross_time
        self.vehicle = vehicle

    def __str__(self):
        return self.vehicle


# class Bike(object):
#     def __init__(self):
#         self.speed = 10
#         self.crater_cross_time = 2
#
#     def __str__(self):
#         return "Bike"
#
#
# class Tuktuk(object):
#     def __init__(self):
#         self.speed = 12
#         self.crater_cross_time = 1
#
#     def __str__(self):
#         return "Tuktuk"
#
#
# class Car(object):
#     def __init__(self):
#         self.speed = 20
#         self.crater_cross_time = 3
#
#     def __str__(self):
#         return "Car"
