import ADS1256

from constants import LIGHT_SENSOR_CHANNEL, RESISTIVE_GROUND_HUMIDITY_CHANNEL, CAPACITIVE_GROUND_HUMIDITY_CHANNEL

ADC = ADS1256.ADS1256()
ADC.ADS1256_init()
ADC_Value = ADC.ADS1256_GetAll()


def read(channel):
    return ADC.ADS1256_GetChannalValue(channel) * 5.0 / 0x7fffff


def get_light_level():
    return 1 / read(LIGHT_SENSOR_CHANNEL)


def get_resistive_ground_humidity():
    return read(RESISTIVE_GROUND_HUMIDITY_CHANNEL)


def get_capacitive_ground_humidity():
    return read(CAPACITIVE_GROUND_HUMIDITY_CHANNEL)
