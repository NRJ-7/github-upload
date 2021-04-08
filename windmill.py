import random
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from sys import argv 
from math import sin,cos,pi
plt.style.use('dark_background')

S = [(0,0),(1,1)] #initial set of points
hook = S[0]

start_point = (0,0)
fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

xs = [start_point[0]]
ys = [start_point[1]]

def animate(i):
	# x, y values to be plotted 
	w.append(w[i] + g*np.cos(th[i]*np.pi)*dt/l - f*w[i]*dt/m)
	th.append(th[i] + w[i]*dt)
	x_ball = (hook[0] - l*np.cos(th[i]*np.pi))
	y_ball = (hook[1] - l*np.sin(th[i]*np.pi))
	#w.append((2*g/l/*np.sin(th[i]*np.pi))**0.5*np.sin(th[i]*np.pi))
	x = np.linspace(hook[0],x_ball,10,endpoint=True)
	y = np.linspace(hook[1],y_ball,10,endpoint=True)

	line.set_data(x, y) 
	return line,
	
ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()