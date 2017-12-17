with open('day16-input.txt', 'r') as f:
	input = f.read()
steps = input.split(',')

programs = [chr(ord('a') + x) for x in range(0,16)]

def exchange(args, p):
	args = map(int, args)
	b = p[args[0]]
	p[args[0]] = p[args[1]]
	p[args[1]] = b
	return p

moves = {
	's': lambda x, p: p[-int(x[0]):] + p[:-int(x[0])],
	'x': exchange,
	'p': lambda a, p: [a[0] if x == a[1] else a[1] if x == a[0] else x for x in p]
}


count = 0
history = [programs[:]]
goal = 1000000000
while True:
	for step in steps:
		programs = moves[step[0]](step[1:].split("/"), programs)
	if count == 0:
		print("Part 1: {}".format("".join(programs)))
	if programs not in history:
		history.append(programs[:])
	else:	# Once we've got the period, we can just get the correct entry
		programs = history[goal % len(history)]
		break
	count += 1
	if count == goal: # In case it's before we've found a repeat
		break
	
print("Part 2: {}".format("".join(programs)))
