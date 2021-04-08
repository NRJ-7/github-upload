from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

ep0 = 8.854e-12 # Farads / metre 

def draw(*args, type = 'line'):
    fig = plt.figure()
    if type == '3d':
        ax = fig.gca(projection = '3d')
        ax.plot_surface(args[0], args[1], args[2], cmap = 'viridis', edgecolor = 'none')
    else:
        ax = fig.gca()
        if type == 'line':
            ax.plot(args[0], args[1])
        elif type == 'heat':
            im = ax.pcolormesh(args[0], args[1], args[2], shading = 'auto')
            fig.colorbar(im, ax = ax)
        elif type == 'quiver':
            ax.quiver(args[0], args[1], args[2][1], args[2][0])
        elif type == 'stream':
            ax.streamplot(args[0], args[1], args[2][1], args[2][0])
        elif type == 'scatter':
            ax.scatter(args[0], args[1])
    plt.show()

def distance(*pos):
    l = len(pos) // 2
    sum = 0
    for i in range(l):
        sum += (pos[i] - pos[i + l])**2
    return sum**0.5

def get_potential(charges, *args):
    if len(args) == 2: # 2D case
        X, Y = args[0], args[1]
        v = np.zeros(X.shape)
        for i in tqdm(range(X.shape[0])):
            for j in range(X.shape[1]):
                for pos, val in charges.items():
                    if X[i, j] == pos[0] and Y[i, j] == pos[1]:
                        continue
                    dist = distance(X[i, j], Y[i, j], pos[0], pos[1])
                    v[i, j] += val / (4*np.pi*ep0*dist)
    else: # 1D case
        x = args[0]
        v = np.zeros(x.shape)
        for i in tqdm(range(x.shape[0])):
            for pos, val in charges.items():
                if x[i] == pos[0]:
                    v[i] = None
                    continue
                dist = abs(x[i] - pos[0])
                v[i] += val / (4*np.pi*ep0*dist)
    return v

def anim(x, evol, dt):
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure()
    ax = plt.axes(xlim = (x[0], x[len(x)-1]), ylim = (-1, 1))
    line, = ax.plot([], [], lw=2)

    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        line.set_data(x, evol[i])
        if i == len(evol) - 1:
            print('done')
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = FuncAnimation(fig, animate, init_func = init,
                                frames=len(evol), interval = dt, blit = True)
    plt.show()


def divergence(E, dx, dy):
    Ex = E[1]
    Ey = E[0]

    return np.gradient(Ex, dx, axis = 1) + np.gradient(Ey, dy, axis = 0)
