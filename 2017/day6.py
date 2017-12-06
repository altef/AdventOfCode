#input = "0	2	7	0"
input = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"

memory = [int(x) for x in input.split()]

# Part 1
steps = 0
history = []
while True:
	history.append(str(memory))
	v = max(memory)
	i = memory.index(v)
	memory[i] = 0
	for x in range(0, v):
		memory[(i+x+1)%len(memory)] += 1
	steps += 1
	if str(memory) in history:
		break

print("Part 1: {} steps".format(steps))


# Part 2

steps = 0
history = str(memory)
while True:
	v = max(memory)
	i = memory.index(v)
	memory[i] = 0
	for x in range(0, v):
		memory[(i+x+1)%len(memory)] += 1
	steps += 1
	if str(memory) == history:
		break

print("Part 2: {} steps".format(steps))