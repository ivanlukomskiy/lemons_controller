import logging
from collections import deque
from statistics import mean

from constants import SENSOR_READING_ACCUMULATOR_CAPACITY
from influx_writer import write_to_influx


class SensorReadingAccumulator:
    def __init__(self, name, getter):
        self.readings = deque([])
        self.name = name
        self.getter = getter

    def read(self):
        try:
            value = self.getter()
            self.readings.append(value)
        except Exception as e:
            logging.error(f'Failed to get {self.name} reading: {e}')
            self.readings.append(None)
        if len(self.readings) > SENSOR_READING_ACCUMULATOR_CAPACITY:
            self.readings.popleft()

    def get(self):
        readings_filtered = [r for r in self.readings if r is not None]
        if len(readings_filtered) == 0:
            return None
        return mean(readings_filtered)

    def store(self):
        value = self.get()
        if value:
            write_to_influx(self.name, value)
        else:
            logging.error(f'Failed to write {self.name}: no data')
