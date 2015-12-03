// Part 1
var data = '>';
var pos = [0,0];
var gifts = {'0,0': 1};
for(var i=0; i < data.length; i++) {
  switch(data[i]) {
    case '<': pos[0]--; break;
    case '>': pos[0]++; break;
    case '^': pos[1]--; break;
    case 'v': pos[1]++; break;
  }
  gifts[pos.join(',')]=1;
}
$('p').text(Object.keys(gifts).length);








// Part 2 - got a little more complicated. Now supporting N santas.
var data = '^v^v^v^v^v';
var Santa = function() { 
  return {
    pos: [0,0],
    gifts: {'0,0':1}
  };
}
var santas = [new Santa(), new Santa()];	
var step = 0;
for(var i=0; i < data.length; i++) {
  var santa = step++ % santas.length;
  switch(data[i]) {
    case '<': santas[santa].pos[0]--; break;
    case '>': santas[santa].pos[0]++; break;
    case '^': santas[santa].pos[1]--; break;
    case 'v': santas[santa].pos[1]++; break;
  }
  santas[santa].gifts[santas[santa].pos.join(',')] = 1;
}
var gifts = [].concat.apply([], santas.map(
  function(a) {return Object.keys(a.gifts)})
);
$('p').text($.unique(gifts).length);