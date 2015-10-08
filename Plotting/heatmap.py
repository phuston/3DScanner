import serial
import time
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# raw_input("Press enter to begin the scan... [ENTER] "

clamp = lambda n, minn, maxn: max(min(maxn, n), minn)

ser = serial.Serial('/dev/ttyACM0', 9600)
print "We have hacked into the mainframe..."
time.sleep(1)

rngs = []
hdis = []
vdis = []

plotted = 0

while plotted < 500:
    if (ser.inWaiting() > 0):
        try:
            data = ser.readline()
            print data
        except Exception, e:
            print "Failed to read in the usual spot: ", e
            continue

    # try:
    #     vals = data.split(" ")
    #     rng = clamp(float(vals[0]), 0, 800)
    #     hRad = math.radians(int(vals[1]))
    #     vRad = math.radians(int(vals[2]))

    #     # hDis = rng*math.sin(hRad)
    #     # vDis = rng*math.sin(vRad)
    #     # dis = rng*math.cos(hRad)

    #     rngs.append(rng)
    #     hdis.append(hRad)
    #     vdis.append(vRad) 

    #     plotted += 1

    # except Exception, e:
    #     print e

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.ion()
plt.show()

ax.scatter(rngs,hdis,vdis, c='r', marker='o')

plt.draw()

raw_input()
