from scd30_i2c import SCD30

MEASUREMENT_INTERVAL = 2 # seconds

scd30 = SCD30()

scd30.set_measurement_interval(MEASUREMENT_INTERVAL)
scd30.start_periodic_measurement()

time.sleep(MEASUREMENT_INTERVAL)

for i in range(10):
	if scd30.get_data_ready():
		m = scd30.read_measurement()
		if m is not None:
			print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh: {m[2]:.2f}%")
		time.sleep(MEASUREMENT_INTERVAL)
	else:
		time.sleep(0.2)

scd30.stop_periodic_measurement()
