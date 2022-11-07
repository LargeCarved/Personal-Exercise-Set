<?php
echo date("y-m-d") . "<br>";

$picture = "123.jpg";
$picture_name = strstr($picture, ".");
if ($picture_name != ".jpg") {
    echo "图片格式不正确！";
} else {
    echo "正确的图片格式";
}
echo "<br>";

$str = "今天我买了西瓜，切成了好几个西瓜，把切好的西瓜分给了舍友，舍友说这个西瓜很好吃";
$str1 = "西瓜";
$str2 = "**";
echo str_ireplace($str1, $str2, $str);
echo "<br>";
