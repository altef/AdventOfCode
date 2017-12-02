<?php
	$pw = 'hepxcrrq';
	do {
		$pw++;
		if (strlen($pw) > 8) $pw = substr($pw, 1);
		$result = check($pw);		
	} while (!$result);
	echo $pw;
	
	
	function check($string) {
		$straight = array();
		$omit = array('i', 'o', 'l');
		$pairs = array();
		$last = null;
		for($i=0; $i<strlen($string); $i++) {
			$c = $string[$i];
			if (in_array($c, $omit)) 
				return false;
			if (count($straight) < 3 ) {
				if (count($straight) > 0 ) {
					$b = $straight[count($straight)-1];
					if (++$b == $c) {
						$straight[] = $c;
					} else {
						$straight = array($c);
					}
				} else 
					$straight = array($c);
			}
			
			if($last == $c) {
				$pairs[$c] = 1;
				$last = null;
			} else
				$last = $c;			
			
		}
		return count($straight) == 3 && count($pairs) > 1;
	}

?>