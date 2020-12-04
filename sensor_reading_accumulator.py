import logging

from influx_writer import write_to_influx

logger = logging.getLogger(__name__)


class SensorReadingAccumulator:
    def __init__(self, name, getter):
        self.name = name
        self.getter = getter

    def read(self):
        try:
            value = self.getter()
            logger.debug(f'Got value {value} for {self.name}')
            write_to_influx(self.name, value)
            logger.debug(f'Successfully written {self.name} to influx')
        except Exception as e:
            logger.error(f'Failed to handle {self.name} reading: {e}')
