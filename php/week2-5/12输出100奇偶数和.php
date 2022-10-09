<?php
$sum = 0;
for ($i = 0; $i <= 100; $i++) {
    if ($i % 2 == 0) {
        $sum = $sum + $i;
    }
}
echo "1-100的偶数的和=" . $sum . "</br>";
$sum = 0;
for ($i = 0; $i <= 100; $i++) {
    if ($i % 2 != 0) {
        $sum = $sum + $i;
    }
}
echo "1-100的奇数的和=" . $sum;
