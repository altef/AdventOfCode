import copy

with open('day13-input.txt', 'r') as f:
	input = f.read()

indices = []
for line in input.split("\n"):
	index, junk = line.split(":")
	indices.append(int(index))

layers = [None] * (max(indices) + 1)
for line in input.split("\n"):
	index, depth = line.split(":")
	layers[int(index)] = [None]*int(depth.strip())
	layers[int(index)][0] = 1


def run(firewall, stealth_mode = False, debug = False):
	packets = []
	count = 0
	while True:
		if stealth_mode or len(packets) == 0:
			packets.append({
				'delay': count,
				'position': -1,
				'severity': 0,
				'caught': False
			})
			
		for packet in packets:
			packet['position'] += 1
			if packet['position'] >= len(firewall):
				if stealth_mode: # We're only interested in a sneaky packet
					if packet['caught'] is False:
						return packet['delay']
					continue
				else:	# We're only interested in the first packet
					return packet['severity']
			if firewall[packet['position']] is not None and firewall[packet['position']][0] is not None:
				packet['caught'] = True
				packet['severity'] += packet['position'] * len(firewall[packet['position']])
		
		# remove any that are out of range, we don't care about them anymore
		packets = filter(lambda x: x['position'] < len(firewall), packets)
		
		if debug:
			print("\nCount: {}".format(count))
			print("{} packets in play".format(len(packets)))
			for i in range(0, len(firewall)):
				print("{}: {}".format(i, firewall[i]))
		
		# Move the scanners
		for layer in firewall:
			if layer is None:
				continue
			for i in range(0, len(layer)):
				if layer[i] is not None:
					scanner = layer[i]
					layer[i] = None
					if not (0 <= i + scanner < len(layer)):
						scanner *= -1
					layer[i+scanner] = scanner
					break
		count += 1
		#if count % 100 == 0:
		#	print("On pass {} with {} packets in play".format(count, len(packets)))


severity = run(copy.deepcopy(layers), debug=False)
print("Part 1: {}".format(severity))

delay = run(copy.deepcopy(layers), stealth_mode=True, debug=False)
print("Part 2: {}".format(delay))
