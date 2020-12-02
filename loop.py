import argparse
import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from sensor_reading_accumulator import SensorReadingAccumulator
from sensors import get_light_level, get_resistive_ground_humidity, get_capacitive_ground_humidity

parser = argparse.ArgumentParser()
parser.add_argument(
    "-log",
    "--log",
    default="warning",
    help=(
        "Provide logging level. "
        "Example --log debug', default='warning'"),
    )

options = parser.parse_args()
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(options.log.lower())
if level is None:
    raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)

sensors = [
    SensorReadingAccumulator('light_level', get_light_level),
    SensorReadingAccumulator('resistive_ground_humidity', get_resistive_ground_humidity),
    SensorReadingAccumulator('capacitive_ground_humidity', get_capacitive_ground_humidity),
]


def refresh_readings():
    logger.debug("Refreshing readings")
    for sensor in sensors:
        sensor.read()


def store_metrics():
    logger.debug("Saving readings")
    for sensor in sensors:
        sensor.store()


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_readings, CronTrigger(second='*/15'))
    scheduler.add_job(store_metrics, CronTrigger(second='0'))
    scheduler.start()

    try:
        while True:
            time.sleep(5)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
