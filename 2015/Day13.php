<?php
	$lines = file('day13-data.txt');
	
	$people = array();
	foreach($lines as $line) {
		if (preg_match('/(.*) would ([a-z]+) ([\d]+) happiness units by sitting next to (.*)\.$/', $line, $matches)) {
			$value = $matches[3]*($matches[2] === "gain" ? 1 : -1);
			if (!array_key_exists($matches[1], $people)) 
				$people[$matches[1]] = array();
			
			if (!array_key_exists($matches[4], $people)) 
				$people[$matches[4]] = array();

			if (!array_key_exists($matches[1], $people[$matches[4]])) 
				$people[$matches[4]][$matches[1]] = 0;
			if (!array_key_exists($matches[4], $people[$matches[1]])) 
				$people[$matches[1]][$matches[4]] = 0;

			
			$people[$matches[1]][$matches[4]] += $value;
			$people[$matches[4]][$matches[1]] += $value;
		}
	}
	
	// Part 2
	$people['me'] = array();
	foreach($people as $k=>$v) {
		if ($k == 'me') continue;
		$people[$k]['me'] = 0;
		$people['me'][$k] = 0;
	}
	
	// Figure out all the unique combinations, because why not brute force it.
	// There are going to be equivalent ones, but w/e I don't care.
	$combos = array();
	$all = array_keys($people);
	$first = array_shift($all);
	permute($all, array($first));
	
	
	$max = 0;
	foreach($combos as $combo) {
		$offset = 0;
		$first = array_shift($combo);
		$last = $first;
		foreach($combo as $name) {
			$offset += $people[$last][$name];
			$last = $name;
		}
		$offset += $people[$last][$first];
		//echo "$first," . implode(",", $combo)." -> " . $offset . "\n";
		$max = max($offset, $max);
	}
	
	echo $max."\n";

	function permute($list, $sofar = array()) {
		global $combos;
		if (count($list) == 0) {
			$combos[] = $sofar;
			return;
		}

		$output = array();
		foreach($list as $i=>$l) {
			$a = $list;
			$b = $sofar;
			$b[] = $l;
			array_splice($a, $i, 1);
			permute($a, $b);
		}
		return $output;
	}
	
	
?>