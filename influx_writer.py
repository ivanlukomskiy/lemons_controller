import time

from influxdb import InfluxDBClient

from constants import DB_NAME

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database(DB_NAME)


def write_to_influx(metric_name, value):
    data = []
    timestamp = int(time.time())
    data.append(f'{metric_name} value={value} {timestamp}')
