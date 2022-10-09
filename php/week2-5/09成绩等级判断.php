<?php
$score = 90;
if ($score >= 0 && $score <= 100) {
    if ($score >= 90 && $score <= 100) {
        $result = 'A';
    } elseif ($score >= 80) {
        $result = 'B';
    } elseif ($score >= 70) {
        $result = 'C';
    } elseif ($score >= 60) {
        $result = 'D';
    } else {
        $result = 'E';
    }
} else {
    $result = "分数非法";
}
?>
<h2>成绩等级判断</h2>
<p> 您输入的成绩是： <?php echo $score ?> </p>
<p> 判断结果是： <?php echo $result ?> </p>
