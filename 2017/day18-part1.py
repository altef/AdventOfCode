with open('day18-input.txt', 'r') as f:
	input = f.read()

pc = 0
registers = {}
last = None

program = [x.split() for x in input.split("\n")]

while pc < len(program):
	command = program[pc][0]
	x = program[pc][1]
	if x not in registers:
		registers[x] = 0
	y = None
	if len(program[pc]) > 2:
		y = program[pc][2]
		try:
			y = int(y)
		except:
			y = registers[y]
	if command == 'set':
		registers[x] = y
	elif command == 'snd':
		last = registers[x]
	elif command == 'add':
		registers[x] += y
	elif command == 'mul':
		registers[x] *= y
	elif command == 'mod':
		registers[x] = registers[x] % y
	elif command == 'rcv':
		if registers[x] != 0:
			print("Part 1: {}".format(last))
			registers[x] = last
			break
	elif command == 'jgz':
		if registers[x] > 0:
			pc += y
			continue
	pc += 1

