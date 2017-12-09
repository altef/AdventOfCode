with open('day9-input.txt', 'r') as f:
    input = f.read()


garbage = False # Are we in a garbage sequence?
cancel = False # Should we cancel the next character?
stack = 0 # The current size of the stack
score = 0 # Part one's score
junk = 0 # Part 2 - how much garbage we've seen
for char in input:
	if cancel:
		cancel = False
		continue
	
	if char == '!':
		cancel = True
		continue
	
	if garbage:
		if char == '>':
			garbage = False
		else:
			junk += 1
		continue
	else:
		if char == '<':
			garbage = True
	
	if char == '{':
		stack += 1
		score += stack
	if char == '}':
		stack -= 1


print("Part 1: {}".format(score))
print("Part 2: {}".format(junk))