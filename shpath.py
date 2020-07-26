import time

class city:
	def __init__(self):
		self.index = 0
		self.neighbours = {}

def min_cost(c1,c2,path_covered):
	if c1 == c2:
		return 0
	if frozenset([c1,c2]) in min_cost_dict:
		return min_cost_dict[frozenset([c1,c2])]
	cost = 200001
	path_covered.append(c1)
	for cname in cities:
		if c1 in cities[cname].neighbours and cities[cname].index not in path_covered:
			tmp_cost = cities[cname].neighbours[c1] + min_cost(cities[cname].index,c2,path_covered)
			if tmp_cost < cost:
				cost = tmp_cost
	path_covered.pop()
	min_cost_dict[frozenset([c1,c2])] = cost
	return cost

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
	print(min_cost(c1,c2,[]))

end = time.time()
print(f"Execution Time: {(end - start)*1000} ms")