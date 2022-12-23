<?php
$title = $_POST['title'] ?? '';
$content = $_POST['content'] ?? '';
$a_id = $_POST['author'] ?? 0;

# 安全判定
if(empty($title) || empty($content)){
    # 错误跳转重来
    header('refresh:3;url=myadd.php');
    echo '新闻标题和内容都不能为空！';
    exit;
}

$link = mysqli_connect('localhost', 'root', '', 'news', '3308');
if (!$link) {
    exit(mysqli_connect_error());
}
if (!mysqli_set_charset($link, 'utf8')) {
    exit(mysqli_error($link));
}

$sql = 'INSERT INTO `news` VALUES(NULL, \'' . $title . '\', \'' .
         $content . '\', ' . $a_id . ',' . time() . ')';
$res = mysqli_query($link, $sql);

if ($res) {
    header('refresh:2;url=index.php');
    echo '新闻：' . $title . ' 新增成功！';
} else {
    header('refresh:3;url=myadd.php');
    echo '新闻：' . $title . '新增失败！';
}

?>