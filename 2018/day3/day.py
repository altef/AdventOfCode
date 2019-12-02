import sys, re

def parts(lines):

	#1 @ 1,3: 4x4
	rects = []
	for line in lines:
		m = re.search('^#([^\s]+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)$', line.strip())
		if m:
			id, x, y, w, h = m.groups()
			rects.append({
				'id': id,
				'x': int(x),
				'y': int(y),
				'width': int(w),
				'height': int(h),
				'overlap': False
			})
		else:
			raise ValueError("Whoa this line doesn't match the expected format: {}".format(line))
	
	
	overlap = {}
	
	for i in range(0, len(rects)):
		a = rects[i]
		for j in range(i, len(rects)):
			b = rects[j]
			if a == b:
				continue
			if intersect(a,b):
				rects[j]['overlap'] = True
				rects[i]['overlap'] = True
				
				for k in range(b['x'], b['x'] + b['width']):
					for t in range(b['y'], b['y'] + b['height']):
						fakerect = {
							'x': k,
							'y': t,
							'width': 1,
							'height': 1,
							'id': 'pixel'
						}
						if intersect(a, fakerect):
							overlap[keyname(k,t)] = 1

	print("Stage 1: {}".format(len(overlap)))
	print("Stage 2: {}".format([x['id'] for x in rects if not x['overlap']]))

def keyname(x,y):
	return "{}, {}".format(x,y)

def intersect(a, b):
	if b['x'] >= a['x'] + a['width'] or b['x'] + b['width'] <= a['x']:
		return False
	
	if b['y'] >= a['y'] + a['height'] or b['y'] + b['height'] <= a['y']:
		return False
	
	return True



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
			parts(lines)
