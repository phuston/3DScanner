import serial
from time import sleep
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def parse_serial(data):

	vals = data.split(" ")
	rng = (10650.08*(int(vals[0]))**(-0.935)) - 10

	theta = np.radians(int(vals[1]))

	return [rng, theta]

if __name__ == '__main__':
	degrees = []
	rngs = []

	raw_input("Press ENTER to begin Serial connection. ")
	ser = serial.Serial('/dev/ttyACM1',9600,timeout=50)
	print "Hacking into the mainframe... "
	sleep(3)
	# ser.readline()
	raw_input("Press ENTER to begin. ")

	# ser.readline()

	plots = 0

	serin = ""
	ser.write('d')
	sleep(1)

	while plots < 100:
		ser.write('d')
		if (ser.inWaiting() > 0):
			serin = ser.readline()

		try:
			rng,theta = parse_serial(serin)
			if rng > 80:
				rng = 80
			degrees.append(theta)
			rngs.append(rng)
			plots +=1

		except Exception, e:
			print e
			continue

		sleep(.1)

	plt.plot(degrees, rngs)
	plt.xlabel("Degrees (Radians)")
	plt.ylabel("Distance")
	plt.title("2d Letter Scan (Degrees vs. Distance)")
	plt.show()

	raw_input("Press ENTER to exit the render.")

