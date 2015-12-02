// Did these seperately on jsfiddle.net - didn't realize each day had two parts
// HTML section was: <textarea>[data]</textarea><p></p>

// Part 1
var data = $('textarea').val().split("\n");
var sum = 0;
for(var i=0; i < data.length; i++) {
  var d = data[i].split("x");
  var areas = d.map(function(a) {return d.reduce(function(b,c) { return c*b; })/a});
  areas.sort(function(a,b) {return a - b;});
  sum += areas.map(function(a) {return 2*a}).reduce(function(a,b) {return a+b;}) + areas[0];
}
$('p').text(sum);                    
                    


// Part 2
var data = $('textarea').val().split("\n");
var sum = 0;
for(var i=0; i < data.length; i++) {
  var d = data[i].split("x");
  var areas = d.map(function(a) {return a*2});
  var bow = d.reduce(function(a,b) {return a*b;}); 
  areas.sort(function(a,b) {return b - a;});
  areas.shift();
  sum += areas.reduce(function(a,b) {return a+b}) + bow;
}
$('p').text(sum);      