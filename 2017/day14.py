import day10


input = 'oundnydw'
count = 0

grid = []
for i in range(0, 128):
	hashstr = day10.knothash('{}-{}'.format(input, i))
	binstr = str(bin(int(hashstr, 16)))[2:].zfill(128)
	count += binstr.count('1')
	
	grid.append([None if x == "0" else 0 for x in binstr])

print("Step 1: {}".format(count))


def apply_range(y, x, value):
	if grid[y][x] != 0:
		return
	
	grid[y][x] = value
	if y > 0:
		apply_range(y-1, x, value)
	if y < 127:
		apply_range(y+1, x, value)
	if x > 0:
		apply_range(y, x-1, value)
	if x < 127:
		apply_range(y, x+1, value)


group = 0
for t in range(0, len(grid)):
	for i in range(0, len(grid[t])):
		if grid[t][i] == 0:
			group += 1
			apply_range(t, i, group)

print("Step 2: {}".format(group))

