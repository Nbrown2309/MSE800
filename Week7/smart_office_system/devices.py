from abc import ABC, abstractmethod


# Parent class
class SmartDevice(ABC):

    @abstractmethod
    def device_status(self):
        pass


# Child class 1
class SmartLight(SmartDevice):

    def device_status(self):
        print("Smart Light is ON")


# Child class 2
class SmartFan(SmartDevice):

    def device_status(self):
        print("Smart Fan is ON")


# Child class 3
class SmartAirConditioner(SmartDevice):

    def device_status(self):
        print("Smart Air Conditioner is ON")