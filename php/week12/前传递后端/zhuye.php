<?php
echo "欢迎您的到来，我的朋友！！";
// print_r($_COOKIE);
// print_r($_SESSION);
// echo "<a href='./loginout.php'>退出登录</a>";

session_start();
if (!isset($_SESSION['user'])) {
    header('location:./login.html');
}
echo '首页，';
echo '<a href="./loginout.php">退出登录</a>！！';
