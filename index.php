<?php 
    // Start MySQL Connection
    include('connect.php'); 
?>

<html>
    <head>
        <title>GyroMaze Leaderboard</title>
        <style type="text/css">
            .table_titles, .table_cells_odd, .table_cells_even {
                    padding-right: 20px;
                    padding-left: 20px;
                    color: #000;
                    
            }
            .table_titles {
                color: #FFF;
                background-color: #666;
            }
            .table_cells_odd {
                background-color: #CCC;
            }
            .table_cells_even {
                background-color: #FAFAFA;
            }
            table {
                border: 2px solid #333;
                float: left;
                margin-left: 20px;
                margin-right: 20px;
            }
            body { font-family: "Trebuchet MS", Arial; }
        </style>
    </head>
    <body>
        <h1 style="margin-left:20px;">GyroMaze Leaderboard</h1>
    <table border="0" cellspacing="0" cellpadding="4">
        <tr>
            <td class="table_titles">Maze 1 Times</td>
          </tr>

          <?php
                // Retrieve all records and display them
                $result = mysqli_query($dbh, "SELECT times FROM gametimes WHERE maze_id = 1 ORDER BY times ASC LIMIT 10 ");

                // Used for row color toggle
                $oddrow = true;

                // process every record
                while( $row = mysqli_fetch_array($result) )
                {
                    if ($oddrow) 
                    { 
                        $css_class=' class="table_cells_odd"'; 
                    }
                    else
                    { 
                        $css_class=' class="table_cells_even"'; 
                    }

                    $oddrow = !$oddrow;

                    echo '<tr>';
                    echo '   <td'.$css_class.'>'.$row["times"].'</td>';
                    echo '</tr>';
                }
            ?>

        </table>
        <table border="0" cellspacing="0" cellpadding="4">
        <tr>
            <td class="table_titles">Maze 2 Times</td>
          </tr>

          <?php
                // Retrieve all records and display them
                $result = mysqli_query($dbh, "SELECT times FROM gametimes WHERE maze_id = 2 ORDER BY times ASC LIMIT 10 ");

                // Used for row color toggle
                $oddrow = true;

                // process every record
                while( $row = mysqli_fetch_array($result) )
                {
                    if ($oddrow) 
                    { 
                        $css_class=' class="table_cells_odd"'; 
                    }
                    else
                    { 
                        $css_class=' class="table_cells_even"'; 
                    }

                    $oddrow = !$oddrow;

                    echo '<tr>';
                    echo '   <td'.$css_class.'>'.$row["times"].'</td>';
                    echo '</tr>';
                }
            ?>

        </table>
        <table border="0" cellspacing="0" cellpadding="4">
        <tr>
            <td class="table_titles">Maze 3 Times</td>
          </tr>

          <?php
                // Retrieve all records and display them
                $result = mysqli_query($dbh, "SELECT times FROM gametimes WHERE maze_id = 3 ORDER BY times ASC LIMIT 10 ");

                // Used for row color toggle
                $oddrow = true;

                // process every record
                while( $row = mysqli_fetch_array($result) )
                {
                    if ($oddrow) 
                    { 
                        $css_class=' class="table_cells_odd"'; 
                    }
                    else
                    { 
                        $css_class=' class="table_cells_even"'; 
                    }

                    $oddrow = !$oddrow;

                    echo '<tr>';
                    echo '   <td'.$css_class.'>'.$row["times"].'</td>';
                    echo '</tr>';
                }
            ?>

        </table>
    </body>
</html>
