<?php
$sex = 'male';
$age = 61;
if ($age >= 60) {
    if ($sex == "male") {
        echo "这位先生已经退休" . ($age - 60) . "年了";
    } else {
        echo "这位女士已经退休" . ($age - 60) . "年了";
    }
} else {
    if ($sex == "male") {
        echo "这位先生在工作，还有" . $age . "年就退休了";
    } else {
        echo "这位先生在工作，还有" . $age . "年就退休了";
    }
}
