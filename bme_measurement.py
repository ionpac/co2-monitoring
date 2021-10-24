import bme380
import i2c_pwm
import time

# Stuff for BME280
ADDRESS_BME = 0x76
calibration_params = None

def measure():
	global ADDRESS_BME
	global calibration_params
	global TEMPERATURE_OFFSET

	with i2c_pwm.i2c_lock:
		sample = bme280.sample(i2c_pwm.i2c, ADDRESS_BME, calibration_params)
	data = {'temperature': sample.temperature, 'pressure': sample.pressure, 'humidity': sample.humidity}
	print(data)

def setup():
	with i2c_pwm.i2c_lock:
		try:
			calibration_params = bme280.load_calibration_params(i2c_pwm.i2c, ADDRESS_BME)
		except Exception as e:
			print(e)


setup()

for i in range(10):
	measure()
