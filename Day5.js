// Part 1.  Went a little crazy with this

var text = $('textarea').val();
var lines = text.split("\n");

var check = new function() {
  var vowels, last, not;
  var _not = ["ab", "cd", "pq", "xy"];
  var _vowels =["a", "e", "i", "o", "u"];
  var o = {
    reset: function() {
      vowels = _vowels.map(function(a) {return 0;});
      last = null;
      not = _not.map(function(a) { return {str: a, pos:0}});
    },
    
    vowels: function(c) {
      var i = _vowels.indexOf(c);
      if (i > -1)
        vowels[i]++;
      return vowels.reduce(function(a,b) {return a + b;}) >= 3;
    },
    
    double: function(c) {
      if (last === true || c == last)
        return last = true;
      last = c;
      return false;
    },
    
    omit: function(c) {
      for(var i=0; i < not.length; i++) {
        (not[i].pos >= not[i].str.length || c == not[i].str[not[i].pos]) ? not[i].pos++ : not[i].pos = 0;
       	if (not[i].pos >= not[i].str.length)
          return false;
      }
      return true;      
    },
    v: function() {
      return not;
    }
  }
  o.reset();
  return o;
}

var good = 0;
for(i=0; i < lines.length; i++) {
  check.reset();
  var o, v, d;
  for(t=0; t < lines[i].length; t++) {
    var c = lines[i][t];
    v = check.vowels(c);
    d = check.double(c);
    o = check.omit(c);	
  }
  if (v && d && o)  // the calls aren't in here due to short-circuiting
      good++;
}
$('p').text(good + "/" + lines.length);







// Part 2
var text = $('textarea').val();
var lines = text.split("\n");

var check = new function() {
  var pairs, sandy;
  var o = {
    reset: function() {
      pairs = ' ';
      sandy = ['', '', ''];
    },
    sandwhich: function(c) {
      if (sandy === true) return true;
      sandy.shift();
      sandy.push(c);
      if (sandy[0] == sandy[2]) {
        return sandy = true;
      }
      return false;      
    },
    pairs: function(c) {
      if (pairs === true) return true;
      var str = pairs[pairs.length-1] + c;
      var i = pairs.indexOf(str);
      pairs += c;
      if (i < pairs.length-3 && i > -1) {
        return pairs = true;
      }
      return false;
    },
    v: function() {
      return not;
    }
  }
  o.reset();
  return o;
}

var good = 0;
for(i=0; i < lines.length; i++) {
  check.reset();
  var s, p;
  for(t=0; t < lines[i].length; t++) {
    var c = lines[i][t];
    s = check.sandwhich(c);
    p = check.pairs(c);
    if (s && p) { // There are no immediate fail conditions
      good++;
    	break;
    }
  }
}
$('p').text(good + "/" + lines.length);