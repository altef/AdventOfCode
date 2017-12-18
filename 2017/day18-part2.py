from enum import Enum
import msvcrt


# Define statuses
class Status(Enum):
	DONE = 0
	SENT = 1
	WAITING = 2


def describe(thread, tid):
	print("		thread: {}".format(tid))
	print("		registers: {}".format(thread['registers']))
	print("		input: {}".format(thread['in']))
	print("		ouput: {}".format(thread['out']))

def execute(thread, tid):
	count = 0 
	while thread['pc'] < len(thread['program']):
		count += 1
		
		line = thread['program'][thread['pc']]
		cmd = line[0]
		x = line[1]
		
		# Instantiate any we haven't seen
		if x.isalpha():
			if x not in thread['registers']:
				thread['registers'][x] = 0
			xval = thread['registers'][x]
		else:
			xval = int(x)
		
		# Figure out Y
		y = None
		if len(line) > 2:
			if line[2].isalpha():
				y = thread['registers'][line[2]]
			else:
				y = int(line[2])

		if cmd == 'jgz' and xval > 0:
			thread['pc'] += y
		else:
			thread['pc'] += 1
			if cmd == 'set':
				thread['registers'][x] = y
			elif cmd == 'snd':
				thread['out'].append(xval)
				thread['send_count'] += 1
				return Status.SENT
			elif cmd == 'add':
				thread['registers'][x] += y
			elif cmd == 'mul':
				thread['registers'][x] *= y
			elif cmd == 'mod':
				thread['registers'][x] = thread['registers'][x] % y
			elif cmd == 'rcv':
				if len(thread['in']) == 0:
					thread['pc'] -= 1
					return Status.WAITING
				else:
					old = len(thread['in'])
					thread['registers'][x] = thread['in'].pop(0)
					
	describe(thread, tid)
	return Status.DONE








if __name__ == "__main__":
	with open('day18-input.txt', 'r') as f:
		input = f.read()

	# Set up the threads
	threads = []
	for i in range(0,2):
		threads.append({
			'pc': 0,
			'registers': {'p': i},
			'in': [],
			'out': None,
			'program': [x.split() for x in input.split("\n")],
			'send_count': 0
		})
	
	
	# Set up the pipes
	threads[0]['out'] = threads[1]['in']
	threads[1]['out'] = threads[0]['in']

	# Execute
	while True:
		results = [execute(threads[i], i) for i in range(0, len(threads))]
		if all(x == results[0] for x in results) and results[0] != Status.SENT:
			if results[0] == Status.WAITING:
				print("Deadlocked.")
			break

	print("Part 2: {}".format(threads[1]['send_count']))