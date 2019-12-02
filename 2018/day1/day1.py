import sys

def part1(lines):
	chunks = [x.strip() for x in lines]
	start = 0
	for c in chunks:
		op = c[0]
		val = c[1:]
		start += (1 if op == '+' else -1) * int(val)
	print("Part 1: {}".format(start))


def part2(lines):
	lines = [x.strip() for x in lines]
	history = {0: -1}
	start = 0
	index = 0
	while(True):
		c = lines[index % len(lines)]
		op = c[0]
		val = c[1:]
		start += (1 if op == '+' else -1) * int(val)
		if start in history:
			print("Part 2: {}".format(start))
			break
		else:
			history[start] = index
		index += 1

def usage():
	print("Usage: python day1.py [file]")
	print()

if __name__ == "__main__":
	if len(sys.argv) < 1:
		usage()
	else:
		file = sys.argv[1]
		with open(file) as f:
			lines = f.readlines()
			part1(lines)
			part2(lines)
