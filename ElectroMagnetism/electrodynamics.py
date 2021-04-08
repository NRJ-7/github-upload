import numpy as np
from functions import *

charge = 1e-13 # Coulomb
c = 299792458 # speed of light (metre / second)

start = -1 # metre
stop = 1 # metre
num_grid = 5001
Nt = 1001

x, dx = np.linspace(start, stop, num_grid, retstep = True)
offset = dx / 2 # to avoid infinities 

t, dt = np.linspace(0, 1e-10, Nt, retstep = True)

# Define initial charge profile
"""
Define charge profile.
"""
charges = {(0 + offset,) : charge}
# rho = np.zeros(num_grid)
# for pos, val in charges.items():
#     for i in range(num_grid):
#         if x[i] <= pos[0] and x[i+1] > pos[0]:
#             rho[i] += charge / dx
# draw(x, rho)


# Calculate initial potential profile
"""
Define a function that takes charge profile as input and calculates the initial potential profile.
"""
v_init = get_potential(charges, x)
v_init[0] = v_init[1]
v_init[num_grid-1] = v_init[num_grid-2]
draw(x, v_init)
E_init = np.gradient(-v_init, dx)
draw(x, E_init)
# v_init = np.zeros(num_grid)
# for i in range(1, num_grid-1):
#     v_init[i] = np.sin(x[i])
# v_init[0] = v_init[1]
# v_init[num_grid-1] = v_init[num_grid-2]
# draw(x, v_init)
# E_init = np.gradient(-v_init, dx)
# draw(x, E_init)


# Use maxwell equations to calculate time evolution
v_evol = [v_init, v_init]

E_evol = [E_init, E_init]

for n in tqdm(range(1, Nt)):
    E = E_evol[n]
    d2V = np.gradient(-E, dx)
    v_new = (c*dt)**2 * d2V + 2*v_evol[n] - v_evol[n-1]
    v_new[0] = v_new[1]
    v_new[num_grid-1] = v_new[num_grid-2]
    # draw(x, v_new)
    E_new = np.gradient(-v_new, dx)
    # draw(x, E_new)
    v_evol.append(v_new)
    E_evol.append(E_new)

anim(x, v_evol, dt)
"""
GADBAD HAI!!! :( 
"""

# plt.show()