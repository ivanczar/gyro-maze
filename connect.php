<?php
$MyUsername = "ivan";  
$MyPassword = "ivan123";  
$MyHostname = "localhost";  

$dbh = mysqli_connect($MyHostname , $MyUsername, $MyPassword);
$selected = mysqli_select_db($dbh, 'GyroMazeDB');
?>