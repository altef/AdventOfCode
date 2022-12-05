import re

with open('day5-input.txt', 'r') as file:
	data = file.read()

stacks_definition, instructions = [x.split('\n') for x in data.split('\n\n')]
stacks = [[] for x in range(int((len(stacks_definition[0]) + 1) / 4))]

for line in stacks_definition[-2::-1]:
	for i in range(1, len(line), 4):
		if line[i] != ' ':
			stacks[int((i-1)/4)].append(line[i])

stacks2 = [s.copy() for s in stacks] # Copy it for part 2

for line in instructions:
	movements = [int(x) for x in re.search('move (\d+) from (\d+) to (\d+)', line).groups()]
	for i in range(movements[0]): # Part 1
		stacks[movements[2]-1].append(stacks[movements[1]-1].pop())
	# Part 2
	stacks2[movements[2]-1] += stacks2[movements[1]-1][-1*movements[0]:]
	stacks2[movements[1]-1] = stacks2[movements[1]-1][:-1*movements[0]]


results = [''.join([x[-1] for x in s]) for s in [stacks, stacks2]]
print(f"Part 1: {results[0]}\nPart 2: {results[1]}")
