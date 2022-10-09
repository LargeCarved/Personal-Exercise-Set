<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>成绩判断</title>
</head>

<body>
	<form action="" method="post">
		请输入成绩：
		<input type="text" name="text">
		<input type="submit" name="submit">
	</form>
	<?php
	if (isset($_POST['submit'])) {
		$score = $_POST['text'];
		if ($score >= 0 and $score <= 100) {
			if ($score >= 90) {
				$lv = "优秀";
			} else if ($score >= 80) {
				$lv = "良好";
			} else if ($score >= 70) {
				$lv = "中等";
			} else if ($score >= 60) {
				$lv = "及格";
			} else {
				$lv = "不合格";
			}
			echo "你的成绩是$lv";
		}
	}
	?>
</body>

</html>
