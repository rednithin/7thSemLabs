<link rel="shortcut icon" href="data:image/x-icon;," />
<?php 
$allTheStates = "Mississippi Alabama Texas Massachusetts Kansas";
	$statesArray = [];
	$states = explode(' ', $allTheStates);
	foreach ($states as $state) {
		if (preg_match('/xas$/', ($state))) {
			$statesArray[0] = ($state);
		}
		else if (preg_match('/^k.*s$/i', ($state))) {
			$statesArray[1] = ($state);
		}
		else if (preg_match('/^M.*s$/', ($state))) {
			$statesArray[2] = ($state);
		}
		else if (preg_match('/a$/', ($state))) {
			$statesArray[3] = ($state);
		}
	}
	print_r($statesArray);

?>
