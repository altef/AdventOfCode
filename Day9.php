<?php
	$lines = file('data.txt');
	
	$nodes = array();
	foreach($lines as $line) {
		list($route, $distance) = explode(" = ", trim($line));
		list($from, $to) = explode(' to ', $route);

		if (!array_key_exists($from, $nodes))
			$nodes[$from] = array();
		if (!array_key_exists($to, $nodes))
			$nodes[$to] = array();
		$nodes[$from][$to] = intval($distance);
		$nodes[$to][$from] = intval($distance);	
	}	
	
	
	$all = count(array_keys($nodes));
	$min = PHP_INT_MAX;
	$max = 0;
	$minroute = null;
	$maxroute = null;
	
	foreach($nodes as $p=>$c) {
		process($c, array($p));
	}

	echo implode(" -> ", $minroute) . " = " . $min . "\n";
	echo implode(" -> ", $maxroute) . " = " . $max;
	
	
	function process($places, $route=array(), $total=0) {
		global $all, $nodes, $min, $minroute, $max, $maxroute;
		foreach($places as $place=>$distance) {
			if (count($route) == $all) {
				
				if ( $min > $total ) {
					$minroute = $route;
					$min = $total;
				} else if ($max < $total) {
					$maxroute = $route;
					$max = $total;
				}
				return;
			}
			if (in_array($place, $route)) {
				continue;
			}
			process($nodes[$place], array_merge($route, array($place)), $total + $distance);
		}
	}
	
?>