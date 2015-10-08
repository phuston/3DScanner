import serial
from time import sleep
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def transform_coord(data):
	# Function to translate voltage into distance
	rng = (17640*(int(data[0])**(-1.071)))

	# Throw out inaccurate values over 80cm
	if rng > 80:
		return 0

	theta = data[1]
	phi = data[2]

	# Transform spherical coordinates into cartesian
	x = rng*np.cos(theta)*np.sin(phi)
	y = rng*np.sin(theta)*np.sin(phi)
	z = rng*np.cos(phi)

	return [x,y,z]

def parse_serial(data):
	# Split serival values, convert to correct data types
	vals = data.split(" ")
	rng = float(vals[0])

	theta = np.radians(int(vals[1]))
	phi = np.radians(int(vals[2]))

	return [rng, theta, phi]

if __name__ == '__main__':
	# Set up arrays to hold point data temporarily

	# Points in one color below threshold value to show the letter
	xletter = []
	yletter = []
	zletter = []

	# Points in another color above threshold value to show background
	xback = []
	yback = []
	zback = []

	# Set up plotting
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('Z')

	plt.ion() # Make the plot 'interactive'
	plt.show()

	serin = ""

	# Set up the serial connection
	raw_input("Press ENTER to begin Serial connection. ")
	ser = serial.Serial('/dev/ttyACM1',9600,timeout=50)
	print "Hacking into the mainframe... "
	sleep(2)

	print "Hacking complete"
	sleep(1)
	raw_input("Press ENTER to begin. ")

	plots = 0

	while plots < 400:
		ser.write('d') # Ping Arduino to send data back

		# Check to see if data is available
		if (ser.inWaiting() > 0):
			serin = ser.readline()

			if "STOP" in serin:
				break

		try:
			x,y,z = transform_coord(parse_serial(serin))

		except Exception, e:
			print e
			continue

		# Add point data to temporary value stores
		if z > letter_threshold:
			xback.append(x)
			yback.append(y)
			zback.append(z)
		else:
			xletter.append(x)
			yletter.append(y)
			zletter.append(z)

		# If 20 points have been captured, add them to the plot in correct colors
		if (len(xletter) + len(xback)) >= 20:
			ax.scatter(zletter,xletter,yletter,c='r',marker='.')
			ax.scatter(zback,xback,yback,c='b',marker='.')
			xletter, yletter, zletter, xback, yback, zback = [], [], [], [], [], []

			plt.draw()
			sleep(.1)

			plots += 1

	raw_input("Press ENTER to exit the render.")

