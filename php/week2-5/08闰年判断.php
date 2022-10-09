<?php
$year = 2021;
if ($year % 4 == 0 && $year % 100 != 0 || $year % 400 == 0) {
    $result = $year . "是闰年";
} else {
    $result = $year . "是平年";
}
?>
<h2>闰年的判断</h2>
<p>输入的年份：<?php echo $year ?></p>
<p>判断的结果：<?php echo $result ?></p>
