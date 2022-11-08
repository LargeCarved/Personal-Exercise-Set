<?php
header('Content-Type:text/html;charset=utf-8');
// 立即定向
// header('Location:http://www.baidu.com');
// 延时定向
// header('Refresh:3;url=http://www.baidu.com');
// echo '3秒后自动跳转到百度...，如无反应请' . '<a href="http://www.baidu.com">请点击这里</a>';

// header('Content-type:application/octet-stream');
// header('Content-disposition:attachment;filename="美女.jpg');
// echo file_get_contents('帅哥.jpg');

setcookie('name', 'value');
setcookie('name', 'value', time() + 1800);   // 30分钟后过期
setcookie('name', 'value', time() + 60 * 60 * 24); // 一天后过期
setcookie('name', '', time() - 1); // 立即过期（相当于删除Cookie）
