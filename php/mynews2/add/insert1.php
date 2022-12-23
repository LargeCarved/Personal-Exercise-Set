<?php 
include 'sql.php';

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
$conn=connect('root','','news',$error);
if(!$conn){
	exit($error);
}
$sql = 'INSERT INTO `news` VALUES(NULL, \'' . $title . '\', \'' .
         $content . '\', ' . $a_id . ',' . time() . ')';
$res=query($conn,$sql,$error);

if ($res) {
    header('refresh:2;url=index.php');
    echo '新闻：' . $title . ' 新增成功！';
} else {
    header('refresh:3;url=myadd.php');
    echo '新闻：' . $title . '新增失败！';
}
?>