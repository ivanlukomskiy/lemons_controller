import logging
from collections import deque
from statistics import median

from constants import SENSOR_READING_ACCUMULATOR_CAPACITY
from influx_writer import write_to_influx

logger = logging.getLogger(__name__)


class SensorReadingAccumulator:
    def __init__(self, name, getter):
        self.readings = deque([])
        self.name = name
        self.getter = getter

    def read(self):
        try:
            value = self.getter()
            logger.debug(f'Got value {value} for {self.name}')
            self.readings.append(value)
        except Exception as e:
            logger.error(f'Failed to get {self.name} reading: {e}')
            self.readings.append(None)
        if len(self.readings) > SENSOR_READING_ACCUMULATOR_CAPACITY:
            self.readings.popleft()

    def get(self):
        readings_filtered = [r for r in self.readings if r is not None]
        if len(readings_filtered) == 0:
            return None
        return median(readings_filtered)

    def store(self):
        value = self.get()
        logger.debug(f'Going to write {value} for {self.name}')
        if value:
            try:
                write_to_influx(self.name, value)
                logger.debug(f'Successfully written {self.name} to influx')
            except Exception as e:
                logger.error(f'Failed to write {self.name}: {e}')
        else:
            logger.error(f'Failed to write {self.name}: no data')
