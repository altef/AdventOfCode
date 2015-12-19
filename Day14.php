<?php
$lines = file('data.txt');
	
	$reindeer = array();
	foreach($lines as $line) {
		if (preg_match('/(.*) can fly ([\d]+) km\/s for ([\d]+) seconds, but then must rest for ([\d]+) seconds.$/ ', $line, $matches)) {
			$reindeer[$matches[1]] = array(
				'states'=> array(
					array(
						'speed' => $matches[2],
						'duration' => $matches[3]
					),
					array(
						'duration' => $matches[4],
						'speed' => 0
					)
				),
				'current' => array(
					'state'=>0,
					'remaining'=>$matches[3]
				),
				'distance' => 0,
				'score' => 0
			);
		}
	}
	
	$duration = 2503;
	for($t=0; $t < $duration; $t++) {
		$max = 0;
		foreach($reindeer as $name=>$data) {
			$reindeer[$name]['current']['remaining']--;
			$reindeer[$name]['distance'] += $reindeer[$name]['states'][$reindeer[$name]['current']['state']]['speed'];
			if ($reindeer[$name]['current']['remaining'] == 0) {
				$reindeer[$name]['current']['state'] ^= 1;
				$reindeer[$name]['current']['remaining'] = $reindeer[$name]['states'][$reindeer[$name]['current']['state']]['duration'];
			}
			$max = max($max, $reindeer[$name]['distance']);
		}
		foreach($reindeer as $name=>$data) {
			if ($reindeer[$name]['distance'] == $max)
				$reindeer[$name]['score']++;
		}
	}
	
	echo "After $duration seconds:\n";
	foreach($reindeer as $name=>$data) {
		echo "\t $name: ". $data['distance']." km for a total of ".$data['score']." points\n";
	}

?>