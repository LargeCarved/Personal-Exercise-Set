<?php
$link = @mysqli_connect('localhost', 'root', 'a1592648', 'student01', '3306');
echo $link ? '成功' : '失败';
if (!$link) {
    exit(mysqli_connect_error());
}
if (!mysqli_set_charset($link, 'utf8')) {
    exit(mysqli_error($link));
}
$sql = 'UPDATE `student` SET `age`=19 WHERE `id`=5';
$result = mysqli_query($link, $sql);
if (!$result) {
    exit(mysqli_error($link));
}
echo mysqli_affected_rows($link);
mysqli_close($link);
