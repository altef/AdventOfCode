package days;

class Day3 extends Day {

	private function parse(line:String) {
		return line.split(",")
			.map(
				(node)->{
					direction: node.charAt(0), 
					count: Std.parseInt(node.substr(1))
				}
			);
	}

	// Return an iterator
	private function nodes(line:String) {
		var nodes = parse(line);

		var position = [0, 0];
		return {
			hasNext: function() {
				return nodes.length > 0;
			},
			next: function() {
				switch(nodes[0].direction) {
					case 'U': position[1]--;
					case 'D': position[1]++;
					case 'L': position[0]--;
					case 'R': position[0]++;
				}
				if (--nodes[0].count == 0)
					nodes.shift();
				return position;
			}
		}
	}

	private function distances(intersections:Array<Array<Int>>):Array<Int> {
		return intersections.map((a)->(Std.int(Math.abs(a[0]) + Math.abs(a[1]))));
	}


	override public function part1(data:String):String {
		// I was tempted to do line segment intersection, since I already have haxe code for it: https://gigglingcorpse.com/2015/06/25/line-segment-intersection/
		// but that's so long and I'm so lazy

		var lines = data.split("\n");
		var wire1:Map<String, Bool> = new Map<String, Bool>();
		for(p in nodes(lines[0]))
			wire1.set(haxe.Json.stringify(p), true);

		var intersections = [];
		for(p in nodes(lines[1]))
			if (wire1.exists(haxe.Json.stringify(p)))
				intersections.push(p.copy());
		
		// Return the smallest distance
		var closest = Lambda.fold(distances(intersections), (a,b)->(b < 0 || a < b ? a : b), -1);
		return Std.string(closest);
	}


	override public function part2(data:String):String {
		// And now I'm glad I didn't do line segment intersections, because the above maps to this more easily
		var lines = data.split("\n");
		var wire1:Map<String, Int> = new Map<String, Int>();
		var count = 1;
		for(p in nodes(lines[0])) {
			var key = haxe.Json.stringify(p);
			if (!wire1.exists(key))
				wire1.set(key, count);
			count++;
		}

		var distance = -1;
		count = 1;
		for(p in nodes(lines[1])) {
			var key = haxe.Json.stringify(p);
			if (wire1.exists(key)) {
				var first = wire1.get(key);
				if (distance < 0 || distance > first + count)
					distance = first + count;
			}
			count++;
		}
		
		// Return the smallest distance
		return Std.string(distance);
	}
}