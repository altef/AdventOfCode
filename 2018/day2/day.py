import sys

def part1(lines):
	counts = [0,0]
	for line in lines:
		values = process_box_IDs(line)
		if 2 in values:
			counts[0] += 1
		if 3 in values:
			counts[1] += 1
	print("Stage 1: {}".format(counts[0]*counts[1]))

def process_box_IDs(line):
	letter_counts = {}
	for c in line:
		if c not in letter_counts:
			letter_counts[c] = 0
		letter_counts[c] += 1
	
	number_counts = {}
	for key, value in letter_counts.items():
		if value not in number_counts:
			number_counts[value] = 0
		number_counts[value] += 1
	
	return number_counts;


def part2(lines):
	for a in lines:
		for b in lines:
			if a == b:
				continue
			
			divergence = 0
			skip = -1
			for i in range(0, len(a)):
				if a[i] != b[i]:
					divergence += 1
					skip = i
					if divergence > 1:
						break
			if divergence == 1:
				print("Part 2: {}".format(a[:skip] + a[skip+1:]))
				return
			


def usage():
	print("Usage: python day.py [file]")
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