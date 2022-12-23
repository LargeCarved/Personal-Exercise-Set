<?php
include '../sql.php';
header("content-type:text/html;charset=utf8");
include './login.html';
$conn = connect('root', 'a1592648', 'news', $error);
if (!$conn) die($error);

$user = isset($_POST['user']) ? $_POST['user'] : "";
$pwd = isset($_POST['pwd']) ? $_POST['pwd'] : "";

if (empty($user) || empty($pwd)) {
  return false;
}

if (!empty($user) && !empty($pwd)) { //建立连接
  $sql = "SELECT username,password FROM `users` WHERE username = '$user' and password = '$pwd'";
  $result = $conn->query($sql);
  $row = mysqli_fetch_array($result); //判断用户名或密码是否正确
  if ($user == $row['username'] && $pwd == $row['password']) {
    // 创建cookie
    // 过期时间被设置为一个月（60 秒 * 60 分 * 24 小时 * 30 天）
    $expire = time() + 60 * 60 * 24 * 30;
    setcookie("user1", $user, $expire);
    setcookie("pwd1", $pwd, $expire);
    //关闭数据库,可进行页面跳转
    header("refresh:2;sucess.php");
    // echo "登录成功！";
    mysqli_close($conn);
  } else {
    //用户名或密码错误
    echo "<script>alert('用户名或密码错误，请重新输入！');location.href='login.php';</script>";
  }
} else {
  //用户名或密码为空
  echo "<script>alert('用户名或密码不能为空，请重新输入！');location.href='login.php';</script>";
}
