<html>
<head>
	<title> Database Program </title>
</head>
<body>
	<form action="10.php" method="post" autocomplete="off">
		<input name="name" placeholder="Name" required />
		<br />
		<input name="usn" placeholder="USN" required/>
		<br />
		<input name="branch" placeholder="Branch" required/>
		<br />
		<input name="sem" placeholder="Semester" required/>
		<br />
		<button type="submit">Add</button>
	</form>
<?php

	function printTable($title, $rows) {
		echo $title."<br>";
		echo "<table><tr><th>Name</th><th>USN</th><th>Branch</th><th>Semester</th></tr>";
		foreach($rows as $row) {
			echo "<tr><td>$row[0]</td><td>$row[1]</td><td>$row[2]</td><td>$row[3]</td></tr>";
		}
		echo "</table>";
	}

	$conn = mysqli_connect('localhost', 'root', '528751011', 'webdb');
	if(!$conn) {
		echo "Cant connect to db";
	}
	if(isset($_POST['name'])) {
		$query = "INSERT INTO STUDENTS VALUES('".$_POST["name"]."','".$_POST["usn"]."','".$_POST["branch"]."','".$_POST["sem"]."')";
		$res = mysqli_query($conn, $query);

		if(!$res) {
			echo "Can't Insert USN Clash<br><br>";
		}
	}	
	$query = "SELECT * FROM STUDENTS";
	$res = mysqli_query($conn, $query);
	$rows = mysqli_fetch_all($res);
	

	printTable("Unsorted", $rows);

	for($i = 0; $i < count($rows) - 1; $i++) {
		$minIndex = $i;
		for($j = $i+1; $j < count($rows); $j++) {
			if(strcmp($rows[$j][0], $rows[$minIndex][0]) < 0) {
				$minIndex = $j;
			}
		}
		$temp = $rows[$i];
		$rows[$i] = $rows[$minIndex];
		$rows[$minIndex] = $temp;
	}

	printTable("Sorted", $rows);
?>
