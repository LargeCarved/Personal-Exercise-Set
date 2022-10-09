<?php
$a = 1;
var_dump($a); //int
$a = $a + 2.0;
var_dump($a); //float
var_dump(is_bool('1')); //true
var_dump(is_string('php')); //true
var_dump(is_float('23')); //false
var_dump(is_int('23.0')); //false
var_dump(is_numeric('45.6')); //true,数字字符串
var_dump(is_int(23));//true
