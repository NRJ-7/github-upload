import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import time
plt.style.use('dark_background')

l = 0.3				# length of rod
th0 = 0.1			# initial angle of rod with x-axis in radians
Nt = 50000			# number of time instants
dt = 1e-3			# time step value in seconds

fig = plt.figure() 
ax = plt.axes(xlim=(-10, 10), ylim=(-10,10)) 
line, = ax.plot([], [], lw=2)
# setting a title for the plot 
plt.title('Euler Spiral') 
# hiding the axis details 
plt.axis('off') 

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

th = [0]
x = [0]
y = [0]
# animation function - pendulum
def animate1(i):
	# x, y values to be plotted
	phi = (th0*i*(i-1)/2) % np.pi*2
	th.append(phi)
	x.append(x[i] + l*np.cos(phi))
	y.append(y[i] + l*np.sin(phi))

	line.set_data(x, y) 
	return line,	
	
# call the animator	 
anim1 = animation.FuncAnimation(fig, animate1, init_func=init, 
							frames=Nt, interval=dt*1e4, blit=True)

"""
# save the animation as mp4 video file 
anim1.save('coil.gif',writer='imagemagick')
anim2.save('coil.gif',writer='imagemagick')
view rawcoil.py hosted with ❤ by GitHub
"""
plt.show()