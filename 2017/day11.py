import operator

with open('day11-input.txt', 'r') as f:
	input = f.read()

directions = {
	'n': (0, -1),
	's': (0, +1),
	'nw': (-1, -.5),
	'ne': (1, -.5),
	'sw': (-1, .5),
	'se': (1, .5)
}

distances = []
def distance(position):
	x,y = map(abs, position)
	if x < .5*y:
		return x*.5 + y 
	else:
		return x

position = [0,0]
for direction in input.split(","):
	position = (map(operator.add, position, directions[direction]))
	distances.append(distance(position))

print("Part 1: {}".format(distance(position)))
print("Part 2: {}".format(max(distances)))
