from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

x_line = np.linspace(-15, 15, 1000)
psi = (1/((np.pi**0.25))*np.exp(-x_line**2/2))
y_line = psi*np.cos(x_line)
z_line = psi*np.sin(x_line)
ax.plot3D(x_line, y_line, z_line, 'red')
"""
z_points = 15 * np.random.random(100)
x_points = np.cos(z_points) + 0.1 * np.random.randn(100)
y_points = np.sin(z_points) + 0.1 * np.random.randn(100)
ax.scatter3D(x_points, y_points, z_points, c=z_points, cmap='hsv');
"""
plt.show()
"""
fig = plt.figure()
x = np.linspace(-10,10)
i = np.sqrt(-1)

psi = (1/((np.pi**0.25))*exp(i*k*x - x**2/2)

fig.plt.plot(x,psi)
"""