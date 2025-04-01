<?php
$image2d = [];
for ($i = 0; $i < 9; $i++) {
    for ($j = 0; $j < 9; $j++) {
        $image2d[$i][$j] = 4 - max(abs($i - 4), abs($j - 4));
    }
}
print_r($image2d);