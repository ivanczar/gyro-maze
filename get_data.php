<?php
    include("connect.php");
    
    $mazeID = $_GET["maze_id"];
    $SQL = "SELECT times FROM gametimes WHERE maze_id = $mazeID ORDER BY times ASC LIMIT 1";
    
    $request = mysqli_query($dbh, $SQL);
    
    echo json_encode(mysqli_fetch_assoc($request));
?>
