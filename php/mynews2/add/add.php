<?php 
include 'sql.php';
$conn=connect('root','','news',$error);
if(!$conn){
	exit($error);
}
$sql='SELECT `id`,`name` FROM `author`';
$authors=read($conn,$sql,$error,true);
include 'myadd.html';

?>