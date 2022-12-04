with open('day3-input.txt', 'r') as file:
	sacks = [x.rstrip() for x in file.readlines()]

def evaluate(i):
	v = ord(i)
	a = ord('a')
	return v - a + 1 if v >= a else v - ord('A') + 27

def elfgroups(iterable, n=3):
	l = len(iterable)
	for ndx in range(0, l, n):
		yield iterable[ndx:min(ndx + n, l)]

results = [0,0]
for sack in sacks:
	length = len(sack)
	memory = {}
	for i in range(length):
		try:
			memory[sack[i]] = 0 if i < length/2 else memory[sack[i]] + 1
		except: # since the else references the index, it'll fail for ones that don't exist
			pass # which is convenient because we want to ignore those anyway, and i was too lazy to write it more clearly
	matches = [k for k,v in memory.items() if v > 0]
	results[0] += sum([evaluate(x) for x in matches])

for group in elfgroups(sacks):
	memory = {}
	for t in range(len(group)): # Could just be 3
		for letter in group[t]:
			memory[letter] = memory.get(letter, 0) | (1 << t) # Turning on a specific bit for each entry in the group
	matches = [k for k,v in memory.items() if v == pow(2, len(group)) - 1] # could just be three; basically checking that all three bits are set
	results[1] += sum([evaluate(x) for x in matches])

print(f"Part 1: {results[0]}\nPart 2: {results[1]}")