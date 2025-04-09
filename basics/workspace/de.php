<?php
$image2d = [];
for ($i = 0; $i < 9; $i++) {
    for ($j = 0; $j < 9; $j++) {
        $image2d[$i][$j] = 4 - max(abs($i - 4), abs($j - 4));
    }
}

$final_string = "";
for ($i = 0; $i < 9; $i++) {
    
    if($i > 0){
        $line = "";
    }else{
    $line = "| - | - | - | - | - | - | - | - | - | <br>"; 
    }
    for ($j = 0; $j < 9; $j++) {
    	$string = "| " . $image2d[$i][$j] . " ";
    	$final_string .= $string;
    }
    $final_string .= " |";
    $final_string .= "<br>";
    $final_string .= $line;
    
}

echo "<div>";
echo "<h1>Původní</h1>";
echo $final_string;
echo "</div>";

/* 
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 3 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 4 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 3 | 3 | 3 | 2 | 1 | 0 |
| 0 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 0 |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
*/

function dilatace($image2d) {
    $final = [];

    for ($i = 0; $i < 9; $i++) {
        for ($j = 0; $j < 9; $j++) {
            $neighbors = [];

            if ($i > 0) $neighbors[] = $image2d[$i - 1][$j]; // Nahoru
            if ($i < 8) $neighbors[] = $image2d[$i + 1][$j]; // Dolů
            if ($j > 0) $neighbors[] = $image2d[$i][$j - 1]; // Levá
            if ($j < 8) $neighbors[] = $image2d[$i][$j + 1]; // Pravá

            $neighbors[] = $image2d[$i][$j]; 

            $final[$i][$j] = max($neighbors); 
        }
    }

    foreach ($final as $row) {
        echo implode(" ", $row) . "<br>";
    }
}


function eroze($image2d) {
    $final = [];

    for ($i = 0; $i < 9; $i++) {
        for ($j = 0; $j < 9; $j++) {
            $neighbors = [];

            if ($i > 0) $neighbors[] = $image2d[$i - 1][$j]; // Nahoru
            if ($i < 8) $neighbors[] = $image2d[$i + 1][$j]; // Dolů
            if ($j > 0) $neighbors[] = $image2d[$i][$j - 1]; // Levá
            if ($j < 8) $neighbors[] = $image2d[$i][$j + 1]; // Pravá

            $neighbors[] = $image2d[$i][$j]; 

            $final[$i][$j] = min($neighbors); 
        }
    }

    foreach ($final as $row) {
        echo implode(" ", $row) . "<br>";
    }
}

echo "<div>";
echo "<h1>Upravená</h1>";
eroze($image2d);
echo "</div>";  