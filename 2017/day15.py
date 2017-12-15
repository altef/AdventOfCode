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


def next(generator):
	divisor = 2147483647
	next = (generator['last'] * generator['coeff']) % divisor
	generator['last'] = next
	return next

def picky_next(generator):
	divisor = 2147483647
	while True:
		next = (generator['last'] * generator['coeff']) % divisor
		generator['last'] = next
		if next % generator['mod'] == 0:
			break
	return next


def check(number, picky = False):
	matches = 0
	
	if picky:
		fn = picky_next
	else:
		fn = next

	for i in range(0, number):
		o = []
		for generator in generators:
			r = fn(generator)
			o.append(str(bin(r))[2:].zfill(32))
		if o[0][16:] == o[1][16:]:
			matches += 1
	return matches

#print("Part 1: {}".format(check(40000000)))

print("Part 2: {}".format(check(5000000, True)))
