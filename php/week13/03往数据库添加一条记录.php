<?php
$link = @mysqli_connect('localhost', 'root', 'a1592648', 'student01', '3306');
if (!$link) {
    exit(mysqli_connect_error());
}
//设置字符集
if (!mysqli_set_charset($link, 'utf8')) {
    exit(mysqli_error($link));
}
$sql = 'INSERT INTO `student` VALUES(NULL,\'LYZ\',19)';
$result = mysqli_query($link, $sql);
if ($result) {
    echo mysqli_insert_id($link);
} else {
    exit(mysqli_error($link));
}
// if ($result) {
//     mysqli_free_result($result);
// }
mysqli_close($link);
