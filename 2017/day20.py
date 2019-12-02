import operator

with open('day20-input.txt', 'r') as f:
	lines = f.read().splitlines()

particles = []


def parse(prop):
	return map(int, prop[3:-1].split(','))

id = 0
for line in lines:
	props = line.split(', ')
	particles.append({
		'p': parse(props[0]),
		'v': parse(props[1]),
		'a': parse(props[2]),
		'd': None,
		'id': id
	})
	id += 1


for i in range(0, 10000):
	for p in particles:
		p['v'] = map(operator.add, p['v'], p['a'])
		p['p'] = map(operator.add, p['v'], p['p'])
		p['d'] = reduce(lambda a,b: abs(a) + abs(b), p['p'])
	
	# Part 2
	# Remove collisions
	print("{}: Number of particles: {}".format(i, len(particles)))
	t = len(particles) - 1
	while t >= 0:
		#print("Comparing {}".format(t))
		p = particles[t]['p']
		removed = 0
		k = t-1
		while k >= 0:
			#print("	with {}".format(k))
			if cmp(particles[k]['p'], p) == 0:
				#print("removing one!")
				if removed == 0:
					del particles[t]
				removed += 1
				del particles[k]
			k -= 1
		t = t - removed - 1
		

particles.sort(key =lambda x: x['d'])
print("Part 1: {}".format(particles[0]['id']))
print("Part 2: {}".format(len(particles)))