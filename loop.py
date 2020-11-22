import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from sensor_reading_accumulator import SensorReadingAccumulator
from sensors import get_light_level, get_resistive_ground_humidity, get_capacitive_ground_humidity

sensors = [
    SensorReadingAccumulator('light_level', get_light_level),
    SensorReadingAccumulator('resistive_ground_humidity', get_resistive_ground_humidity),
    SensorReadingAccumulator('capacitive_ground_humidity', get_capacitive_ground_humidity),
]


def refresh_readings():
    logging.debug("Refreshing readings")
    for sensor in sensors:
        sensor.read()


def store_metrics():
    logging.debug("Saving readings")
    for sensor in sensors:
        sensor.store()


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_readings, CronTrigger(second='0'))
    scheduler.add_job(store_metrics, CronTrigger(minute='*/5'))
    scheduler.start()

    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
