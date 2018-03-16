import RPi.GPIO as GPIO
from enum import Enum

class Status(Enum):
    PASSING = 1
    FAILING = 2
    BUILDING = 3
    UNKNOWN = 4



class LightController(object):
    def __init__(self):
        self.lights = {
            'red': 3,
            'blue': 5,
            'green': 7 }
        self.setupGPIO()

    def set_status(self, status):
        switcher = {
            Status.PASSING: lambda x: self.lights['green'],
            Status.FAILING: lambda x: self.lights['red'],
            Status.BUILDING: lambda x: self.lights['blue'] }


    def red(self, light):
        GPIO.output(light, 0)

    def setupGPIO():
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.lights.values(), GPIO.OUT)

    def cleanup():
        GPIO.cleanup()
