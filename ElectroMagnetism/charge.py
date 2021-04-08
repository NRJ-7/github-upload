import numpy as np
from functions import *

charge = 1 # Coulomb

start = -1 # metre
stop = 1 # metre
num_grid = 1001

x, dx = np.linspace(start, stop, num_grid, retstep = True)
offset = dx / 2 # to avoid infinites
X, Y = np.meshgrid(x, x)

# Specify charge positions
charges = {(-0.5 + offset, 0 + offset) : charge, (0.5 + offset , 0 + offset) : -charge}
# charges = {}
# for i in range(num_grid // 4, 3*num_grid // 4):
#     charges[(x[i] + 5e-3 , 0)] = charge

# Get potential profile from given charge profile
v = get_potential(charges, X, Y)
draw(X, Y, v, type = '3d')

# Get Electric field from calculated potential profile
E = np.gradient(-v, dx, dx)
draw(X, Y, E, type = 'stream')

draw(X, Y, ep0*divergence(E, dx, dx), type = 'heat')

plt.show()