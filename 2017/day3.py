# I did this one in an ugly way 

# Part 1 A
def findCircle(input):
	for i in range(0, input):
		if circle(i) >= input:
			return i


def circle(c):
	return (c*2+1)*(c*2+1)


def steps(i):
	if i == 1:
		return 0
	
	c = findCircle(i)
	end = circle(c)
	start = circle(c-1) + 1
	index = i - start
	height = c*2+1
	segment_index = index%(height-1)
	offset = abs(segment_index - ((height-1)/2) + 1)
	steps = int(offset + c)
	return steps


# Part 1 B
def part1b(i):
	x,y = indexToCoords(i)
	return abs(x) + abs(y)


def coordsToIndex(x,y):
	# figure out what edge it's on
	c = max(abs(x), abs(y))
	start = circle(c-1) + 1
	height = c*2+1
	if x == c:
		segment = 0
		index = abs(y - c + 1)
		if y == c:
			index = circle(c)-start
	elif y == -c:
		segment = 1
		index = abs(x - c + 1)
	elif x == -c:
		segment = 2
		index = y + c - 1
	elif y == c:
		segment = 3
		index = x + c - 1
	
	return start + index +  segment * c * 2


def indexToCoords(i):
	if i == 1:
		return (0,0)
	c = findCircle(i)
	start = circle(c-1) + 1
	index = i - start
	height = c*2+1
	segment_index = index%(height-1)
	segment = int(index/(height-1))
	if segment == 0:
		return (c, -(segment_index - c + 1))
	elif segment == 1:
		return (-(segment_index - c + 1), -c)
	elif segment == 2:
		return (-c, (segment_index - c + 1))
	elif segment == 3:
		return ((segment_index - c + 1), c)


print("Part 1: {}".format(steps(361527)))
print("Part 1b: {}".format(part1b(361527)))


# Part B
def adjacent(i):
	x,y = indexToCoords(i)
	adj = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1)]
	indices = [coordsToIndex(*x) for x in adj]
	return [data[x] if x in data else 0 for x in indices]

i = 2
data = {1: 1}
while True:
	if i not in data:
		v = sum(adjacent(i))
		if v > 361527:
			print("Part 2: {}".format(v))
			break
		data[i] = v
	i += 1
























