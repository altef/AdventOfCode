with open('day2-input.txt', 'r') as file:
	matches = file.readlines()


results = [0,0]
for match in matches:
	a,b = match.rstrip().split(' ')
	a = ord(a) - ord('A') # A in numbers
	b = ord(b) - ord('X') # B in numbers
	w = (a + b + 2) % 3 # What hand to play if we want the outcome to be B
	results[0] += ((b - a + 4) % 3) * 3 + b + 1 # The first part is to calculate the outcome as a value from 0 to 2
	results[1] += b*3 + w + 1 # In this one b is already the outcome

print(f"Part 1: {results[0]}\nPart 2: {results[1]}")