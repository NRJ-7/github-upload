import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import time
plt.style.use('dark_background')

g = 9.8				# gravity in m/(s^2)
m = 1				# mass of ball in kg
u_in = (100,20)	# initial velocity in m/s
pos_in = (0,0)		# initial position of ball
Nt = 50000			# number of time instants
dt = 0.01			# time step value in seconds
ge = 0.7			# coefficient of elastic collision with ground
f = 0.2				# coefficient of friction

fig = plt.figure() 
ax = plt.axes(xlim=(-5, 800), ylim=(-5, 30)) 
line, = ax.plot([], [], lw=2)

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points
x = [pos_in[0]]
y = [pos_in[1]]
ux = [u_in[0]]
uy = [u_in[1]]

# animation function 
def animate(i): 
	# x, y values to be plotted 
	ux.append(ux[i] - f*ux[i]*dt/m)
	uy.append(uy[i] - f*uy[i]*dt/m - g*dt)
	x.append(x[i] + ux[i]*dt)
	y.append(y[i] + uy[i]*dt)
	if y[i + 1] <= 0.1:
		uy[i + 1] = -uy[i]*ge
	
	line.set_data(x, y) 
	return line, 

###################################################
###################################################

"""
(tim,dt) = np.linspace(0,20,Nt,endpoint=True,retstep=True)	# time

for i in range(Nt - 1):
	ux.append(ux[i])
	uy.append(uy[i] - g*dt)
	x.append(x[i] + ux[i]*dt)
	y.append(y[i] + uy[i]*dt)
	if y[i + 1] <= 0:
		uy[i + 1] = -uy[i + 1]
	plt.plot(x,y)
	plt.show()
	time.sleep(dt)
"""
###################################################
###################################################
	
# setting a title for the plot 
plt.title('Creating a projectile with matplotlib!') 
# hiding the axis details 
plt.axis('off') 

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init, 
							frames=Nt, interval=dt, blit=True) 
"""
# save the animation as mp4 video file 
anim.save('coil.gif',writer='imagemagick') 
view rawcoil.py hosted with ❤ by GitHub
"""
plt.show()