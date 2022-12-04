with open('day1-input.txt', 'r') as file:
	data = file.read()
elves = [sum([int(item) for item in elf.split('\n')]) for elf in data.split('\n\n')]
elves.sort()
print(f"Part 1: {elves[-1]}")
print(f"Part 2: {sum(elves[-3:])}")