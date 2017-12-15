def next(generator, respect_mod = False):
	divisor = 2147483647
	while True:
		next = (generator['last'] * generator['coeff']) % divisor
		generator['last'] = next
		if not respect_mod or next % generator['mod'] == 0:
			break
	return next


def check(number, picky = False):
	generators = [
		{
			'name': 'A',
			'last': 679,
			'coeff': 16807,
			'mod': 4,
		},
		{
			'name': 'B',
			'last': 771,
			'coeff': 48271,
			'mod': 8
		}
	]
	
	matches = 0
	for i in range(0, number):
		o = []
		for generator in generators:
			r = next(generator, picky)
			o.append(r & 0xFFFF)
		if all(x == o[0] for x in o):
			matches += 1
	return matches



if __name__ == "__main__":
	print("Part 1: {}".format(check(40000000)))
	print("Part 2: {}".format(check(5000000, True)))
