<link rel="shortcut icon" href="data:image/x-icon;,">
<?php
$openHandler = fopen("counter.txt", "r");
$count = intval(fread($openHandler, 100));
fclose($openHandler);
echo $count++;
$closeHandler = fopen("counter.txt", "w");
fwrite($closeHandler, $count);
fclose($closeHandler);

// $count = (int)file_get_contents("counter.txt");
// echo $count++;
// file_put_contents("counter.txt", $count);
?>