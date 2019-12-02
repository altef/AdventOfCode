import operator
import msvcrt

with open('day19-input.txt', 'r') as f:
	lines = f.read().splitlines()


pos = [lines[0].index('|'), 0]
mode = 'down'
offset = {
	'down': [0, 1],
	'up': [0, -1],
	'left': [-1, 0],
	'right': [1, 0]
}

str = ''




def cango(mode, pos):
	if pos[1] < 0 or pos[1] < 0:
		return False
	#print("Can go {} to {}? {}".format(mode, pos, lines[pos[1]][pos[0]]))
	c = char(pos)
	if mode in ['up', 'down']:
		return c not in ['-', ' ']
	else:
		return c not in ['|', ' ']

def add(*args):
	args = list(args)
	buffer = args.pop()
	while True:
		if len(args) > 0:
			next = args.pop()
			buffer = map(operator.add, buffer, next)
		else:
			return buffer

def char(pos):
	try:
		return lines[pos[1]][pos[0]]
	except:
		return ' '

count = 1
while True:
	
	# Append characters
	if lines[pos[1]][pos[0]].isalpha():
		str += lines[pos[1]][pos[0]]
	
	# Move
	#print("{}: {}".format(mode, lines[pos[1]][pos[0]]))
	next = add(pos, offset[mode])
	#print("next: {}".format(char(next)))
	if char(next) is ' ' or (not cango(mode, next) and not cango(mode, add(next, offset[mode]))):
		#print("Can't continue going {}".format(mode))
		if mode in ['up', 'down']:
			if cango('left', add(pos, offset['left'])):
				#print("I can go left!")
				mode = 'left'
			elif cango('right', add(pos, offset['right'])):
				#print("I can go right!")
				mode = 'right'
			else:
				break
		elif mode in ['left', 'right']:
			if cango('up', add(pos, offset['up'])):
				mode = 'up'
			elif cango('down', add(pos, offset['down'])):
				mode = 'down'
			else:
				break
	
	pos = add(pos, offset[mode])
	count += 1
	#result = msvcrt.getch()
	#if result == 'x':
	#	break


print("Part 1: {}".format(str))
print("Part 2: {}".format(count))