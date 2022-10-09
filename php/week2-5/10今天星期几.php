<?php
date_default_timezone_set('PRC');
$week = date("D");
switch ($week) {
    case 'Mon':
        echo "星期一";
        echo date("Y/m/d H:i:s");
        break;
    case 'Tue':
        echo "星期二";
        echo date("Y/m/d H:i:s");
        break;
    case 'Wed':
        echo "星期三";
        echo date("Y/m/d H:i:s");
        break;
    case 'Thu':
        echo "星期四";
        echo date("Y/m/d H:i:s");
        break;
    case 'Fri':
        echo "星期五";
        echo date("Y/m/d H:i:s");
        break;
    case 'Sat':
        echo "星期六";
        echo date("Y/m/d H:i:s");
        break;
    case 'Sun':
        echo "星期天";
        echo date("Y/m/d H:i:s");
        break;
    default:
        echo "获取失败! ";
        break;
}
