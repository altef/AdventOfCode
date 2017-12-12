with open('day12-input.txt', 'r') as f:
	input = f.read()


map = {}

for line in input.split('\n'):
	chunks = line.split(' ')
	f = chunks[0]
	t = [x.strip(',') for x in chunks[2:]]
	if f not in map:
		map[f] = []
	map[f] += t
	for i in t:
		if i not in map:
			map[i] = []
		map[i] += t + [f]

for k,v in map.iteritems():
	map[k] = list(set(v))

lst = []
def search(index):
	lst.append(index)
	for k,v in map.iteritems():
		all = [k] + v
		if index in all:
			for a in all:
				if a not in lst:
					search(a)

					
search('0')
print("Step 1: {}".format(len(lst)))

groups = 0
while True:
	groups += 1
	keys = map.keys()
	print(len(keys))
	if len(keys) > 0:
		print("Searching for {}".format(keys[0]))
		search(keys[0])
		for i in lst:
			del map[i]
		lst = []
	else:
		break
print("Step 2: {}".format(groups))