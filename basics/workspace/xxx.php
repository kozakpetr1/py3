<?php
$adjMatrix = [
    [0,   50,  0,   0,    0,        0,     0,    22,   41],  // VDF
    [50,  0,   24,  0,    0,        0,     0,    0,    0],   // DC
    [0,   24,  0,   90,   0,        0,     0,    0,    0],   // USTI
    [0,   0,   90,  0,    65,       33,    0,    0,    0],   // PRAHA
    [0,   0,   0,   65,   0,        0,     45,   0,    48],  // MBOLES
    [0,   0,   0,   33,   0,        0,     51,   0,    0],   // MELNIK
    [0,   0,   0,   0,    45,       51,    0,    10,   0],   // CLIPA
    [22,  0,   0,   0,    0,        0,     10,   0,    0],   // NBOR
    [41,  0,   0,   0,    48,       0,     0,    0,    0]    // LIBEREC
];

function findPath($adjMatrix, $start, $end) {
    $numNodes = count($adjMatrix);
    $visited = array_fill(0, $numNodes, false);
    $dist = array_fill(0, $numNodes, INF);
    $prev = array_fill(0, $numNodes, -1);
    
    $dist[$start] = 0;
    
    for ($i = 0; $i < $numNodes; $i++) {
        $minDist = INF;
        $u = -1;
        
        for ($j = 0; $j < $numNodes; $j++) {
            if (!$visited[$j] && $dist[$j] < $minDist) {
                $minDist = $dist[$j];
                $u = $j;
            }
        }

        if ($u == -1) break;  
        $visited[$u] = true;

        for ($v = 0; $v < $numNodes; $v++) {
            if ($adjMatrix[$u][$v] > 0 && !$visited[$v] && $dist[$u] + $adjMatrix[$u][$v] < $dist[$v]) {
                $dist[$v] = $dist[$u] + $adjMatrix[$u][$v];
                $prev[$v] = $u;
            }
        }
    }
    
    $path = [];
    for ($u = $end; $u != -1; $u = $prev[$u]) {
        array_unshift($path, $u);
    }
    
    return [$path, $dist[$end]];
}

$startCity = 0; // DC
$endCity = 8;   // LIBEREC

list($path, $distance) = findPath($adjMatrix, $startCity, $endCity);

$cities = ["VDF", "DC", "USTI", "PRAHA", "MBOLES", "MELNIK", "CLIPA", "NBOR", "LIBEREC"];
echo "Cesta z " . $cities[$startCity] . " do " . $cities[$endCity] . ":\n";
echo "Path: ";
foreach ($path as $node) {
    echo $cities[$node] . " ";
}
echo "\nVzdálenost: $distance km\n";
?>
