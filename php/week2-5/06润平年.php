<?php
for($i=1876;$i<=2022;$i++){
	if($i%4==0 && $i%100!=0 || $i%400==0){
		echo $i.'是闰年';
		echo '<br>';
	}
}
