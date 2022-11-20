<?php
$username = trim($_POST['username']);
$pwd = trim($_POST['pwd']);
// var_dump($_POST);
// if (empty($username) || empty($pwd)) {
//     header('location:./login.html');
// }
$user = ['username' => 'lyzsir', 'pwd' => '123'];
if ($user['username'] !== $username) {
    exit('用户名错误！<a href="./login.html">重试</a>');
}
if ($user['pwd'] !== $pwd) {
    exit('密码错误！<a href="./login.html">重试</a>');
}
// session_start();
@session_start(['cookie_httponly' => true]);
$_SESSION['user'] = ['username' => $username, 'pwd' => $pwd];
header('location:./zhuye.php');
