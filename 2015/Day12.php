<?php
	$obj = json_decode(file_get_contents('data.txt'), true);
	echo recursive_add($obj);
	
	function recursive_add($obj) {
		$total = 0;
		foreach($obj as $k=>$v) {
			if(is_scalar($v)) {
				$total += $v;
				if ($v === "red" && is_assoc($obj)) // part 2 
					return 0;
				
			} else
				$total += recursive_add($obj[$k]);
		}
		return $total;
	}
	
	function is_assoc(array $array) {
	  return (bool)count(array_filter(array_keys($array), 'is_string'));
	}
	
?>