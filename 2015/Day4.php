<?php
// Part 1
$secret = 'bgvyzdsv';
$i = 1;
do {
	$hash = md5($secret.$i++);
} while(strpos($hash, '00000') !== 0); 	// For part 2, add a 0
echo ($i-1)."\n";
?>