class Gate {
	
	public var input:Array<Dynamic>;
	private var type:String;
	
	
	public function new(type:String, a:Dynamic, ?b:Dynamic) {
		this.input = new Array<Dynamic>();
		this.input.push(a);
		this.input.push(b);
		this.type = type;
	}
	
	public function process(inputs:Array<Int>) {
		switch(this.type) {
			case 'AND': return inputs[0] & inputs[1];
			case 'OR': return inputs[0] | inputs[1];
			case 'LSHIFT': return inputs[0] << inputs[1];
			case 'RSHIFT': return inputs[0] >> inputs[1];
			case 'NOT': return 0xFFFF ^ inputs[0];
			case 'WIRE': return inputs[0];
		}
		throw(this.type + " is not a valid gate.");
	}
}