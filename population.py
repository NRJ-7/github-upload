import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import time
plt.style.use('dark_background')


Nt = 500				# number of time instants
dt = 1				# time step value in seconds
r_in = 3.8			# biotic capacity
r_fn = 4
p_in = 0.01			# initial population

fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)
#ax = plt.axes(xlim=(-2, Nt*dt), ylim=(-0.2*r,2*r)) 
#line, = ax.plot([], [], lw=2)
"""
# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 
"""
# lists to store x and y axis points
t = np.linspace(0,Nt*dt,Nt + 1,endpoint=True)
rvals = np.linspace(r_in,r_fn,5,endpoint=True)
for r in rvals:
	p = [p_in]
	for i in range(Nt):
		p.append(r*p[i]*(1 - p[i]))
	plt.plot(t,p)

"""
# animation function 
def animate(i): 
	# x, y values to be plotted 
	p.append(r*p[i]*(1 - p[i]))
	x.append(i + 1)

	line.set_data(x, p) 
	return line,
"""	
# setting a title for the plot 
#plt.title('Population Graph with matplotlib!') 
# hiding the axis details 
#plt.axis('off') 

# call the animator	 
#anim = animation.FuncAnimation(fig, animate, init_func=init, 
#							frames=Nt, interval=dt*1000, blit=True) 
"""
# save the animation as mp4 video file 
anim.save('coil.gif',writer='imagemagick') 
view rawcoil.py hosted with ❤ by GitHub
"""
plt.grid('on')
plt.show(fig)