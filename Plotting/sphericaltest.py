import numpy as np

phi=np.radians(90)
theta=np.radians(90)
rng=10

x = rng*np.cos(theta)*np.sin(phi)
y = rng*np.sin(theta)*np.sin(phi)
z = rng*np.cos(phi)

print (x,y,z)