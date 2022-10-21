<head>
    <style>
        figure {
            display: block;
            background: black;
            border-radius: 50%;
            height: 40px;
            line-height: 38px;
            width: 40px;
            margin: 20px 5px;
            float: left;
            text-align: center;
            color: #FFFFFF;
            font-weight: bolder;
        }

        .red {
            background: -webkit-radial-gradient(10px 10px, circle, #ff0000, #000);
            background: -moz-radial-gradient(10px 10px, circle, #ff0000, #000);
            background: -ms-radial-gradient(10px 10px, circle, #ff0000, #000);
            background: radial-gradient(10px 10px, circle, #ff0000, #000);
        }

        .blue {
            background: -webkit-radial-gradient(10px 10px, circle, #0000ff, #000);
            background: -moz-radial-gradient(10px 10px, circle, #0000ff, #000);
            background: -ms-radial-gradient(10px 10px, circle, #0000ff, #000);
            background: radial-gradient(10px 10px, circle, #0000ff, #000);
        }
    </style>
</head>

<body>
    <?php
    $red_num = range(1, 33);
    //产生红球33个，它就是一个数组。
    $keys = array_rand($red_num, 6);
    //从红球数组中随机取6个键,顺序
    shuffle($keys);
    //打乱随机6个键。
    foreach ($keys as $value) {
        $red[] = $red_num[$value] < 10 ? '0' . $red_num[$value] : $red_num[$value];
    }
    //先存到一个数组我们的随机6个红球!
    foreach ($red as $value) {
        echo "<figure class=\"red\"> {$value} </figure>";
    }
    $blue_num = rand(1, 16);
    // 随机产生一个1 -16之间的数
    $blue = $blue_num < 10 ? '0' . $blue_num : $blue_num;
    echo "<figure class=\"blue\"> {$blue} </figure>";
    ?>
</body>
