package days;

class Day2 extends Day {

	private function loadProgram(data:String):Array<Int> {
		var memory:Array<Int> = new Array<Int>();
		for (code in data.split(","))
			memory.push(Std.parseInt(code));
		return memory;
	}


	private function execute(memory:Array<Int>):Array<Int> {
		var pointer = 0;
		while(true) {
			switch(memory[pointer]) {
				case 1:
					memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]];
				case 2:
					memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]];
				case 99:
					break;
				default:
					throw "Unexpected OpCode: " + memory[pointer] + " at " + pointer;
			}
			pointer += 4;
			if (pointer > memory.length)
				throw "Termination code not found.";
		}
		return memory;
	}

	override public function part1(data:String):String {
		// Load the program
		var memory = this.loadProgram(data);
		
		// Transform the program
		memory[1] = 12;
		memory[2] = 2;

		// Run the program
		memory = this.execute(memory);
	
		return Std.string(memory[0]);
	}


	override public function part2(data:String):String {
		for(noun in 0...100) {
			for(verb in 0...100) {
				var memory = this.loadProgram(data);
				memory[1] = noun;
				memory[2] = verb;
				memory = this.execute(memory);
				if (memory[0] == 19690720)
					return Std.string(noun) + Std.string(verb);
			}
		}
		return "Not found.";
	}
}