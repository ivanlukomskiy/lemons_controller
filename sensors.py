import ADS1256
import Adafruit_DHT
import glob
import time

from constants import LIGHT_SENSOR_CHANNEL, RESISTIVE_GROUND_HUMIDITY_CHANNEL, CAPACITIVE_GROUND_HUMIDITY_CHANNEL, \
    DHT_SENSOR, DHT_PIN


ADC = ADS1256.ADS1256()
ADC.ADS1256_init()

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read(channel):
    return ADC.ADS1256_GetAll()[channel] / 0x7fffff


def get_light_level():
    return 1 / read(LIGHT_SENSOR_CHANNEL)


def get_resistive_ground_humidity():
    return read(RESISTIVE_GROUND_HUMIDITY_CHANNEL)


def get_capacitive_ground_humidity():
    return read(CAPACITIVE_GROUND_HUMIDITY_CHANNEL)


def get_air_temperature():
    _, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return temperature


def get_air_humidity():
    humidity, _ = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return humidity


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


def get_ground_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
