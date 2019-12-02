import days.Day1;
import days.Day2;

class Aoc {
	static public function main():Void {
		var day:String = haxe.macro.Context.definedValue("day");
		var chunks:Array<String> = day.split(".");
		
		var tests:Array<String> = ["1", "2"];
		if (chunks.length > 1) 
			tests = tests.filter(function(e:String) { return chunks[1] == e; });

		// Allow for passing in test input
		var input:String = haxe.macro.Context.definedValue("input");
		var data = "";
		if (input != null) 
			data = input.split(";").join("\n");

		var dayClass = Type.resolveClass('days.Day' + chunks[0]);
		var daySolver = Type.createInstance(dayClass, []);
		for(test in tests) {
			trace("Elfing day " + chunks[0] + ", part " + test);
			if (input == null) 
				data = sys.io.File.getContent("data/day" + chunks[0] + "." + test + ".txt");
			trace(Reflect.field(daySolver, "part" + test)(data) + "\n");
		}

	}
}