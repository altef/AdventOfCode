
step = 312
buffer = [0]
pos = 0
for i in range(1, 2018):
	pos = (pos + step) % len(buffer)
	buffer.insert(pos + 1, i)
	pos += 1


print("Step 1: {}".format(buffer[pos+1]))

length = 1
after_zero = None
pos = 0
for i in range(1, 50000001):
	pos = (pos + step) % length
	if pos == 0:
		after_zero = i
	pos += 1
	length += 1

print("Step 2: {}".format(after_zero))
