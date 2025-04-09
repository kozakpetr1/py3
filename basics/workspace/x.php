<?php
function ezop($command, $value){
    switch($command){
        case 'I@':
            echo "Zadejte hodnotu @: ";
            $input = trim(fgets(STDIN));
            $value = $input;
            break;
        
        case 'G@':
            $value = RandomNumber();
            break;

        case 'O@':
            echo $value;
            break;

        case '@+':
            $value++;
            break;

        case '@-':
            $value--;
            break;

        case '@0':
            $value = 0;
            break;

        case '@#':
            echo "Skript ukončen. ";
            break;

        default:
            echo "Byl zadán neplatný příkaz. Zkontrolujte prosím příkaz a zkuste znovu... ";
            exit(1);
    }
}

function RandomNumber(){
    return rand(-1024, 1024);
}

$prikaz = $argv[1];
$prikazy = str_split($prikaz, 2);

$hodnota = 0;

foreach($prikazy as $x){
    ezop($x, $hodnota);
}