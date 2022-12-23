<?php
include 'Sql.php';
$conn = connect('root','','news',$error);
if(!$conn) die($error);
# 组织数据SQL，获取数据（手动组织：需要连表）
$sql = "select n.*,a.name from news n left join author a on n.a_id = a.id";
$news = read($conn,$sql,$error,true);
include 'index.html';
?>