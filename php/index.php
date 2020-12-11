<?php

function isPrime($num)
{
    if ($num == 2) {
        return true;
    }
    if ($num == 1 || $num %2 == 0) {
        return false;
    }
    $to = sqrt($num) + 1;
    for ($i = 3; $i <= $to; $i += 2) {
        if ($num % $i == 0) {
            return false;
        }
    }
    return true;
}

function run($N)
{
    for ($i = 0; $i <= $N; $i++) {
        $isPrime = isPrime($i);
        // if ($isPrime) {
        //     var_dump($i);
        // }
    }
}

// php ./php/index.php
// php8 -dopcache.enable=1 -dopcache.enable_cli=1 -dopcache.jit=1255 -dopcache.jit_buffer_size=100M ./php/index.php
// 22.418176174164
// 8.63338804245
function main()
{
    $st = microtime(true);
    run(10000000);

    echo microtime(true) - $st;
}

main();
