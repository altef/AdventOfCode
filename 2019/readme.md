## Advent of Code 2019

I did this a bit of a weird way, because I decided to use Haxe.  
* To run a day: `haxe -main Aoc --interp -D day=1`
* To run a day's part: `haxe -main Aoc --interp -D day=1.1` or `haxe -main Aoc --interp -D day=1.2`

I'm explicitly adding the imports at the top of `Aoc.hx` since using `import days.*` doesn't work nicely with `Type.resolveClass`.
 
To pass in test input, you can tack on `-D input=14` or, for multiple lines, `-D input=12;15;10943`.

 

