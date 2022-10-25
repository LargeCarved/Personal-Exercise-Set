<?php
function test($year)
{
    if ($year % 4 == 0 && $year % 100 != 0 || $year % 400 == 0) {
        echo $year . "是闰年";
    } else {
        echo $year . "是平年";
    }
}
test(2000);

function add($a, $b)
{
    return "</br>" . ($a + $b) . "</br>";
}
echo add(123, 321);

function array1($arr)
{
    $sum = 0;
    foreach ($arr as $i) {
        if ($i % 2 != 0 || $i / 1 == 1) {
            $sum += $i;
        }
    }
    return $sum;
}
$arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
echo array1($arr);
