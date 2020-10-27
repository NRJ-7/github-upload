import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import time
plt.style.use('dark_background')

hook = (0,2)		# position of hook
l = 1				# length of rod
g = 9.8				# gravity in m/(s^2)
m = 1				# mass of ball in kg
th_in = np.pi/3			# initial angle of rod with x-axis in radians
w_in = 0			# initial angular velocity in rads/s
Nt = 50000			# number of time instants
dt = 0.05			# time step value in seconds
f = 0.5				# friction coefficient

fig = plt.figure() 
ax = plt.axes(xlim=(-2, 2), ylim=(0,3)) 
line, = ax.plot([], [], lw=2)
# setting a title for the plot 
plt.title('Creating a pendulum with matplotlib!') 
# hiding the axis details 
plt.axis('off') 

#fig = plt.figure() 
#ax = plt.axes(xlim=(-2,5), ylim=(-5,5)) 
#line, = ax.plot([], [], lw=2)
## setting a title for the plot 
#plt.title('Phase space') 
#plt.grid(color='w')

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points
th = [th_in]
w = [w_in]

# animation function - pendulum
def animate1(i):
	# x, y values to be plotted 
	w.append(w[i] + g*np.cos(th[i])*dt/l - f*w[i]*dt/m)
	th.append(th[i] + w[i+1]*dt)
	x_ball = (hook[0] - l*np.cos(th[i]))
	y_ball = (hook[1] - l*np.sin(th[i]))
	#w.append((2*g/l/*np.sin(th[i]*np.pi))**0.5*np.sin(th[i]*np.pi))
	x = np.linspace(hook[0],x_ball,10,endpoint=True)
	y = np.linspace(hook[1],y_ball,10,endpoint=True)

	line.set_data(x, y) 
	return line,	

# animation function - phase space 
def animate2(i):
	line.set_data(th, w) 
	return line,	
	
# call the animator	 
anim1 = animation.FuncAnimation(fig, animate1, init_func=init, 
							frames=Nt, interval=dt*1e3, blit=True)

#anim2 = animation.FuncAnimation(fig, animate2, init_func=init, 
#							frames=Nt, interval=dt*1e3, blit=True)
"""
# save the animation as mp4 video file 
anim1.save('coil.gif',writer='imagemagick')
anim2.save('coil.gif',writer='imagemagick')
view rawcoil.py hosted with ❤ by GitHub
"""
plt.show()