<?php 
$link = mysqli_connect('localhost', 'root', 'a1592648', 'news', '3306');
if (!$link) {
    exit(mysqli_connect_error());
}
if (!mysqli_set_charset($link, 'utf8')) {
    exit(mysqli_error($link));
}
// 获取作者信息
$result = mysqli_query($link, 'SELECT `id`,`name` FROM `author`');
if (!$result) {
    exit(mysqli_error($link));
}
$authors = [];
while ($row = mysqli_fetch_assoc($result)) {
    $authors[] = $row;
}
include 'myadd.html';
