import random
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from sys import argv 
from math import sin,cos,pi
plt.style.use('dark_background')

num_vertices = 3#int(argv[1])
print(num_vertices)
vertices = []
xs = []
ys = []
for i in range(num_vertices):
	vx = 10*cos(i*2*pi/num_vertices + pi/2)
	vy = 10*sin(i*2*pi/num_vertices + pi/2)
	xs.append(vx)
	ys.append(vy)
	vertices.append((vx,vy))
	print(xs)
	print(ys)
	print(vertices)
"""
A = (0,2*(3**0.5))
B = (2,0)
C = (-2,0)
fixed_points = [A,B,C]
"""
start_point = (1,3)
fig = plt.figure()
#creating a subplot 
ax1 = fig.add_subplot(1,1,1)

xs.append(start_point[0])
ys.append(start_point[1])

def animate(i):
	vertex_index = random.randint(0,num_vertices - 1)
	#print(vertex_index)
	newpt_x = (xs[i + num_vertices] + vertices[vertex_index][0])/2
	newpt_y = (ys[i + num_vertices] + vertices[vertex_index][1])/2
	xs.append(newpt_x)
	ys.append(newpt_y)
	#print(xs)
	#print(ys)

	ax1.clear()
	ax1.scatter(xs, ys, s=0.1)
	ax1.axis('off')
	plt.title('Chaos Game')

ani = animation.FuncAnimation(fig, animate, interval=20)
plt.show()