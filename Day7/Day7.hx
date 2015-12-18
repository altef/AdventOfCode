import sys.io.File;
using StringTools;
using Lambda;

class Day7 {
	static var functions = ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"];
    static public function main() {
		if (Sys.args().length == 0)
			throw("Please specify a line to show the ouput for, ex: neko Day7 a");

		var fin = File.read('data.txt', false);
		var d7 = new Day7();
		try {
			while(true) {
				var line = fin.readLine();
				d7.process(line);
			}
		} catch(e:haxe.io.Eof) {
		
		}
		fin.close();
		var a = Sys.args();
		trace(a[0] + " = " + d7.request(a[0]));
    }
	
	var gates:Map<String, Gate>;
	var values:Map<String, Int>;
	
	function request(output) {
		var t = Std.parseInt(output);
		if ( t != null ) {
			return t;
		}
			
		if (values.exists(output)) {
			return values[output];
		}
		var gate = gates.get(output);
		
		// Recursively calculate...
		var ins = new Array<Int>();
		for(input in gate.input) {
			if (input != null) {
				var v = request(input);
				ins.push(v);
				values.set(input, v); // for speed
			}			
		}
		return gate.process(ins) & 0xFFFF;
	}
	
	private function new() {
		gates = new Map<String, Gate>();
		values = new Map<String, Int>();
	}
	
	private function process(line:String) {
		var chunks = line.split(" ").map(function(a) {return a.trim(); });
		var out = chunks.pop();
		if (chunks.pop() != "->")
			throw("Invalid line format: " + line);
		
		chunks.reverse();
		var history:Array<String> = [chunks.pop()];
		var c:String;
		do {
			c = chunks.pop();
			var last = history.pop();
			if (functions.indexOf(last) > -1) { // It's a function
				gates.set(out, new Gate(last, history[0], c));
				return;
			} else {
				history.push(last);
			}
			history.push(c);
		} while (c != null);
		
		var v = Std.parseInt(history[0]);
		if (v == null)
			gates.set(out, new Gate('WIRE', history[0]));
		else
			values.set(out, v & 0xFFFF );
	}
}