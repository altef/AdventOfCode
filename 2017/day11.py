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

position = [0,0]
for direction in input.split(","):
	position = (map(operator.add, position, directions[direction]))

print(position)
x,y = position

distance = None

print("Distance: {}".format(distance))
