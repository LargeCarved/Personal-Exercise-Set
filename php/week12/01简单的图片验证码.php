<?php
// 创建画布
$img = imagecreatetruecolor(400, 400);
// 给画布分配纯白色背景
$img_color = imagecolorallocate($img, mt_rand(200, 255), mt_rand(200, 255), mt_rand(200, 255));
// 用白色填充画布
imagefill($img, 0, 0, $img_color);
//给字符分配颜色
$str_color = imagecolorallocate($img, mt_rand(0, 150), mt_rand(0, 150), mt_rand(0, 150));
//将字符写入画布中
imagestring($img, 4, 180, 190, 'hello', $str_color);
// 向页面输出图片
header('content-type:image/jpeg');
imagejpeg($img, 'test.jpeg');
imagedestroy($img);
