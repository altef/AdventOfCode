package days;

class Day4 extends Day {


	private function isValid(s:String):Bool {
		// It has to be 6 characters long
		if (s.length != 6)
			return false;

		// It has to have at least one character that's the same as the previous character
		var match = false;
		for(i in 1...s.length)
			if (s.charAt(i) == s.charAt(i-1)) {
				match = true;
				break;
			}
		if (match == false)
			return false;
		
		// The digits can never decrease
		for(i in 1...s.length)
			if (Std.parseInt(s.charAt(i)) < Std.parseInt(s.charAt(i-1)))
				return false;

		return true;
	}


	private function getValidFromRange(data:String):Array<String> {
		var range = data.split("-").map((a)->Std.parseInt(a));
		var valid = [];
		for(d in range[0]...range[1]) {
			var s = Std.string(d);
			if (isValid(s))
				valid.push(s);
		}
		return valid;
	}


	override public function part1(data:String):String {
		var valid = getValidFromRange(data);
		return Std.string(valid.length);
	}


	override public function part2(data:String):String {
		var valid = getValidFromRange(data);
		valid = Lambda.filter(valid, (a)->{
			var last = a.charAt(0);
			var count = 1;
			for(i in 1...a.length) {
				if (a.charAt(i) != last) {
					if (count == 2)
						return true;
					last = a.charAt(i);
					count = 1;
				} else count++;
			}
			return count == 2;			
		});
		return Std.string(valid.length);
	}
}