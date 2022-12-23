<?php
$title = $_POST['title'] ?? '';
$content = $_POST['content'] ?? '';
$a_id = $_POST['author'] ?? 0;

# 安全判定
if (empty($title) || empty($content)) {
    # 错误跳转重来
    echo "<script>alert('标题或内容不能为空！');location='myadd.php';</script>";
    // header('refresh:3;url=myadd.php');
    // echo '新闻标题和内容都不能为空！';
    // exit;
    return false;
}

$link = mysqli_connect('localhost', 'root', 'a1592648', 'news', '3306');
if (!$link) {
    exit(mysqli_connect_error());
}
if (!mysqli_set_charset($link, 'utf8')) {
    exit(mysqli_error($link));
}

$sql = 'INSERT INTO `news` VALUES(NULL, \'' . $title . '\', \'' . $content . '\', ' . $a_id . ',' . time() . ')';
$res = mysqli_query($link, $sql);

if ($res) {
    echo "<script>alert('新闻" . $title . "添加成功！');location='myadd.php';</script>";
    // header('refresh:2;url=myadd.php');
    // echo '新闻：' . $title . ' 新增成功！';
} else {
    echo "<script>alert('新闻" . $title . "添加失败！');location='myadd.php';</script>";
    // header('refresh:3;url=myadd.php');
    // echo '新闻：' . $title . '新增失败！';
}
