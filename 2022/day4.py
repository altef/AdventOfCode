with open('day4-input.txt', 'r') as file:
	assignments = [x.rstrip() for x in file.readlines()]

# Look both ways
def inside(orders):
	for i in range(len(orders)):
		if orders[i][0] >= orders[i-1][0] and orders[i][1] <= orders[i-1][1]:
			return i
	return -1

results = [0,0]
for assignment in assignments:
	orders = [[int(y) for y in x.split('-')] for x in assignment.split(',')]
	results[0] += 1 if inside(orders) > -1 else 0
	results[1] += 1 if orders[0][1] >= orders[1][0] and orders[0][0] <= orders[1][1] else 0

print(f"Part 1: {results[0]}\nPart 2: {results[1]}")