<?php
//设定字符集
header('Content-type:text/html;charset=utf-8');
//定义一个常量，保存所有商品的折扣
const DISCOUNT = 0.8;
//定义变量，保存所有商品的名称
$fruit1 = '香蕉';
$fruit2 = '苹果';
$fruit3 = '橘子';
//对应商品的购买数量（斤）
$fruit1_num = 2;
$fruit2_num = 1;
$fruit3_num = 3;
//对应商品的价格（元/斤）
$fruit1_price = 7.99;
$fruit2_price = 6.89;
$fruit3_price = 3.99;
//依次计算每件商品的总价格
$fruit1_total = $fruit1_num * $fruit1_price;
$fruit2_total = $fruit2_num * $fruit2_price;
$fruit3_total = $fruit3_num * $fruit3_price;
//计算所有商品总价格
//计算公式：所有商品价格 =（香蕉总价格+苹果总价格+橘子总价格）*商品折扣
$total = ($fruit1_total + $fruit2_total + $fruit3_total) * DISCOUNT;
?>


<title>服务器信息</title>
<table border="1" cellpadding="1" cellspacing="0">
    <tr>
        <td>商品名称</td>
        <td>购买数量(斤)</td>
        <td>商品价格(元/斤)</td>
    </tr>
    <tr>
        <td><?php echo $fruit1; ?></td>
        <td><?php echo $fruit1_num; ?></td>
        <td><?php echo $fruit1_price; ?></td>
    </tr>
    <tr>
        <td><?php echo $fruit2; ?></td>
        <td><?php echo $fruit2_num; ?></td>
        <td><?php echo $fruit2_price; ?></td>
    </tr>
    <tr>
        <td><?php echo $fruit3; ?></td>
        <td><?php echo $fruit3_num; ?></td>
        <td><?php echo $fruit3_price; ?></td>
    </tr>
    <tr>
        <td colspan="3">
            商品折扣：<span><?php echo DISCOUNT; ?></span>
        </td>
    </tr>
    <tr>
        <td colspan="3">
            打折后购买商品总价格：<?php echo $total; ?> 元
        </td>
    </tr>
</table>
