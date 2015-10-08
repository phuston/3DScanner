import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def randrange(n, vmin, vmax):
    return (vmax-vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xdegrees = range(-30, 30)

ydegrees = range(-30, 30)

ranges = [-(.03*(x**2)+100) for x in xdegrees]

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.ion()
plt.show()

for ydeg in ydegrees:
	yrad = math.radians(ydeg)
	for i in range(len(xdegrees)):
		xrad = math.radians(xdegrees[i])
		rng = ranges[i]

		yval = rng*math.sin(yrad)
		xval = rng*math.sin(xrad)

		print "range: {}, xval:{}, yval: {}".format(rng, xval, yval)

		ax.scatter([xval], [yval], [rng], c='r', marker='o')

		plt.draw()