<?php
var_dump(explode("p", "applepenpane")); //字符转数组
var_dump(explode("p", "applepenpane", 2));
var_dump(explode("p", "applepenpane", -2));

$str = ["a", "b", "c"]; //数组转字符
var_dump(implode(',', $str));

$arr = range('a', 'd'); //建立一个指定范围的元素数组
print_r($arr);

$stu = [
    ['Tom', 'male', 18],
    ['Alice', 'female', 19],
    ['Julia', 'female', 14]
];
echo count($stu) . " "; // 3,3个数组
echo count($stu, 1); // 12,所有元素
echo "<br>";

$arr1 = ['food' => 'tea', 2, 4];
$arr2 = ['a', 'food' => 'Cod', 'type' => 'jpg', 4];
$res = array_merge($arr1, $arr2); //合并
print_r($res);
echo "<br>";

print_r(array_chunk($res, 2)); //分割数组
echo "<br>";
print_r(array_chunk($res, 2, true));
echo "<br>";
