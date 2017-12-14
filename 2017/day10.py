with open('day10-input.txt', 'r') as f:
    input = f.read()



def hash(input, somenumbers, current_pos = 0, skip_size = 0):
	l = somenumbers[:]
	#print(l)
	for input in inputs:
		start = current_pos % len(l)
		end = (start + input) % len(l)
		
	#	print("{}: {} to {}".format(input, start, end))
		
		sub = []
		if end < start:
			sub = l[start:] + l[:end]
		elif end > start:
			sub = l[start:end]
		
	#	print("sub: {}".format(sub))
		sub = list(reversed(sub))
		
		if end < start:
			l = sub[len(l)-start:] + l[end:start] + sub[:len(l)-start]
		elif end > start:
			l = l[:start]  + sub + l[end:]
	#		print("new l: {}\n".format(l))
		current_pos +=  input + skip_size
		skip_size += 1
	return(l, current_pos, skip_size)


# Part 1
#inputs = [x for x in input.split(',')]
#l, cp, ss = hash(inputs, [x for x in range(0, 256)])
#print("Step 1: {}".format(l[0]*l[1]))


# loop through 64 times
#input = '1,2,4'
inputs = [x for x in input.split(',')]
inputs = [ord(x) for x in input] + [17, 31, 73, 47, 23]
ss = 0
cp = 0
l = [x for x in range(0, 256)]
for i in range(0, 64):
	#print("hash: {}, {}".format(cp, ss))
	l, cp, ss = hash(inputs, l, cp, ss)

# xor sequence
hash = []
for i in range(0, len(l), 16):
	#print("Hashing {} to {} of {}".format(i, i+16, len(l)))
	hash.append(reduce(lambda a,b: a^b, l[i:i+16]))

print("Step 2: {}".format("".join(["{:02x}".format(x) for x in hash])))