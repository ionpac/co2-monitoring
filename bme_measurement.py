import bme280
import smbus2
import time

# Stuff for BME280
ADDRESS_BME = 0x76


I2C_PORT = 1
bus = smbus2.SMBus(I2C_PORT)

calibration_params = bme280.load_calibration_params(bus, ADDRESS_BME)

def measure():
	global ADDRESS_BME
	global calibration_params
	global TEMPERATURE_OFFSET

	sample = bme280.sample(bus, ADDRESS_BME, calibration_params)
	data = {'temperature': sample.temperature, 'pressure': sample.pressure, 'humidity': sample.humidity}
	print(data)

for i in range(10):
	measure()
