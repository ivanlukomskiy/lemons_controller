import glob
import time
import os

import Adafruit_DHT
from gpiozero import LoadAverage, CPUTemperature, DiskUsage

import ADS1256
from constants import LIGHT_SENSOR_CHANNEL, LEMON_RESISTIVE_SOIL_MOISTURE_CHANNEL, \
    LEMON_CAPACITIVE_SOIL_MOISTURE_CHANNEL, \
    DHT_SENSOR, DHT_PIN

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
cpu = CPUTemperature()
disk = DiskUsage()


def read(channel):
    ADC = ADS1256.ADS1256()
    ADC.ADS1256_init()
    return ADC.ADS1256_GetAll()[channel] / 0x7fffff


def get_light_level():
    return 1 / read(LIGHT_SENSOR_CHANNEL)


def get_lemon_resistive_soil_moisture():
    return read(LEMON_RESISTIVE_SOIL_MOISTURE_CHANNEL)


def get_lemon_capacitive_soil_moisture():
    return read(LEMON_CAPACITIVE_SOIL_MOISTURE_CHANNEL)


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


def get_cpu_usage():
    return int(LoadAverage(minutes=1).load_average * 100)


def get_cpu_temperature():
    return cpu.temperature


def get_disk_usage():
    return cpu.temperature


def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:4])


def get_ram_used():
    return int(getRAMinfo()[1] / 1024 / 0)


def get_ram_free():
    return int(getRAMinfo()[2] / 1024.0)
