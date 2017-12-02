var start = "1113222113";
for(var i=0; i < 50; i++) {
	start = lookandsay(start);
}
console.log(start.length);


function lookandsay(str) {
	var last = null;
  var count = 0;
  var out = "";
	for(var i = 0; i < str.length; i++) {
  	if (last != str[i]) {
    	if (last != null)	out += count + last;
     	count = 1;
      last = str[i];
    } else
    	count++;
  }
 	return out + count + last;  
}