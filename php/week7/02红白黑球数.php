<?php
// for ($red = 1; $red < 25; $red++) {
//     for ($white = 1; $white < 31; $white++) {
//         for ($black = 1; $black < 28; $black++) {
//             if ($red + $white == 25 and $white + $black == 31 and $red + $black == 28) {
//                 echo '红球：' . $red . '<br>' . '白球：' . $white . '<br>' . '黑球：' . $black . '<br>';
//             }
//         }
//     }
// }
for ($red = 0; $red <= 25; $red++) {
    $white = 25 - $red;
    $black = 28 - $red;
    if ($white + $black == 31) {
        echo '红球：' . $red . '<br>' . '白球：' . $white . '<br>' . '黑球：' . $black . '<br>';
    }
}
