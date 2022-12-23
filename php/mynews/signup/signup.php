<?php
include '../sql.php';
header("content-type:text/html;charset=utf8");
include './signup.html';
$conn = connect('root', 'a1592648', 'news', $error);
if (!$conn) die($error);

$user = isset($_POST['user']) ? $_POST['user'] : "";
$pwd = isset($_POST['pwd']) ? $_POST['pwd'] : "";

if (empty($user) || empty($pwd)) {
  return false;
}

if (!empty($user) && !empty($pwd)) { //建立连接
  $sql = "INSERT INTO `users` values (null, '$user', '$pwd')";
  $result = $conn->query($sql);
  if ($result) {
    echo mysqli_insert_id($conn);
  } else {
    exit(mysqli_error($conn));
  }
  //关闭数据库,可进行页面跳转
  header("refresh:2;sucess.php");
  // echo "登录成功！";
  mysqli_close($conn);
} else {
  //用户名或密码为空
  echo "<script>alert('用户名或密码不能为空，请重新输入！');location.href='signup.php';</script>";
}
