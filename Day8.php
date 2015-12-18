<?php
	$lines = file("data.txt");
	$total = 0;
	$mem = 0;
	$encoded = 0;
	foreach($lines as $line) {
		$total += strlen(trim($line));
		$str = preg_replace(array(
				"/\\\\\"/",
				"/\\\\\\\\/",
				"/\\\\x[0-9a-fA-F]{2}/",
				"/\"$/",
				"/^\"/",
			),
			array("\"", "\\", "."), 
			$line);
		$mem += strlen(trim($str));		
		
		$str = preg_replace(array(
				"/\\\\/",
				"/\"/",
			),
			array("\\\\\\", "\\\""), 
			$line);
		$e = '"'.trim($str)."\"";
		$encoded += strlen($e);
	}
	echo $total . " - " . $mem . " = " . ($total - $mem) . "\n";
	echo $encoded . " - " . $total . " = " . ($encoded - $total) . "\n";
?>