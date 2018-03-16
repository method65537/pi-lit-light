import sys
import os
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

    def turn_on(self, light):
        GPIO.output(light, 1)

    def turn_off(self, light):
        GPIO.output(light, 0)

    def all_off(self):
        GPIO.output(self.lights.values(), 0)

    def set_status(self, status):
        on_light = None
        if status == Status.PASSING:
            on_light = self.lights['green']
        elif status == Status.FAILING:
            on_light = self.lights['red']
        elif status == Status.BUILDING:
            on_light = self.lights['blue']

        self.all_off()
        self.turn_on(on_light)

    def setupGPIO(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.lights.values(), GPIO.OUT)

    def cleanup(self):
        GPIO.cleanup()

# for demo
#  python pi-lit-light/lightcontroller.py red
#  python pi-lit-light/lightcontroller.py green
#  python pi-lit-light/lightcontroller.py blue

if __name__ == '__main__':
    if len(sys.argv) > 1:
        color = sys.argv[1]
        status = None
        if color == 'red':
            os.system('omxplayer -o local ~/Downloads/test.mp3')
            status = Status.FAILING
        elif color == 'green':
            status = Status.PASSING
        elif color == 'blue':
            status = Status.BUILDING
        controller = LightController()
        controller.set_status(status)
