import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import time
plt.style.use('dark_background')

hook = (0,2)		# position of hook
l1 = 1				# length of rod for ball1
l2 = 1				# length of rod for ball2
g = 9.8				# gravity in m/(s^2)
m1 = 1				# mass of ball1 in kg
m2 = 1				# mass of ball2 in kg
th1_in = 0			# initial angle of rod with x-axis of ball1
th2_in = 0			# initial angle of rod with x-axis of ball2
w1_in = 0			# initial angular velocity of ball1
w2_in = 0			# initial angular velocity of ball2
Nt = 50000			# number of time instants
dt = 0.0001			# time step value in seconds

fig = plt.figure() 
ax = plt.axes(xlim=(-3, 3), ylim=(-1,4)) 
line, = ax.plot([], [], lw=2)

# initialization function 
def init(): 
	# creating an empty plot/frame 
	line.set_data([], []) 
	return line, 

# lists to store x and y axis points
th1 = [th1_in]
th2 = [th2_in]
w1 = [w1_in]
w2 = [w2_in]
#x1 = []
#x2 = []
#y1 = []
#y2 = []

# animation function 
def animate(i): 
	# x, y values to be plotted
	F2 = (m2*g*(np.cos(th2[i]*np.pi)*np.sin((th1[i] - th2[i])*np.pi) + np.sin(th2[i]*np.pi)) + m2*(w2[i]**2)*l2)/(1 + (m2/m1)*(np.sin((th1[i] - th2[i])*np.pi)**2))
	F3 = m2*g*np.cos(th1[i]*np.pi) - (m2/m1)*F2*np.sin((th1[i] - th2[i])*np.pi)
	w1.append(w1[i] + F3/m2*dt/l1)
	w2.append(w2[i] + g*np.cos(th2[i]*np.pi) - F3/m2*np.cos((th1[i] - th2[i])*np.pi))
	th1.append(th1[i] + w1[i]*dt)
	th2.append(th2[i] + w2[i]*dt)
	"""
	x1.append(hook[0] - l1*np.cos(th1[i]*np.pi))
	y1.append(hook[1] - l1*np.sin(th1[i]*np.pi))
	x2.append(x1[i] - l2*np.cos(th2[i]*np.pi))
	y2.append(y1[i] - l2*np.sin(th2[i]*np.pi))
	"""
	x1_ball = (hook[0] - l1*np.cos(th1[i]*np.pi))
	y1_ball = (hook[1] - l1*np.sin(th1[i]*np.pi))
	x2_ball = (x1_ball - l2*np.cos(th2[i]*np.pi))
	y2_ball = (y1_ball - l2*np.sin(th2[i]*np.pi))
	
	x1 = np.linspace(hook[0],x1_ball,10,endpoint=True)
	y1 = np.linspace(hook[1],y1_ball,10,endpoint=True)
	x2 = np.linspace(x1_ball,x2_ball,10,endpoint=True)
	y2 = np.linspace(y1_ball,y2_ball,10,endpoint=True)
	x = np.append(x1,x2)
	y = np.append(y1,y2)

	line.set_data(x,y)
	return line,
	
# setting a title for the plot 
plt.title('Creating a double-pendulum with matplotlib!') 
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