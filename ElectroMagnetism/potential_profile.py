import numpy as np
from tqdm import tqdm
from functions import draw

start = -10
stop = 10
num_grid = 101
# tol = 1e-20
num_iter = 1001

x, dx = np.linspace(start, stop, num_grid, retstep = True)
X, Y = np.meshgrid(x, x)

# initial potential profile
v = np.zeros((num_grid, num_grid))
# fix_pts = []
v[:, 0] = 1
# for i in range(45, 55):
    # for j in range(49, 52):
    #     v[i, j] = 1
v[num_grid - 1, 0:51] = 2
v[0, 0:51] = 2
# fixed_points = [((0, 1), (num_grid - 1, 2), (50, 0)] 
# for pos, val in fixed_points:
#     v[pos] = val

# print(v)
# print()

# draw(X, Y, v, type = 'heat')

# lap = np.diag(-2*np.ones(num_grid), 0) + np.diag(np.ones(num_grid - 1), 1) + np.diag(np.ones(num_grid - 1), -1)
# # set boundary condition
# lap[0, 0:2] = 0
# lap[num_grid - 1, num_grid - 2 : num_grid] = 0
# # print(lap)

# Avg_mtx = np.diag(np.ones(num_grid - 1)/2, 1) + np.diag(np.ones(num_grid - 1)/2, -1)
# Avg_mtx[[0, num_grid - 1], [0, num_grid - 1]] = 1
# Avg_mtx[[0, num_grid - 1], [1, num_grid - 2]] = 0
# print(Avg_mtx)

# err = 1e2
v_old = v
# while err > tol:
for i in tqdm(range(num_iter)):
    v_new = v_old
    for i in range(1, num_grid - 1):
        for j in range(1, num_grid - 1):
            # if i in range(45, 55) and j in range(49, 52):
            #     continue
            v_new[i, j] = np.sum(v_old[[i-1, i+1, i, i], [j, j, j-1, j+1]]) / 4
    # for pos, val in fixed_points:
    #     v_new[pos] = val
    # err = np.sum((v_new - v_old)**2)
    v_old = v_new
print(v_old)
# print("Error:", err)

draw(X, Y, v_old, type = '3d')

E = np.gradient(-v_old)
print(E)

draw(X, Y, E, type = 'quiver')