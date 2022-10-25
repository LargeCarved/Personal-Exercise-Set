<?php
function userinfo($name, $sex, $addr = '北京')
{
    echo '</br>用户名为：' . $name;
    echo '</br>性别为：' . $sex;
    echo '</br>地址为：' . $addr;
}
userinfo("jack", "男", "england");
userinfo("Lily", "女", "湖南");
userinfo("小明", "男");
