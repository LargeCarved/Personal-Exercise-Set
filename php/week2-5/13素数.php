<?php
for ($i = 1; $i <= 100; $i++) {
	$count = 0;
	for ($j = 1; $j < $i; $j++) {
		if ($i % $j == 0) {
			$count++;
		}
	}
	if ($count == 1) {
		echo $i . "&nbsp;";
	}
}
