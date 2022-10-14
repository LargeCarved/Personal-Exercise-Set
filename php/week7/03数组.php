<?php
// 实操一
$fruits = array(0 => 'apple', 1 => 'orange', 2 => 'pear');
$fruits1 = array('apple', 'orange', 'pear');
print_r($fruits);
echo '</br>';
var_dump($fruits1);
echo '</br>';

//实操二:短数组
$fruits3 = [233 => 'apple', 666 => 'orange', 'nb' => 'pear'];
$fruits4 = ['apple', 'orange', 'pear'];
print_r($fruits3);
echo '</br>';
var_dump($fruits4);
echo '</br>';

// 实操三:关联
$student = array('id' => 1, 'name' => 'soft', 'yuwen' => 90, 'shuxue' => 90, 'yingyu' => 100);
$student1 = ['id' => 1, 'name ' => 'soft', 'yuwen' => 90, 'shuxue' => 90, 'yingyu' => 100];
print_r($student);
echo '</br>';
var_dump($student1);
echo '</br>';

//以上就是数组的定义
echo $fruits[0];
echo '</br>';
echo $student['yingyu'];
echo '</br>';
$fruits[3] = 'banna';
echo $fruits[3];
echo '</br>';
unset($fruits[1]); //删除
var_dump(isset($fruits[1])); //判断元素存不存在

//以上是数组的访问和新增
//实操四:二维数组
$data = array(
    0 => array('name' => 'Tom', 'gender' => '男'),
    1 => array('name' => 'Lucy', 'gender' => '女'),
    2 => array('name' => 'Jimmy', 'gender' => '男')
);

//实操五:遍历
foreach ($fruits as $value) {
    echo $value . "<br/>";
}

foreach ($fruits as $key => $value) {
    echo $key . "=>" . $value . "<br/>";
}

//作业
$phparray = array('id' => 20210101, 'name' => 'hncst', 'major' => '软件技术', 'php' => 100);
$phpmyarray = ['id' => 20210101, 'name' => 'hncst', 'major' => '软件技术', 'php' => 100];
$phparray['javascript'] = 99;
echo $phpmyarray['name'] . "</br>";
foreach ($phparray as $k => $v) {
    echo $k . ":" . $v . " ";
}
echo "</br>";
foreach ($phpmyarray as $k => $v) {
    echo $k . ":" . $v . " ";
}
