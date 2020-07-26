import time

class city:
	def __init__(self):
		self.index = 0
		self.neighbours = {}

def dijsktra(c1,c2):
	if c1 == c2:
		return 0

	sptset = set([])
	citylist = list(range(1,num_cities + 1))
	sptlen = 0
	distance_vals = [None]*num_cities
	distance_vals[c1 - 1] = 0
	for cname in cities:
		if c1 != cities[cname].index:
			distance_vals[cities[cname].index - 1] = 200001

	while sptlen != num_cities:
		min_dist = 200001
		u = 0
		for ci in citylist:
			tmp_dist = distance_vals[ci - 1]
			if tmp_dist < min_dist:
				min_dist = tmp_dist
				u = ci
		sptset.add(u)
		citylist.remove(u)
		sptlen += 1

		for cname in cities:
			if cities[cname].index == u:
				for v in cities[cname].neighbours:
					tmp_dist = distance_vals[u - 1] + cities[cname].neighbours[v]
					if tmp_dist < distance_vals[v - 1]:
						distance_vals[v - 1] = tmp_dist
				break

	return distance_vals[c2 - 1]

num_cities = int(input())
cities = {}
for i in range(num_cities):
	temp_city = city()
	name = input()
	temp_city.index = i + 1
	num_neighbours = int(input())
	
	for j in range(num_neighbours):
		neighbour = input().split(" ")
		temp_city.neighbours[int(neighbour[0])] = int(neighbour[1])
	
	cities[name] = temp_city

num_paths = int(input())
paths = []
for i in range(num_paths):
	paths.append(tuple(input().split(" ")))

min_cost_dict = {}

start = time.time()

for t in paths:
	c1 = cities[t[0]].index
	c2 = cities[t[1]].index
	print(dijsktra(c1,c2))

end = time.time()

print(f"Execution Time: {(end - start)*1000} ms")