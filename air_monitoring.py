import bme280
import smbus2
import time
from datetime import datetime
import sqlite3
import signal

MEASUREMENT_INTERVAL = 2

# Stuff for BME280
ADDRESS_BME = 0x76

I2C_PORT = 1
bus = smbus2.SMBus(I2C_PORT)

calibration_params = bme280.load_calibration_params(bus, ADDRESS_BME)

def measure():
	global ADDRESS_BME
	global calibration_params

	sample = bme280.sample(bus, ADDRESS_BME, calibration_params)
	data = {'temperature': sample.temperature, 'pressure': sample.pressure, 'humidity': sample.humidity}
	# data = {'temperature': 1.5, 'pressure': 2.1, 'humidity': 4}
	return data

with sqlite3.connect('bme.db') as con:
	con.execute('''
	CREATE TABLE IF NOT EXISTS "bme_measurements" (
		"datetime"	TEXT,
		"temperature"	REAL,
		"pressure"	REAL,
		"humidity"	REAL
	);''')

	for i in range(10):
		current_time = str(datetime.now())
		data = measure()
		to_insert = [
			(current_time, data["temperature"], data["pressure"], data["humidity"]),
		]
		con.executemany("INSERT INTO bme_measurements ('datetime', 'temperature', 'pressure', 'humidity') VALUES (?, ?, ?, ?)", to_insert)
		con.commit()
		time.sleep(MEASUREMENT_INTERVAL)
