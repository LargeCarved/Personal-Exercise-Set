<?php
function getVericode($width, $height, $lines = 10, $length = 4)
{
    //增加画布，给画布背景填充随机颜色
    $img = imagecreatetruecolor($width, $height);
    $bg_color = imagecolorallocate($img, mt_rand(200, 255), mt_rand(200, 255), mt_rand(200, 255));
    imagefill($img, 0, 0, $bg_color);

    //增加26大写字母并打乱输出前4个，输出到画布上
    $str_arr = range('A', 'Z');
    shuffle($str_arr);
    $captcha = '';
    for ($i = 0; $i < $length; $i++) {
        $captcha .= $str_arr[$i] . " ";
    }
    $str_color = imagecolorallocate($img, mt_rand(0, 80), mt_rand(0, 80), mt_rand(0, 80));
    imagestring($img, 5, 30, 10, $captcha, $str_color);

    //增加10条随机长宽角度随机颜色的线
    for ($i = 0; $i < $lines; $i++) {
        $line_color = imagecolorallocate($img, mt_rand(0, 255), mt_rand(0, 255), mt_rand(0, 255));
        imageline($img, mt_rand(0, $width), mt_rand(0, $height), mt_rand(0, $width), mt_rand(0, $height), $line_color);
    }

    //保存文件，清除缓存
    header('content-type:image/png');
    imagepng($img, 'test.png');
    imagedestroy($img);
}
//调用函数
getVericode(120, 30);
