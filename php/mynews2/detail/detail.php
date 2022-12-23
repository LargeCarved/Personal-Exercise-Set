<?php
include '../sql.php';
$conn = connect('root', 'a1592648', 'news', $error);
if (!$conn) die($error);
$str = $_SERVER["QUERY_STRING"];
$arr = explode('=', $str);
$sql = "select * from news where id = " . $arr[1];
$news = read($conn, $sql, $error, true);
include 'detail.html';
