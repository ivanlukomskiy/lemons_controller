import gpioexp

from constants import LIGHT_SENSOR_PIN, RESISTIVE_GROUND_HUMIDITY_PIN, CAPACITIVE_GROUND_HUMIDITY_PIN

exp = gpioexp.gpioexp()


def get_light_level():
    return 1 / exp.analogRead(LIGHT_SENSOR_PIN)


def get_resistive_ground_humidity():
    return exp.analogRead(RESISTIVE_GROUND_HUMIDITY_PIN)


def get_capacitive_ground_humidity():
    return exp.analogRead(CAPACITIVE_GROUND_HUMIDITY_PIN)
