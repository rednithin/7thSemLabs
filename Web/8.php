<link rel="shortcut icon" href="data:image/x-icon;," />
<?php 
  $value = "";
  if(isset($_POST["expression"])) {
    $expression = $_POST["expression"];
    $value = eval("return ".$expression.";");
  }

  echo '<form action="8.php" method="post">';
  echo '<input name="expression" value="'.$value.'" />';
  echo '<button type="submit">Submit</button>';
  echo '</form>';

  $matrix1 = [[1,2],[3,4]];
  $matrix2 = [[5,6],[7,8]];
  $rows = 2;
  $columns = 2;
  $transpose = [];
  for($i = 0; $i < $columns; $i++) {
    for($j = 0; $j <$rows; $j++) {
      $transpose[$i][$j] = $matrix1[$j][$i];
    }
  }
  print_r($transpose);
  $mul = [];
  for($i = 0; $i < $rows; $i++) {
    for($j = 0; $j <$columns; $j++) {
      for($k = 0; $k < $rows; $k++) {
        $mul[$i][$j] += $matrix1[$i][$k] *$matrix2[$k][$j];
      }
    }
  }
  print_r($mul)
?>