package days;

class Day5 extends Day {

	private function loadProgram(data:String):Array<Int> {
		var memory:Array<Int> = new Array<Int>();
		for (code in data.split(","))
			memory.push(Std.parseInt(code));
		return memory;
	}


    private function execute(memory:Array<Int>):Array<Int> {
		var pointer = 0;
		while(true) {
            var op = memory[pointer] % 100;
            var mode = Std.string(Std.int(memory[pointer] / 100));
            var size = 4;

            var param = (i)->(mode.length - i < 0 || mode.charAt(mode.length - i) == "0")  ? memory[memory[pointer+i]] : memory[pointer+i];

        	switch(op) {
				case 1:
					memory[memory[pointer + 3]] = param(1) + param(2);	
                case 2:
					memory[memory[pointer + 3]] = param(1) * param(2);	
                case 3:
                    trace("The program is requesting input:");
                    memory[memory[pointer+1]] = Std.parseInt(Sys.stdin().readLine());
                    size = 2;
                case 4:
                    trace("Output: " + param(1));
                    size = 2;
                case 5:
                    if (param(1) != 0) {
                        pointer = param(2);
                        continue;
                    }
                    size = 3;

                case 6:
                    if (param(1) == 0) {
                        pointer = param(2);
                        continue;
                    }
                    size = 3;
                case 7:
                    memory[memory[pointer + 3]] = param(1) < param(2) ? 1 : 0;
                case 8:
                    memory[memory[pointer + 3]] = param(1) == param(2) ? 1 : 0;
				case 99:
					break;
				default:
					throw "Unexpected OpCode: " + memory[pointer] + " at " + pointer;
			}

			pointer += size;
			if (pointer > memory.length)
				throw "Termination code not found.";
		}
		return memory;
	}

	override public function part1(data:String):String {
		// Load the program
		var memory = this.loadProgram(data);
		
		// Run the program
		memory = this.execute(memory);
	
		return "Done";
	}


	override public function part2(data:String):String {
		return part1(data); // They're exactly the same
	}
}