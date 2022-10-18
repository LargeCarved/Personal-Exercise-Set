<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <?php
    $goods = [
        ['name' => '主板', 'price' => 379, 'producing' => '广东', 'num' => 3],
        ['name' => '显卡', 'price' => 799, 'producing' => '上海', 'num' => 2],
        ['name' => '硬盘', 'price' => 589, 'producing' => '北京', 'num' => 5]
    ];
    $total = 0;
    ?>
    <table border="1" cellpadding="1" cellspacing="0">
        <tr>
            <td colspan="5">商品订货单</td>
        </tr>
        <tr>
            <td>商品名称</td>
            <td>价格(元)</td>
            <td>产地</td>
            <td>数量</td>
            <td>总价(元)</td>
        </tr>
        <?php foreach ($goods as $values) { ?>
            <tr>
                <td><?php echo $values['name']; ?></td>
                <td><?php echo $values['price']; ?></td>
                <td><?php echo $values['producing']; ?></td>
                <td><?php echo $values['num']; ?></td>
                <td><?php echo $values['price'] * $values['num']; ?></td>
                <?php $total += $values['price'] * $values['num']; ?>
            </tr>
        <?php } ?>
        <tr>
            <td colspan="5">总计 : <?php echo $total; ?>元</td>
        </tr>
    </table>
</body>

</html>
