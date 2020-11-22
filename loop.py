import logging
import os
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
    print("Refreshing readings")


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_readings, CronTrigger(second='0'))
    scheduler.start()

    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    logging.error('Print something')

    try:
        while True:
            print('tick')
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
