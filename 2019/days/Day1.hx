package days;

class Day1 extends Day {

	// sum floor(x/3)-2
	override public function part1(data:String):String {
		var count:Int = 0;
		for (line in data.split("\n"))
			count += Std.int(Std.parseInt(line)/3) - 2;
		return Std.string(count);
	}

	private function getFuelMass(mass:Int, runningSum:Int = 0):Int {
		var fuel = Std.int(mass/3) - 2;
		if (fuel <= 0)
			return runningSum;
		return getFuelMass(fuel, fuel + runningSum);
	}

	override public function part2(data:String):String {
		var total:Int = 0;
		for(line in data.split("\n")) {
			var mass = Std.parseInt(line);
			total += this.getFuelMass(mass);
		}
		return Std.string(total);
	}
}