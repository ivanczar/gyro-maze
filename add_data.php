<?php
    include("connect.php");

    $maze_id = $_GET["maze_id"];
    $times = $_GET["times"];

    $SQL = "INSERT INTO gametimes(maze_id, times) VALUES ($maze_id, $times)";     
    mysqli_query($dbh, $SQL);

?>
