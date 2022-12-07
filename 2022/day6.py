with open("day6-input.txt", "r") as file:
	data = file.read()

def first_unique_n(data, length):
	i = length - 1
	while True:
		match = -1
		for t in range(length): # Compare each of the four to the rest
			for j in range(1, length - t): # We don't care which way we do the comparison, so why do them twice
				if data[i - length + 1 + t] == data[i - length + 1 + t + j]:
					match = t
					i += t # Skip ahead if we find a match, since any before it will just contain it
					break
			if match != -1:
				break
		if match == -1:
			return i + 1
		if i >= len(data):
			return -1
		i += 1

print(f"Part 1: {first_unique_n(data, 4)}\nPart 2: {first_unique_n(data, 14)}")