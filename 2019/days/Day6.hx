package days;

import haxe.ds.Map;

class Orbital {
    public static var map:Map<String,Orbital> = new Map<String,Orbital>();
    public var orbits:String;
    public var depth:Int = -1;

    public function steps():Int {
        if (depth > -1) return depth;
        if (orbits == 'COM') return 1;
        return 1 + map.get(orbits).steps();
    }

    public function new(body:String, orbits:String) {
        this.orbits = orbits;
        map.set(body, this);
    }
}

class Day6 extends Day {

	override public function part1(data:String):String {       
        for(orbit in data.split("\n")) {
            var bodies = orbit.split(")");
            new Orbital(bodies[1], bodies[0]);
        }
        var total = 0;
        for(body in Orbital.map.keys()) {
            total += Orbital.map.get(body).steps();
        }
		return Std.string(total);
	}


	override public function part2(data:String):String {
        for(orbit in data.split("\n")) {
            var bodies = orbit.split(")");
            new Orbital(bodies[1], bodies[0]);
        }
        // Start with YOU
        var path = ['YOU'];
        while(path[path.length-1] != 'COM') 
            path.push(Orbital.map.get(path[path.length-1]).orbits);
        
        // Start with Santa
        var path2 = ['SAN'];
        while(path2[path2.length-1] != 'COM') {
            path2.push(Orbital.map.get(path2[path2.length-1]).orbits);
            if (path.indexOf(path2[path2.length-1]) > -1)
                break;
        }
        return Std.string(path.indexOf(path2[path2.length-1]) + path2.length - 3); // You, Santa, and the one overlap
	}
}