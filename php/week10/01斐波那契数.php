<?php
function fb($n)
{
    if ($n <= 2) {
        return 1;
    } else {
        return fb($n - 1) + fb($n - 2);
    }
}
echo fb(4) . "</br>";

function calculate($a, $b, $func, $gwg)
{
    return $func($a, $b) + $gwg($a, $b);
}

echo calculate(100, 200, function ($a, $b) {
    return $a + $b;
}, function ($a, $b) {
    return $a * $b;
}) . "</br>";

function cc($num)
{
    for ($i = 0; $i <= 10; $i++) {
        if ($num($i)) {
            continue;
        }
        echo $i . "-";
    }
    function Number_1($a)
    {
        return $a % 2 == 0; //打印不能被2整除的数
    }
    function Number_2($b)
    {
        return $b >= 6; //打印小于6的数
    }
    cc("Number_1");
    echo "<br>";
    cc("Number_2");
}

$str1 = "PHP学习手册!";               // 定义字符串常量
$str2 = "PHP学习手册!";               // 定义字符串常量
$str3 = "phpcn";                      // 定义字符串常量
$str4 = "PHPCN";                      // 定义字符串常量
echo strcmp($str1, $str2);             // 这两个字符串相等
echo strcmp($str3, $str4);             // 注意该函数区分大小写
echo strcasecmp($str3, $str4);          //该函数不区分大小写
